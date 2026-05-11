# Contributing

Thanks for helping maintain issueflow-skills.

## Development Checks

Run the validator before opening a pull request:

```bash
python scripts/validate.py
```

The validator checks skill frontmatter, plugin metadata, marketplace metadata, and accidental machine-local references.

## Skill Changes

- Keep each `SKILL.md` focused on one job.
- Keep `name` and the folder name identical.
- Put trigger language in `description`.
- Move detailed guidance into `references/` when the skill body starts getting long.
- Keep reusable scaffold files in `templates/`.
- Avoid personal paths, hostnames, user names, and repo-specific assumptions.

## Plugin Changes

- Update `.codex-plugin/plugin.json` when install-surface copy, keywords, or version changes.
- Keep marketplace entries in `.agents/plugins/marketplace.json` installable from this repository root.
- Prefer stable semantic versions once the repo is published.

## Release Checklist

1. Update `.codex-plugin/plugin.json` version.
2. Update `CHANGELOG.md`.
3. Run `python scripts/validate.py`.
4. Push and tag the release after the remote is attached.
