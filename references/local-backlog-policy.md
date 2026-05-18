# Local Backlog Policy

Use a local backlog when GitHub issues are not attached yet.

## Recommended files

- `docs/plan/PLAN.md` or another primary plan when the project is plan-driven
- `docs/plan/PLAN_ANCHOR.md` or an equivalent compact plan summary
- `backlog/BOARD.md`
- `backlog/CURRENT_STATE.md`
- `backlog/BRAINSTORMS.md` or `backlog/brainstorms/`
- `backlog/WAVES.md`
- `backlog/issues/active/0001-...md`
- `backlog/issues/done/0001-...md`
- `backlog/issues/archive/0001-...md`

## Why

- preserves issue-driven structure before hosted tooling exists
- keeps numbering and handoff discipline
- gives autonomous cycles somewhere durable to place next-issue and wave candidates
- lets agents start from current pointers instead of reading every old issue
- lets AI agents work against durable local issue files
- records subagent authorization so parallel work does not depend on guesswork

## Rule

Do not lower issue quality just because the issue is local instead of hosted.

Local issues should still carry:

- problem
- slice shape or support reason
- acceptance criteria
- test plan
- scope
- docs plan
- handoff notes
- branch, base snapshot, and merge/return-to-develop status
- origin: `brainstorm`, `autonomous-scan`, `review-finding`, `compound-learning`, or `user-request`

The current-state file should name only the active issue or wave, plan anchor summary, current plan gaps, recent proof pointer, relevant solution index entries, and subagent authorization policy. It should not duplicate the whole backlog or full plan.

Keep the active issue set intentionally small enough to scan.

In many projects that means only a few issues. When the team wants a wider near-term horizon, it is still okay to keep roughly `6-10` active issues as long as:

- they are grouped into explicit waves in `backlog/WAVES.md`
- the current implementation still focuses on one dependency wave at a time
- older completed issues keep moving into `done/` and `archive/`
- issue branches still merge into `develop`, or open the required PR path, before another issue starts from the checkout
- after merge or PR creation, the checkout returns to `develop`

This lets AI agents see the next chunk of work without turning the whole project history into one giant active queue.

If a project plan exists, active issues should still make the current plan direction visible.

Good practice:

- keep at least one active `core` issue that clearly advances the product promise
- avoid filling the whole active lane with internal-only work while the core slice is still weak
- prefer active `core` issues that can be implemented as vertical slices instead of disconnected layers
- keep branch status visible so stale `issue/*` branches do not become the default workspace
- note plan relationship and plan update status in issue bodies when that context matters
