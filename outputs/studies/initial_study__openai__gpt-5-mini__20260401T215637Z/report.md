# AdvancedIF Initial Study Report

## Setup

- Model: `openai/gpt-5-mini`
- Judge model: `openai/gpt-5-mini`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215637Z`
- Sequence harness used: `advancedif_iter_skill`

## Aggregate Metrics


| Variant                  | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| ------------------------ | ---------------------- | ----------------- | --------------------- | ------------ | ------------------ | ----------- | ---------- |
| Iterative                | 0.9556                 | 0.7500            | 0.0000                | 8399.3       | 0.1462             | 1.4167      | 0.0000     |
| RLM                      | 0.9509                 | 0.6667            | 0.0000                | 10485.0      | 0.0971             | 1.0833      | 0.0000     |
| GEPA-optimized iterative | 0.8889                 | 0.7500            | 0.0093                | 7743.1       | 0.1440             | 1.4167      | 0.0000     |


## Paired Deltas

- Paired examples: 12
- `reward_delta_rlm_minus_iter`: -0.0046 (95% CI -0.0480 to 0.0387)
- `efficiency_delta_rlm_minus_iter`: -0.0492 (95% CI -0.0840 to -0.0143)
- RLM reward win rate across paired examples: 0.1667
- RLM efficiency win rate across paired examples: 0.2500

## Carryover And Transfer

- Carryover reward mean: 0.9583
- Transfer frozen mean: 0.8085
- Transfer empty-control mean: 0.7106
- `transfer_lift_mean`: 0.0979
- Transfer pairs: 6
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: -0.0071
- First-submission lift slope by task index: 0.0000

### Task-Index Means


| Task index | Skill words | Criterion satisfaction | First-submission lift |
| ---------- | ----------- | ---------------------- | --------------------- |
| 0          | 126.0       | 1.0000                 | 0.0000                |
| 1          | 126.0       | 1.0000                 | 0.0000                |
| 2          | 126.0       | 0.8333                 | 0.0000                |
| 3          | 126.0       | 1.0000                 | 0.0000                |
| 4          | 126.0       | 1.0000                 | 0.0000                |
| 5          | 126.0       | 0.9167                 | 0.0000                |


## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? Inconclusive. The paired reward delta is -0.0046.
- Q2. Is it more token-efficient? Inconclusive. The efficiency delta is -0.0492.
- Q3. Do models in this setup write skills that generalize to other tasks? Yes. The transfer lift is 0.0979.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Weak yes. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? GEPA main-eval criterion satisfaction is 0.8889. `gepa_minus_iter` is -0.0667, and `gepa_minus_rlm` is -0.0620.
- GEPA best validation score: 1.0000

## Recommendation

- Use `advancedif_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215637Z/evals/advancedif_iter_skill--openai--gpt-5-mini/cd8e9889`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215637Z/evals/advancedif_rlm_skill--openai--gpt-5-mini/3ce20a8e`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215637Z/sequence_run`
- GEPA optimization: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215637Z/gepa_run`
- GEPA main eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/studies/initial_study__openai__gpt-5-mini__20260401T215637Z/evals/advancedif_iter_skill--openai--gpt-5-mini/3ae6307c`

