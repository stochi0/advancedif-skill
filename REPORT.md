# AdvancedIF Skill Benchmark Report

## What This Repo Is Doing

This repo is a focused experimental testbed for studying answer refinement on semi-verifiable instruction-following tasks. It uses the `facebook/AdvancedIF` dataset as the base task and wraps it in two controllable harnesses:

- `advancedif_iter_skill`: a non-RLM iterative refinement setup where the model answers directly, can query a restricted judge, and can update a carried `skill.md` artifact.
- `advancedif_rlm_skill`: an RLM-based setup where the model works inside a persistent Python/sandbox environment, reads task files from disk, can query the same restricted judge, and can persist a carried `skill.md`.

The common structure is:

1. Give the model an AdvancedIF conversation.
2. Hide the full grading rubric from the model.
3. Let the model optionally submit draft answers to a judge that knows the full rubric.
4. Restrict the judge feedback to a small channel:
   - `score_only`
   - `one_violation`
   - `none`
5. Measure how well the model improves its final answer, how efficiently it does so, and whether any written skill artifact helps on future tasks.

This lets the repo act as a concrete initial testbed for three research axes:

- long-horizon capabilities via RLMs
- self-improving scaffolds and harnesses
- hard-to-verify or semi-verifiable tasks

## Why This Setup Exists

The goal is not to start with training. The goal is to make the evaluation setting concrete enough that later training questions become obvious and defensible.

The motivating idea is:

- pick an established semi-verifiable benchmark
- give the policy only partial judge feedback
- compare a plain iterative scaffold against an RLM scaffold
- allow the policy to write a reusable skill artifact at test time
- probe whether that skill transfers across tasks rather than just helping on one example

AdvancedIF is a good fit because each example has multiple hidden rubric criteria, and the repo can evaluate final outputs against those criteria while only exposing limited feedback during the rollout.

## The Concrete Experiment

### Dataset framing

The repo uses three AdvancedIF benchmark regimes:

- `complex_if_single_turn_v5`
- `carried_context_multi_turn_eval_v5`
- `system_steerability_v2`

It builds a stratified pilot split with the following counts per regime:

- `dev_gepa`: 15
- `main_eval`: 30
- `carryover_sequences`: 9
- `transfer_probe`: 6

That produces:

- `dev_gepa`: 45 total examples
- `main_eval`: 90 total examples
- `carryover_sequences`: 3 sequences of 9 tasks each
- `transfer_probe`: 18 total examples

Each carryover sequence is balanced across regimes, with 3 tasks from each regime.

### Judge design

The judge has the full gold rubric and scores a candidate answer per criterion. Internally, the final reward is:

- `final_criterion_satisfaction`

which is the fraction of rubric items satisfied by the final answer.

During the rollout, the policy does not see the rubric directly. It only sees one of:

- `score_only`: fraction of hidden criteria satisfied
- `one_violation`: one revealed violated criterion, or all-clear
- `none`: acknowledgement only

This is the core semi-verifiable setup: the policy gets a constrained verification signal, not full supervision.

### Harnesses being compared

#### 1. Non-RLM iterative harness

The policy gets tools to:

- submit a draft answer to the judge
- update a carried skill artifact

It operates as a normal iterative answer-refinement policy.

#### 2. RLM harness

The policy works in a persistent Python REPL and filesystem sandbox. It:

- reads the conversation from materialized task files
- reads `skill.md`
- drafts and revises an answer
- optionally queries the judge
- optionally updates the skill artifact

This is the long-horizon version of the same task. It keeps the task fixed while changing the scaffold.

### Sequential skill-carryover experiment

The repo also includes a sequential rollout experiment in [`sequence_runner.py`](/Users/ayushb/home/workspaces/prime_intellect/athena/experiments/advancedif_skill_benchmark/sequence_runner.py):

1. Run a carryover sequence of tasks with skill updates enabled.
2. Carry the final written skill forward through the sequence.
3. Freeze the resulting skill.
4. Evaluate transfer on held-out probe tasks under two conditions:
   - `transfer_frozen`: use the carried skill
   - `transfer_empty_control`: replace it with the empty template

This isolates whether test-time skill writing is merely overfitting to sequence tasks or actually yielding reusable guidance.

### GEPA comparison

The repo also includes a prompt-optimization baseline via GEPA on `dev_gepa`. This provides a comparison point for:

- scaffolded test-time adaptation with tools and skill writing
- prompt-only optimization without the RLM harness

## What Questions This Experiment Is Trying To Answer

Below are the main research questions implied by the setup, along with the metrics already present in the repo for answering them.

### Q1. Is an RLM harness with skill iteration better or worse than non-RLM iterative refinement under the same restricted judge feedback?

This is the most immediate question and the cleanest initial testbed question.

Comparison:

- `advancedif_rlm_skill` vs `advancedif_iter_skill`
- matched on:
  - model
  - feedback mode
  - dataset split
  - judge model

Primary metrics:

- `final_criterion_satisfaction`
- `all_criteria_pass`
- `first_submission_lift`

How to interpret:

- Higher `final_criterion_satisfaction` means better final rubric coverage.
- Higher `all_criteria_pass` means more examples with complete success.
- Higher `first_submission_lift` means the scaffold actually improves the answer over the first judged draft rather than merely producing a good first attempt.

Why this matters:

- It answers whether long-horizon RLM behavior is useful on this task at all, before adding training.

### Q2. Is the RLM harness more token-efficient than the non-RLM iterative harness?

A more capable scaffold is not automatically a better scaffold if it burns too much budget.

Primary metrics:

- `total_token_count`
- `judge_call_count`
- `judge_query_count`
- `judge_prompt_token_count`
- `judge_completion_token_count`

Derived comparison to report:

- reward per token, or reward per 1k tokens

How to interpret:

- If RLM improves score but uses vastly more tokens, its practical value is weaker.
- If RLM matches or exceeds iterative performance at similar or lower total token cost, that is strong evidence that the scaffold is useful.

Why this matters:

- This is the cleanest way to evaluate the tradeoff between richer reasoning loops and actual efficiency.

### Q3. Can models write skills at test time that generalize to other tasks?

This is the core self-improving scaffold question.

Comparison:

- `transfer_frozen` vs `transfer_empty_control`

Primary metrics:

- transfer-time `final_criterion_satisfaction`
- transfer-time `all_criteria_pass`

Derived comparison to report:

- `transfer_lift = transfer_frozen score - transfer_empty_control score`

How to interpret:

- Positive lift means the written skill helps on unseen probe tasks.
- Near-zero or negative lift suggests the skill is not useful, is too task-specific, or is simply ignored.

Why this matters:

- It tells you whether skill-writing is creating reusable task knowledge or just transient local adaptation.

### Q4. If multiple tasks are attempted sequentially with skill carryover, do skills become more abstract and less overfit over time?

This is the longitudinal version of the skill question.

Comparison:

- within each carryover sequence, by `task_index`

Primary metrics:

- `skill_word_count_metric`
- `skill_heading_completeness_metric`
- `final_criterion_satisfaction`
- `first_submission_lift`

How to interpret:

- If skill length grows without improving downstream performance, the skill may be accumulating clutter.
- If performance holds or improves while skill size stabilizes, that suggests the artifact is becoming more compact and reusable.
- `skill_heading_completeness_metric` is a light sanity check that the artifact stays structurally valid, not a real quality metric by itself.

Why this matters:

- It gives an initial operational answer to whether self-improving scaffolds learn reusable abstractions at test time.

### Q5. How does this compare to prompt optimization strategies like GEPA?

This is the baseline question for whether the extra scaffold complexity is earning its keep.

Comparison:

- iterative baseline
- GEPA-optimized iterative baseline
- RLM harness

Primary metrics:

- `final_criterion_satisfaction`
- `all_criteria_pass`
- `total_token_count`
- `first_submission_lift`

How to interpret:

- If GEPA closes most of the gap to RLM, then prompt optimization may be the cheaper intervention.
- If RLM still clearly wins, then the benefit likely comes from interaction structure and long-horizon adaptation rather than prompt quality alone.

Why this matters:

- It clarifies whether future work should prioritize scaffold design, prompt optimization, or eventual training.

## Suggested Initial Testbed Scope

Given the three broad directions:

- long-horizon capabilities via RLMs
- self-improving scaffolds/harnesses
- hard-to-verify tasks

the repo is already scoped in a reasonable order. The initial focus should be:

### Phase 1: Establish whether the RLM harness is useful at all

Run:

- iterative vs RLM on `main_eval`
- feedback modes:
  - `score_only`
  - `one_violation`
  - optionally `none` as a lower-information control

Answer:

- does the RLM scaffold improve final rubric satisfaction?
- does it improve first-submission-to-final refinement?
- is the gain worth the token cost?

### Phase 2: Test whether written skills transfer

Run:

- carryover sequence experiment
- compare frozen skill vs empty control on transfer probes

Answer:

- do skill artifacts generalize at all?
- are they helping because they encode reusable strategy, or just because they leak local specifics?

### Phase 3: Compare against prompt-only optimization

Run:

- GEPA on `dev_gepa`
- compare its resulting policy against iterative and RLM evaluations on the same task family

Answer:

- do we need the scaffold, or can prompt optimization recover most of the benefit?

This is a good ordering because it starts with the clearest question, adds the self-improvement question second, and only then asks whether the extra complexity beats a simpler optimization baseline.

## What This Repo Already Gives You

This repo already provides a useful pre-training research harness because it fixes the task and lets you vary the adaptation mechanism.

Concretely, it already supports:

- a semi-verifiable benchmark with hidden rubric criteria
- restricted judge feedback channels
- a plain iterative baseline
- an RLM baseline with persistent workspace interaction
- test-time skill writing and carryover
- held-out transfer probes for the skill artifact
- a prompt-optimization comparison point via GEPA

That is enough to answer the initial qualitative and quantitative questions:

- is RLM useful here?
- when is it useful?
- is it efficient enough?
- do skill artifacts actually generalize?
- is the benefit from the scaffold or from prompt quality?

## Bottom Line

This repo is best understood as a controlled benchmark for studying whether a small-model RLM scaffold can learn useful answer-refinement strategies on semi-verifiable instruction-following tasks, especially when it can iteratively query a limited judge and write a reusable skill for itself at test time.

The central questions are not about raw benchmark performance alone. They are about:

- scaffold usefulness
- efficiency
- transfer
- abstraction vs overfitting
- and whether these gains survive comparison to simpler alternatives like iterative refinement or GEPA

That makes this a strong initial experimental setup for deciding what future training runs would actually be interesting.
