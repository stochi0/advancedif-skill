from __future__ import annotations

import json

from core.config import BENCHMARK_REGIMES, EnvironmentConfig
from core.dataset import build_benchmark_splits


def make_raw_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for regime in BENCHMARK_REGIMES:
        for idx in range(70):
            rows.append(
                {
                    "benchmark_name": regime,
                    "conversation_history": json.dumps(
                        [{"role": "user", "content": f"{regime} request {idx}"}]
                    ),
                    "prompt_metadata": json.dumps(
                        {"rubrics": json.dumps([f"{regime} rubric a", f"{regime} rubric b"])}
                    ),
                }
            )
    return rows


def test_stratified_split_sizes_and_no_overlap():
    cfg = EnvironmentConfig(dataset_rows=make_raw_rows(), split_seed=13)
    splits = build_benchmark_splits(cfg)

    assert len(splits.dev_gepa) == 45
    assert len(splits.main_eval) == 90
    assert len(splits.transfer_probe) == 18
    assert len(splits.carryover_sequences) == 3
    assert all(len(sequence) == 9 for sequence in splits.carryover_sequences)

    ids = set()
    for collection in (
        splits.dev_gepa,
        splits.main_eval,
        splits.transfer_probe,
        *splits.carryover_sequences,
    ):
        for example in collection:
            assert example.example_id not in ids
            ids.add(example.example_id)


def test_carryover_sequences_are_balanced_by_regime():
    cfg = EnvironmentConfig(dataset_rows=make_raw_rows(), split_seed=13)
    splits = build_benchmark_splits(cfg)

    for sequence in splits.carryover_sequences:
        counts = {regime: 0 for regime in BENCHMARK_REGIMES}
        for example in sequence:
            counts[example.benchmark_name] += 1
        assert counts == {regime: 3 for regime in BENCHMARK_REGIMES}
