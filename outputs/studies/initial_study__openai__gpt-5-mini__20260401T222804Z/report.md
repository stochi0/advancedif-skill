# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-5-mini`
- Judge model: `deepseek/deepseek-v3.2`
- Feedback mode: `none`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T222804Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant   | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --------- | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative | 0.9271                 | 0.7812            | 0.0000                | 5142.4       | 0.2123             | 1.0312      | 0.0000     |
| RLM       | 0.8506                 | 0.5938            | 0.0000                | 12822.1      | 0.0742             | 0.9375      | 0.0000     |


## Paired Deltas

- Paired examples: 32
- `reward_delta_rlm_minus_iter`: -0.0765 (95% CI -0.1847 to 0.0318)
- `efficiency_delta_rlm_minus_iter`: -0.1381 (95% CI -0.1680 to -0.1082)
- RLM reward win rate across paired examples: 0.1250
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.9778
- Transfer frozen mean: 0.7429
- Transfer empty-control mean: 0.8689
- `transfer_lift_mean`: -0.1260
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
| 4          | 126.0       | 1.0000                 | 0.0000                |
| 5          | 126.0       | 1.0000                 | 0.0000                |
| 6          | 126.0       | 1.0000                 | 0.0000                |
| 7          | 126.0       | 1.0000                 | 0.0000                |
| 8          | 126.0       | 0.8000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.0765.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.1381.
- Q3. Do models in this setup write skills that generalize to other tasks? No. The transfer lift is -0.1260.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? No. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T222804Z/evals/advancedif_iter_skill--openai--gpt-5-mini/1a0d2223`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T222804Z/evals/advancedif_rlm_skill--openai--gpt-5-mini/500d571f`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T222804Z/sequence_run`

