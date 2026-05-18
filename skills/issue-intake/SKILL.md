---
name: issue-intake
description: Validate whether an issue is ready for implementation in an issue-driven Git Flow-lite workflow. Use when deciding if work can start, if labels are sufficient, or if acceptance criteria and test plans are strong enough.
---

# issue-intake

This skill decides whether an issue is ready to branch from `develop`.

## Ready-to-start checklist

- Problem, evidence or evidence gap, acceptance criteria, test plan, affected area, scope, and out-of-scope are concrete.
- Ambiguity is resolved or explicitly marked as an assumption.
- Origin is named: `brainstorm`, `autonomous-scan`, `review-finding`, `compound-learning`, or `user-request`.
- Plan relationship is named when a plan exists: `aligned`, `extension`, `conflict`, or `deviation`; required plan updates/decisions are done or blocking.
- Product issues name target user goal experience and vertical slice shape; support-only work names downstream core slice.
- Issue is not atomized unless high-risk, blocking, or independently revertible.
- Wave issues name ownership lane, dependency order, proof command, and worktree or serialization decision.
- UI issues name audience, primary action, first-viewport priority, visual direction, aesthetic bar, and copy tone/target-language naturalness.
- Durable harness target exists for user-visible behavior changes.

For greenfield projects, allow the baseline proof to be scaffold-level validation first, then tighten the definition of green as the app grows.

## Red flags

- Vague target: "clean this up", "fix the UI", "this/that/the flow", or undefined product terms.
- Hidden assumption changes behavior, data ownership, proof, rollout, UX, or plan truth.
- Bug lacks reproduction; user-visible change lacks proof idea.
- Scope spans unrelated systems, or layer-only work has no consumer slice.
- Product work lists features but not before state, primary product moment, or after state.
- UI criteria only prove diagnostics/admin/proof panels, or omit aesthetic/native-copy review.
- Plan link, plan-change decision, or extension/conflict handling is missing.
- Internal work outranks missing core product work without justification.
- Oversized issue should be a corrective wave; atomized issue should be combined.
- Autonomous cycle creates one issue while independent wave lanes are ready.
- Broad feature skipped `issue-brainstorm` despite unclear success criteria, UX, data behavior, or proof.

## Package resources

Use `../../references/two-track-routing.md`, `../../references/autonomous-wave-generation.md`, `../../references/issue-sizing-and-scheduling.md`, `../../references/plan-alignment.md`, `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`, `../../references/vertical-slice-architecture.md`, and `../../references/experience-first-ui.md` only when readiness depends on track, wave shape, issue size, scheduler role, plan truth, target experience, slice shape, or UI quality.

## Decision states

- `ready`: can dispatch now
- `needs-clarification`: ask for missing issue details
- `needs-split`: break into smaller issues
- `needs-combine`: combine with nearby tiny candidates before dispatch
- `needs-wave`: group independent ready issues into a scheduled wave
- `blocked`: external dependency or red baseline blocks implementation

## Output

- Decision state
- Missing fields, if any
- Suggested split, combine, or wave grouping
- Suggested labels and branch slug
- Required harness update category
- Origin and wave membership, if any
- Plan alignment, relationship, and plan-change readiness
- Vertical slice/support readiness, target goal experience readiness, and UI experience-first readiness

## Hand-off

- `ready` -> `issue-dispatch`
- `needs-clarification` -> `issue-raise`
