---
name: issueflow
description: Umbrella entrypoint for issue-driven Git Flow-lite work. Use to adopt issueflow, clarify a feature, continue an autonomous cycle, schedule parallel worktree lanes, govern a plan-first project, or route issue discovery, proof, merge, and compound learning.
---

# issueflow

Route the request, preserve project truth, and keep implementation moving through issues to `develop`.

## Hard gates

- In autonomous cycles, keep the main thread as scheduler, reviewer, integrator, and merge-gate owner. Delegate implementation when workers are authorized; otherwise record a no-safe-delegation rationale before editing issue code.
- `issueflow parallel` explicitly authorizes subagents and worktrees. Plain `issueflow` does not. For complex work, shape independent lanes first; request `issueflow parallel` only if missing worker authorization would force main-thread or serialized implementation.
- `Serialized` controls dependency or merge order; it does not authorize main-thread implementation.
- After dispatch, continue read-only scheduling instead of idling. Before `wait_agent`, scan and record Ready/Active, backlog/drafts, plan gaps, proof/test failures, review/feedback findings, solution follow-ups, and stale/deferred candidates. If nothing can dispatch, record one reason: `no-candidate-after-minimum-scan`, `overlaps-active-lane`, `active-lane-budget-full`, or `blocked-on-worker-output`.

## Routing

- New/adopting repo -> `repo-bootstrap`
- Ambiguous feature, product, or UI request -> `issue-brainstorm`
- Concrete problem or issue draft -> `issue-raise`
- Readiness -> `issue-intake`
- Branch/worktree/worker scheduling -> `issue-dispatch`
- Web or Flutter implementation -> `implement-web` or `implement-flutter`
- Proof -> `qa-web-proof` or `qa-flutter-proof`
- `issue/* -> develop` -> `merge-gate`
- Post-merge learning and cleanup -> `issue-compound`
- `develop -> main` -> `release-gate`

## Two tracks

- **Autonomous Cycle:** on continue, iterate, resume, failures, reviews, or feedback, scan durable signals and create the next issue or multi-issue wave without waiting for the user to name every task.
- **Interactive Feature Intake:** read repo context, clarify implementation-critical ambiguity, compare 2-3 approaches, obtain direction, then create an issue or wave. Concrete low-risk bugs may use a compact intake.

If work already changed before routing, backfill the issue, wave, and proof trail honestly.

## Project truth and context

- Read macro then micro context: current-state pointer, plan anchor, current wave/issue, recent proof, branch/worktrees, next action, then matching solution-index entries.
- Treat the active plan as product truth. Classify work as `aligned`, `extension`, `conflict`, or `deviation`; update or record a decision before dispatching extensions/conflicts.
- Plan work must name the target user goal experience and user-visible proof.
- Prefer medium user-visible vertical slices and waves of independent lanes. Combine tiny related findings; do not create one-issue waves without a concrete reason.
- Keep `PLAN_ANCHOR.md` and `CURRENT_STATE.md` bounded. Search archives before opening them; never bulk-load completed issues, old waves/proof, or all solution notes.
- If automation needs user input, credentials, or a product/policy choice, pause it with a resume condition; do not delete it.

## Finish contract

- Start fresh issue work from `develop`; use `issue/*` branches/worktrees for implementation.
- An issue finishes only after merge or PR/merge-queue handoff to `develop`, integrated proof as required, durable state updates, and returning the root checkout to `develop`.
- Record follow-up work as issues or a concrete no-follow-up rationale.
- Run `issue-compound` when work produced reusable learning, prevention rules, failed approaches, follow-up triggers, plan gaps, or stale active context.

## References

Load only what the current decision needs:

- Tracks/planning: `../../references/two-track-routing.md`, `../../references/interactive-brainstorming.md`, `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`
- Scheduling: `../../references/autonomous-wave-generation.md`, `../../references/issue-sizing-and-scheduling.md`, `../../references/parallel-delivery.md`
- Lifecycle/context: `../../references/branch-lifecycle.md`, `../../references/automation-governance.md`, `../../references/compound-learning.md`, `../../references/context-governance.md`, `../../references/history-compaction.md`
- Product shape: `../../references/vertical-slice-architecture.md`, `../../references/experience-first-ui.md`
- Full policy conflicts/onboarding: `../../OPERATING-MODEL.md`
- Durable artifacts: `../../templates/`
