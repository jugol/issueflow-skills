# Stack Selection

Use this when a greenfield product plan asks whether the first client should be web-first or Flutter-first.

## Choose web-first when

- debugging speed matters more than native packaging
- browser inspection and overlays will be important
- Playwright will give faster QA leverage
- frontend, backend, and admin can all benefit from one TypeScript-first toolchain

## Choose Flutter-first when

- native mobile feel is the immediate product risk
- the core UI is app-native rather than browser-like
- widget, integration, and golden tests are a better fit for the team's delivery shape
- a web admin can remain separate while the primary client needs Flutter now

## Rule of thumb

If the first risk to retire is complex shared logic, browser-visible behavior, debug visibility, or tooling, start web-first.

If the first risk to retire is native app interaction and shipping on-device UX, start Flutter-first.
