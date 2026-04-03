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

## Lessons Learned
- For word count constraints, verify each section meets its specific requirement (e.g., 100-200 words for standard sections, 3x length for special sections)
- Creative titles should be descriptive and engaging, not just the subject name
- When one section has different requirements (like "theory" vs "explanation"), ensure that distinction is clear in both content and length
- Separators between sections help visual organization
