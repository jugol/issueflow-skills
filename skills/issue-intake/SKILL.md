---
name: issue-intake
description: Decide whether an issue is implementation-ready. Use to check scope, acceptance criteria, proof, plan alignment, issue size, vertical-slice shape, UI direction, wave ownership, and dispatch readiness.
---

# issue-intake

Decide whether work may branch from `develop`.

## Readiness

- Problem/evidence, acceptance criteria, proof plan, scope/out-of-scope, area, and assumptions are concrete.
- Origin and plan relationship are named; extension/conflict decisions are complete.
- Product work names target goal experience and a medium vertical slice; support work names a downstream core slice.
- Wave lanes name owner, dependency, proof, and worktree/serialization decision.
- UI work names audience, primary action, visual direction, aesthetic bar, copy language/tone, and durable proof.

Reject or reshape vague targets, missing reproduction/proof, unrelated scope, layer-only work without a consumer, feature lists without a before/product-moment/after experience, UI proven only by diagnostics, hidden plan drift, unjustified internal priority, atomized work, oversized independent outcomes, one-issue waves, or broad features that skipped brainstorming.

## Decision

- `ready` -> `issue-dispatch`
- `needs-clarification` -> `issue-raise`
- `needs-split`, `needs-combine`, or `needs-wave` -> return the proposed shape
- `blocked` -> name the external dependency or red baseline

Report missing fields, labels/branch slug, harness category, origin/wave, plan readiness, slice/experience/UI readiness, and handoff.

Load only the reference needed for the disputed decision: `../../references/issue-sizing-and-scheduling.md`, `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`, `../../references/vertical-slice-architecture.md`, `../../references/experience-first-ui.md`, or `../../references/autonomous-wave-generation.md`.
