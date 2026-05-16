# Two-Track Routing

Issueflow has two planning tracks.

## Autonomous Cycle Track

Use this when the user or automation asks to continue, iterate, resume, clean up remaining work, process test failures, process review findings, process playtest feedback, or move from a completed issue to the next useful issue.

Default behavior:

- scan durable signals before asking the user what to do next
- scan plan gaps when a plan anchor or `docs/plan/` exists
- create or update follow-up issues when the next work is visible
- make a wave when two or more independent issues can move separately
- include at least one `core` issue unless the wave is explicitly stabilization-only
- record a concrete no-follow-up rationale when there is no useful next issue
- pause, not delete, the existing automation when user input or approval blocks the next step

## Interactive Feature Intake Track

Use this when the user describes a feature, product behavior, UI change, or broad improvement request.

Default behavior:

- inspect local context before asking questions
- compare the request with the active plan as `aligned`, `extension`, `conflict`, or `deviation`
- clarify success criteria, UX, scope, data needs, and proof
- propose two or three approaches with tradeoffs when there are meaningful options
- turn the approved direction into one issue or a wave
- avoid implementation dispatch until the direction is intake-ready and any required plan update or decision note exists

## Tie-breakers

- Clear bug with reproduction: compact `issue-raise`, then intake.
- Multiple defects or feedback points: Autonomous Cycle Track and corrective wave.
- Ambiguous product request: Interactive Feature Intake Track.
- Post-merge or PR handoff: `issue-compound` after merge-gate.
