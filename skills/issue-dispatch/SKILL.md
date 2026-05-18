---
name: issue-dispatch
description: Dispatch implementation-ready issues into Git Flow-lite work branches from develop, decide whether multiple issues can run in parallel safely, and preserve isolation through issue-scoped ownership.
---

# issue-dispatch

Dispatch work only when the baseline is green and the issue is ready.

## Preconditions

- Baseline checks on `develop` are green.
- The issue passed intake.
- The target branch is `develop`.
- The current checkout is `develop`, or the work will use a new isolated worktree created from `develop`.
- No unrelated `issue/*` branch is being reused as the workspace.
- The repo's local proof commands are known.
- If a plan anchor exists, the issue's relationship to that plan is explicit.
- If the issue extends or conflicts with the plan, the plan update, decision-log entry, or plan-change note is already recorded.
- The issue has a vertical slice shape, or a support-only/contract-first reason with a named downstream core slice.
- For wave dispatch, each lane has an owner, proof command, dependency note, and worktree or serialization decision.

## Branching rules

- Branch format: `issue/<n>-<slug>`
- Branch from `develop`
- Use isolated worktrees when multiple issues run in parallel
- Use worktree-first dispatch when two or more lanes have disjoint ownership and separable proof commands
- For wave dispatch, keep the root checkout on `develop` as the scheduler/integration checkout; create each `issue/*` branch inside its own worktree
- If two issues touch the same files or same feature slice, serialize them
- Prefer one branch per vertical slice for product work
- Never dispatch a new issue from an existing `issue/*` branch
- If already on `issue/*`, block dispatch unless that branch matches the same issue id
- In autonomous wave work, the main agent must first scan for non-overlapping lanes and delegate them when allowed; direct implementation by the main agent needs a no-safe-delegation rationale
- Block one-issue waves unless there is a concrete reason it must still be tracked as a wave

## Branch lifecycle

Dispatch must record:

- current branch before dispatch
- target issue id and branch name
- base `develop` snapshot or commit
- whether this is a normal checkout or isolated worktree
- expected post-merge return path to `develop`

Use `../../references/branch-lifecycle.md` when the checkout is already on an issue branch, when worktrees are involved, or when prior issue work is unfinished.

If the previous issue branch has not merged, decide explicitly:

- finish and send it to `merge-gate`
- park it and create a separate worktree from `develop`
- serialize the new issue until the old branch merges

Do not keep working on the previous issue branch just because it is already checked out.
Do not dispatch a new issue from a branch that is merely merge-ready. Merge it to `develop`, or park it and start the new issue from a fresh `develop` worktree.

## Parallel safety

Run in parallel only when all of these are true:

- File ownership is disjoint or nearly disjoint
- Acceptance criteria do not depend on another open issue
- Test harness updates do not overwrite the same baselines
- Release order does not matter
- Both issues can name a stable base snapshot from `develop`

If independent issues are parallelized, record for each one:

- base `develop` snapshot or commit
- owned files or owned area
- expected harness touchpoints
- whether merge queue is required
- lane proof command, especially in multi-package repos
- plan classification: `core`, `support`, `internal`, or `deviation`

When the repo has multiple packages or services, prefer package-lane dispatch:

- one issue per ownership lane when possible
- one package-local proof command per lane
- a wave record when multiple lanes move together
- if one lane defines a shared contract for the others, mark it as `contract-first`
- if a support lane is dispatched before its consumer, name the downstream vertical slice and expected restack point

Use `../../references/parallel-delivery.md`, `../../references/issue-sizing-and-scheduling.md`, and `../../templates/PARALLEL-WAVE.template.md` when dispatching a multi-issue wave.

For wave dispatch, prefer `.worktrees/` or the repo's established worktree location. Confirm it is ignored or otherwise safe before creating local worktrees. If worktrees are not safe, serialize or use the repo-approved parallelism policy.

When worktrees are used, do not switch the root checkout away from `develop` for lane implementation. The root checkout coordinates status, proof review, queue order, merge-gate, and integration.

When subagents are available and policy allows them, dispatch independent wave lanes with issue id, worktree path, owned paths, out-of-scope boundaries, proof command, dependency notes, and expected summary format. Use `high` reasoning effort by default for implementation workers; use `medium` only for trivial low-risk lanes. The worker prompt must explicitly say the worker is not alone, must use only its assigned worktree, must not touch the root `develop` checkout, and must not revert other workers' changes. The main agent tracks lane status, proof, conflicts, and merge order.

Serialize instead of parallelizing when issues change shared contracts such as:

- root wrapper scripts
- shared schema modules
- generated fixtures or golden baselines
- root-level proof registries that another in-flight issue also edits
- a new contract-provider issue that downstream lanes are already consuming without revalidation

Also serialize or re-prioritize when a wave becomes too internally focused:

- if the repo still lacks a real user-facing slice, do not dispatch a full wave of `internal` issues
- if a plan emphasizes visuals, interaction, or a primary workflow, ensure at least one dispatched issue clearly advances that promise
- if the issue changes a user-facing screen, ensure the assigned lane owns aesthetic review and native-language copy review, not only functional implementation

When a live playtest or user report produces multiple product-facing failures:

- create one corrective wave for that batch
- parallelize issues whose write scopes are disjoint
- do not treat the feedback batch as closed until every issue in that corrective wave is implemented and re-verified

## Dispatch output

- Branch name
- Suggested owner skill
- Expected files or areas
- Parallel or serialized decision
- Required QA skill after implementation
- Base snapshot for later merge validation
- Wave id if the issue belongs to a planned parallel batch
- Plan classification and any drift warning
- Plan-change status when the issue is an extension, conflict, or deviation
- Vertical slice boundary or support-only justification
- UI aesthetic and native-copy review owner when the issue changes screens or visible text
- Current branch before dispatch
- Base `develop` snapshot
- Worktree-first decision and lane paths when this is a wave
- Scheduler checkout path and confirmation that it remains on `develop`
- Non-overlap lane scan and main-agent-direct-work rationale, if any
- One-issue wave rationale, if applicable
- Subagent delegation plan or no-delegation rationale when this is a wave
- Worker reasoning effort, default `high`, or `medium` with trivial-lane rationale
- Worker prompt root-checkout and other-worker guardrails
- Post-merge return-to-`develop` note

## Hand-off routing

- Web-heavy issue -> `implement-web`
- Flutter-heavy issue -> `implement-flutter`
- Mixed issue -> split if possible, otherwise declare the dominant stack
