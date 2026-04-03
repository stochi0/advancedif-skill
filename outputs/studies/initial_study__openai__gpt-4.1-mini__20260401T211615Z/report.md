# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-4.1-mini`
- Judge model: `openai/gpt-4.1-mini`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T211615Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.9306                 | 0.8750            | 0.0000                | 1748.2       | 0.5707             | 1.0000      | 0.0000     |
| RLM                      | 0.7287                 | 0.6250            | 0.0000                | 12707.4      | 0.0688             | 0.9375      | 0.0000     |
| GEPA-optimized iterative | 0.9500                 | 0.9375            | 0.0000                | 1815.1       | 0.5937             | 0.9375      | 0.0000     |


## Paired Deltas

- Paired examples: 16
- `reward_delta_rlm_minus_iter`: -0.2019 (95% CI -0.3808 to -0.0229)
- `efficiency_delta_rlm_minus_iter`: -0.5019 (95% CI -0.5962 to -0.4077)
- RLM reward win rate across paired examples: 0.0625
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.9841
- Transfer frozen mean: 0.8705
- Transfer empty-control mean: 0.8648
- `transfer_lift_mean`: 0.0057
- Transfer pairs: 16
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.0000
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 1.0000                 | 0.0000                |
| 1          | 126.0       | 1.0000                 | 0.0000                |
| 2          | 126.0       | 1.0000                 | 0.0000                |
| 3          | 126.0       | 1.0000                 | 0.0000                |
| 4          | 126.0       | 0.8571                 | 0.0000                |
| 5          | 126.0       | 1.0000                 | 0.0000                |
| 6          | 126.0       | 1.0000                 | 0.0000                |
| 7          | 126.0       | 1.0000                 | 0.0000                |
| 8          | 126.0       | 1.0000                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.2019.
- Q2. Is it more token-efficient? No. The efficiency delta is -0.5019.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0057.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.9500. `gepa_minus_iter` is 0.0194, and `gepa_minus_rlm` is 0.2213.
- GEPA best validation score: 1.0000

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T211615Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/5b5b2841`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T211615Z/evals/advancedif_rlm_skill--openai--gpt-4.1-mini/4bb18387`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T211615Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T211615Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-4.1-mini__20260401T211615Z/evals/advancedif_iter_skill--openai--gpt-4.1-mini/6059cbb4`

