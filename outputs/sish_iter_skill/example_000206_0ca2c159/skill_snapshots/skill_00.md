# Skill

## When To Use
- Use this skill when answering AdvancedIF prompts with multiple explicit constraints.

## Procedure
1. Read the full conversation carefully and track all constraints from the beginning.
2. List ALL concrete constraints before drafting, including timing, activities, themes, and quantities.
3. Draft the answer in the requested format.
4. Use the judge feedback tool before finalizing when useful.
5. Verify all constraints are met, especially when making iterative changes.

## Common Failure Modes
- Missing one or more formatting constraints.
- Answering the right topic in the wrong structure.
- Ignoring carried context from earlier turns.
- Losing track of constraints when making multiple revisions.
- Not maintaining quantities (time, amounts) when reallocating or changing elements.

## Answer Checklist
- Every explicit instruction is covered.
- Formatting and ordering requirements are satisfied.
- Negative constraints are respected.
- When reallocating time or activities, maintain the same total quantities.
- All constraints from previous turns are still satisfied after making changes.

## How To Use Judge Feedback
- Treat score changes as a signal about constraint coverage.
- If one violated criterion is revealed, fix that issue first.
- Do not overfit to a single revealed failure if other constraints may still be missing.
- Re-check ALL constraints when score is below 1.0, not just the most recent changes.
