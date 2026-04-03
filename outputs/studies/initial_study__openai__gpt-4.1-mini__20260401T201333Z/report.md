# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-4.1-mini`
- Judge model: `openai/gpt-4.1-mini`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T201333Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 1.0000                 | 1.0000            | 0.0000                | 1469.0       | 0.7074             | 1.0000      | 0.0000     |
| RLM                      | 1.0000                 | 1.0000            | 0.0000                | 8493.0       | 0.1182             | 1.0000      | 0.0000     |
| GEPA-optimized iterative | 1.0000                 | 1.0000            | 0.0000                | 1508.0       | 0.6879             | 1.0000      | 0.0000     |


## Paired Deltas

- Paired examples: 2
- `reward_delta_rlm_minus_iter`: 0.0000 (95% CI 0.0000 to 0.0000)
- `efficiency_delta_rlm_minus_iter`: -0.5891 (95% CI -0.8729 to -0.3053)
- RLM reward win rate across paired examples: 0.0000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 1.0000
- Transfer frozen mean: 1.0000
- Transfer empty-control mean: 1.0000
- `transfer_lift_mean`: 0.0000
- Transfer pairs: 3
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.0000
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 1.0000                 | 0.0000                |
| 1          | 126.0       | 1.0000                 | 0.0000                |
| 2          | 126.0       | 1.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? Inconclusive. The paired reward delta is 0.0000.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.5891.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0000.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 1.0000. `gepa_minus_iter` is 0.0000, and `gepa_minus_rlm` is 0.0000.
- GEPA best validation score: 1.0000

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T201333Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/92d20164`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T201333Z/evals/advancedif_rlm_skill--openai--gpt-4.1-mini/caac3a34`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T201333Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T201333Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T201333Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/b6f5448a`

