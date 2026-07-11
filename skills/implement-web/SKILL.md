---
name: implement-web
description: Implement an approved web issue on its issue branch with durable browser proof. Use for scoped browser product work after dispatch and before qa-web-proof.
---

# implement-web

Implement only the approved issue. If called by the main thread in an autonomous cycle, require a recorded no-safe-delegation rationale; otherwise use the assigned worker/worktree.

## Gates

- Work on matching `issue/<n>-<slug>` from `develop`; stop on a stale or unrelated issue branch.
- Preserve scope and the approved vertical slice.
- Add durable coverage for every user-visible behavior change and run canonical local checks.
- Do not expose diagnostics or proof UI as the product experience unless the issue explicitly requires operational tooling.

## UI work

Make the intended primary action/object dominant, use a polished domain-specific layout, keep diagnostics hidden/test-only, and review the rendered browser surface for responsive behavior, aesthetics, interaction states, and fluent target-language copy. For non-icon scene/product imagery, use real generated or captured raster assets rather than procedural/vector-looking substitutes.

When direction is unclear, make a compact design decision before coding. Load `../../references/experience-first-ui.md` for the full quality bar.

## Harness

- Bug -> regression test
- Feature/workflow -> durable scenario/spec
- Vertical slice -> contract/state path plus browser-visible outcome
- Risky integration -> integration coverage
- Shared UI/experience change -> durable visual or interaction contract

Load `../../references/harness-governance.md` when choosing or registering long-lived coverage.

## Required handoff

- Changed behavior and affected specs are automated.
- Harness registry is updated when durable coverage is added.
- Canonical checks pass on the correct issue branch.
- Proof is not manual-only or screenshot-only.

Then hand off to `qa-web-proof`.
