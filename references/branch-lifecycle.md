# Branch Lifecycle

Issueflow branch isolation only works when every issue branch has a clear beginning and end.

## Core rule

- `develop` is the dispatch base.
- `issue/<n>-<slug>` is for exactly one issue.
- A new issue must not start on an existing `issue/*` branch.
- Every completed issue branch must pass through `merge-gate`.
- A proven issue is not complete while the working checkout remains on `issue/*`.
- After approval, merge into `develop` directly unless repo policy requires a PR or merge queue.
- After merge, PR creation, or explicit merge-blocked handoff, return the working checkout to `develop`.

An `issue/*` branch is not a long-running workspace. It is a temporary delivery lane.

## Before starting work

Before raising, dispatching, or implementing a new concrete change, check:

- current branch
- working tree status
- linked issue id, if already on `issue/*`
- whether the current branch already has unmerged work
- whether `develop` is current enough for a safe base

Use the repo's normal git tooling for this, such as `git branch --show-current`, `git status --short`, and `git rev-parse --short HEAD`.

If the current branch is `issue/*`:

- continue only if the requested work belongs to that same issue
- otherwise stop and route the existing branch to QA and `merge-gate`, or create an explicitly separate worktree from `develop`
- do not quietly implement a second issue on the same branch

## Dispatch sequence

Use this sequence for a normal issue:

1. Check out `develop`.
2. Update or verify `develop` according to the repo's policy.
3. Run the baseline proof required before dispatch.
4. Create `issue/<n>-<slug>` from `develop`.
5. Record the base snapshot or commit.
6. Implement only the approved issue scope.

If parallel work is needed, create separate issue branches or worktrees from `develop`. Do not multiplex unrelated issues inside one branch.

## Finish sequence

Use this sequence when implementation is complete:

1. Run the implementation skill's required local proof.
2. Run the matching QA proof skill.
3. Run `merge-gate`.
4. Save the issue branch name and ensure the working tree is clean except for intentional merge work.
5. Check out `develop`.
6. Update or verify `develop` according to repo policy.
7. Merge the issue branch into `develop`, or open the repo-required PR/merge-queue path.
8. Resolve merge conflicts on the integration path, preserving the approved issue scope.
9. Rerun the required integrated proof on `develop` after the merge or after any conflict resolution.
10. Update the issue, backlog board, and harness registry with proof and closure notes.
11. Leave the working checkout on `develop`.
12. Delete or archive the issue branch only according to repo policy.

Do not begin the next issue from the completed issue branch.

If repo policy requires PR-only integration, the agent should still return the local checkout to `develop` after opening or updating the PR. The final handoff must state that integration is pending review instead of claiming the issue is fully merged.

If merge conflicts occur, do not mark the issue complete until conflicts are resolved and the integrated proof passes on `develop`.

## Mismatch repair

If later work was accidentally committed on an older issue branch:

- identify which commits belong to the old issue and which belong to later work
- avoid adding more work to the stale branch
- finish or merge the original issue if it is valid
- move unrelated work to the correct issue branch by cherry-pick, patch, or a repo-approved split strategy
- record the repair in the issue or wave notes

Treat this as process repair, not as permission to keep using the stale branch.
