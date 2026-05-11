# issueflow-skills

Issueflow is a Codex plugin and Agent Skills pack for issue-driven development with Git Flow-lite.

It helps an agent follow a durable loop:

1. Raise or refine an issue from natural language.
2. Validate that the issue is implementation-ready.
3. Dispatch work from `develop` into isolated `issue/<n>-<slug>` branches.
4. Implement inside issue scope only.
5. Prove the result with durable QA evidence.
6. Merge into `develop` only after `merge-gate`.
7. Promote from `develop` to `main` through `release-gate`.

## Package Layout

This repository is also the plugin root.

```text
issueflow-skills/
├── .codex-plugin/plugin.json
├── .agents/plugins/marketplace.json
├── skills/
├── references/
├── templates/
├── scripts/validate.py
└── OPERATING-MODEL.md
```

Codex loads the skills from `./skills/`. The shared references and templates are packaged next to the skills so the whole workflow can be installed as one plugin.

## Guides

- [English guide](./docs/README_en.md)
- [Korean guide](./docs/README_ko.md)

## Install

After publishing this repo to GitHub, add it as a Codex plugin marketplace:

```bash
codex plugin marketplace add <owner>/issueflow-skills --ref main
codex plugin marketplace upgrade issueflow-skills
```

Then restart Codex, open `/plugins`, choose the `Issueflow Skills` marketplace, and install `Issueflow`.

For local testing before publishing, run this from the repository root:

```bash
codex plugin marketplace add .
```

Direct skill installation with `$skill-installer` is possible, but the plugin install is preferred because it keeps all related skills, references, and templates together.

## Update Across Computers

Use `main` as the marketplace ref when your computers should track the latest maintained version:

```bash
codex plugin marketplace add <owner>/issueflow-skills --ref main
codex plugin marketplace upgrade issueflow-skills
```

Run `upgrade` on each computer whenever you want to refresh the installed plugin cache. For unattended refresh, schedule that command with Task Scheduler, cron, or another local automation on each computer.

Use a release tag when a computer should stay pinned until you intentionally move it:

```bash
codex plugin marketplace add <owner>/issueflow-skills --ref v0.2.0
```

See [UPDATE.md](./UPDATE.md) for publisher and consumer update workflows.

## Skills

- `issueflow`: umbrella router for the pack
- `issue-raise`: turn rough work into implementation-ready issues
- `issue-intake`: decide whether an issue can start
- `issue-dispatch`: create issue-scoped branches or worktrees
- `repo-bootstrap`: add issueflow scaffolding to a repo
- `implement-web`: implement browser-based issue work with durable proof
- `implement-flutter`: implement Flutter issue work with durable proof
- `qa-web-proof`: produce Playwright-backed web QA evidence
- `qa-flutter-proof`: produce Flutter widget, integration, and golden evidence
- `merge-gate`: decide whether `issue/*` can merge into `develop`
- `release-gate`: decide whether `develop` can promote to `main`

## Core Rules

- Concrete development work starts with an issue or a confirmed existing issue.
- Work branches start from `develop` and use `issue/<n>-<slug>`.
- One issue branch owns one issue scope.
- Product work should prefer vertical slices with user-visible outcomes.
- User-facing UI should be experience-first, not proof-dashboard-first.
- Every completed branch needs durable local proof before merge.
- Nothing merges into `develop` without `merge-gate`.
- A proven issue is only merge-ready until it enters `develop`.
- Resolved issues must leave the checkout on `develop`, not on `issue/*`.
- Nothing promotes to `main` without `release-gate`.

## Shared References

- [OPERATING-MODEL.md](./OPERATING-MODEL.md)
- [branch-lifecycle.md](./references/branch-lifecycle.md)
- [contract-naming.md](./references/contract-naming.md)
- [experience-first-ui.md](./references/experience-first-ui.md)
- [github-adoption.md](./references/github-adoption.md)
- [greenfield-bootstrap.md](./references/greenfield-bootstrap.md)
- [harness-governance.md](./references/harness-governance.md)
- [local-backlog-policy.md](./references/local-backlog-policy.md)
- [local-checks-policy.md](./references/local-checks-policy.md)
- [parallel-delivery.md](./references/parallel-delivery.md)
- [plan-alignment.md](./references/plan-alignment.md)
- [pr-template-policy.md](./references/pr-template-policy.md)
- [stack-selection.md](./references/stack-selection.md)
- [vertical-slice-architecture.md](./references/vertical-slice-architecture.md)

## Templates

- [BACKLOG-BOARD.template.md](./templates/BACKLOG-BOARD.template.md)
- [GITHUB-ISSUE-FORM.example.yml](./templates/GITHUB-ISSUE-FORM.example.yml)
- [ISSUE.template.md](./templates/ISSUE.template.md)
- [PARALLEL-WAVE.template.md](./templates/PARALLEL-WAVE.template.md)
- [PLAN-ANCHOR.template.md](./templates/PLAN-ANCHOR.template.md)
- [PULL_REQUEST.template.md](./templates/PULL_REQUEST.template.md)
- [PULL_REQUEST.core-and-extension.example.md](./templates/PULL_REQUEST.core-and-extension.example.md)
- [TEST-HARNESS-REGISTRY.template.md](./templates/TEST-HARNESS-REGISTRY.template.md)
- [check-local.example.ps1](./templates/check-local.example.ps1)
- [check-local.example.sh](./templates/check-local.example.sh)
- [github-workflow-local-parity.example.yml](./templates/github-workflow-local-parity.example.yml)

## Maintain

Run validation before publishing changes:

```bash
python scripts/validate.py
```

When releasing a new version:

1. Update `.codex-plugin/plugin.json`.
2. Update `CHANGELOG.md`.
3. Or run `python scripts/release.py <version>` to update both.
4. Run `python scripts/validate.py`.
5. Tag the release in Git after the remote is attached.

Suggested GitHub topics for discoverability:

```text
codex, codex-plugin, agent-skills, issueflow, git-flow-lite, issue-driven-development, qa, playwright, flutter
```
