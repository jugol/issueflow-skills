---
name: qa-flutter-proof
description: Prove a Flutter issue with widget, integration, and golden evidence before merge-gate. Use after Flutter implementation to verify behavior, visuals, regressions, and rerunnable checks.
---

# qa-flutter-proof

Prove the approved behavior on the issue branch.

## Required evidence

- Widget or integration coverage tied to acceptance criteria and the real app path
- Golden evidence for stable visual changes, with intentional baseline updates noted
- Deterministic surface, pixel ratio, locale, theme, and production-equivalent fonts
- Regression coverage for bugs and durable state/domain plus visible proof for vertical slices
- Rerunnable canonical commands and explicit pass/fail result
- Harness registry update when durable coverage is added

## Visual gate

Inspect the rendered app for primary-action clarity, composition, spacing, hierarchy, imagery, interaction states, and fluent target-language copy. Reject diagnostic/proof UI standing in for the promised product or a visibly broken/generic result. Automated assertions alone do not satisfy this gate.

Load `../../references/experience-first-ui.md` for visual/copy criteria and `../../references/harness-governance.md` for durable proof decisions.

## Output and handoff

Report behavior, tests, changed goldens and rationale, commands, evidence, and merge recommendation. When proof passes and completion was requested, continue directly to `merge-gate`; stop on `issue/*` only when merge is blocked, PR-only policy applies, or proof-only was requested.
