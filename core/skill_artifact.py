from __future__ import annotations

import re
from pathlib import Path

REQUIRED_SKILL_HEADINGS = [
    "# Skill",
    "## When To Use",
    "## Procedure",
    "## Common Failure Modes",
    "## Answer Checklist",
    "## How To Use Judge Feedback",
]

EMPTY_SKILL_TEMPLATE = """# Skill

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
"""


def normalize_skill_markdown(skill_markdown: str) -> str:
    text = skill_markdown.replace("\r\n", "\n").strip()
    return text + "\n"


def validate_skill_markdown(skill_markdown: str) -> tuple[bool, str, str]:
    normalized = normalize_skill_markdown(skill_markdown)
    position = 0
    missing: list[str] = []
    for heading in REQUIRED_SKILL_HEADINGS:
        idx = normalized.find(heading, position)
        if idx < 0:
            missing.append(heading)
        else:
            position = idx + len(heading)
    if missing:
        return (
            False,
            "Skill markdown must contain the required headings in order: " + ", ".join(missing),
            normalized,
        )
    return True, "accepted", normalized


def write_skill(path: str | Path, skill_markdown: str) -> str:
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    normalized = normalize_skill_markdown(skill_markdown)
    path_obj.write_text(normalized, encoding="utf-8")
    return str(path_obj.resolve())


def snapshot_skill(snapshot_dir: str | Path, ordinal: int, skill_markdown: str) -> str:
    snapshot_path = Path(snapshot_dir) / f"skill_{ordinal:02d}.md"
    return write_skill(snapshot_path, skill_markdown)


def skill_word_count(skill_markdown: str) -> int:
    return len(re.findall(r"\b\w+\b", skill_markdown))


def skill_heading_completeness(skill_markdown: str) -> float:
    present = sum(1 for heading in REQUIRED_SKILL_HEADINGS if heading in skill_markdown)
    return present / len(REQUIRED_SKILL_HEADINGS)
