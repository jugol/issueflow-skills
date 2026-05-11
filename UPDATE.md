# Update Model

Issueflow updates through the Codex plugin marketplace mechanism.

## Publisher Flow

When you maintain the plugin:

1. Edit skills, references, templates, or metadata.
2. Record the user-facing change under `## Unreleased` in `CHANGELOG.md`.
3. Run validation:

```bash
python scripts/validate.py
```

4. Bump the plugin version:

```bash
python scripts/release.py 0.2.0
```

5. Commit and tag:

```bash
git add .
git commit -m "Release issueflow 0.2.0"
git tag v0.2.0
git push origin main --tags
```

## Consumer Flow

On each computer that should receive updates, add the marketplace once:

```bash
codex plugin marketplace add <owner>/issueflow-skills --ref main
```

Then refresh installed marketplace plugins whenever you want the latest version:

```bash
codex plugin marketplace upgrade issueflow-skills
```

Restart Codex after an upgrade if the new skills do not appear immediately.

## Optional Automatic Refresh

Codex provides the `upgrade` command; fully automatic refresh depends on the computer running that command on a schedule.

Windows Task Scheduler example:

```powershell
schtasks /Create /SC DAILY /TN "Codex Issueflow Plugin Upgrade" /TR "codex plugin marketplace upgrade issueflow-skills" /ST 09:00
```

macOS or Linux cron example:

```cron
0 9 * * * codex plugin marketplace upgrade issueflow-skills
```

Use a pinned ref such as a release tag when stability matters more than immediate updates:

```bash
codex plugin marketplace add <owner>/issueflow-skills --ref v0.2.0
```

Use `main` when every computer should track the latest maintained version.
