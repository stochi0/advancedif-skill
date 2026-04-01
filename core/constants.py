from __future__ import annotations

DEFAULT_POLICY_MODELS = [
    "openai/gpt-4.1-mini",
]

DEFAULT_JUDGE_MODEL = "z-ai/glm-4.7"
DEFAULT_REFLECTION_MODEL = "openai/gpt-4.1-mini"

DEFAULT_INDEPENDENT_FEEDBACK_MODES = ["none", "score_only", "one_violation"]
DEFAULT_CARRYOVER_FEEDBACK_MODES = ["score_only", "one_violation"]

DEFAULT_HARNESSES = [
    "advancedif_iter_skill",
    "advancedif_rlm_skill",
]

DEFAULT_SAMPLING_ARGS = {"temperature": 0.2}
DEFAULT_GEPA_SAMPLING_ARGS = {"temperature": 0.2}

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

HARNESS_LABELS = {
    "advancedif_iter_skill": "iter_skill",
    "advancedif_rlm_skill": "rlm_skill",
}
