---
name: qa-web-proof
description: Produce strong QA evidence for web issues using Playwright and related durable harness checks. Use before merging a web issue branch into develop.
---

# qa-web-proof

This skill proves that a web issue is actually solved.

## Required QA stack

- Playwright for browser-visible behavior
- Existing unit or integration tests where appropriate
- Stable local commands for fast and full checks

## Playwright policy

- Test user-visible behavior, not implementation details
- Prefer resilient locators and web-first assertions
- Capture trace on failure, and keep screenshot or video when useful
- Mock or control third-party dependencies when nondeterminism would hide the real result

## Minimum evidence

- Named Playwright coverage tied to the issue
- Slice-level evidence that the real user path reaches the changed behavior
- Command list that can be rerun
- Clear pass or fail result
- If behavior changed visually, include screenshots or snapshot evidence
- Local project checks pass before or alongside Playwright proof

## Visual issue bar

For UI, art-direction, or interaction-polish issues, Playwright assertions are necessary but not enough.

- Capture or inspect the actual browser surface after the change.
- Confirm the primary user-visible object is recognizable without reading debug text.
- For non-icon scene or product assets, fail proof if the main image is SVG/procedural/CSS/canvas drawing or a vector-looking manual composite exported to JPG/PNG instead of real generated or captured raster imagery.
- Confirm the screen is aesthetically intentional to a human viewer: balanced composition, good spacing, readable hierarchy, appropriate imagery, and polished interaction states.
- Confirm visible copy sounds fluent and natural to a native speaker in the target language, especially story text, choices, labels, onboarding, errors, and calls to action.
- Fail the proof if the default screen reads as a QA dashboard, debug console, or admin board when the issue promised a user-facing product experience.
- Fail the proof if screenshots look ugly, broken, generic, visually confusing, or if visible copy sounds stiff, translated, or uncommon, even when functional assertions pass.
- Confirm responsive layout does not crop or cover the main interaction surface.
- For declutter passes, assert that debug diagnostics remain available through stable attributes or an inspector while the default user-facing copy does not expose raw payload delimiters, IDs, or QA labels.
- Prefer durable DOM assertions for visual contracts that matter repeatedly, such as critical overlays, product-specific affordances, visible state transitions, or important interaction targets.

## Harness policy

- If this issue fixed a bug, a regression spec must exist afterward
- If this issue added a workflow, the workflow must exist in long-lived spec coverage afterward
- If this issue delivered a vertical slice, proof must cover both the important contract or state transition and the browser-visible outcome
- If this issue changed user-facing UI, proof must show the real experience surface, not only a diagnostic or proof page
- If this issue changed user-facing copy, proof or review notes must include a native-language naturalness check
- Update the harness registry when adding durable coverage

Use `../../references/harness-governance.md` for registry and long-lived proof decisions. Use `../../references/experience-first-ui.md` when the QA decision depends on visual hierarchy, aesthetics, or copy naturalness.

## Output

- What behavior was tested
- Which specs prove it
- Which commands were run
- What evidence is attached
- Whether merge to `develop` is allowed

## Hand-off

If proof passes and the user asked to complete the issue, continue to `merge-gate` immediately. Do not stop with the checkout still on `issue/*` unless merge is blocked, the repo requires PR-only review, or the user explicitly asked for proof only.
