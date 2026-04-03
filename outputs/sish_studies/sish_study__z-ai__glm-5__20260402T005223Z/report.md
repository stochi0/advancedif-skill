# Self-Improving Skill Harness (SISH) Report

## Setup

- Model: `z-ai/glm-5`
- Judge model: `z-ai/glm-5`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T005223Z`
- Sequence harness used: `sish_iter_skill`

## Aggregate Metrics

| Variant | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Iterative | 0.0000 | 0.0000 | 0.0000 | 0.0 | 0.0000 | 0.0000 | 0.0000 |
| RLM | 0.0000 | 0.0000 | 0.0000 | 0.0 | 0.0000 | 0.0000 | 0.0000 |

## Paired Deltas

- Paired examples: 2
- `reward_delta_rlm_minus_iter`: 0.0000 (95% CI 0.0000 to 0.0000)
- `efficiency_delta_rlm_minus_iter`: 0.0000 (95% CI 0.0000 to 0.0000)
- RLM reward win rate across paired examples: 0.0000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.0000
- Transfer frozen mean: 0.0000
- Transfer empty-control mean: 0.0000
- `transfer_lift_mean`: 0.0000
- Transfer pairs: 0
- Skill length slope by task index: 0.0000
- Carryover reward slope by task index: 0.0000
- First-submission lift slope by task index: 0.0000

### Task-Index Means

| Task index | Skill words | Criterion satisfaction | First-submission lift |
| --- | ---: | ---: | ---: |
| 0 | 126.0 | 0.0000 | 0.0000 |
| 1 | 126.0 | 0.0000 | 0.0000 |

## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? Inconclusive. The paired reward delta is 0.0000.
- Q2. Is it more token-efficient? Inconclusive. The efficiency delta is 0.0000.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0000.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `sish_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T005223Z/evals/sish_iter_skill--z-ai--glm-5/0bde1442`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T005223Z/evals/sish_rlm_skill--z-ai--glm-5/c488278e`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T005223Z/sequence_run`

## Experiment scope

- Concrete allow/deny list: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/self_improving_skill_experiment/SCOPE.md`
- Env ids: `sish_iter_skill`, `sish_rlm_skill` — LOCA-bench tasks via the vendored `loca_bench_rlm` package (default config: `task_configs/hard_256k_one_per_family.json`), same skill markdown schema as the parent repo, SISH prompts, and LOCA evaluator feedback on submit.
- `sequence_research_metrics` in `experiment_summary.json` adds a lexical abstraction proxy for sequential carryover rows (not a substitute for human coding).
