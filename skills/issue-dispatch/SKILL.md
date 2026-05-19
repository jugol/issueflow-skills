---
name: issue-dispatch
description: Dispatch implementation-ready issues into Git Flow-lite branches or worktrees from develop, decide parallel lane safety, record explicit subagent authorization, schedule worker handoffs, keep the root checkout as coordinator, and preserve issue-scoped ownership.
---

# issue-dispatch

Dispatch only from a green `develop` baseline and an intake-ready issue.

## Delegation gate

Before any code edit on an issue branch, decide whether the lane can be delegated as one bounded worker task. If yes, dispatch the worker and keep the root checkout as coordinator/integrator; if no, record the no-safe-delegation rationale before editing.

After dispatch, the main agent should keep scheduling instead of waiting by default: update the scheduler board, scan read-only for non-overlapping next candidates, and prepare safe follow-up lanes. Call `wait_agent` only when all safe scheduler actions are exhausted or blocked on worker output. Additional lane dispatch needs explicit subagent authorization, active-lane budget, and non-overlap with current worker ownership.

Before calling `wait_agent` while workers are active, perform and record a before-wait scheduler scan. Dispatch another worker if authorization, active-lane budget, non-overlap, and merge order are clear. If not dispatching, record exactly why: `no-candidate`, `overlaps-active-lane`, `active-lane-budget-full`, or `blocked-on-worker-output`.

## Preconditions

- Green `develop` baseline, intake-ready issue, known repo-local proof commands.
- Checkout is `develop`, or the lane will use an isolated worktree created from `develop`; never reuse an unrelated `issue/*` branch.
- Plan relationship is explicit; extensions/conflicts already have plan update, decision entry, or plan-change note.
- Issue shape is a vertical slice, or support/contract-first with a downstream core slice.
- Wave lanes name owner, proof command, dependency, and worktree or serialization decision.
- Subagent authorization is explicit when workers will be used; valid sources are `issueflow parallel` in the current user request or automation prompt, or a current-state handoff quoting that approval. For complex work, run the non-overlap scan first. If lanes are safe but authorization is missing, ask the user to run or confirm `issueflow parallel`; do not serialize or implement in the main thread solely because permission is missing.

## Branching and worktree rules

- Branch format: `issue/<n>-<slug>`
- Branch from `develop`.
- Prefer one branch per vertical slice; never dispatch new work from an existing `issue/*` branch unless it matches the same issue id.
- Use worktree-first dispatch when two or more lanes have disjoint ownership and separable proof commands.
- For waves, keep the root checkout on `develop` as scheduler/integration checkout; create each `issue/*` branch inside its own worktree.
- If two issues touch the same files or feature slice, serialize them.
- Treat `serialized` as dependency or merge-order control, not a ban on worker delegation unless the lane is explicitly marked fully serialized.
- Block one-issue waves unless there is a concrete reason to track the work as a wave.

## Branch lifecycle

Record current branch, target issue id, branch name, base `develop` snapshot, checkout/worktree mode, and expected post-merge return path to `develop`.

Use `../../references/branch-lifecycle.md` when the checkout is already on an issue branch, when worktrees are involved, or when prior issue work is unfinished.

If the previous issue branch has not merged, decide explicitly:

- finish and send it to `merge-gate`
- park it and create a separate worktree from `develop`
- serialize the new issue until the old branch merges

Do not keep working on a previous issue branch just because it is already checked out. If it is merge-ready, merge it to `develop` or park it before dispatching fresh work.

## Parallel safety

Run lanes in parallel only when ownership is disjoint, acceptance criteria do not depend on another open issue, harness updates do not overwrite the same baselines, release order does not matter, and each lane has a stable `develop` base.

For each parallel lane, record base snapshot, owned area, harness touchpoints, merge-queue need, lane proof command, and plan classification: `core`, `support`, `internal`, or `deviation`.

For multi-package repos, prefer package-lane dispatch: one issue per ownership lane, one package-local proof command per lane, wave record when lanes move together, `contract-first` for shared contract providers, and downstream core slice/restack point for support lanes.

Use `../../references/parallel-delivery.md`, `../../references/issue-sizing-and-scheduling.md`, and `../../templates/PARALLEL-WAVE.template.md` when dispatching a multi-issue wave.

For waves, prefer `.worktrees/` or the repo's established worktree location; confirm it is ignored or repo-approved. If worktrees are unsafe, serialize or follow repo policy.

When worktrees are used, keep the root checkout on `develop`. It coordinates status, proof review, queue order, merge-gate, and integration.

When subagents are explicitly authorized, dispatch independent lanes with issue id, worktree path, owned paths, out-of-scope boundaries, proof command, dependency notes, and expected summary format. Use `high` reasoning effort by default for implementation, QA, review, intake, scope investigation, and scheduling-influencing workers, even when read-only; use `medium` only for trivial lanes that cannot affect issue shape or wave scheduling. Worker prompts must say the worker is not alone, must use only the assigned worktree, must not touch the root `develop` checkout, and must not revert other workers' changes.

Serialize when lanes touch shared contracts: root wrapper scripts, shared schema modules, generated fixtures/golden baselines, root proof registries, or a contract provider already consumed by downstream lanes without revalidation.

Serialize or re-prioritize when the repo lacks a real user-facing slice, the plan's visual/interaction promise is not advanced, or a screen/copy lane lacks aesthetic and native-copy review.

When live feedback produces multiple product-facing failures, create one corrective wave, parallelize disjoint scopes, and keep the batch open until every issue is implemented and re-verified.

## Dispatch output

- Branch/workspace: branch name, current branch, base `develop` snapshot, worktree decision, scheduler checkout path, return-to-`develop` note.
- Scope: owner skill, expected files/areas, vertical slice or support rationale, plan classification, drift warning, and plan-change status.
- Scheduling: parallel/serialized decision, wave id, active-lane budget, non-overlap scan, before-wait scheduler scan, one-issue wave rationale if any.
- Delegation: subagent authorization source, `issueflow parallel` confirmation or no-parallel rationale, assignment or no-delegation rationale, worker effort, root-checkout and other-worker guardrails.
- Proof: required QA skill, lane proof command, UI aesthetic/native-copy owner when screens or visible text change.

## Hand-off routing

- Web-heavy issue -> `implement-web`
- Flutter-heavy issue -> `implement-flutter`
- Mixed issue -> split if possible, otherwise declare the dominant stack
