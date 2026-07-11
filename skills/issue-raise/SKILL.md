---
name: issue-raise
description: Turn a concrete problem, improvement, plan gap, or approved feature direction into a focused implementation-ready GitHub or local issue through minimal clarification and fan-out checks.
---

# issue-raise

Turn rough work into durable issues without losing user intent.

## Workflow

1. Extract origin, problem/evidence, impact, desired outcome, constraints, and missing facts.
2. Clarify implementation-blocking ambiguity: actors, states, product terms, UX/data ownership, proof, rollout, or plan truth. Ask one or two focused questions at a time; infer only low-risk details.
3. Classify against the active plan: `aligned`, `extension`, `conflict`, or `deviation`. Resolve extensions/conflicts before dispatch.
4. Shape a medium vertical slice with target goal experience, user-visible outcome, required contract/domain path, and proof. Support-only work must name its downstream core slice.
5. Run fan-out: split independent outcomes, owners, proof commands, dependencies, or rollout risks; combine tiny findings that share one outcome and proof story.
6. Draft from `../../templates/ISSUE.template.md`, then create the GitHub issue after confirmation or use the local backlog.

Preserve an approved brainstorm approach and rejected alternatives. For autonomous work, record the triggering signal. If code already changed, backfill honestly with changed scope and existing proof.

## Required issue fields

- Title, origin, problem/evidence, acceptance criteria, test plan
- Scope/out-of-scope, docs, assumptions, and handoff
- Plan relationship and update decision
- Target goal experience, slice/support rationale, owner and QA skill
- For UI: audience, primary action, first-viewport priority, visual direction, aesthetic bar, copy language/tone, and hidden-diagnostics expectation

## Rules

- Route broad unapproved product direction to `issue-brainstorm`.
- Acceptance criteria describe an end-to-end user path, not only a technical layer.
- Weak evidence remains a validation task, not a claimed fact.
- Use `../../references/issue-sizing-and-scheduling.md`, `../../references/autonomous-wave-generation.md`, and `../../templates/PARALLEL-WAVE.template.md` when two or more issues move together.
- Use plan/product references only when needed: `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`, `../../references/vertical-slice-architecture.md`, `../../references/experience-first-ui.md`.

## Handoff

- Ready draft -> `issue-intake`
- Missing decisions -> return the draft and exact questions
