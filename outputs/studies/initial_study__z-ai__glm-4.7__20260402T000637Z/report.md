# AdvancedIF Initial Study Report

## Setup

- Model: `z-ai/glm-4.7`
- Judge model: `deepseek/deepseek-v3.2`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260402T000637Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant   | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --------- | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative | 0.7778                 | 0.5000            | -0.0278               | 58606.0      | 0.2576             | 2.0000      | 0.0000     |
| RLM       | 0.6167                 | 0.2500            | 0.0000                | 11902.5      | 0.0497             | 0.2500      | 0.0000     |


## Paired Deltas

- Paired examples: 4
- `reward_delta_rlm_minus_iter`: -0.1611 (95% CI -0.7668 to 0.4446)
- `efficiency_delta_rlm_minus_iter`: -0.2079 (95% CI -0.3877 to -0.0281)
- RLM reward win rate across paired examples: 0.5000
- RLM efficiency win rate across paired examples: 0.2500

## Carryover And Transfer

- Carryover reward mean: 0.9167
- Transfer frozen mean: 0.5000
- Transfer empty-control mean: 0.9286
- `transfer_lift_mean`: -0.4286
- Transfer pairs: 2
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.1667
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.8333                 | 0.0000                |
| 1          | 126.0       | 1.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.1611.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.2079.
- Q3. Do models in this setup write skills that generalize to other tasks? No. The transfer lift is -0.4286.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? No. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260402T000637Z/evals/advancedif_iter_skill--z-ai--glm-4.7/a6f0e962`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260402T000637Z/evals/advancedif_rlm_skill--z-ai--glm-4.7/5ca6e9dd`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260402T000637Z/sequence_run`

