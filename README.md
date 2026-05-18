# issueflow-skills

Issueflow is a Codex plugin and Agent Skills pack for issue-driven development with Git Flow-lite, plan governance, two-track planning, and compound learning.

It helps an agent follow a durable loop:

1. Discover or clarify the next issue through autonomous scan, plan-gap scan, or interactive brainstorming.
2. Shape medium-sized issues or a multi-issue wave.
3. Validate that the issue is implementation-ready.
4. Dispatch work from `develop` into isolated `issue/<n>-<slug>` branches or worktrees.
5. Implement inside issue scope only.
6. Prove the result with durable QA evidence.
7. Merge into `develop` only after `merge-gate`.
8. Capture reusable learning with `issue-compound`.
9. Promote from `develop` to `main` through `release-gate`.

Issueflow can start from a single detailed product plan. As the project grows, it keeps a compact plan anchor and optional `docs/plan/` structure so agents can compare new work against product truth without loading every planning document.

Issueflow keeps long-running projects manageable by reading current pointers first and searching archives only when needed.
Autonomous cycles preserve both macro direction, such as product promise and wave goal, and micro direction, such as the active issue, proof pointer, branch/worktree, and next action.
Completed issue history should compact into `docs/history/` or the repo's equivalent archive so `PLAN_ANCHOR.md` and `CURRENT_STATE.md` stay short.
Autonomous cycles should combine related tiny findings into medium vertical slices, form waves when independent lanes exist, and keep the main agent focused on scheduling and integration.

## Package Layout

This repository is also the plugin root.

```text
issueflow-skills/
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── .claude-plugin/marketplace.json
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

## Install For Codex

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

## Install For Claude Code

Issueflow is also packaged as a Claude Code plugin marketplace. In Claude Code, add the marketplace and install the plugin:

```text
/plugin marketplace add jugol/issueflow-skills
/plugin install issueflow@issueflow-skills
```

Claude plugin skills are namespaced. Invoke the umbrella skill directly with:

```text
/issueflow:issueflow
```

For local testing before publishing, start Claude Code with the plugin directory:

```bash
claude --plugin-dir .
```

## Update Across Computers

Use `main` as the marketplace ref when your computers should track the latest maintained version:

```bash
codex plugin marketplace add <owner>/issueflow-skills --ref main
codex plugin marketplace upgrade issueflow-skills
```

Run `upgrade` on each computer whenever you want to refresh the installed plugin cache. For unattended refresh, schedule that command with Task Scheduler, cron, or another local automation on each computer.

For Claude Code, refresh the marketplace and update the plugin:

```bash
claude plugin marketplace update issueflow-skills
claude plugin update issueflow@issueflow-skills
```

Use a release tag when a computer should stay pinned until you intentionally move it:

```bash
codex plugin marketplace add <owner>/issueflow-skills --ref v0.3.4
```

See [UPDATE.md](./UPDATE.md) for publisher and consumer update workflows.

## Skills

- `issueflow`: umbrella router for the pack
- `issue-brainstorm`: clarify user-requested features before issue creation
- `issue-raise`: turn rough work into implementation-ready issues
- `issue-intake`: decide whether an issue can start
- `issue-dispatch`: create issue-scoped branches or worktrees
- `repo-bootstrap`: add issueflow scaffolding to a repo
- `implement-web`: implement browser-based issue work with durable proof
- `implement-flutter`: implement Flutter issue work with durable proof
- `qa-web-proof`: produce Playwright-backed web QA evidence
- `qa-flutter-proof`: produce Flutter widget, integration, and golden evidence
- `merge-gate`: decide whether `issue/*` can merge into `develop`
- `issue-compound`: capture reusable learning and follow-up triggers after merge or PR handoff
- `release-gate`: decide whether `develop` can promote to `main`

## Core Rules

- Concrete development work starts with an issue or a confirmed existing issue.
- Work branches start from `develop` and use `issue/<n>-<slug>`.
- One issue branch owns one issue scope.
- Product work should prefer vertical slices with user-visible outcomes.
- Issues should be medium-sized by default: neither atomized nor hiding independent outcomes.
- Product plans should name the target user goal experience, not only feature lists.
- A durable product plan should act as source of truth: aligned work cites it, extensions update it, conflicts need a plan-change decision, and missing planned behavior becomes plan-gap issue candidates.
- Feature requests go through interactive brainstorming when the direction is ambiguous.
- Imprecise user requests should trigger focused clarification before implementation-critical assumptions become issue scope.
- Automation and continuation cycles actively scan for follow-up issues and waves.
- Autonomous waves should use the main agent as scheduler/integrator and delegate independent lanes when allowed.
- During a wave, the root checkout should stay on `develop`; issue branches should live in separate worktrees.
- User-blocked automations should be paused with a resume condition, not deleted.
- Independent wave lanes should prefer worktrees when ownership and proof are separable.
- User-facing UI should be experience-first, not proof-dashboard-first.
- Active context stays small: read current-state pointers first, then search archived issues, old waves, and solution notes only when relevant.
- Completed issue details compact into history; active files keep only recent summaries and pointers.
- Every completed branch needs durable local proof before merge.
- Nothing merges into `develop` without `merge-gate`.
- A proven issue is only merge-ready until it enters `develop`.
- Resolved issues must leave the checkout on `develop`, not on `issue/*`.
- Nothing promotes to `main` without `release-gate`.
- Reusable lessons should be captured in `docs/solutions/` when they can help future agents.

## Shared References

- [OPERATING-MODEL.md](./OPERATING-MODEL.md)
- [branch-lifecycle.md](./references/branch-lifecycle.md)
- [autonomous-wave-generation.md](./references/autonomous-wave-generation.md)
- [automation-governance.md](./references/automation-governance.md)
- [compound-learning.md](./references/compound-learning.md)
- [context-governance.md](./references/context-governance.md)
- [contract-naming.md](./references/contract-naming.md)
- [experience-first-ui.md](./references/experience-first-ui.md)
- [github-adoption.md](./references/github-adoption.md)
- [greenfield-bootstrap.md](./references/greenfield-bootstrap.md)
- [goal-experience-planning.md](./references/goal-experience-planning.md)
- [harness-governance.md](./references/harness-governance.md)
- [history-compaction.md](./references/history-compaction.md)
- [interactive-brainstorming.md](./references/interactive-brainstorming.md)
- [issue-sizing-and-scheduling.md](./references/issue-sizing-and-scheduling.md)
- [local-backlog-policy.md](./references/local-backlog-policy.md)
- [local-checks-policy.md](./references/local-checks-policy.md)
- [parallel-delivery.md](./references/parallel-delivery.md)
- [plan-alignment.md](./references/plan-alignment.md)
- [plan-governance.md](./references/plan-governance.md)
- [pr-template-policy.md](./references/pr-template-policy.md)
- [stack-selection.md](./references/stack-selection.md)
- [two-track-routing.md](./references/two-track-routing.md)
- [vertical-slice-architecture.md](./references/vertical-slice-architecture.md)

## Templates

- [BACKLOG-BOARD.template.md](./templates/BACKLOG-BOARD.template.md)
- [BRAINSTORM.template.md](./templates/BRAINSTORM.template.md)
- [CURRENT-STATE.template.md](./templates/CURRENT-STATE.template.md)
- [CYCLE-COMPACTION.template.md](./templates/CYCLE-COMPACTION.template.md)
- [GITHUB-ISSUE-FORM.example.yml](./templates/GITHUB-ISSUE-FORM.example.yml)
- [HISTORY-INDEX.template.md](./templates/HISTORY-INDEX.template.md)
- [ISSUE.template.md](./templates/ISSUE.template.md)
- [PARALLEL-WAVE.template.md](./templates/PARALLEL-WAVE.template.md)
- [PLAN-ANCHOR.template.md](./templates/PLAN-ANCHOR.template.md)
- [PLAN-CHANGE.template.md](./templates/PLAN-CHANGE.template.md)
- [PULL_REQUEST.template.md](./templates/PULL_REQUEST.template.md)
- [PULL_REQUEST.core-and-extension.example.md](./templates/PULL_REQUEST.core-and-extension.example.md)
- [SOLUTION.template.md](./templates/SOLUTION.template.md)
- [SOLUTION-INDEX.template.md](./templates/SOLUTION-INDEX.template.md)
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
codex, codex-plugin, agent-skills, issueflow, git-flow-lite, issue-driven-development, brainstorming, compound-engineering, worktrees, qa, playwright, flutter
```
