# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-4.1-mini`
- Judge model: `openai/gpt-4.1-mini`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212354Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics

| Variant | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Iterative | 0.9258 | 0.7188 | 0.0039 | 2942.3 | 0.4374 | 1.0000 | 0.0000 |
| RLM | 0.7290 | 0.5781 | 0.0000 | 12728.9 | 0.0613 | 0.9219 | 0.0000 |
| GEPA-optimized iterative | 0.9010 | 0.7344 | 0.0000 | 2767.4 | 0.4255 | 0.9844 | 0.0000 |

## Paired Deltas

- Paired examples: 64
- `reward_delta_rlm_minus_iter`: -0.1967 (95% CI -0.2917 to -0.1018)
- `efficiency_delta_rlm_minus_iter`: -0.3761 (95% CI -0.4296 to -0.3227)
- RLM reward win rate across paired examples: 0.0938
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.9619
- Transfer frozen mean: 0.8795
- Transfer empty-control mean: 0.8685
- `transfer_lift_mean`: 0.0111
- Transfer pairs: 18
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: -0.0133
- First-submission lift slope by task index: 0.0000

### Task-Index Means

| Task index | Skill words | Criterion satisfaction | First-submission lift |
| --- | ---: | ---: | ---: |
| 0 | 126.0 | 1.0000 | 0.0000 |
| 1 | 126.0 | 1.0000 | 0.0000 |
| 2 | 126.0 | 1.0000 | 0.0000 |
| 3 | 126.0 | 1.0000 | 0.0000 |
| 4 | 126.0 | 0.8571 | 0.0000 |
| 5 | 126.0 | 1.0000 | 0.0000 |
| 6 | 126.0 | 1.0000 | 0.0000 |
| 7 | 126.0 | 1.0000 | 0.0000 |
| 8 | 126.0 | 0.8000 | 0.0000 |

## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.1967.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.3761.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0111.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.9010. `gepa_minus_iter` is -0.0247, and `gepa_minus_rlm` is 0.1720.
- GEPA best validation score: 1.0000

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212354Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/c5b84f8c`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212354Z/evals/advancedif_rlm_skill--openai--gpt-4.1-mini/e16cef0c`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212354Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212354Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212354Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/de5ffe8f`
