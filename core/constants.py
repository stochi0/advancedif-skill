from __future__ import annotations

DEFAULT_JUDGE_MODEL = "z-ai/glm-4.7"

DEFAULT_SAMPLING_ARGS = {"temperature": 0.2}

STATE_COLUMNS = [
    "rollout_output_dir",
    "current_skill_markdown",
    "current_skill_path",
    "skill_snapshot_paths",
    "skill_update_count",
    "criterion_vector",
    "final_answer",
    "judge_history",
    "judge_calls",
    "judge_queries",
    "judge_prompt_tokens",
    "judge_completion_tokens",
    "first_submission_score",
    "first_submission_answer",
    "last_submission_score",
    "final_score",
]
