from __future__ import annotations

from pathlib import Path

from core.skill_artifact import (
    EMPTY_SKILL_TEMPLATE,
    snapshot_skill,
    validate_skill_markdown,
    write_skill,
)


def test_validate_skill_markdown_accepts_template():
    valid, message, normalized = validate_skill_markdown(EMPTY_SKILL_TEMPLATE)
    assert valid is True
    assert message == "accepted"
    assert normalized.startswith("# Skill")


def test_validate_skill_markdown_rejects_missing_sections():
    valid, message, _normalized = validate_skill_markdown("# Skill\n\n## Procedure\n")
    assert valid is False
    assert "## When To Use" in message


def test_write_and_snapshot_skill(tmp_path: Path):
    current_path = write_skill(tmp_path / "current_skill.md", EMPTY_SKILL_TEMPLATE)
    snapshot_path = snapshot_skill(tmp_path / "snapshots", 1, EMPTY_SKILL_TEMPLATE)

    assert Path(current_path).is_file()
    assert Path(snapshot_path).is_file()
