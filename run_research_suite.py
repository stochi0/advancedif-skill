from __future__ import annotations

import argparse
from pathlib import Path

EVAL_CONFIGS = [
    "configs/eval/iter_score_only_main_eval.toml",
    "configs/eval/iter_one_violation_main_eval.toml",
    "configs/eval/iter_none_main_eval.toml",
    "configs/eval/rlm_score_only_main_eval.toml",
    "configs/eval/rlm_one_violation_main_eval.toml",
    "configs/eval/rlm_none_main_eval.toml",
]

GEPA_CONFIGS = [
    "configs/gepa/iter_score_only_gepa.toml",
]

SEQUENCE_COMMANDS = [
    "uv run python sequence_runner.py --env advancedif_iter_skill --model openai/gpt-4.1-mini --feedback-mode score_only --judge-model z-ai/glm-4.7",
    "uv run python sequence_runner.py --env advancedif_iter_skill --model openai/gpt-4.1-mini --feedback-mode one_violation --judge-model z-ai/glm-4.7",
    "uv run python sequence_runner.py --env advancedif_rlm_skill --model openai/gpt-4.1-mini --feedback-mode score_only --judge-model z-ai/glm-4.7",
    "uv run python sequence_runner.py --env advancedif_rlm_skill --model openai/gpt-4.1-mini --feedback-mode one_violation --judge-model z-ai/glm-4.7",
]


def build_suite_markdown() -> str:
    lines = ["# Research Suite Commands", "", "## Independent Evaluations", ""]
    lines.extend([f"- `uv run prime eval run {config}`" for config in EVAL_CONFIGS])
    lines.extend(["", "## GEPA", ""])
    lines.extend([f"- `uv run prime gepa run {config}`" for config in GEPA_CONFIGS])
    lines.extend(["", "## Carryover And Transfer", ""])
    lines.extend([f"- `{command}`" for command in SEQUENCE_COMMANDS])
    return "\n".join(lines).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print or write the minimal command list for the AdvancedIF suite."
    )
    parser.add_argument(
        "-o",
        "--output-path",
        default=None,
        help="Write markdown to this path. If omitted, print to stdout.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    text = build_suite_markdown()
    if args.output_path is None:
        print(text, end="")
        return
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    print(output_path.resolve())


if __name__ == "__main__":
    main()
