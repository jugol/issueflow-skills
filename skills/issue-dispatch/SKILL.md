---
name: issue-dispatch
description: Dispatch ready issues from develop into Git Flow-lite branches or worktrees, decide parallel safety, authorize and prompt workers, keep the root checkout as scheduler/integrator, and control merge order.
---

# issue-dispatch

Dispatch only from a green `develop` baseline with an intake-ready issue.

## Delegation gate

Before any issue-code edit, decide whether the lane is a bounded worker task. If yes, dispatch it and keep the root checkout as coordinator; if no, record the no-safe-delegation rationale before editing.

Worker use requires explicit authorization from `issueflow parallel` in the current request/automation prompt or a current-state handoff quoting it. For complex work, run the non-overlap scan first. If authorization alone blocks safe parallelism, ask for `issueflow parallel`; do not silently implement or serialize in the main thread.

## Preconditions

- Issue is ready, plan relationship is resolved, and proof commands are known.
- Checkout is `develop`, or an isolated worktree will branch from `develop`; never reuse an unrelated `issue/*` branch.
- Each lane names owner, owned paths, dependency, proof, worktree/serialization decision, and vertical-slice or downstream-core rationale.

## Branch and lane rules

- Branch as `issue/<n>-<slug>` from `develop`.
- Prefer one branch per medium vertical slice.
- Use worktrees when two or more lanes have disjoint ownership and separable proof. Keep root on `develop` for scheduling, review, queue order, and integration.
- Serialize shared files/contracts, schemas, fixtures/goldens, root registries, or dependent consumer/provider changes.
- `Serialized` means dependency/merge order, not a ban on worker delegation.
- Block one-issue waves unless wave-level tracking has a concrete benefit.
- If prior issue work is unfinished, explicitly finish/merge, park in its worktree, or serialize the new issue.

For every worker prompt include issue id, assigned worktree, owned paths, out-of-scope boundaries, proof command, dependencies, and expected summary. State that other workers exist, the root `develop` checkout is off-limits, and other changes must not be reverted. Default to `high` reasoning effort for implementation, QA, review, intake, investigation, and scheduling-relevant work; use `medium` only when a trivial lane cannot affect issue shape or scheduling.

## Scheduler loop

After dispatch, update state and keep finding non-overlapping work. Before `wait_agent`, scan Ready/Active, backlog/drafts, plan gaps, proof/test failures, review/feedback, solution follow-ups, and stale/deferred candidates. Dispatch when authorization, lane budget, ownership, and merge order are clear.

If no lane dispatches, record exactly one reason: `no-candidate-after-minimum-scan`, `overlaps-active-lane`, `active-lane-budget-full`, or `blocked-on-worker-output`. Ready/Active alone is not a minimum scan.

## Dispatch record

Record:

- branch/worktree, base `develop` snapshot, scheduler checkout, and return path
- scope, plan class, owner, owned paths, dependencies, and proof
- wave id, lane budget, non-overlap decision, merge order, and before-wait scan
- authorization source, worker effort/prompt guardrails, or no-delegation rationale
- QA skill and UI aesthetic/native-copy owner when relevant

## References and handoff

- Branch/worktrees: `../../references/branch-lifecycle.md`
- Parallel safety, sizing, and wave template: `../../references/parallel-delivery.md`, `../../references/issue-sizing-and-scheduling.md`, `../../templates/PARALLEL-WAVE.template.md`
- Web -> `implement-web`; Flutter -> `implement-flutter`; split mixed work when ownership/proof is separable.
