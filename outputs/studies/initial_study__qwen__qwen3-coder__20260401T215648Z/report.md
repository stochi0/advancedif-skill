# AdvancedIF Initial Study Report

## Setup

- Model: `qwen/qwen3-coder`
- Judge model: `deepseek/deepseek-v3.2`
- Feedback mode: `one_violation`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__qwen__qwen3-coder__20260401T215648Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.4736                 | 0.1875            | 0.0000                | 1733.8       | 0.2602             | 0.8750      | 0.0000     |
| RLM                      | 0.2188                 | 0.1875            | 0.0000                | 1890.8       | 0.1192             | 1.0000      | 0.0000     |
| GEPA-optimized iterative | 0.4860                 | 0.3125            | 0.0000                | 1728.9       | 0.2666             | 0.6250      | 0.0000     |


## Paired Deltas

- Paired examples: 16
- `reward_delta_rlm_minus_iter`: -0.2548 (95% CI -0.4720 to -0.0377)
- `efficiency_delta_rlm_minus_iter`: -0.1409 (95% CI -0.2431 to -0.0387)
- RLM reward win rate across paired examples: 0.1250
- RLM efficiency win rate across paired examples: 0.1250

## Carryover And Transfer

- Carryover reward mean: 0.5061
- Transfer frozen mean: 0.5850
- Transfer empty-control mean: 0.6391
- `transfer_lift_mean`: -0.0542
- Transfer pairs: 8
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.1505
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.0000                 | 0.0000                |
| 1          | 126.0       | 0.0000                 | 0.0000                |
| 2          | 126.0       | 0.7273                 | 0.0000                |
| 3          | 126.0       | 0.0000                 | 0.0000                |
| 4          | 126.0       | 0.5714                 | 0.0000                |
| 5          | 126.0       | 0.7500                 | 0.0000                |
| 6          | 126.0       | 1.0000                 | 0.0000                |
| 7          | 126.0       | 1.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.2548.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.1409.
- Q3. Do models in this setup write skills that generalize to other tasks? No. The transfer lift is -0.0542.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? No. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.4860. `gepa_minus_iter` is 0.0124, and `gepa_minus_rlm` is 0.2672.
- GEPA best validation score: 0.6667

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__qwen__qwen3-coder__20260401T215648Z/evals/advancedif_iter_skill--qwen--qwen3-coder/ad33cf6f`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__qwen__qwen3-coder__20260401T215648Z/evals/advancedif_rlm_skill--qwen--qwen3-coder/2f344574`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__qwen__qwen3-coder__20260401T215648Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__qwen__qwen3-coder__20260401T215648Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__qwen__qwen3-coder__20260401T215648Z/evals/advancedif_iter_skill--qwen--qwen3-coder/d56fbb8e`

