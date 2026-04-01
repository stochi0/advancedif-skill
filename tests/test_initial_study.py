from __future__ import annotations

from run_initial_study import build_initial_study_markdown


def test_initial_study_markdown_mentions_narrow_protocol():
    text = build_initial_study_markdown(
        model="openai/gpt-4.1-mini",
        judge_model="z-ai/glm-4.7",
        sequence_env="advancedif_rlm_skill",
    )

    assert "Matched Iterative vs RLM" in text
    assert "configs/eval/iter_score_only_main_eval.toml" in text
    assert "configs/eval/rlm_score_only_main_eval.toml" in text
    assert "--env advancedif_rlm_skill" in text
    assert "score_only" in text
