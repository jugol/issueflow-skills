---
name: implement-flutter
description: Implement a Flutter issue inside approved scope while growing the long-lived widget, integration, and visual harness. Use for Flutter product work that must land with deterministic test evidence before merging into develop.
---

# implement-flutter

Implement the approved Flutter issue and leave behind stronger durable coverage.

If the caller is the main thread in an autonomous cycle, do not implement directly unless `issue-dispatch` recorded a no-safe-delegation rationale. Prefer worker implementation, then review and integrate.

## Core rules

- Work from `issue/<n>-<slug>` branched off `develop`
- Confirm the branch issue id matches the approved issue before editing
- Stay inside approved issue scope
- Stop instead of implementing when the checkout is a stale or unrelated `issue/*` branch
- Preserve the approved vertical slice boundary; do not expand into unrelated layers
- Strengthen widget, integration, or visual coverage with the change
- Run the repo's local check commands before asking for merge proof

## Experience-first UI rules

- Build the intended product experience before exposing proof UI.
- Do not default to dashboards, card grids, status boards, debug rails, or admin shells unless the issue or product domain explicitly asks for them.
- Hide raw diagnostics in semantics, test helpers, collapsed developer surfaces, or test-only state.
- For user-facing screens, make the primary action, object, scene, or workflow visually dominant in the first viewport.
- Use current, polished, domain-specific layout and visual language; do not rely on explanatory copy to make a weak interface understandable.
- Judge the in-app screen aesthetically, not only functionally: composition, spacing, typography, imagery, motion, and interaction states should look intentional and appealing to a human user.
- Review visible copy in the target language. Story text, labels, choices, errors, onboarding, and calls to action should sound fluent, natural, and commonly phrased to a native speaker, not translated or awkward.
- When design direction is vague, make a compact design pass before coding: audience, first-read object, primary action, visual reference, palette, typography, asset plan, and key states.
- Avoid generic card-soup layouts and one-note dashboard palettes unless the domain is operational software.
- Before hand-off, inspect the rendered app surface and ask whether a user would know what to do, whether it looks like the promised product, whether it is aesthetically good enough, and whether the copy sounds native.

## Harness rules

- Bug fix -> add a regression-oriented widget or integration test
- New behavior -> add a new widget or integration path
- Vertical slice -> prove the state/domain path and the visible Flutter surface together
- Shared UI change -> add or update golden coverage
- Experience-first UI -> protect visual hierarchy, first action, native-copy quality, aesthetic fit, and hidden diagnostics with widget, integration, or golden proof
- Navigation or data flow risk -> add integration coverage

Use `../../references/harness-governance.md` when adding durable coverage and `../../references/experience-first-ui.md` when rendered UI or native-copy quality is part of the issue.

## Font and rendering rule

Golden and widget rendering must use the app's real font setup, or a deterministic test-only equivalent that matches production metrics closely enough to avoid false diffs.

Do not rely on default fallback fonts if the app ships with custom fonts.

## Required proof before hand-off

- Widget or integration evidence for changed behavior
- Golden updates for stable UI surfaces when visuals changed
- Test harness registry updated when new long-lived coverage is added
- Local project checks pass on the issue branch

## Hand-off

When implementation is complete, hand off to `qa-flutter-proof`.
