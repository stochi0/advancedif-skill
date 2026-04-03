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

## Current Task Constraints
1.  **No supplements or medication.**
2.  **No placing anything on the head/hair.** (due to overheating and appearance concerns)
3.  **Clearly organized:** Use titles, bold text, and bullet points.
4.  **Specific sections:** "At Home", "Out Shopping", and "Out at Work" only.
5.  **No duplicate suggestions** across sections.
6.  **Functionality:** Suggestions must allow for hand use (shopping, working, dog walking, etc.).
