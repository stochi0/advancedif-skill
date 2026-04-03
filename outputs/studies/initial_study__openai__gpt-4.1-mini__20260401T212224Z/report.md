# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-4.1-mini`
- Judge model: `openai/gpt-4.1-mini`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212224Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.9338                 | 0.8438            | 0.0000                | 1919.2       | 0.5636             | 1.0000      | 0.0000     |
| RLM                      | 0.6803                 | 0.5312            | -0.0312               | 12690.8      | 0.0667             | 0.9375      | 0.0000     |
| GEPA-optimized iterative | 0.9335                 | 0.8438            | 0.0000                | 1921.2       | 0.5747             | 0.9688      | 0.0000     |


## Paired Deltas

- Paired examples: 32
- `reward_delta_rlm_minus_iter`: -0.2535 (95% CI -0.4065 to -0.1004)
- `efficiency_delta_rlm_minus_iter`: -0.4969 (95% CI -0.5607 to -0.4332)
- RLM reward win rate across paired examples: 0.0625
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.9619
- Transfer frozen mean: 0.9059
- Transfer empty-control mean: 0.8421
- `transfer_lift_mean`: 0.0638
- Transfer pairs: 18
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: -0.0133
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 1.0000                 | 0.0000                |
| 1          | 126.0       | 1.0000                 | 0.0000                |
| 2          | 126.0       | 1.0000                 | 0.0000                |
| 3          | 126.0       | 1.0000                 | 0.0000                |
| 4          | 126.0       | 0.8571                 | 0.0000                |
| 5          | 126.0       | 1.0000                 | 0.0000                |
| 6          | 126.0       | 1.0000                 | 0.0000                |
| 7          | 126.0       | 1.0000                 | 0.0000                |
| 8          | 126.0       | 0.8000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.2535.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.4969.
- Q3. Do models in this setup write skills that generalize to other tasks? Yes. The transfer lift is 0.0638.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.9335. `gepa_minus_iter` is -0.0002, and `gepa_minus_rlm` is 0.2532.
- GEPA best validation score: 1.0000

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212224Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/53e7bae5`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212224Z/evals/advancedif_rlm_skill--openai--gpt-4.1-mini/5470be80`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212224Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212224Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T212224Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/b7c60a6d`

