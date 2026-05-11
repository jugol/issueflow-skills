---
name: issueflow
description: Umbrella entrypoint for the issueflow pack. Use when the user wants to adopt or follow the Git Flow-lite issue-driven workflow, including vertical-slice-oriented issue delivery, but has not named the exact sub-skill yet.
---

# issueflow

This is the front door to the pack.

## Routing

- New repo or adopting the workflow in an existing repo -> `repo-bootstrap`
- Rough problem statement that should become an issue -> `issue-raise`
- Existing issue needs readiness review -> `issue-intake`
- Ready issue needs branching and ownership -> `issue-dispatch`
- Web implementation work -> `implement-web`
- Flutter implementation work -> `implement-flutter`
- Web QA proof before merge -> `qa-web-proof`
- Flutter QA proof before merge -> `qa-flutter-proof`
- Merge decision for `issue/* -> develop` -> `merge-gate`
- Release decision for `develop -> main` -> `release-gate`

## Shared package resources

Load package-level references only when the task needs deeper guidance. Paths are relative to this `SKILL.md`:

- `../../OPERATING-MODEL.md` for the full Git Flow-lite operating model
- `../../references/plan-alignment.md` when work must be checked against a product plan
- `../../references/vertical-slice-architecture.md` when shaping product issues
- `../../references/experience-first-ui.md` when UI work drifts toward proof dashboards
- `../../references/branch-lifecycle.md` when stale issue branches or worktrees are involved
- `../../references/parallel-delivery.md` when multiple issue branches can move together
- `../../templates/ISSUE.template.md` and `../../templates/PARALLEL-WAVE.template.md` when scaffolding durable local artifacts

## Default behavior

If the user asks broadly how to use the workflow in a repo, start with `repo-bootstrap`.

If the user arrives with only a project plan or product plan, still start with `repo-bootstrap` and generate the first issue wave from that plan.

If a plan already exists, treat it as an active constraint, not just bootstrap context. Keep checking new issues and waves against that plan as work progresses.

For product work, recommend vertical slice architecture as the default shape: one core issue should carry a thin user-visible behavior through the needed domain, contract, UI, and proof surfaces. If a support or contract-first issue is needed, name the downstream core slice it enables.

For user-facing UI, recommend experience-first design: the default screen should look and feel like the intended product, not a dashboard made to display proof. Keep diagnostics hidden, collapsed, test-only, or in stable attributes unless the product is actually an operational dashboard.

For screen judgment, explicitly check more than implementation correctness. The in-app surface should look aesthetically intentional to a human viewer, and all user-facing copy should sound natural to a fluent native speaker in the target language. If screenshots look ugly, broken, generic, or visually confusing, or if visible text sounds stiff, translated, or uncommon, treat the issue as unfinished even when automated checks pass.

For non-icon scene or product assets, require real raster imagery: generated or captured JPG/PNG files. SVG, CSS/canvas drawing, or hand-built vector-looking composites are acceptable for icons and controls only; do not pass them off as main scene assets, even when exported to JPG/PNG.

Before starting a new concrete change, check branch state. If the checkout is already on `issue/*`, continue only when the request belongs to that same issue. Otherwise route the stale branch through QA and `merge-gate`, or explicitly park it and dispatch the new issue from `develop`.

When the user asks to finish, complete, close, or resolve an issue, treat the work as unfinished until it is integrated into `develop` and the checkout has returned to `develop`. If repo policy requires PR-only integration, open or update the PR/merge queue path, return the local checkout to `develop`, and state that final integration is pending review.

If the user arrives with a concrete bug, feature idea, or product feedback that implies code changes, start with `issue-raise` before implementation. If the repo already has a matching active issue, use `issue-intake` on that issue instead of creating a duplicate.

If the user arrives with an existing issue link or issue body, start with `issue-intake`.

If an agent discovers it already implemented before routing through issueflow, it must repair the workflow trace before final handoff: create or update the issue, wave note, harness registry entry, and QA proof summary.
