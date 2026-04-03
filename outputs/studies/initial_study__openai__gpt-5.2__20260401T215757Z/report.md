# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-5.2`
- Judge model: `openai/gpt-4.1-nano`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5.2__20260401T215757Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.9140                 | 0.7500            | 0.0423                | 8561.8       | 0.1910             | 2.3750      | 0.0000     |
| RLM                      | 0.7856                 | 0.6667            | -0.0579               | 12554.5      | 0.0684             | 1.2917      | 0.0000     |
| GEPA-optimized iterative | 0.9493                 | 0.7917            | 0.0434                | 6252.9       | 0.1795             | 2.1667      | 0.0000     |


## Paired Deltas

- Paired examples: 24
- `reward_delta_rlm_minus_iter`: -0.1283 (95% CI -0.2658 to 0.0092)
- `efficiency_delta_rlm_minus_iter`: -0.1226 (95% CI -0.1677 to -0.0774)
- RLM reward win rate across paired examples: 0.1250
- RLM efficiency win rate across paired examples: 0.1250

## Carryover And Transfer

- Carryover reward mean: 0.9722
- Transfer frozen mean: 0.9315
- Transfer empty-control mean: 0.9539
- `transfer_lift_mean`: -0.0223
- Transfer pairs: 12
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: -0.0042
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 1.0000                 | 0.0000                |
| 1          | 126.0       | 1.0000                 | 0.0000                |
| 2          | 126.0       | 1.0000                 | 0.0000                |
| 3          | 126.0       | 1.0000                 | 0.0000                |
| 4          | 126.0       | 1.0000                 | 0.0000                |
| 5          | 126.0       | 0.7500                 | 0.0000                |
| 6          | 126.0       | 1.0000                 | 0.0000                |
| 7          | 126.0       | 1.0000                 | 0.0000                |
| 8          | 126.0       | 1.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.1283.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.1226.
- Q3. Do models in this setup write skills that generalize to other tasks? No. The transfer lift is -0.0223.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? No. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.9493. `gepa_minus_iter` is 0.0354, and `gepa_minus_rlm` is 0.1637.
- GEPA best validation score: 1.0000

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5.2__20260401T215757Z/evals/advancedif_iter_skill--openai--gpt-5.2/c3b23f48`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5.2__20260401T215757Z/evals/advancedif_rlm_skill--openai--gpt-5.2/fb5fa7ad`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5.2__20260401T215757Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5.2__20260401T215757Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5.2__20260401T215757Z/evals/advancedif_iter_skill--openai--gpt-5.2/254aab11`

