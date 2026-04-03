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

## Constraint Checklist
1. Story helps with fear of dark: Yes
2. Max 300 words (story): Yes
3. Comic book style writing: Yes
4. Sound effects: Yes
5. Story summary (back of book): Yes
6. Summary max half story word count: Yes
7. List of characters and fears: Yes
8. Each character superhero with different fear: Yes
9. Important flashlight (magic object): Yes
