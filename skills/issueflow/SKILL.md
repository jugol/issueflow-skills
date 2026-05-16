---
name: issueflow
description: Umbrella entrypoint for the issueflow pack. Use when the user wants to adopt or follow the Git Flow-lite issue-driven workflow, including plan-first starts, plan governance, vertical-slice issue delivery, two-track planning, and compound learning, but has not named the exact sub-skill yet.
---

# issueflow

This is the front door to the pack.

## Routing

- New repo or adopting the workflow in an existing repo -> `repo-bootstrap`
- User-requested feature, product behavior, UI change, or ambiguous improvement -> `issue-brainstorm`
- Rough problem statement that should become an issue -> `issue-raise`
- Existing issue needs readiness review -> `issue-intake`
- Ready issue needs branching and ownership -> `issue-dispatch`
- Web implementation work -> `implement-web`
- Flutter implementation work -> `implement-flutter`
- Web QA proof before merge -> `qa-web-proof`
- Flutter QA proof before merge -> `qa-flutter-proof`
- Merge decision for `issue/* -> develop` -> `merge-gate`
- Post-merge learning, prevention notes, or follow-up capture -> `issue-compound`
- Release decision for `develop -> main` -> `release-gate`

## Shared package resources

Load package-level references only when the task needs deeper guidance. Paths are relative to this `SKILL.md`:

- `../../OPERATING-MODEL.md` for the full Git Flow-lite operating model
- `../../references/plan-alignment.md` when work must be checked against a product plan
- `../../references/plan-governance.md` when a plan should be updated, split, or used as the source of truth for next work
- `../../references/two-track-routing.md` when choosing autonomous cycle vs interactive feature intake
- `../../references/interactive-brainstorming.md` when feature requests need clarification
- `../../references/autonomous-wave-generation.md` when a cycle should create follow-up issues or waves
- `../../references/automation-governance.md` when an automation must stop for user input, approval, credentials, or policy choice
- `../../references/compound-learning.md` when completed work should leave reusable memory
- `../../references/context-governance.md` when deciding what not to load or when active context feels noisy
- `../../references/vertical-slice-architecture.md` when shaping product issues
- `../../references/experience-first-ui.md` when UI work drifts toward proof dashboards
- `../../references/branch-lifecycle.md` when stale issue branches or worktrees are involved
- `../../references/parallel-delivery.md` when multiple issue branches can move together
- `../../templates/BRAINSTORM.template.md`, `../../templates/CURRENT-STATE.template.md`, `../../templates/CYCLE-COMPACTION.template.md`, `../../templates/ISSUE.template.md`, `../../templates/PARALLEL-WAVE.template.md`, `../../templates/PLAN-ANCHOR.template.md`, `../../templates/PLAN-CHANGE.template.md`, and `../../templates/SOLUTION.template.md` when scaffolding durable local artifacts

## Default behavior

If the user asks broadly how to use the workflow in a repo, start with `repo-bootstrap`.

Use a two-track router:

- Autonomous Cycle Track: use when a user or automation says to continue, iterate, resume, process failures, process review or playtest feedback, or choose the next useful issue. Scan durable signals and create or update follow-up issues or waves instead of waiting for the user to name every task.
- Interactive Feature Intake Track: use when the user describes a feature, product behavior, UI change, or ambiguous improvement. Route through `issue-brainstorm` before `issue-raise` unless the request is already concrete and low-risk. Actively ask when the user's wording is vague, contradictory, missing success criteria, or using undefined product terms that could change implementation.

Before loading history, apply context governance: read current pointers first, keep the active set small, search archives before opening them, and do not bulk-load completed issues, old waves, superseded brainstorms, old proof logs, or all solution notes.

At the start of an autonomous cycle, read macro direction and micro direction in order: current-state pointer, plan anchor summary, current wave goal, active issue, recent proof pointer, active branch or worktree, next recommended action, then relevant solution index entries. Include current plan gaps when the repo has `docs/plan/` or another primary plan. If these pointers are missing, stale, contradictory, or too broad, perform cycle compaction before selecting or creating the next issue.

If an automation cannot continue because it needs user input, approval, credentials, or a product/policy choice, pause the existing automation instead of deleting it. Record the blocker, question, active issue or wave, branch/worktree, proof pointer, resume condition, and next step in current-state or cycle compaction before asking the user.

If the user arrives with only a project plan or product plan, still start with `repo-bootstrap`, establish `docs/plan/PLAN.md` or the repo's chosen primary plan, create a compact plan anchor, and generate the first issue wave from unimplemented plan gaps.

If a plan already exists, treat it as an active source of truth, not just bootstrap context. Keep checking new issues and waves against that plan as work progresses.

When a user request differs from the plan, classify it before issue creation: `aligned`, `extension`, `conflict`, or `deviation`. For `extension` or `conflict`, update the plan or record a plan-change decision before dispatch. Do not let implementation silently change product truth.

When a user request is imprecise, do not silently fill in implementation-critical details. Ask focused questions tied to decisions such as actor, target screen, state, data ownership, proof, rollout, and plan relationship. Infer only low-risk details from repo context and record the assumption.

For product work, recommend vertical slice architecture as the default shape: one core issue should carry a thin user-visible behavior through the needed domain, contract, UI, and proof surfaces. If a support or contract-first issue is needed, name the downstream core slice it enables.

For user-facing UI, recommend experience-first design: the default screen should look and feel like the intended product, not a dashboard made to display proof. Keep diagnostics hidden, collapsed, test-only, or in stable attributes unless the product is actually an operational dashboard.

For screen judgment, explicitly check more than implementation correctness. The in-app surface should look aesthetically intentional to a human viewer, and all user-facing copy should sound natural to a fluent native speaker in the target language. If screenshots look ugly, broken, generic, or visually confusing, or if visible text sounds stiff, translated, or uncommon, treat the issue as unfinished even when automated checks pass.

For non-icon scene or product assets, require real raster imagery: generated or captured JPG/PNG files. SVG, CSS/canvas drawing, or hand-built vector-looking composites are acceptable for icons and controls only; do not pass them off as main scene assets, even when exported to JPG/PNG.

Before starting a new concrete change, check branch state. If the checkout is already on `issue/*`, continue only when the request belongs to that same issue. Otherwise route the stale branch through QA and `merge-gate`, or explicitly park it and dispatch the new issue from `develop`.

When the user asks to finish, complete, close, or resolve an issue, treat the work as unfinished until it is integrated into `develop` and the checkout has returned to `develop`. If repo policy requires PR-only integration, open or update the PR/merge queue path, return the local checkout to `develop`, and state that final integration is pending review.

After an issue is integrated or handed to the repo's PR/merge queue, perform a forward handoff before calling it done. Update the issue note, backlog or wave board, latest proof pointer, and any automation/run memory so the completed issue cannot be selected again. If the work revealed follow-up defects, polish, or next vertical slices, create or update those issues; if there is no follow-up, say so with a concrete reason.

After merge or PR handoff, run `issue-compound` when the issue produced reusable learning, a recurring prevention rule, a failed approach worth remembering, or follow-up issue triggers.

If the user arrives with a concrete bug or product feedback that implies code changes, start with `issue-raise` before implementation. If the report contains multiple independent findings, create a corrective wave instead of one vague issue. If the repo already has a matching active issue, use `issue-intake` on that issue instead of creating a duplicate.

If the user arrives with an existing issue link or issue body, start with `issue-intake`.

If an agent discovers it already implemented before routing through issueflow, it must repair the workflow trace before final handoff: create or update the issue, wave note, harness registry entry, and QA proof summary.
