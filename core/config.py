from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

from verifiers.types import ClientConfig

PINFERENCE_API_BASE_URL = "https://api.pinference.ai/api/v1"
PINFERENCE_API_KEY_VAR = "PRIME_API_KEY"

BENCHMARK_REGIMES = (
    "complex_if_single_turn_v5",
    "carried_context_multi_turn_eval_v5",
    "system_steerability_v2",
)

PILOT_SPLIT_COUNTS = {
    "dev_gepa": 15,
    "main_eval": 30,
    "carryover_sequences": 9,
    "transfer_probe": 6,
}


def default_client_config() -> ClientConfig:
    return ClientConfig(
        api_key_var=PINFERENCE_API_KEY_VAR,
        api_base_url=PINFERENCE_API_BASE_URL,
    )


@dataclass(frozen=True)
class EnvironmentConfig:
    dataset_name: str = "facebook/AdvancedIF"
    dataset_split: str = "train"
    benchmark_split: Literal["dev_gepa", "main_eval", "carryover_sequences", "transfer_probe"] = (
        "main_eval"
    )
    max_examples: int | None = None
    split_seed: int = 7
    feedback_mode: Literal["score_only", "one_violation", "none"] = "score_only"
    allow_skill_updates: bool = True
    initial_skill_markdown: str | None = None
    max_turns: int = 6
    system_prompt_override: str | None = None
    judge_model: str = "z-ai/glm-4.7"
    judge_sampling_args: dict[str, Any] = field(default_factory=lambda: {"temperature": 0.0})
    judge_client_config: ClientConfig = field(default_factory=default_client_config)
    judge_client: Any | None = field(default=None, repr=False, compare=False)
    dataset_rows: list[dict[str, Any]] | None = field(default=None, repr=False, compare=False)
    output_root: str | None = None
    cache_dir: str | None = None
    context_parent_dir: str | None = None

    @classmethod
    def from_input(
        cls, cfg: EnvironmentConfig | dict[str, Any] | None, **kwargs: Any
    ) -> EnvironmentConfig:
        if isinstance(cfg, cls):
            return cfg

        raw: dict[str, Any] = dict(cfg) if isinstance(cfg, dict) else {}
        raw.update(kwargs)

        jcc_raw = raw.pop("judge_client_config", None)
        merged_cc = default_client_config().model_dump(mode="python")
        if isinstance(jcc_raw, ClientConfig):
            merged_cc.update(jcc_raw.model_dump(mode="python"))
        elif isinstance(jcc_raw, dict):
            merged_cc.update(jcc_raw)

        allowed = {k: v for k, v in raw.items() if k in cls.__dataclass_fields__}
        allowed["judge_client_config"] = ClientConfig.model_validate(merged_cc)
        return cls(**allowed)

    @property
    def package_root(self) -> Path:
        return Path(__file__).resolve().parent.parent

    @property
    def resolved_output_root(self) -> Path:
        if self.output_root:
            return Path(self.output_root).expanduser().resolve()
        return self.package_root / "outputs"

    @property
    def resolved_cache_dir(self) -> Path:
        if self.cache_dir:
            return Path(self.cache_dir).expanduser().resolve()
        return self.resolved_output_root / "judge_cache"

    @property
    def resolved_context_parent_dir(self) -> Path:
        if self.context_parent_dir:
            return Path(self.context_parent_dir).expanduser().resolve()
        return self.package_root / "contexts" / "rlm"
