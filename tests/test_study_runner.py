from __future__ import annotations

import json
from pathlib import Path

from run_study import (
    build_report_markdown,
    choose_sequence_env,
    compare_eval_runs,
    summarize_eval_run,
    summarize_gepa_run,
    summarize_sequence_run,
)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def test_eval_and_sequence_summaries_and_report(tmp_path: Path):
    iter_run_dir = tmp_path / "iter"
    rlm_run_dir = tmp_path / "rlm"
    iter_run_dir.mkdir()
    rlm_run_dir.mkdir()

    iter_meta = {
        "env_id": "advancedif_iter_skill",
        "model": "openai/gpt-4.1-mini",
    }
    rlm_meta = {
        "env_id": "advancedif_rlm_skill",
        "model": "openai/gpt-4.1-mini",
    }
    (iter_run_dir / "metadata.json").write_text(json.dumps(iter_meta), encoding="utf-8")
    (rlm_run_dir / "metadata.json").write_text(json.dumps(rlm_meta), encoding="utf-8")

    write_jsonl(
        iter_run_dir / "results.jsonl",
        [
            {
                "example_id": 1,
                "reward": 0.4,
                "error": None,
                "metrics": {
                    "all_criteria_pass": 0.0,
                    "first_submission_lift": 0.1,
                    "total_token_count": 1000,
                    "judge_call_count": 1.0,
                },
            },
            {
                "example_id": 2,
                "reward": 0.5,
                "error": None,
                "metrics": {
                    "all_criteria_pass": 0.0,
                    "first_submission_lift": 0.0,
                    "total_token_count": 1000,
                    "judge_call_count": 1.0,
                },
            },
        ],
    )
    write_jsonl(
        rlm_run_dir / "results.jsonl",
        [
            {
                "example_id": 1,
                "reward": 0.6,
                "error": None,
                "metrics": {
                    "all_criteria_pass": 1.0,
                    "first_submission_lift": 0.2,
                    "total_token_count": 1200,
                    "judge_call_count": 1.0,
                },
            },
            {
                "example_id": 2,
                "reward": 0.7,
                "error": None,
                "metrics": {
                    "all_criteria_pass": 1.0,
                    "first_submission_lift": 0.1,
                    "total_token_count": 1300,
                    "judge_call_count": 1.0,
                },
            },
        ],
    )

    iter_summary = summarize_eval_run("iter", iter_run_dir)
    rlm_summary = summarize_eval_run("rlm", rlm_run_dir)
    comparison = compare_eval_runs(iter_summary, rlm_summary)

    assert comparison["reward_delta_rlm_minus_iter"] > 0
    assert choose_sequence_env(comparison) == "advancedif_rlm_skill"

    sequence_dir = tmp_path / "sequence"
    sequence_dir.mkdir()
    (sequence_dir / "metadata.json").write_text("{}", encoding="utf-8")
    write_jsonl(
        sequence_dir / "outputs.jsonl",
        [
            {
                "example_id": 10,
                "sequence_id": 0,
                "task_index": 0,
                "phase": "carryover",
                "reward": 0.4,
                "first_submission_lift": 0.0,
                "current_skill_markdown": "# Skill\nhello",
            },
            {
                "example_id": 11,
                "sequence_id": 0,
                "task_index": 1,
                "phase": "carryover",
                "reward": 0.6,
                "first_submission_lift": 0.2,
                "current_skill_markdown": "# Skill\nhello world",
            },
            {
                "example_id": 20,
                "sequence_id": 0,
                "task_index": None,
                "phase": "transfer_frozen",
                "reward": 0.8,
            },
            {
                "example_id": 20,
                "sequence_id": 0,
                "task_index": None,
                "phase": "transfer_empty_control",
                "reward": 0.4,
            },
        ],
    )
    sequence_summary = summarize_sequence_run(
        env_id="advancedif_rlm_skill",
        output_dir=sequence_dir,
        metadata_path=sequence_dir / "metadata.json",
        results_path=sequence_dir / "outputs.jsonl",
    )

    gepa_dir = tmp_path / "gepa"
    gepa_dir.mkdir()
    (gepa_dir / "metadata.json").write_text(
        json.dumps({"best_score": 0.7, "num_candidates": 3, "total_metric_calls": 12}),
        encoding="utf-8",
    )
    (gepa_dir / "best_prompt.txt").write_text("Best prompt", encoding="utf-8")
    gepa_summary = summarize_gepa_run(gepa_dir)

    report = build_report_markdown(
        study_name="Study",
        study_dir=tmp_path,
        model="openai/gpt-4.1-mini",
        judge_model="z-ai/glm-4.7",
        feedback_mode="score_only",
        iter_summary=iter_summary,
        rlm_summary=rlm_summary,
        comparison=comparison,
        sequence_summary=sequence_summary,
        sequence_env="advancedif_rlm_skill",
        gepa_eval_summary=iter_summary,
        gepa_run_summary=gepa_summary,
    )

    assert "Q1." in report
    assert "transfer_lift_mean" in report
    assert "GEPA" in report
