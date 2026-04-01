from __future__ import annotations

import argparse
from pathlib import Path


def build_initial_study_markdown(
    *,
    model: str,
    judge_model: str,
    sequence_env: str = "advancedif_iter_skill",
) -> str:
    lines = [
        "# Initial Study Commands",
        "",
        "This is the recommended first pass for the benchmark.",
        "It narrows the scope to one clean question before running the full suite:",
        "",
        f"- same policy model in both harnesses: `{model}`",
        "- same feedback channel: `score_only`",
        "- same split: `main_eval`",
        f"- same judge model: `{judge_model}`",
        "",
        "## Phase 1: Matched Iterative vs RLM",
        "",
        "- `uv run prime eval run configs/eval/iter_score_only_main_eval.toml`",
        "- `uv run prime eval run configs/eval/rlm_score_only_main_eval.toml`",
        "",
        "Primary metrics to compare:",
        "",
        "- `criterion_satisfaction_mean`",
        "- `all_criteria_pass_rate`",
        "- `first_submission_lift_mean`",
        "- `total_tokens_mean`",
        "- `reward_per_1k_tokens_mean`",
        "",
        "Decision rule:",
        "",
        "- Pick the harness with the better balance of final score and reward per 1k tokens.",
        "- If scores are close, prefer the simpler iterative harness.",
        "",
        "## Phase 2: Carryover And Transfer On The More Promising Harness",
        "",
        f"- Default winner placeholder: `{sequence_env}`",
        f"- `uv run python sequence_runner.py --env {sequence_env} --model {model} --feedback-mode score_only --judge-model {judge_model}`",
        "",
        "What to check:",
        "",
        "- `transfer_frozen` vs `transfer_empty_control`",
        "- `skill_word_count_metric` by `task_index`",
        "- `first_submission_lift` by `task_index`",
        "",
        "## Phase 3: Optional GEPA Follow-Up",
        "",
        "- Run this only if the iterative baseline is competitive enough that prompt-only optimization is a meaningful comparator.",
        "- `uv run prime gepa run configs/gepa/iter_score_only_gepa.toml`",
        "",
        "## Notes",
        "",
        "- The checked-in eval configs already use the matched `score_only` setup with skill updates enabled.",
        "- If you want to test a smaller model, update both score-only eval configs and the sequence runner command to the same model before comparing harnesses.",
        "- This first study is intentionally narrower than the full research suite.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print or write the recommended first-pass AdvancedIF study commands."
    )
    parser.add_argument("--model", default="openai/gpt-4.1-mini")
    parser.add_argument("--judge-model", default="z-ai/glm-4.7")
    parser.add_argument("--sequence-env", default="advancedif_iter_skill")
    parser.add_argument(
        "-o",
        "--output-path",
        default=None,
        help="Write markdown to this path. If omitted, print to stdout.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    text = build_initial_study_markdown(
        model=args.model,
        judge_model=args.judge_model,
        sequence_env=args.sequence_env,
    )
    if args.output_path is None:
        print(text, end="")
        return
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    print(output_path.resolve())


if __name__ == "__main__":
    main()
