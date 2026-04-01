from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import verifiers as vf
from openai import APIError, APITimeoutError, RateLimitError
from verifiers.types import Messages, State
from verifiers.utils.async_utils import maybe_await
from verifiers.utils.client_utils import setup_openai_client
from verifiers.utils.config_utils import ensure_keys

from core.config import EnvironmentConfig
from core.prompts import PER_CRITERION_JUDGE_PROMPT
from core.skill_artifact import skill_heading_completeness, skill_word_count


def extract_json_object(text: str) -> dict[str, Any] | None:
    cleaned = text.strip()
    if "```" in cleaned:
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.MULTILINE)
        cleaned = re.sub(r"\s*```\s*$", "", cleaned, flags=re.MULTILINE)
    start = cleaned.find("{")
    if start < 0:
        return None
    try:
        obj, _ = json.JSONDecoder().raw_decode(cleaned[start:])
    except json.JSONDecodeError:
        return None
    return obj if isinstance(obj, dict) else None


def extract_usage(response: Any) -> tuple[int, int]:
    usage = getattr(response, "usage", None)
    if usage is None:
        return 0, 0
    prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
    completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
    return prompt_tokens, completion_tokens


def parse_gold_rubrics(answer: str) -> list[str]:
    try:
        data = json.loads(answer)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
        return []
    return data


def numbered_gold(gold_rubrics: list[str]) -> str:
    return "\n".join(f"{idx}. {rubric}" for idx, rubric in enumerate(gold_rubrics))


def conversation_to_text(conversation: list[dict[str, Any]] | Messages) -> str:
    blocks: list[str] = []
    for message in conversation:
        role = (
            message.get("role")
            if isinstance(message, dict)
            else getattr(message, "role", "unknown")
        )
        content = (
            message.get("content") if isinstance(message, dict) else getattr(message, "content", "")
        )
        blocks.append(f"[{role}]\n{content}")
    return "\n\n".join(blocks)


@dataclass
class JudgeResult:
    satisfied: list[bool]
    prompt_tokens: int
    completion_tokens: int
    cached: bool = False

    @property
    def score(self) -> float:
        return (
            sum(1 for item in self.satisfied if item) / len(self.satisfied)
            if self.satisfied
            else 0.0
        )

    @property
    def all_pass(self) -> bool:
        return bool(self.satisfied) and all(self.satisfied)


class JudgeCache:
    def __init__(self, cache_dir: str | Path):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, example_id: int, candidate_hash: str, judge_model: str) -> Path:
        model_key = re.sub(r"[^a-zA-Z0-9_.-]+", "_", judge_model)
        return self.cache_dir / model_key / f"{example_id}_{candidate_hash}.json"

    def load(self, example_id: int, candidate_hash: str, judge_model: str) -> JudgeResult | None:
        path = self._path(example_id, candidate_hash, judge_model)
        if not path.is_file():
            return None
        payload = json.loads(path.read_text(encoding="utf-8"))
        return JudgeResult(
            satisfied=list(payload["satisfied"]),
            prompt_tokens=int(payload.get("prompt_tokens", 0)),
            completion_tokens=int(payload.get("completion_tokens", 0)),
            cached=True,
        )

    def save(
        self, example_id: int, candidate_hash: str, judge_model: str, result: JudgeResult
    ) -> None:
        path = self._path(example_id, candidate_hash, judge_model)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                {
                    "satisfied": result.satisfied,
                    "prompt_tokens": result.prompt_tokens,
                    "completion_tokens": result.completion_tokens,
                },
                indent=2,
            ),
            encoding="utf-8",
        )


class AdvancedIFAnswerJudge:
    def __init__(self, cfg: EnvironmentConfig):
        if cfg.judge_client is None:
            ensure_keys([cfg.judge_client_config.api_key_var])
            self.client = setup_openai_client(cfg.judge_client_config)
        else:
            self.client = cfg.judge_client
        self.judge_model = cfg.judge_model
        self.judge_sampling_args = dict(cfg.judge_sampling_args or {})
        self.cache = JudgeCache(cfg.resolved_cache_dir)

    async def evaluate(
        self,
        example_id: int,
        conversation: list[dict[str, Any]] | Messages,
        gold_rubrics: list[str],
        candidate_answer: str,
    ) -> JudgeResult:
        candidate_hash = hashlib.sha256(candidate_answer.encode("utf-8")).hexdigest()[:16]
        cached = self.cache.load(example_id, candidate_hash, self.judge_model)
        if cached is not None:
            return cached

        prompt = PER_CRITERION_JUDGE_PROMPT.format(
            conversation=conversation_to_text(conversation),
            numbered_gold=numbered_gold(gold_rubrics),
            candidate_answer=candidate_answer.strip(),
            n=len(gold_rubrics),
        )
        sampling_args = dict(self.judge_sampling_args)
        if "max_tokens" in sampling_args:
            sampling_args["max_completion_tokens"] = sampling_args.pop("max_tokens")

        try:
            response = await maybe_await(
                self.client.chat.completions.create,
                model=self.judge_model,
                messages=[{"role": "user", "content": prompt}],
                **sampling_args,
            )
        except RateLimitError as err:
            raise RuntimeError(f"Judge rate limit: {err}") from err
        except APITimeoutError as err:
            raise RuntimeError(f"Judge timeout: {err}") from err
        except APIError as err:
            raise RuntimeError(f"Judge API error: {err}") from err

        raw = str(response.choices[0].message.content)
        payload = extract_json_object(raw)
        if not payload or "satisfied" not in payload:
            raise RuntimeError(f"Judge returned unparseable response: {raw}")
        satisfied = payload["satisfied"]
        if not isinstance(satisfied, list) or not all(isinstance(item, bool) for item in satisfied):
            raise RuntimeError(f"Judge returned invalid boolean vector: {raw}")
        prompt_tokens, completion_tokens = extract_usage(response)
        result = JudgeResult(
            satisfied=list(satisfied),
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            cached=False,
        )
        self.cache.save(example_id, candidate_hash, self.judge_model, result)
        return result


def ensure_judge_state(state: State) -> None:
    state.setdefault("judge_queries", 0)
    state.setdefault("judge_calls", 0)
    state.setdefault("judge_prompt_tokens", 0)
    state.setdefault("judge_completion_tokens", 0)
    state.setdefault("judge_history", [])


def register_judge_result(
    state: State,
    stage: str,
    candidate_answer: str,
    result: JudgeResult,
) -> None:
    ensure_judge_state(state)
    state["judge_queries"] += 1
    if not result.cached:
        state["judge_calls"] += 1
        state["judge_prompt_tokens"] += result.prompt_tokens
        state["judge_completion_tokens"] += result.completion_tokens
    state["judge_history"].append(
        {
            "stage": stage,
            "score": result.score,
            "all_pass": result.all_pass,
            "cached": result.cached,
            "candidate_hash": hashlib.sha256(candidate_answer.encode("utf-8")).hexdigest()[:16],
        }
    )


def format_limited_feedback(
    result: JudgeResult,
    gold_rubrics: list[str],
    feedback_mode: str,
) -> str:
    if feedback_mode == "none":
        return "Judge feedback: submission received."
    if feedback_mode == "score_only":
        satisfied = sum(1 for item in result.satisfied if item)
        return (
            "Judge feedback (score only): "
            f"{satisfied}/{len(result.satisfied)} hidden criteria satisfied "
            f"({result.score:.3f})."
        )
    failed_indices = [idx for idx, ok in enumerate(result.satisfied) if not ok]
    if not failed_indices:
        return "Judge feedback (single violated criterion): no failing criterion reported."
    idx = failed_indices[0]
    criterion = gold_rubrics[idx] if idx < len(gold_rubrics) else f"criterion #{idx}"
    return (
        "Judge feedback (single violated criterion): "
        f"hidden rubric item #{idx} is not satisfied: {criterion}"
    )


def candidate_from_completion(completion: Messages | None) -> str:
    if not completion:
        return ""
    for message in reversed(completion):
        role = message.get("role") if isinstance(message, dict) else getattr(message, "role", None)
        if role == "assistant":
            content = (
                message.get("content")
                if isinstance(message, dict)
                else getattr(message, "content", "")
            )
            return str(content or "")
    return ""


def policy_token_total(state: State) -> float:
    total = 0.0
    for step in state.get("trajectory", []):
        usage = getattr(step.get("response"), "usage", None)
        if usage is None:
            continue
        total += float(getattr(usage, "prompt_tokens", 0) or 0)
        total += float(getattr(usage, "completion_tokens", 0) or 0)
    return total


class AdvancedIFAnswerRubric(vf.Rubric):
    def __init__(self, judge: AdvancedIFAnswerJudge):
        super().__init__(parser=vf.Parser())
        self.judge = judge
        self.add_reward_func(self.final_criterion_satisfaction, weight=1.0)
        self.add_metric(self.all_criteria_pass)
        self.add_metric(self.judge_call_count)
        self.add_metric(self.judge_query_count)
        self.add_metric(self.judge_prompt_token_count)
        self.add_metric(self.judge_completion_token_count)
        self.add_metric(self.total_token_count)
        self.add_metric(self.first_submission_lift)
        self.add_metric(self.skill_word_count_metric)
        self.add_metric(self.skill_heading_completeness_metric)

    async def final_criterion_satisfaction(
        self,
        completion: Messages,
        answer: str,
        state: State,
    ) -> float:
        candidate = str(state.get("final_answer") or candidate_from_completion(completion))
        state["final_answer"] = candidate
        gold_rubrics = parse_gold_rubrics(answer)
        conversation = state.get("info", {}).get("conversation") or []
        result = await self.judge.evaluate(
            example_id=int(state.get("example_id", 0)),
            conversation=conversation,
            gold_rubrics=gold_rubrics,
            candidate_answer=candidate,
        )
        register_judge_result(state, stage="final", candidate_answer=candidate, result=result)
        state["criterion_vector"] = list(result.satisfied)
        state["final_judge_result"] = asdict(result)
        state["all_criteria_pass_value"] = 1.0 if result.all_pass else 0.0
        state["final_score"] = result.score
        return result.score

    async def all_criteria_pass(self, state: State) -> float:
        return float(state.get("all_criteria_pass_value", 0.0))

    async def judge_call_count(self, state: State) -> float:
        return float(state.get("judge_calls", 0))

    async def judge_query_count(self, state: State) -> float:
        return float(state.get("judge_queries", 0))

    async def judge_prompt_token_count(self, state: State) -> float:
        return float(state.get("judge_prompt_tokens", 0))

    async def judge_completion_token_count(self, state: State) -> float:
        return float(state.get("judge_completion_tokens", 0))

    async def total_token_count(self, state: State) -> float:
        return (
            policy_token_total(state)
            + float(state.get("judge_prompt_tokens", 0))
            + float(state.get("judge_completion_tokens", 0))
        )

    async def first_submission_lift(self, state: State) -> float:
        first_score = state.get("first_submission_score")
        final_score = state.get("final_score", 0.0)
        if first_score is None:
            return 0.0
        return float(final_score) - float(first_score)

    async def skill_word_count_metric(self, state: State) -> float:
        return float(skill_word_count(str(state.get("current_skill_markdown", ""))))

    async def skill_heading_completeness_metric(self, state: State) -> float:
        return float(skill_heading_completeness(str(state.get("current_skill_markdown", ""))))
