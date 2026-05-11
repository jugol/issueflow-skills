---
name: qa-flutter-proof
description: Produce strong QA evidence for Flutter issues using widget tests, integration tests, and golden tests with reliable font setup. Use before merging a Flutter issue branch into develop.
---

# qa-flutter-proof

This skill proves that a Flutter issue is actually solved.

## Required QA stack

- Widget tests for component and state behavior
- Integration tests for risky end-to-end flows
- Golden tests for stable UI surfaces that changed visually

## Golden policy

- Use golden tests for durable UI states, not every transient animation frame
- Load the app's real font family, or a deterministic test-only equivalent with matching layout characteristics
- Keep surface size, device pixel ratio, locale, and theme deterministic
- Record intentional baseline updates clearly

## Minimum evidence

- Widget or integration proof for the changed behavior
- Slice-level evidence that the real app path reaches the changed behavior
- Golden proof when visuals changed
- Rendered evidence should show the intended user-facing surface, not only diagnostic or proof UI
- Rendered evidence should be judged aesthetically by a human standard: balanced composition, good spacing, readable hierarchy, appropriate imagery, and polished interaction states
- Visible copy should be checked for fluent native-language naturalness in story text, choices, labels, onboarding, errors, and calls to action
- Commands that can be rerun in CI
- Clear note if a golden was intentionally updated
- Local project checks pass before or alongside Flutter proof

## Harness policy

- Bug fix -> persistent regression coverage
- New UI state -> persistent golden or widget coverage
- Vertical slice -> persistent proof for both the state/domain path and the visible app surface
- Experience-first UI -> persistent proof that the primary action, visual hierarchy, aesthetic fit, native-copy quality, and hidden diagnostics remain intact
- Shared design change -> update all impacted durable baselines together
- Update the harness registry when adding durable coverage

Use `../../references/harness-governance.md` for registry and long-lived proof decisions. Use `../../references/experience-first-ui.md` when rendered proof depends on visual hierarchy, aesthetics, or copy naturalness.

## Output

- What behavior was tested
- Which tests prove it
- Which goldens changed and why
- Which commands were run
- Whether merge to `develop` is allowed

## Hand-off

If proof passes and the user asked to complete the issue, continue to `merge-gate` immediately. Do not stop with the checkout still on `issue/*` unless merge is blocked, the repo requires PR-only review, or the user explicitly asked for proof only.
