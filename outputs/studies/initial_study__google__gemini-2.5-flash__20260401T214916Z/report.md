# AdvancedIF Initial Study Report

## Setup

- Model: `google/gemini-2.5-flash`
- Judge model: `google/gemini-2.5-pro`
- Feedback mode: `none`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T214916Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.7856                 | 0.3125            | 0.0000                | 5061.3       | 0.2209             | 1.0000      | 0.0000     |
| RLM                      | 0.2173                 | 0.1875            | 0.0000                | 2670.2       | 0.0697             | 1.0000      | 1.0000     |
| GEPA-optimized iterative | 0.8576                 | 0.5625            | 0.0000                | 5069.6       | 0.2568             | 0.9375      | 0.0000     |


## Paired Deltas

- Paired examples: 16
- `reward_delta_rlm_minus_iter`: -0.5683 (95% CI -0.7773 to -0.3594)
- `efficiency_delta_rlm_minus_iter`: -0.1512 (95% CI -0.2450 to -0.0575)
- RLM reward win rate across paired examples: 0.1250
- RLM efficiency win rate across paired examples: 0.1875

## Carryover And Transfer

- Carryover reward mean: 0.8644
- Transfer frozen mean: 0.8579
- Transfer empty-control mean: 0.7807
- `transfer_lift_mean`: 0.0772
- Transfer pairs: 8
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.0155
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 0.6667                 | 0.0000                |
| 1          | 126.0       | 0.8571                 | 0.0000                |
| 2          | 126.0       | 0.9091                 | 0.0000                |
| 3          | 126.0       | 1.0000                 | 0.0000                |
| 4          | 126.0       | 0.8571                 | 0.0000                |
| 5          | 126.0       | 1.0000                 | 0.0000                |
| 6          | 126.0       | 0.6250                 | 0.0000                |
| 7          | 126.0       | 1.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.5683.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.1512.
- Q3. Do models in this setup write skills that generalize to other tasks? Yes. The transfer lift is 0.0772.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Weak yes. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.8576. `gepa_minus_iter` is 0.0720, and `gepa_minus_rlm` is 0.6404.
- GEPA best validation score: 0.8333

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T214916Z/evals/advancedif_iter_skill--google--gemini-2.5-flash/1087f40b`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T214916Z/evals/advancedif_rlm_skill--google--gemini-2.5-flash/ea082513`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T214916Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T214916Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__google__gemini-2.5-flash__20260401T214916Z/evals/advancedif_iter_skill--google--gemini-2.5-flash/89d5809c`

