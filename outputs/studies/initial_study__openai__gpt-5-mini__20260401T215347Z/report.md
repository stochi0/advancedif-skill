# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-5-mini`
- Judge model: `openai/gpt-4.1-nano`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215347Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant   | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --------- | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative | 0.9844                 | 0.8750            | 0.0000                | 7142.5       | 0.1708             | 1.5000      | 0.0000     |
| RLM       | 1.0000                 | 1.0000            | 0.0000                | 10701.8      | 0.1112             | 1.0000      | 0.0000     |


## Paired Deltas

- Paired examples: 8
- `reward_delta_rlm_minus_iter`: 0.0156 (95% CI -0.0150 to 0.0462)
- `efficiency_delta_rlm_minus_iter`: -0.0596 (95% CI -0.1048 to -0.0143)
- RLM reward win rate across paired examples: 0.1250
- RLM efficiency win rate across paired examples: 0.2500

## Carryover And Transfer

- Carryover reward mean: 0.9722
- Transfer frozen mean: 0.7237
- Transfer empty-control mean: 0.9308
- `transfer_lift_mean`: -0.2071
- Transfer pairs: 8
- Skill length slope by task index: 10.0000
- Carryover reward slope by task index: 0.0026
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 1.0000                 | 0.0000                |
| 1          | 126.0       | 1.0000                 | 0.0000                |
| 2          | 126.0       | 1.0000                 | 0.0000                |
| 3          | 126.0       | 0.7778                 | 0.0000                |
| 4          | 126.0       | 1.0000                 | 0.0000                |
| 5          | 126.0       | 1.0000                 | 0.0000                |
| 6          | 196.0       | 1.0000                 | 0.0000                |
| 7          | 196.0       | 1.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? Inconclusive. The paired reward delta is 0.0156.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.0596.
- Q3. Do models in this setup write skills that generalize to other tasks? No. The transfer lift is -0.2071.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? No. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215347Z/evals/advancedif_iter_skill--openai--gpt-5-mini/4657be06`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215347Z/evals/advancedif_rlm_skill--openai--gpt-5-mini/3d616902`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215347Z/sequence_run`

