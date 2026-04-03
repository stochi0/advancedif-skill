# AdvancedIF Initial Study Report

## Setup

- Model: `google/gemini-2.5-flash`
- Judge model: `google/gemini-2.5-pro`
- Feedback mode: `none`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T215718Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant   | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --------- | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative | 0.8715                 | 0.6429            | 0.0000                | 4637.2       | 0.2489             | 1.0000      | 0.0000     |
| RLM       | 0.1769                 | 0.1429            | 0.0000                | 0.0          | 0.0000             | 0.0000      | 1.0000     |


## Paired Deltas

- Paired examples: 14
- `reward_delta_rlm_minus_iter`: -0.6947 (95% CI -0.8808 to -0.5085)
- `efficiency_delta_rlm_minus_iter`: -0.2489 (95% CI -0.3112 to -0.1865)
- RLM reward win rate across paired examples: 0.0000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.8323
- Transfer frozen mean: 0.7995
- Transfer empty-control mean: 0.8827
- `transfer_lift_mean`: -0.0832
- Transfer pairs: 7
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.0020
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.6667                 | 0.0000                |
| 1          | 126.0       | 0.9286                 | 0.0000                |
| 2          | 126.0       | 0.9091                 | 0.0000                |
| 3          | 126.0       | 1.0000                 | 0.0000                |
| 4          | 126.0       | 0.5714                 | 0.0000                |
| 5          | 126.0       | 1.0000                 | 0.0000                |
| 6          | 126.0       | 0.7500                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.6947.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.2489.
- Q3. Do models in this setup write skills that generalize to other tasks? No. The transfer lift is -0.0832.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? No. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T215718Z/evals/advancedif_iter_skill--google--gemini-2.5-flash/9e3c42ee`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T215718Z/evals/advancedif_rlm_skill--google--gemini-2.5-flash/5ea62c64`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T215718Z/sequence_run`

