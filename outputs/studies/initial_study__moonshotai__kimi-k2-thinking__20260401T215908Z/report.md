# AdvancedIF Initial Study Report

## Setup

- Model: `moonshotai/kimi-k2-thinking`
- Judge model: `deepseek/deepseek-v3.2`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__moonshotai__kimi-k2-thinking__20260401T215908Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.5342                 | 0.2000            | 0.0000                | 0.0          | 0.0000             | 0.0000      | 1.0000     |
| RLM                      | 0.5342                 | 0.2000            | 0.0000                | 0.0          | 0.0000             | 0.0000      | 1.0000     |
| GEPA-optimized iterative | 0.5342                 | 0.2000            | 0.0000                | 0.0          | 0.0000             | 0.0000      | 1.0000     |


## Paired Deltas

- Paired examples: 10
- `reward_delta_rlm_minus_iter`: 0.0000 (95% CI 0.0000 to 0.0000)
- `efficiency_delta_rlm_minus_iter`: 0.0000 (95% CI 0.0000 to 0.0000)
- RLM reward win rate across paired examples: 0.0000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.4667
- Transfer frozen mean: 0.3643
- Transfer empty-control mean: 0.3643
- `transfer_lift_mean`: 0.0000
- Transfer pairs: 5
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: -0.0833
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.5000                 | 0.0000                |
| 1          | 126.0       | 0.5000                 | 0.0000                |
| 2          | 126.0       | 1.0000                 | 0.0000                |
| 3          | 126.0       | 0.0000                 | 0.0000                |
| 4          | 126.0       | 0.3333                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? Inconclusive. The paired reward delta is 0.0000.
- Q2. Is it more token-efficient? Inconclusive. The efficiency delta is 0.0000.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0000.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.5342. `gepa_minus_iter` is 0.0000, and `gepa_minus_rlm` is 0.0000.
- GEPA best validation score: 0.6667

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__moonshotai__kimi-k2-thinking__20260401T215908Z/evals/advancedif_iter_skill--moonshotai--kimi-k2-thinking/44f8e49b`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__moonshotai__kimi-k2-thinking__20260401T215908Z/evals/advancedif_rlm_skill--moonshotai--kimi-k2-thinking/c45d1d2a`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__moonshotai__kimi-k2-thinking__20260401T215908Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__moonshotai__kimi-k2-thinking__20260401T215908Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__moonshotai__kimi-k2-thinking__20260401T215908Z/evals/advancedif_iter_skill--moonshotai--kimi-k2-thinking/93e320df`

