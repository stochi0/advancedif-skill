from __future__ import annotations

from core.skill_artifact import EMPTY_SKILL_TEMPLATE


def feedback_mode_description(feedback_mode: str) -> str:
    if feedback_mode == "score_only":
        return "a score only: the fraction of hidden rubric items your candidate answer satisfies"
    if feedback_mode == "one_violation":
        return "a single violated hidden rubric criterion or an all-clear message"
    return "no contentful feedback beyond acknowledgement that the submission was received"


ITER_SYSTEM_PROMPT = """You are completing the next assistant turn for an AdvancedIF conversation.

Your job is to produce a final assistant answer that satisfies as many hidden rubric criteria as possible.

You have two tools:
- `submit_candidate_answer(candidate_answer)`: get restricted hidden-judge feedback on a draft answer.
- `update_skill(skill_markdown)`: update the carried markdown skill artifact that may help on later tasks.

Use the conversation history exactly as given. Respect all earlier system instructions and carried context.
When you are ready, return the final assistant answer directly in natural language. Do not wrap it in JSON unless the conversation itself asks for JSON.
"""


def render_skill_context(current_skill: str) -> str:
    skill = current_skill.strip() or EMPTY_SKILL_TEMPLATE.strip()
    return (
        "Current carried skill artifact follows. You may update it with the tool, "
        "but you still need to answer the conversation directly.\n\n"
        f"{skill}"
    )


def render_iter_dynamic_skill_message(current_skill: str, feedback_mode: str) -> str:
    return (
        f"{render_skill_context(current_skill)}\n\n"
        "Judge feedback mode for `submit_candidate_answer`: "
        f"{feedback_mode_description(feedback_mode)}."
    )


def render_rlm_task_prompt(
    current_skill: str, feedback_mode: str, allow_skill_updates: bool
) -> str:
    skill_update_instruction = (
        "You may call `update_skill(skill_markdown)` when you want to persist a better carried skill. "
        "After a successful update, also overwrite `skill.md` locally if you want your current sandbox state to match."
        if allow_skill_updates
        else "Skill updates are disabled for this rollout. Read `skill.md` but do not try to persist changes."
    )
    return f"""You are operating in a verifiers RLM environment with a persistent Python REPL and sandbox filesystem.

Task:
- Read the conversation stored in `trajectory/`.
- Produce the next assistant answer for that conversation.
- Read the current carried skill from `skill.md` and use it if helpful.

Available root tools:
- `submit_candidate_answer(candidate_answer)`: returns {feedback_mode_description(feedback_mode)}.
- `update_skill(skill_markdown)`: validates and persists a new carried skill.

Workflow:
1. Inspect `trajectory/manifest.json` and the conversation files.
2. Read `skill.md`.
3. Draft an answer in `answer["content"]`.
4. Optionally submit draft answers through `submit_candidate_answer`.
5. {skill_update_instruction}
6. When done, set `answer["content"]` to the final assistant answer text and `answer["ready"] = True` in the same REPL turn.

Current skill artifact:

{current_skill.strip() or EMPTY_SKILL_TEMPLATE.strip()}
"""


PER_CRITERION_JUDGE_PROMPT = """You are grading a candidate assistant answer against a hidden gold rubric for the same conversation.

Conversation so far:
{conversation}

Gold rubric items (indices 0..n-1):
{numbered_gold}

Candidate assistant answer:
{candidate_answer}

Return one JSON object with exactly this key:
- "satisfied": an array of exactly {n} booleans in rubric order.

Use a strict standard. Partial or vague satisfaction should be marked false.
Return JSON only.
"""


SKILL_META_JUDGE_PROMPT = """Score this markdown skill artifact for abstraction and reusability on future instruction-following tasks.

Return one JSON object with integer scores from 1 to 5 for:
- "abstraction"
- "reusability"
- "specificity_balance"

Skill:
{skill_markdown}
"""
