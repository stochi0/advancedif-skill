# Skill

## When To Use
- Use this skill when answering AdvancedIF prompts with multiple explicit constraints.

## Procedure
1. Read the full conversation carefully.
2. List the concrete constraints before drafting.
3. Draft the answer in the requested format.
4. Use the judge feedback tool before finalizing when useful.

## Common Failure Modes
- Missing one or more formatting constraints.
- Answering the right topic in the wrong structure.
- Ignoring carried context from earlier turns.

## Answer Checklist
- Every explicit instruction is covered.
- Formatting and ordering requirements are satisfied.
- Negative constraints are respected.

## How To Use Judge Feedback
- Treat score changes as a signal about constraint coverage.
- If one violated criterion is revealed, fix that issue first.
- Do not overfit to a single revealed failure if other constraints may still be missing.

Judge feedback mode for `submit_candidate_answer`: no contentful feedback beyond acknowledgement that the submission was received.

## Constraints for this task:
1. Count syllables for the first 100 words of each song.
2. Identify which writer uses the highest number of single-syllable words.
3. Identify which writer uses the highest number of multi-syllable (3 or more) words.
4. Identify which writer uses the highest number of unique words.
5. Count the occurrences of the N-word for each writer.
6. Present the information clearly for comparison.
