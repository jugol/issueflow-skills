---
name: repo-bootstrap
description: Adapt issueflow to a repository by scaffolding plan governance, local proof entrypoints, issue/PR artifacts, branch and worktree policy, bounded context, and the first executable issue or wave.
---

# repo-bootstrap

Adapt the pack to the repo's stack and existing conventions.

## Scaffold

- Issue/PR templates, optional GitHub forms, or a local numbered backlog
- Canonical local checks, optional CI wrappers, and harness registry
- Primary plan, compact plan anchor, current-state pointer, roadmap/decisions/area plans only when scale requires them
- Brainstorm, wave, history/index, compaction, and `docs/solutions/INDEX.md` locations
- `develop`/`issue/*` lifecycle, return-to-`develop` rule, worktree location/ignore policy, and automation pause/resume policy
- Subagent policy. When parallel automation is allowed, put `issueflow parallel` in its prompt and current-state handoff.

Reuse stable repo commands. If missing, add thin cwd-robust platform-aware wrappers; CI should call the same canonical checks.

## Plan-first and greenfield

A repo may begin with one detailed plan. Identify or create `docs/plan/PLAN.md`, then derive:

- a bounded `PLAN_ANCHOR.md` with product promise, target user goal experience, MVP boundaries, non-negotiable UX/art/copy direction, and anti-goals
- stack/topology and plan-change decisions only as needed
- first issue or wave from unimplemented plan gaps, including at least one user-visible vertical slice

Classify work as `core`, `support`, `internal`, or `deviation`. Do not let internal proof layers outrank an absent core product experience without rationale.

## GitHub and PR policy

When GitHub is present, recommend branch protection and required checks on `develop`/`main`, issue forms, and a PR template with summary, linked issue, scope, proof, risk, and docs. Without GitHub, keep equivalent local artifacts.

## Output

Report scaffolded/reused files and commands, plan and target experience, first issue/wave, lifecycle/worktree/subagent policy, context/history/solution locations, automation policy, and next skill.

## References

Load only the needed group:

- Plan/greenfield: `../../references/greenfield-bootstrap.md`, `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`, `../../references/stack-selection.md`
- Repo integration: `../../references/github-adoption.md`, `../../references/local-backlog-policy.md`, `../../references/local-checks-policy.md`, `../../references/pr-template-policy.md`, `../../references/harness-governance.md`
- Lifecycle/context: `../../references/automation-governance.md`, `../../references/context-governance.md`, `../../references/history-compaction.md`, `../../references/compound-learning.md`
- Full model and scaffolds: `../../OPERATING-MODEL.md`, `../../templates/`
