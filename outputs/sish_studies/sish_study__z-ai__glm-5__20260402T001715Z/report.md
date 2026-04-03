# Self-Improving Skill Harness (SISH) Report

## Setup

- Model: `z-ai/glm-5`
- Judge model: `z-ai/glm-5`
- Feedback mode: `score_only`
- Study directory: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T001715Z`
- Sequence harness used: `sish_iter_skill`

## Aggregate Metrics

| Variant | Criterion satisfaction | All-criteria pass | First-submission lift | Total tokens | Reward / 1k tokens | Judge calls | Error rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Iterative | 0.5000 | 0.5000 | -0.3889 | 32449.5 | 0.0243 | 4.5000 | 0.0000 |
| RLM | 0.0000 | 0.0000 | -0.5000 | 16907.5 | 0.0000 | 0.5000 | 0.0000 |

## Paired Deltas

- Paired examples: 2
- `reward_delta_rlm_minus_iter`: -0.5000 (95% CI -1.4800 to 0.4800)
- `efficiency_delta_rlm_minus_iter`: -0.0243 (95% CI -0.0720 to 0.0234)
- RLM reward win rate across paired examples: 0.0000
- RLM efficiency win rate across paired examples: 0.0000

## Carryover And Transfer

- Carryover reward mean: 0.4286
- Transfer frozen mean: 0.0000
- Transfer empty-control mean: 0.0000
- `transfer_lift_mean`: 0.0000
- Transfer pairs: 2
- Skill length slope by task index: 79.0000
- Carryover reward slope by task index: 0.8571
- First-submission lift slope by task index: 1.0110

### Task-Index Means

| Task index | Skill words | Criterion satisfaction | First-submission lift |
| --- | ---: | ---: | ---: |
| 0 | 126.0 | 0.0000 | -1.0000 |
| 1 | 205.0 | 0.8571 | 0.0110 |

## Direct Answers

- Q1. Is the RLM harness + skill iteration setup better or worse than non-RLM iterative refinement with the same judge feedback tool? No. The paired reward delta is -0.5000.
- Q2. Is it more token-efficient? Inconclusive. The efficiency delta is -0.0243.
- Q3. Do models in this setup write skills that generalize to other tasks? Inconclusive. The transfer lift is 0.0000.
- Q4. If multiple tasks are attempted sequentially, with the skill carrying over across tasks, do models eventually write skills which are more high-level or less overfit to specific tasks? Inconclusive. This benchmark only measures that indirectly via transfer lift plus task-index trends, not semantic abstraction directly.
- Q5. How does this compare to prompt optimization strategies like GEPA? Not run in this study.

## Recommendation

- Use `sish_iter_skill` as the next scaffold to study or train against unless you have an external reason to privilege the other harness.
- Treat the skill-generalization answer as the strongest signal for whether self-improving artifacts are worth deeper investment.
- Do not overinterpret Q4: the benchmark can detect transfer and growth patterns, but it does not directly measure whether the learned skill became semantically more abstract.

## Artifacts

- Iterative eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T001715Z/evals/sish_iter_skill--z-ai--glm-5/52fc5cfc`
- RLM eval: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T001715Z/evals/sish_rlm_skill--z-ai--glm-5/02a925d6`
- Sequence run: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/outputs/sish_studies/sish_study__z-ai__glm-5__20260402T001715Z/sequence_run`

## Experiment scope

- Concrete allow/deny list: `/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/self_improving_skill_experiment/SCOPE.md`
- Env ids: `sish_iter_skill`, `sish_rlm_skill` (same judge tools and skill schema as the AdvancedIF benchmark, with SISH-scoped prompts).
- `sequence_research_metrics` in `experiment_summary.json` adds a lexical abstraction proxy for sequential carryover rows (not a substitute for human coding).
