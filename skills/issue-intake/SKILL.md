---
name: issue-intake
description: Validate whether an issue is ready for implementation in an issue-driven Git Flow-lite workflow. Use when deciding if work can start, if labels are sufficient, or if acceptance criteria and test plans are strong enough.
---

# issue-intake

This skill decides whether an issue is ready to branch from `develop`.

## Ready-to-start checklist

- The problem is concrete.
- Evidence exists or the missing evidence is explicitly acknowledged.
- Acceptance criteria are testable.
- A test plan exists.
- Spec or harness targets are named when the issue changes user-visible behavior.
- Scope and out-of-scope are explicit.
- The likely affected area is named.
- The vertical slice shape is clear, or a support-only reason and downstream core slice are named.
- UI issues include audience, primary action, first-viewport priority, and desired visual direction.
- UI issues include the expected aesthetic bar and copy tone or target-language naturalness criteria.
- The issue can be linked to a durable harness update.
- If a project plan exists, the issue can point to the plan promise or constraint it advances, or it is explicitly marked as a deviation.

For greenfield projects, allow the baseline proof to be scaffold-level validation first, then tighten the definition of green as the app grows.

## Red flags

- "Clean this up" with no target
- "Fix the UI" with no expected result
- No reproduction steps for a bug
- No proof idea for a user-visible change
- Scope that spans unrelated systems without being split
- Layer-only work with no named consumer slice
- UI acceptance criteria that only describe proof panels, diagnostics, or admin shells when the product promise is user-facing
- UI acceptance criteria that prove function but never require the screen to look good to a human viewer
- User-facing copy changes with no natural-language review target, especially for localized, narrative, onboarding, or choice-heavy surfaces
- No clear link back to the active product plan
- Internal tooling work that does not justify why it should come before missing core product work

## Package resources

Use `../../references/plan-alignment.md`, `../../references/vertical-slice-architecture.md`, and `../../references/experience-first-ui.md` when readiness depends on product direction, slice shape, or UI quality.

## Decision states

- `ready`: can dispatch now
- `needs-clarification`: ask for missing issue details
- `needs-split`: break into smaller issues
- `blocked`: external dependency or red baseline blocks implementation

## Output

- Decision state
- Missing fields, if any
- Suggested split, if any
- Suggested labels and branch slug
- Required harness update category
- Plan alignment note or realignment warning
- Vertical slice readiness or support-only justification
- Experience-first readiness for UI work

## Hand-off

- `ready` -> `issue-dispatch`
- `needs-clarification` -> `issue-raise`
