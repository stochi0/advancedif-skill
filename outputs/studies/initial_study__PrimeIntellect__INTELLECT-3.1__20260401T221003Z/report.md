# AdvancedIF Initial Study Report

## Setup

- Model: `PrimeIntellect/INTELLECT-3.1`
- Judge model: `z-ai/glm-4.7`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221003Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.9259                 | 0.3333            | 0.0000                | 6255.3       | 0.1888             | 1.0000      | 0.0000     |
| RLM                      | 0.0000                 | 0.0000            | 0.0000                | 2981.3       | 0.0000             | 1.0000      | 0.0000     |
| GEPA-optimized iterative | 0.9259                 | 0.6667            | 0.0000                | 5375.7       | 0.1810             | 1.0000      | 0.0000     |


## Paired Deltas

- Paired examples: 3
- `reward_delta_rlm_minus_iter`: -0.9259 (95% CI -0.9985 to -0.8533)
- `efficiency_delta_rlm_minus_iter`: -0.1888 (95% CI -0.2952 to -0.0823)
- RLM reward win rate across paired examples: 0.0000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.6608
- Transfer frozen mean: 0.9750
- Transfer empty-control mean: 0.9214
- `transfer_lift_mean`: 0.0536
- Transfer pairs: 5
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.0172
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.6667                 | 0.0000                |
| 1          | 126.0       | 0.9231                 | 0.0000                |
| 2          | 126.0       | 0.0000                 | 0.0000                |
| 3          | 126.0       | 1.0000                 | 0.0000                |
| 4          | 126.0       | 0.7143                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.9259.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.1888.
- Q3. Do models in this setup write skills that generalize to other tasks? Yes. The transfer lift is 0.0536.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Weak yes. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.9259. `gepa_minus_iter` is 0.0000, and `gepa_minus_rlm` is 0.9259.
- GEPA best validation score: 0.3333

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221003Z/evals/advancedif_iter_skill--PrimeIntellect--INTELLECT-3.1/2421abbe`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221003Z/evals/advancedif_rlm_skill--PrimeIntellect--INTELLECT-3.1/8257725b`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221003Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221003Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__PrimeIntellect__INTELLECT-3.1__20260401T221003Z/evals/advancedif_iter_skill--PrimeIntellect--INTELLECT-3.1/b3dae83d`

