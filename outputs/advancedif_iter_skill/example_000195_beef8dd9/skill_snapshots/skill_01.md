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

## Constraints for this turn:
1. Five fun summer activities.
2. Overnight activities.
3. Located in Southwestern Ontario.
4. Appropriate for an infant boy, a 6-year-old girl, and two adults.
5. Do not include run-of-the-mill hotel or campground.
6. Special, like Great Wolf Lodge or Toronto Zoo overnight.
7. Each event must cost less than $1000 each.
8. Each event must span 1-2 days.
9. Respond with a numbered list from most expensive to least expensive.
