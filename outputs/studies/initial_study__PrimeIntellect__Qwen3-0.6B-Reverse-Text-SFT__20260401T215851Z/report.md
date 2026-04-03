# AdvancedIF Initial Study Report

## Setup

- Model: `PrimeIntellect/Qwen3-0.6B-Reverse-Text-SFT`
- Judge model: `z-ai/glm-5`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__Qwen3-0.6B-Reverse-Text-SFT__20260401T215851Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant   | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --------- | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative | 0.0000                 | 0.0000            | 0.0000                | 371.8        | 0.0000             | 0.3750      | 1.0000     |
| RLM       | 0.0000                 | 0.0000            | 0.0000                | 0.0          | 0.0000             | 0.0000      | 1.0000     |


## Paired Deltas

- Paired examples: 8
- `reward_delta_rlm_minus_iter`: 0.0000 (95% CI 0.0000 to 0.0000)
- `efficiency_delta_rlm_minus_iter`: 0.0000 (95% CI 0.0000 to 0.0000)
- RLM reward win rate across paired examples: 0.0000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.2143
- Transfer frozen mean: 0.0000
- Transfer empty-control mean: 0.0000
- `transfer_lift_mean`: 0.0000
- Transfer pairs: 4
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: -0.0857
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.0000                 | 0.0000                |
| 1          | 126.0       | 0.8571                 | 0.0000                |
| 2          | 126.0       | 0.0000                 | 0.0000                |
| 3          | 126.0       | 0.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? Inconclusive. The paired reward delta is 0.0000.
- Q2. Is it more token-efficient? Inconclusive. The efficiency delta is 0.0000.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0000.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__Qwen3-0.6B-Reverse-Text-SFT__20260401T215851Z/evals/advancedif_iter_skill--PrimeIntellect--Qwen3-0.6B-Reverse-Text-SFT/197e4280`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__Qwen3-0.6B-Reverse-Text-SFT__20260401T215851Z/evals/advancedif_rlm_skill--PrimeIntellect--Qwen3-0.6B-Reverse-Text-SFT/4de47cf1`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__Qwen3-0.6B-Reverse-Text-SFT__20260401T215851Z/sequence_run`

