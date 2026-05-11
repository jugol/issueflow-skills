---
name: implement-web
description: Implement a web issue inside approved scope while strengthening the durable test harness. Use for browser-based product work that must land with Playwright-backed evidence before merging into develop.
---

# implement-web

Implement the approved issue only. This skill is not allowed to quietly widen scope.

## Core rules

- Work from `issue/<n>-<slug>` branched off `develop`
- Confirm the branch issue id matches the approved issue before editing
- Change only what the issue approved
- Stop instead of implementing when the checkout is a stale or unrelated `issue/*` branch
- Preserve the approved vertical slice boundary; do not expand into unrelated layers
- Add or update durable test coverage for every user-visible behavior change
- Keep the test harness growing with the project
- Run the repo's local check commands before asking for merge proof

## Experience-first UI rules

- Build the intended product experience before exposing proof UI.
- Do not default to dashboards, card grids, status boards, debug rails, or admin shells unless the issue or product domain explicitly asks for them.
- Hide raw diagnostics in data attributes, test helpers, collapsed details, or dev-only inspectors.
- For user-facing screens, make the primary action, object, scene, or workflow visually dominant in the first viewport.
- Use current, polished, domain-specific layout and visual language; do not rely on explanatory copy to make a weak interface understandable.
- For non-icon scene or product assets, use generated or captured JPG/PNG raster imagery. Do not use SVG, CSS/canvas drawing, or hand-built vector-looking composites as the main scene asset, even if exported to an image file.
- Judge the in-app screen aesthetically, not only functionally: composition, spacing, typography, imagery, motion, and interaction states should look intentional and appealing to a human user.
- Review visible copy in the target language. Story text, labels, choices, errors, onboarding, and calls to action should sound fluent, natural, and commonly phrased to a native speaker, not translated or awkward.
- When design direction is vague, make a compact design pass before coding: audience, first-read object, primary action, visual reference, palette, typography, asset plan, and key states.
- Avoid generic card-soup layouts and one-note dashboard palettes unless the domain is operational software.
- Before hand-off, inspect the actual browser surface and ask whether a user would know what to do, whether it looks like the promised product, whether it is aesthetically good enough, and whether the copy sounds native.

## Harness rules

- Bug fix -> add a regression test
- Feature -> add or extend a scenario/spec test
- Vertical slice -> prove the domain/runtime path and the browser-visible result that make the slice real
- Risky integration -> add integration coverage
- Shared UI component -> add or update visual or interaction coverage
- Experience-first UI -> protect visual hierarchy, first action, native-copy quality, aesthetic fit, and hidden diagnostics with browser proof instead of visible QA panels

Use `../../references/harness-governance.md` when adding durable coverage and `../../references/experience-first-ui.md` when the visible screen or copy quality is part of the issue.

## Required proof before hand-off

- Changed behavior demonstrated by automated coverage
- Affected specs updated, not just implementation code
- Test harness registry updated when new long-lived coverage is added
- Local project checks pass on the issue branch

## Do not finish with

- Manual-only proof
- Screenshot-only proof
- Missing regression test for a reproduced bug
- Green local checks on the wrong branch
- Work for a different issue committed on the current issue branch

## Hand-off

When implementation is complete, hand off to `qa-web-proof`.
