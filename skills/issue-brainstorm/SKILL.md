---
name: issue-brainstorm
description: Clarify ambiguous feature, product, and UI requests before issue creation. Use to inspect repo/plan context, ask focused questions, compare 2-3 approaches, approve a direction, and hand it to issue-raise or a wave.
---

# issue-brainstorm

Clarify product direction before implementation.

## Workflow

1. Inspect the plan anchor, current product surface, backlog, related tests, and nearby code/docs.
2. Restate audience, goal, success signal, constraints, and plan relationship: `aligned`, `extension`, `conflict`, or `deviation`.
3. Identify ambiguity in actor, screen/state, UX, data ownership, proof, rollout, or plan truth.
4. Ask one or two high-leverage questions at a time, tied to the decision each answer unlocks.
5. Present 2-3 viable approaches with tradeoffs and a recommendation.
6. Obtain direction; resolve or record plan extensions/conflicts before dispatch.
7. Choose one medium vertical-slice issue or a wave of independent outcomes/owners/proof paths, then hand off to `issue-raise`.

For a concrete low-risk request, use a compact brainstorm: confirm direction and proof, then proceed. Do not use a generic questionnaire, implement before direction is clear, or silently reopen rejected approaches without new evidence.

UI direction should cover first user-visible action, primary object, aesthetic bar, copy tone/language, and anti-goals.

## Output

Record clarified goal/success, answers or assumptions, plan decision, recommended and rejected approaches, issue/wave decision, and `issue-raise` handoff.

Load `../../references/interactive-brainstorming.md` for the detailed method, `../../references/plan-governance.md` for product-truth changes, and `../../references/autonomous-wave-generation.md` plus `../../templates/PARALLEL-WAVE.template.md` for wave shaping. Use `../../templates/BRAINSTORM.template.md` or `../../templates/PLAN-CHANGE.template.md` only when a durable note is needed.
