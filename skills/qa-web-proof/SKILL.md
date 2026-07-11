---
name: qa-web-proof
description: Prove a web issue with Playwright and durable repo checks before merge-gate. Use after web implementation to verify the real user path, regressions, visuals, and rerunnable evidence.
---

# qa-web-proof

Prove the approved behavior on the issue branch.

## Required evidence

- Playwright coverage tied to acceptance criteria and the real user path
- Existing unit/integration checks where relevant
- Rerunnable commands and explicit pass/fail result
- Failure traces and useful screenshots/video; controlled third-party nondeterminism
- Regression coverage for bugs and durable workflow coverage for features
- Contract/state plus browser-visible proof for vertical slices
- Harness registry update when durable coverage is added

Use resilient locators and web-first assertions; test behavior rather than implementation details.

## Visual gate

For UI, copy, or interaction changes, inspect the actual responsive browser surface. Reject proof when the promised product reads as debug/admin UI, the primary experience is obscured, imagery violates the approved asset direction, layout is broken/generic, or target-language copy is awkward. Automated assertions alone do not satisfy this gate.

Load `../../references/experience-first-ui.md` for visual/copy criteria and `../../references/harness-governance.md` for durable proof decisions.

## Output and handoff

Report behavior, specs, commands, attached evidence, and merge recommendation. When proof passes and completion was requested, continue directly to `merge-gate`; stop on `issue/*` only when merge is blocked, PR-only policy applies, or proof-only was requested.
