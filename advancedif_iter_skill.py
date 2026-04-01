from __future__ import annotations

from typing import Any

import verifiers as vf
from core.config import EnvironmentConfig
from core.iter_env import IterSkillEnv


def load_environment(
    config: EnvironmentConfig | dict[str, Any] | None = None, **kwargs: Any
) -> vf.Environment:
    if isinstance(config, EnvironmentConfig):
        env_config = config
        env_kwargs = dict(kwargs)
    else:
        merged = dict(config) if isinstance(config, dict) else {}
        merged.update(kwargs)
        config_fields = set(EnvironmentConfig.__dataclass_fields__)
        env_config = EnvironmentConfig.from_input(
            {key: value for key, value in merged.items() if key in config_fields}
        )
        env_kwargs = {key: value for key, value in merged.items() if key not in config_fields}
    return IterSkillEnv(env_config, **env_kwargs)
