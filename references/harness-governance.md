# Harness Governance

The harness is the durable proof surface that grows with the product.

It should prove user-visible behavior, important contracts, and integration boundaries without leaking QA scaffolding into the default product UI.

## What belongs in the harness

- smoke checks that prove the app starts and critical routes load
- regression tests for confirmed bugs
- scenario or spec tests for user-visible flows
- integration tests for risky boundaries
- visual tests for stable UI surfaces
- accessibility checks where they are feasible and deterministic
- schema, fixture, or contract validators for shared data shapes
- package-local proof entrypoints for independently owned apps or services

## Product-first proof

Before expanding meta review, admin, or signoff surfaces, make sure the project has at least one real user-facing slice that a human can use.

The harness should not become the product UI. Prefer:

- stable data attributes
- hidden or collapsed debug affordances
- fixtures and helper models
- screenshots of the real user surface
- focused automated assertions

A test can pass while the product still fails if the default screen reads like a QA dashboard instead of the promised experience.

A test can also pass while the product still fails if the rendered screen is ugly, broken-looking, visually confusing, or linguistically awkward. For UI and copy work, the harness evidence should support a human judgment of the actual in-app surface, including aesthetic quality and native-language naturalness.

## Coverage by change type

- `bug`: add a regression test that fails before the fix and passes after.
- `feature`: add or extend a scenario/spec path that exercises the new behavior.
- `refactor`: prove equivalence with tests, snapshots, or invariant checks.
- `ui`: add or refresh visual, interaction, or accessibility coverage for the changed state.
- `performance`: add repeatable measurement and a documented threshold.
- `contract`: add sample fixtures or schema tests that prove the contract is executable.

## Contract and handoff proof

If an issue introduces a new payload, schema, content grammar, or handoff contract, prove both:

- the reusable contract or schema itself
- at least one real adapter, UI surface, or consumer path

If several packages need the same mapping, move it into a shared registry or shared helper and add at least one consumer proof so glue code does not become an accidental source of truth.

When state moves across a user action or workflow transition, prove the transition at the action boundary. Do not infer that a later screen is correct only because an internal object contains the expected data.

## Browser and UI proof

For browser or app-runtime proof:

- test user-visible behavior, not implementation details
- use resilient locators and stable assertions
- control nondeterministic third-party dependencies
- capture screenshots, video, or traces when visual behavior changed or when failure diagnosis would otherwise be opaque
- assert hidden diagnostics through attributes or helpers rather than visible QA copy
- inspect the first viewport when layout, hierarchy, or first-use clarity matters
- inspect visible copy when wording, localization, narrative, onboarding, choices, labels, or errors changed

For visual changes, screenshots or goldens should show the actual product surface. A cropped debug panel or proof-only route is not enough. If the screenshot or golden looks aesthetically poor, or the visible copy sounds unnatural to a fluent native speaker, the proof should block completion until repaired.

## Focused proof commands

When running focused proof from a large shared suite, target the exact test title or a unique issue-specific phrase. Broad filters can run unrelated long scenarios first, hide the new proof behind legacy failures, and waste the debugging loop.

Prefer stable local proof entrypoints that can also be called by CI:

- package-local checks for independently owned packages
- root wrappers that compose package checks
- CI workflows that call the same local commands instead of inventing separate CI-only logic

## Registry

Each project should keep a test harness registry.

Suggested fields:

- Test id
- Layer
- Feature or area
- File path
- Trigger issue
- Owner
- Flake status
- Notes

Use [TEST-HARNESS-REGISTRY.template.md](../templates/TEST-HARNESS-REGISTRY.template.md) as the starting point.

## Anti-patterns

- fixing a bug without adding regression coverage
- relying only on manual QA for repeated user flows
- treating flaky tests as normal
- deleting tests because they are inconvenient
- letting visual baselines drift without documented intent
- proving only a diagnostic surface when the issue changed user-facing behavior
- accepting an ugly or broken-looking screen because functional assertions are green
- accepting stiff, translated, or uncommon copy because no assertion failed

## Practical rule

If an issue changes user-visible behavior, the harness must tell that story after the issue closes.
