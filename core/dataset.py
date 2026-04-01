from __future__ import annotations

import json
import random
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from datasets import Dataset, load_dataset
from verifiers.types import RolloutInput

from core.config import BENCHMARK_REGIMES, PILOT_SPLIT_COUNTS, EnvironmentConfig
from core.skill_artifact import EMPTY_SKILL_TEMPLATE, write_skill


@dataclass(frozen=True)
class AdvancedIFExample:
    example_id: int
    benchmark_name: str
    conversation: list[dict[str, Any]]
    gold_rubrics: list[str]


@dataclass(frozen=True)
class BenchmarkSplits:
    dev_gepa: list[AdvancedIFExample]
    main_eval: list[AdvancedIFExample]
    carryover_sequences: list[list[AdvancedIFExample]]
    transfer_probe: list[AdvancedIFExample]


def parse_conversation_history(raw: str) -> list[dict[str, Any]]:
    data = json.loads(raw)
    if not isinstance(data, list):
        raise ValueError("conversation_history must decode to a list")
    return [dict(message) for message in data]


def parse_rubrics(raw_prompt_metadata: str) -> list[str]:
    metadata = json.loads(raw_prompt_metadata)
    rubrics = metadata.get("rubrics", [])
    if isinstance(rubrics, str):
        rubrics = json.loads(rubrics)
    if not isinstance(rubrics, list) or not all(isinstance(item, str) for item in rubrics):
        raise ValueError("prompt_metadata.rubrics must decode to list[str]")
    return rubrics


def safe_segment(text: str, max_len: int = 48) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "_", text.strip())[:max_len] or "unknown"


def load_examples(cfg: EnvironmentConfig) -> list[AdvancedIFExample]:
    rows: list[dict[str, Any]]
    if cfg.dataset_rows is not None:
        rows = list(cfg.dataset_rows)
    else:
        ds = load_dataset(cfg.dataset_name, split=cfg.dataset_split)
        rows = [dict(row) for row in ds]

    examples: list[AdvancedIFExample] = []
    for idx, row in enumerate(rows):
        examples.append(
            AdvancedIFExample(
                example_id=idx,
                benchmark_name=str(row["benchmark_name"]),
                conversation=parse_conversation_history(row["conversation_history"]),
                gold_rubrics=parse_rubrics(row["prompt_metadata"]),
            )
        )
    return examples


def build_benchmark_splits(cfg: EnvironmentConfig) -> BenchmarkSplits:
    grouped = {name: [] for name in BENCHMARK_REGIMES}
    for example in load_examples(cfg):
        if example.benchmark_name in grouped:
            grouped[example.benchmark_name].append(example)

    total_required = sum(PILOT_SPLIT_COUNTS.values())
    for regime in BENCHMARK_REGIMES:
        regime_examples = grouped[regime]
        if len(regime_examples) < total_required:
            raise ValueError(
                f"Benchmark regime {regime!r} has {len(regime_examples)} examples, "
                f"but the pilot requires at least {total_required}."
            )
        random.Random(cfg.split_seed).shuffle(regime_examples)

    dev_gepa: list[AdvancedIFExample] = []
    main_eval: list[AdvancedIFExample] = []
    transfer_probe: list[AdvancedIFExample] = []
    carryover_by_regime: dict[str, list[AdvancedIFExample]] = {}

    for regime in BENCHMARK_REGIMES:
        regime_examples = grouped[regime]
        dev_end = PILOT_SPLIT_COUNTS["dev_gepa"]
        main_end = dev_end + PILOT_SPLIT_COUNTS["main_eval"]
        carry_end = main_end + PILOT_SPLIT_COUNTS["carryover_sequences"]
        transfer_end = carry_end + PILOT_SPLIT_COUNTS["transfer_probe"]

        dev_gepa.extend(regime_examples[:dev_end])
        main_eval.extend(regime_examples[dev_end:main_end])
        carryover_by_regime[regime] = regime_examples[main_end:carry_end]
        transfer_probe.extend(regime_examples[carry_end:transfer_end])

    sequences: list[list[AdvancedIFExample]] = [[], [], []]
    orderings = [
        BENCHMARK_REGIMES,
        (BENCHMARK_REGIMES[1], BENCHMARK_REGIMES[2], BENCHMARK_REGIMES[0]),
        (BENCHMARK_REGIMES[2], BENCHMARK_REGIMES[0], BENCHMARK_REGIMES[1]),
    ]
    for seq_idx, regime_order in enumerate(orderings):
        for round_idx in range(3):
            for regime in regime_order:
                carry_index = seq_idx * 3 + round_idx
                sequences[seq_idx].append(carryover_by_regime[regime][carry_index])

    return BenchmarkSplits(
        dev_gepa=dev_gepa,
        main_eval=main_eval,
        carryover_sequences=sequences,
        transfer_probe=transfer_probe,
    )


def flatten_carryover_sequences(bundle: BenchmarkSplits) -> list[AdvancedIFExample]:
    return [example for sequence in bundle.carryover_sequences for example in sequence]


def get_examples_for_split(cfg: EnvironmentConfig) -> list[AdvancedIFExample]:
    all_examples = load_examples(cfg)
    grouped_counts = {
        regime: sum(1 for example in all_examples if example.benchmark_name == regime)
        for regime in BENCHMARK_REGIMES
    }
    if grouped_counts and min(grouped_counts.values()) < sum(PILOT_SPLIT_COUNTS.values()):
        examples = (
            list(all_examples[: cfg.max_examples])
            if cfg.max_examples is not None
            else list(all_examples)
        )
        return examples

    bundle = build_benchmark_splits(cfg)
    if cfg.benchmark_split == "dev_gepa":
        examples = bundle.dev_gepa
    elif cfg.benchmark_split == "main_eval":
        examples = bundle.main_eval
    elif cfg.benchmark_split == "transfer_probe":
        examples = bundle.transfer_probe
    else:
        examples = flatten_carryover_sequences(bundle)

    if cfg.max_examples is not None:
        return list(examples[: cfg.max_examples])
    return list(examples)


def build_rollout_input(
    example: AdvancedIFExample,
    initial_skill_markdown: str | None = None,
) -> RolloutInput:
    return RolloutInput(
        prompt=list(example.conversation),
        answer=json.dumps(example.gold_rubrics, ensure_ascii=False),
        task=f"advancedif::{example.benchmark_name}",
        example_id=example.example_id,
        info={
            "benchmark_name": example.benchmark_name,
            "conversation": example.conversation,
            "initial_skill_markdown": initial_skill_markdown or EMPTY_SKILL_TEMPLATE,
        },
    )


def build_dataset(cfg: EnvironmentConfig) -> Dataset:
    rows = [
        build_rollout_input(example, initial_skill_markdown=cfg.initial_skill_markdown)
        for example in get_examples_for_split(cfg)
    ]
    return Dataset.from_list(rows)


def materialize_rlm_context(
    context_root: str | Path,
    example: AdvancedIFExample,
    skill_markdown: str,
) -> str:
    root = Path(context_root)
    root.mkdir(parents=True, exist_ok=True)
    workspace = root / f"{example.example_id:06d}_{safe_segment(example.benchmark_name)}"
    if workspace.exists():
        shutil.rmtree(workspace)
    traj_dir = workspace / "trajectory"
    traj_dir.mkdir(parents=True, exist_ok=True)

    file_names: list[str] = []
    for idx, message in enumerate(example.conversation):
        role = str(message.get("role", "unknown"))
        file_name = f"{idx:04d}_{safe_segment(role, 16)}.txt"
        content = message.get("content", "")
        if isinstance(content, list):
            text = json.dumps(content, ensure_ascii=False)
        else:
            text = str(content)
        (traj_dir / file_name).write_text(text, encoding="utf-8")
        file_names.append(file_name)

    (traj_dir / "manifest.json").write_text(
        json.dumps({"files": file_names}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    write_skill(workspace / "skill.md", skill_markdown)
    return str(workspace.resolve())
