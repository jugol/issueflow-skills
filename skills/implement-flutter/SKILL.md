---
name: implement-flutter
description: Implement an approved Flutter issue on its issue branch with durable widget, integration, or golden coverage. Use after dispatch and before qa-flutter-proof.
---

# implement-flutter

Implement only the approved issue. If called by the main thread in an autonomous cycle, require a recorded no-safe-delegation rationale; otherwise use the assigned worker/worktree.

## Gates

- Work on matching `issue/<n>-<slug>` from `develop`; stop on a stale or unrelated issue branch.
- Preserve scope and the approved vertical slice.
- Strengthen widget, integration, or visual coverage and run canonical local checks.
- Keep diagnostics test-only or behind developer surfaces unless the issue asks for operational UI.

## UI work

Make the intended primary action/object dominant, use a polished domain-specific layout, and inspect the rendered app for aesthetics, interaction states, and fluent target-language copy. When direction is unclear, make a compact design decision before coding. Load `../../references/experience-first-ui.md` for the full quality bar.

## Harness

- Bug -> regression widget/integration test
- Feature -> durable widget/integration path
- Vertical slice -> state/domain path plus visible app outcome
- Shared visual change -> golden coverage
- Navigation/data-flow risk -> integration coverage

Use the app's real fonts, or deterministic equivalents with matching metrics, in widget/golden rendering. Load `../../references/harness-governance.md` for registry and long-lived proof choices.

## Required handoff

- Changed behavior has widget or integration evidence.
- Stable visual changes have intentional golden updates.
- Harness registry is updated when durable coverage is added.
- Canonical checks pass on the correct issue branch.

Then hand off to `qa-flutter-proof`.
