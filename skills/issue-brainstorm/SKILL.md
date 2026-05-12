---
name: issue-brainstorm
description: Clarify user-requested features, product changes, UI changes, and ambiguous improvements before issue creation. Use for the interactive feature intake track when Codex should explore repo context, ask focused questions, propose 2-3 approaches with tradeoffs, and then hand off to issue-raise or a multi-issue wave.
---

# issue-brainstorm

Use this before implementation when the user describes a feature, product behavior, UI change, or broad improvement.

## Workflow

1. Ground in the repo first: inspect the plan anchor, backlog, current product surface, related tests, and nearby code or docs.
2. Restate the likely goal, audience, success signal, and major constraints.
3. Ask one or two focused questions only when the answer materially changes scope, UX, data shape, proof, or rollout.
4. Present two or three viable approaches with tradeoffs and a recommendation.
5. Decide whether the approved direction is one issue or a wave:
   - one issue when the work has one vertical slice and one ownership lane
   - a wave when independent slices, packages, UI/backend lanes, or corrective findings can move separately
6. Hand off the approved direction to `issue-raise`; if a wave is needed, use `../../templates/PARALLEL-WAVE.template.md`.

## Rules

- Do not dispatch implementation before the direction is clear enough for `issue-intake`.
- Keep questions small and high leverage. Avoid generic questionnaires.
- If the request is already concrete and low-risk, run a compact brainstorm: restate the direction, name the proof, and proceed to `issue-raise`.
- Include UX direction, copy tone, first user-visible action, and anti-goals for UI work.
- Record rejected approaches briefly so later agents do not reopen the same decision without new evidence.

## Package resources

- `../../references/interactive-brainstorming.md` for the brainstorming procedure
- `../../references/two-track-routing.md` for deciding whether this track applies
- `../../references/autonomous-wave-generation.md` for deciding single issue vs wave
- `../../templates/BRAINSTORM.template.md` for durable local notes when the repo keeps planning artifacts

## Output

- Clarified goal and success criteria
- Key answers or assumptions
- Recommended approach and rejected alternatives
- Single-issue or wave decision
- Handoff target: `issue-raise`, `issue-intake`, or `issue-dispatch`
