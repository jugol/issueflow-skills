---
name: repo-bootstrap
description: Apply the issueflow workflow to a concrete repository by scaffolding plan governance, local-first check entrypoints, issue and PR templates, optional GitHub forms, vertical-slice-oriented issue shaping, and workflow notes that match the shared Git Flow-lite process.
---

# repo-bootstrap

This skill takes the shared pack and adapts it to a real repository.

## Goals

- Adapt issueflow to the repo without hard-coding one stack's commands everywhere.
- Keep local verification as canonical, with GitHub integration when available.
- Convert a plan or rough brief into the first executable issue/wave.
- Establish plan governance, target user goal experience, branch lifecycle, worktree/subagent policy, context compaction, and compound-learning locations.
- Default product work to vertical slices and experience-first UI quality, not proof dashboards.

## Scaffold

- Issue, PR, and optional GitHub form/templates; local backlog when GitHub is absent.
- Local check entrypoints, optional CI wrappers that call the same commands, and test harness registry.
- Current-state pointer, cycle compaction location, history archive/index, and automation pause policy.
- Plan governance: primary plan, compact anchor, roadmap, decisions, and optional area plans.
- Brainstorm, wave, and solution-note locations plus `docs/solutions/INDEX.md`.
- Branch lifecycle checklist for `develop`, `issue/*`, merge, and return-to-`develop`.
- Worktree ignore/policy such as `.worktrees/`, explicit subagent authorization policy, and `issueflow parallel` as the automation-prompt authorization trigger when parallel delivery is expected.
- Greenfield stack and repo-topology decision record when needed.

## Package resources

Use these package resources when the repo needs more than the core checklist:

- Full model: `../../OPERATING-MODEL.md`
- Greenfield/plan references: `../../references/greenfield-bootstrap.md`, `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`, `../../references/stack-selection.md`
- Issue-flow references: `../../references/two-track-routing.md`, `../../references/interactive-brainstorming.md`, `../../references/autonomous-wave-generation.md`
- Repo integration references: `../../references/github-adoption.md`, `../../references/local-backlog-policy.md`, `../../references/local-checks-policy.md`, `../../references/pr-template-policy.md`, `../../references/harness-governance.md`
- Lifecycle memory references: `../../references/automation-governance.md`, `../../references/compound-learning.md`, `../../references/context-governance.md`, `../../references/history-compaction.md`
- Scaffolds: `../../templates/`

## Local-first rule

If the repo already has stable local commands like `npm run test`, `pnpm test`, or `flutter test`, reuse them.

If not, create thin cwd-robust, platform-aware wrapper scripts instead of long copy-paste command lists. Do not add package-manager indirection for checks that can be one deterministic script call.

## GitHub rule

If the repo uses GitHub, recommend:

- issue forms, PR template, branch protection on `develop`/`main`, required checks that mirror local commands, and a PR/merge process that returns checkout to `develop`

If the repo does not use GitHub, keep the same issue and proof structure in local files.

## Greenfield rule

If the project begins with only a plan document, create or identify:

- primary plan, preferably `docs/plan/PLAN.md`
- compact `PLAN_ANCHOR.md`, including target user goal experience
- `DECISIONS.md`, `ROADMAP.md`, and `areas/` only when sequencing, plan-change history, or scan cost justifies them
- first stack/topology decision, local proof entrypoint, branch lifecycle rule, and current-state pointer
- cycle compaction, history archive/index, brainstorm/wave, and solution-note locations
- subagent authorization policy: explicitly allowed, not allowed, or approval required; if allowed for automations, record `issueflow parallel` in the automation prompt and current-state pointer
- first issue or wave from unimplemented plan gaps, preferably with at least one thin user-visible vertical slice

The anchor summary should capture core product promise, target user goal experience, non-negotiable UX/art targets, copy tone, first-session or primary-action experience, MVP boundaries, and explicit anti-goals.

When creating the first issue wave, tag each issue mentally or explicitly as `core`, `support`, `internal`, or `deviation`.

Route later plan extensions/conflicts through plan governance before dispatch. Prefer core vertical slices; name downstream consumers for support/contract-first work. For UI-heavy plans, make the first product slice experience-first and include aesthetic/native-copy expectations. Do not spend multiple waves on internal proof layers while the core product promise is absent.

## PR template rule

Keep the core required sections stable across projects:

summary, linked issue, scope, proof, risk review, and docs.

Project-specific sections may be appended below the core. Do not let custom sections replace the core proof structure.

## Output

- Files scaffolded or recommended
- Plan governance paths, target user goal experience, and missing-question handoff
- Existing commands reused and wrapper commands added
- Optional GitHub files/actions
- Initial issue wave or first issue
- Current-state, compaction, history, brainstorm, wave, and solution-note locations
- Automation pause/resume policy
- Branch lifecycle, worktree policy, and subagent authorization policy
- Vertical-slice, experience-first UI, aesthetic, and native-copy expectations
- Follow-up skill to use next
