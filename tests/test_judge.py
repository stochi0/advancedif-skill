from __future__ import annotations

import json

from core.config import EnvironmentConfig
from core.judge import AdvancedIFAnswerJudge, format_limited_feedback


class _FakeChatCompletions:
    def __init__(self):
        self.calls = 0

    async def create(self, model, messages, **kwargs):
        self.calls += 1
        content = messages[0]["content"]
        satisfied = [True, True] if "final answer" in content else [False, True]

        class _Usage:
            prompt_tokens = 10
            completion_tokens = 4

        class _Message:
            content = json.dumps({"satisfied": satisfied})

        class _Choice:
            message = _Message()

        class _Response:
            usage = _Usage()
            choices = [_Choice()]

        return _Response()


class _FakeClient:
    def __init__(self):
        self.chat = type("Chat", (), {"completions": _FakeChatCompletions()})()


async def test_judge_uses_disk_cache(tmp_path):
    client = _FakeClient()
    cfg = EnvironmentConfig(
        cache_dir=str(tmp_path),
        judge_client=client,
    )
    judge = AdvancedIFAnswerJudge(cfg)

    result_one = await judge.evaluate(
        example_id=1,
        conversation=[{"role": "user", "content": "hello"}],
        gold_rubrics=["a", "b"],
        candidate_answer="draft answer",
    )
    result_two = await judge.evaluate(
        example_id=1,
        conversation=[{"role": "user", "content": "hello"}],
        gold_rubrics=["a", "b"],
        candidate_answer="draft answer",
    )

    assert result_one.cached is False
    assert result_two.cached is True
    assert client.chat.completions.calls == 1


def test_feedback_formatter_modes():
    from core.judge import JudgeResult

    result = JudgeResult(satisfied=[False, True], prompt_tokens=0, completion_tokens=0)
    gold = ["criterion one", "criterion two"]
    assert "1/2" in format_limited_feedback(
        JudgeResult(satisfied=[True, False], prompt_tokens=0, completion_tokens=0),
        gold,
        "score_only",
    )
    assert "criterion one" in format_limited_feedback(result, gold, "one_violation")
    assert format_limited_feedback(result, gold, "none") == "Judge feedback: submission received."
