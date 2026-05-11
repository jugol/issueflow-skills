# Local Backlog Policy

Use a local backlog when GitHub issues are not attached yet.

## Recommended files

- `backlog/BOARD.md`
- `backlog/issues/active/0001-...md`
- `backlog/issues/done/0001-...md`
- `backlog/issues/archive/0001-...md`

## Why

- preserves issue-driven structure before hosted tooling exists
- keeps numbering and handoff discipline
- lets AI agents work against durable local issue files

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
- note plan alignment or deviation in issue bodies when that context matters
