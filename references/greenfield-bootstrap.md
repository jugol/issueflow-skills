# Greenfield Bootstrap

Greenfield projects need a slightly different bootstrap than mature repos.

## First deliverables

- plan anchor summary
- experience direction summary for user-facing products
- stack decision
- repo-topology decision
- local backlog board
- first numbered issue wave
- local proof entrypoint

## Green baseline

At the start, green means:

- the scaffold is valid
- the issue files are valid
- the local proof command runs successfully

Do not block greenfield work on nonexistent product tests. Tighten the bar as real code and real tests appear.

## First issue wave

A good initial wave usually contains:

- bootstrap and stack selection
- first vertical slice, shaped as a thin end-to-end user-visible path
- first domain schema
- first content grammar or fixture issue

This gives the project one completed issue, one implementation issue, and one or two system-definition issues.

If the plan contains a strong user-facing, visual, or interaction promise, the first vertical slice must visibly aim at that promise instead of spending the full first wave on admin or QA-only layers.

Use [vertical-slice-architecture.md](./vertical-slice-architecture.md) to keep the first implementation issue from becoming a horizontal scaffold with no user-facing proof.

Use [experience-first-ui.md](./experience-first-ui.md) to keep the first product screen from becoming a dashboard, proof board, or setup console when the plan asks for a consumer app, creative tool, or polished product experience.
