#!/usr/bin/env python3
"""Validate the issueflow skill pack and plugin metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
MARKDOWN_LINK_RE = re.compile(r"\]\(([^)]+)\)")
TEXT_EXTENSIONS = {
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".sh",
    ".txt",
    ".yaml",
    ".yml",
}
LOCAL_PATTERNS = [
    re.compile(r"(^|[^A-Za-z])[A-Za-z]:[\\/]"),
    re.compile(r"[/\\]Users[/\\]", re.IGNORECASE),
    re.compile(r"\bAppData\b", re.IGNORECASE),
    re.compile(r"\bHOME[/\\]", re.IGNORECASE),
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation should report every parse failure.
        fail(errors, f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return {}


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        fail(errors, f"{path.relative_to(ROOT)} must start with YAML frontmatter")
        return {}

    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(errors, f"{path.relative_to(ROOT)} has no closing frontmatter marker")
        return {}

    frontmatter: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            fail(errors, f"{path.relative_to(ROOT)} has invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"').strip("'")

    return frontmatter


def validate_skills(errors: list[str]) -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        fail(errors, "skills/ directory is missing")
        return

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if not skill_dirs:
        fail(errors, "skills/ contains no skill directories")
        return

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            fail(errors, f"{skill_dir.relative_to(ROOT)} is missing SKILL.md")
            continue

        frontmatter = parse_frontmatter(skill_md, errors)
        name = frontmatter.get("name")
        description = frontmatter.get("description")

        if not name:
            fail(errors, f"{skill_md.relative_to(ROOT)} is missing name")
        elif name != skill_dir.name:
            fail(errors, f"{skill_md.relative_to(ROOT)} name must match folder name")
        elif not NAME_RE.match(name):
            fail(errors, f"{skill_md.relative_to(ROOT)} name must be kebab-case")

        if not description:
            fail(errors, f"{skill_md.relative_to(ROOT)} is missing description")


def validate_plugin(errors: list[str]) -> None:
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        fail(errors, ".codex-plugin/plugin.json is missing")
        return

    manifest = load_json(manifest_path, errors)
    if not manifest:
        return

    name = manifest.get("name")
    if not name or not NAME_RE.match(name):
        fail(errors, ".codex-plugin/plugin.json name must be kebab-case")

    skills_path = manifest.get("skills")
    if skills_path:
        if not skills_path.startswith("./"):
            fail(errors, ".codex-plugin/plugin.json skills path must start with ./")
        resolved = (ROOT / skills_path).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(errors, ".codex-plugin/plugin.json skills path must stay inside the repo")
        if not resolved.is_dir():
            fail(errors, ".codex-plugin/plugin.json skills path does not exist")
    else:
        fail(errors, ".codex-plugin/plugin.json must point to ./skills/")


def validate_claude_plugin(errors: list[str]) -> None:
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not manifest_path.is_file():
        fail(errors, ".claude-plugin/plugin.json is missing")
        return

    manifest = load_json(manifest_path, errors)
    if not manifest:
        return

    name = manifest.get("name")
    if not name or not NAME_RE.match(name):
        fail(errors, ".claude-plugin/plugin.json name must be kebab-case")

    description = manifest.get("description")
    if not description:
        fail(errors, ".claude-plugin/plugin.json is missing description")

    skills_path = manifest.get("skills")
    if skills_path:
        if not skills_path.startswith("./"):
            fail(errors, ".claude-plugin/plugin.json skills path must start with ./")
        resolved = (ROOT / skills_path).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(errors, ".claude-plugin/plugin.json skills path must stay inside the repo")
        if not resolved.is_dir():
            fail(errors, ".claude-plugin/plugin.json skills path does not exist")


def validate_marketplace(errors: list[str]) -> None:
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    if not marketplace_path.is_file():
        fail(errors, ".agents/plugins/marketplace.json is missing")
        return

    marketplace = load_json(marketplace_path, errors)
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail(errors, ".agents/plugins/marketplace.json must contain plugins[]")
        return

    for entry in plugins:
        name = entry.get("name")
        if not name or not NAME_RE.match(name):
            fail(errors, "marketplace plugin entry name must be kebab-case")

        policy = entry.get("policy", {})
        if policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
            fail(errors, f"marketplace entry {name} has invalid policy.installation")
        if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
            fail(errors, f"marketplace entry {name} has invalid policy.authentication")
        if not entry.get("category"):
            fail(errors, f"marketplace entry {name} is missing category")

        source = entry.get("source", {})
        if source.get("source") == "local":
            source_path = source.get("path", "")
            if not source_path.startswith("./"):
                fail(errors, f"marketplace entry {name} local path must start with ./")
                continue
            resolved = (ROOT / source_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"marketplace entry {name} local path must stay inside the repo")
                continue
            if not (resolved / ".codex-plugin" / "plugin.json").is_file():
                fail(errors, f"marketplace entry {name} does not point at a plugin root")


def validate_claude_marketplace(errors: list[str]) -> None:
    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not marketplace_path.is_file():
        fail(errors, ".claude-plugin/marketplace.json is missing")
        return

    marketplace = load_json(marketplace_path, errors)
    plugins = marketplace.get("plugins")
    if not marketplace.get("name") or not NAME_RE.match(marketplace.get("name", "")):
        fail(errors, ".claude-plugin/marketplace.json name must be kebab-case")
    if not isinstance(marketplace.get("owner"), dict) or not marketplace["owner"].get("name"):
        fail(errors, ".claude-plugin/marketplace.json must contain owner.name")
    if not isinstance(plugins, list) or not plugins:
        fail(errors, ".claude-plugin/marketplace.json must contain plugins[]")
        return

    for entry in plugins:
        name = entry.get("name")
        if not name or not NAME_RE.match(name):
            fail(errors, "Claude marketplace plugin entry name must be kebab-case")

        source = entry.get("source")
        if isinstance(source, str):
            if not source.startswith("./"):
                fail(errors, f"Claude marketplace entry {name} relative source must start with ./")
                continue
            resolved = (ROOT / source).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"Claude marketplace entry {name} relative source must stay inside the repo")
                continue
            if not (resolved / ".claude-plugin" / "plugin.json").is_file():
                fail(errors, f"Claude marketplace entry {name} does not point at a Claude plugin root")
        elif isinstance(source, dict):
            source_type = source.get("source")
            if source_type not in {"github", "url", "git-subdir", "npm"}:
                fail(errors, f"Claude marketplace entry {name} has invalid source.source")
            if source_type == "github" and not source.get("repo"):
                fail(errors, f"Claude marketplace entry {name} github source is missing repo")
        else:
            fail(errors, f"Claude marketplace entry {name} source must be string or object")


def validate_version_consistency(errors: list[str]) -> None:
    manifests = [
        ROOT / ".codex-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "marketplace.json",
    ]
    versions: dict[str, str] = {}

    for path in manifests:
        data = load_json(path, errors)
        version = data.get("version")
        if not version or not SEMVER_RE.match(str(version)):
            fail(errors, f"{path.relative_to(ROOT)} must contain a semantic version")
            continue
        versions[str(path.relative_to(ROOT))] = str(version)

    if len(set(versions.values())) > 1:
        joined = ", ".join(f"{path}={version}" for path, version in sorted(versions.items()))
        fail(errors, f"plugin versions must match: {joined}")


def validate_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if "://" in target:
                continue

            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"{path.relative_to(ROOT)} links outside repo: {target}")
                continue
            if not resolved.exists():
                fail(errors, f"{path.relative_to(ROOT)} has broken link: {target}")


def validate_no_local_content(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in LOCAL_PATTERNS:
            if pattern.search(text):
                fail(errors, f"{path.relative_to(ROOT)} contains local machine-specific text")
                break


def main() -> int:
    errors: list[str] = []

    validate_skills(errors)
    validate_plugin(errors)
    validate_claude_plugin(errors)
    validate_marketplace(errors)
    validate_claude_marketplace(errors)
    validate_version_consistency(errors)
    validate_markdown_links(errors)
    validate_no_local_content(errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
