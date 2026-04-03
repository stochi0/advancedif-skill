# Judge Calls Comparison Report

Generated at (UTC): `2026-04-03 09:17:12Z`

Inclusion rule: only studies whose directory contains both `report.md` and `study_summary.json`.

Total eligible studies: **26**

## Overall comparison

- Iterative env (`advancedif_iter_skill`) average `judge_calls_mean`: **1.026843**
- RLM env (`advancedif_rlm_skill`) average `judge_calls_mean`: **0.778245**
- Average delta (`rlm - iter`): **-0.248598**
- Conclusion: **RLM uses fewer judge calls on average** across eligible studies.
- Studies where Iterative used fewer calls: **3**
- Studies where RLM used fewer calls: **13**
- Studies tied: **10**

## Per-model averages

| Model | Studies | Iter avg | RLM avg | Delta (RLM-Iter) | Lower-calls env |
|---|---:|---:|---:|---:|---|
| `PrimeIntellect/INTELLECT-3.1` | 2 | 1.000000 | 1.000000 | 0.000000 | Tie |
| `PrimeIntellect/Qwen3-0.6B-Reverse-Text-SFT` | 1 | 0.375000 | 0.000000 | -0.375000 | RLM |
| `anthropic/claude-sonnet-4.6` | 1 | 1.125000 | 1.500000 | 0.375000 | Iterative |
| `google/gemini-2.5-flash` | 2 | 1.000000 | 0.500000 | -0.500000 | RLM |
| `moonshotai/kimi-k2-thinking` | 1 | 0.000000 | 0.000000 | 0.000000 | Tie |
| `openai/gpt-4.1-mini` | 9 | 1.000000 | 0.991319 | -0.008681 | RLM |
| `openai/gpt-5-mini` | 4 | 0.986979 | 0.755208 | -0.231771 | RLM |
| `openai/gpt-5.2` | 1 | 2.375000 | 1.291667 | -1.083333 | RLM |
| `qwen/qwen3-coder` | 1 | 0.875000 | 1.000000 | 0.125000 | Iterative |
| `z-ai/glm-4.7` | 2 | 1.500000 | 0.125000 | -1.375000 | RLM |
| `z-ai/glm-5` | 2 | 1.000000 | 0.625000 | -0.375000 | RLM |

## Per-study details

| Study | Model | Feedback mode | Iter calls mean | RLM calls mean | Delta (RLM-Iter) | Lower-calls env |
|---|---|---|---:|---:|---:|---|
| `initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221003Z` | `PrimeIntellect/INTELLECT-3.1` | `score_only` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221010Z` | `PrimeIntellect/INTELLECT-3.1` | `score_only` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__PrimeIntellect__Qwen3-0.6B-Reverse-Text-SFT__20260401T215851Z` | `PrimeIntellect/Qwen3-0.6B-Reverse-Text-SFT` | `score_only` | 0.375000 | 0.000000 | -0.375000 | RLM |
| `initial_study__anthropic__claude-sonnet-4.6__20260401T215702Z` | `anthropic/claude-sonnet-4.6` | `one_violation` | 1.125000 | 1.500000 | 0.375000 | Iterative |
| `initial_study__google__gemini-2.5-flash__20260401T214916Z` | `google/gemini-2.5-flash` | `none` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__google__gemini-2.5-flash__20260401T215718Z` | `google/gemini-2.5-flash` | `none` | 1.000000 | 0.000000 | -1.000000 | RLM |
| `initial_study__moonshotai__kimi-k2-thinking__20260401T215908Z` | `moonshotai/kimi-k2-thinking` | `score_only` | 0.000000 | 0.000000 | 0.000000 | Tie |
| `initial_study__openai__gpt-4.1-mini__20260401T173837Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__openai__gpt-4.1-mini__20260401T174021Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__openai__gpt-4.1-mini__20260401T174507Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__openai__gpt-4.1-mini__20260401T201333Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__openai__gpt-4.1-mini__20260401T203051Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 1.125000 | 0.125000 | Iterative |
| `initial_study__openai__gpt-4.1-mini__20260401T211615Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 0.937500 | -0.062500 | RLM |
| `initial_study__openai__gpt-4.1-mini__20260401T212224Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 0.937500 | -0.062500 | RLM |
| `initial_study__openai__gpt-4.1-mini__20260401T212354Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 0.921875 | -0.078125 | RLM |
| `initial_study__openai__gpt-4.1-mini__20260402T091321Z` | `openai/gpt-4.1-mini` | `score_only` | 1.000000 | 1.000000 | 0.000000 | Tie |
| `initial_study__openai__gpt-5-mini__20260401T215305Z` | `openai/gpt-5-mini` | `one_violation` | 0.000000 | 0.000000 | 0.000000 | Tie |
| `initial_study__openai__gpt-5-mini__20260401T215347Z` | `openai/gpt-5-mini` | `score_only` | 1.500000 | 1.000000 | -0.500000 | RLM |
| `initial_study__openai__gpt-5-mini__20260401T215637Z` | `openai/gpt-5-mini` | `score_only` | 1.416667 | 1.083333 | -0.333333 | RLM |
| `initial_study__openai__gpt-5-mini__20260401T222804Z` | `openai/gpt-5-mini` | `none` | 1.031250 | 0.937500 | -0.093750 | RLM |
| `initial_study__openai__gpt-5.2__20260401T215757Z` | `openai/gpt-5.2` | `score_only` | 2.375000 | 1.291667 | -1.083333 | RLM |
| `initial_study__qwen__qwen3-coder__20260401T215648Z` | `qwen/qwen3-coder` | `one_violation` | 0.875000 | 1.000000 | 0.125000 | Iterative |
| `initial_study__z-ai__glm-4.7__20260401T235624Z` | `z-ai/glm-4.7` | `score_only` | 1.000000 | 0.000000 | -1.000000 | RLM |
| `initial_study__z-ai__glm-4.7__20260402T000637Z` | `z-ai/glm-4.7` | `score_only` | 2.000000 | 0.250000 | -1.750000 | RLM |
| `initial_study__z-ai__glm-5__20260401T232656Z` | `z-ai/glm-5` | `none` | 1.000000 | 0.750000 | -0.250000 | RLM |
| `initial_study__z-ai__glm-5__20260402T000446Z` | `z-ai/glm-5` | `none` | 1.000000 | 0.500000 | -0.500000 | RLM |
