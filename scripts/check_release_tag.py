#!/usr/bin/env python3
"""Verify that a Git tag matches .codex-plugin/plugin.json."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag", nargs="?", default=os.environ.get("GITHUB_REF_NAME", ""))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    tag = args.tag

    if not tag:
        raise SystemExit("Provide a tag or set GITHUB_REF_NAME")

    version = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")).get("version")
    expected = f"v{version}"

    if tag != expected:
        raise SystemExit(f"Release tag {tag!r} does not match plugin version {expected!r}")

    print(f"Release tag {tag} matches plugin version {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
