# AdvancedIF Initial Study Report

## Setup

- Model: `z-ai/glm-4.7`
- Judge model: `deepseek/deepseek-v3.2`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260401T235624Z`
- Sequence harness used: `advancedif_rlm_skill`

## Aggregate Metrics


| Variant   | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --------- | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative | 0.7778                 | 0.0000            | 0.0000                | 2474.0       | 0.3366             | 1.0000      | 0.0000     |
| RLM       | 0.8333                 | 0.5000            | 0.0000                | 13545.5      | 0.0612             | 0.0000      | 0.0000     |


## Paired Deltas

- Paired examples: 2
- `reward_delta_rlm_minus_iter`: 0.0556 (95% CI -0.2711 to 0.3822)
- `efficiency_delta_rlm_minus_iter`: -0.2754 (95% CI -0.4249 to -0.1260)
- RLM reward win rate across paired examples: 0.5000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.5000
- Transfer frozen mean: 0.5000
- Transfer empty-control mean: 0.5000
- `transfer_lift_mean`: 0.0000
- Transfer pairs: 2
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.0000
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.5000                 | 0.0000                |
| 1          | 126.0       | 0.5000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? Yes. The paired reward delta is 0.0556.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.2754.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0000.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `advancedif_rlm_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260401T235624Z/evals/advancedif_iter_skill--z-ai--glm-4.7/551b2631`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260401T235624Z/evals/advancedif_rlm_skill--z-ai--glm-4.7/b3b3b7d1`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__z-ai__glm-4.7__20260401T235624Z/sequence_run`

