#!/usr/bin/env python3
"""Prepare an issueflow plugin release by bumping manifests and CHANGELOG.md."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
CLAUDE_MANIFEST_PATH = ROOT / ".claude-plugin" / "plugin.json"
CLAUDE_MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"
CHANGELOG_PATH = ROOT / "CHANGELOG.md"
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Semantic version to release, for example 0.2.0")
    parser.add_argument("--date", default=date.today().isoformat(), help="Release date in YYYY-MM-DD format")
    parser.add_argument("--dry-run", action="store_true", help="Print the planned change without writing files")
    return parser.parse_args()


def update_json_version(path: Path, version: str, dry_run: bool) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    old_version = manifest.get("version")
    manifest["version"] = version

    if dry_run:
        print(f"{path.relative_to(ROOT)}: {old_version} -> {version}")
        return

    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_claude_marketplace(version: str, dry_run: bool) -> None:
    marketplace = json.loads(CLAUDE_MARKETPLACE_PATH.read_text(encoding="utf-8"))
    old_version = marketplace.get("version")
    marketplace["version"] = version

    if dry_run:
        print(f"{CLAUDE_MARKETPLACE_PATH.relative_to(ROOT)}: {old_version} -> {version}")
        return

    CLAUDE_MARKETPLACE_PATH.write_text(
        json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def update_changelog(version: str, release_date: str, dry_run: bool) -> None:
    text = CHANGELOG_PATH.read_text(encoding="utf-8")
    release_heading = f"## {version} - {release_date}"

    if release_heading in text:
        raise SystemExit(f"{CHANGELOG_PATH.relative_to(ROOT)} already contains {release_heading}")

    lines = text.splitlines()
    unreleased_index = next(
        (index for index, line in enumerate(lines) if line.startswith("## ") and "Unreleased" in line),
        None,
    )

    if unreleased_index is None:
        raise SystemExit("CHANGELOG.md must contain an Unreleased heading before releasing")

    old_heading = lines[unreleased_index]
    lines[unreleased_index] = release_heading

    if lines[:1] == ["# Changelog"]:
        lines[1:1] = ["", "## Unreleased", "", "- No changes yet."]

    new_text = "\n".join(lines).rstrip() + "\n"

    if dry_run:
        print(f"{CHANGELOG_PATH.relative_to(ROOT)}: {old_heading!r} -> {release_heading!r}")
        return

    CHANGELOG_PATH.write_text(new_text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    version = args.version.removeprefix("v")

    if not SEMVER_RE.match(version):
        raise SystemExit("Version must be semantic, for example 0.2.0")

    update_json_version(MANIFEST_PATH, version, args.dry_run)
    update_json_version(CLAUDE_MANIFEST_PATH, version, args.dry_run)
    update_claude_marketplace(version, args.dry_run)
    update_changelog(version, args.date, args.dry_run)

    if args.dry_run:
        print(f"Dry run complete for v{version}.")
    else:
        print(f"Prepared release v{version}.")
        print("Next: run python scripts/validate.py, commit, tag, and push.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
