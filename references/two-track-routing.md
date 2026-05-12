# Two-Track Routing

Issueflow has two planning tracks.

## Autonomous Cycle Track

Use this when the user or automation asks to continue, iterate, resume, clean up remaining work, process test failures, process review findings, process playtest feedback, or move from a completed issue to the next useful issue.

Default behavior:

- scan durable signals before asking the user what to do next
- create or update follow-up issues when the next work is visible
- make a wave when two or more independent issues can move separately
- include at least one `core` issue unless the wave is explicitly stabilization-only
- record a concrete no-follow-up rationale when there is no useful next issue

## Interactive Feature Intake Track

Use this when the user describes a feature, product behavior, UI change, or broad improvement request.

Default behavior:

- inspect local context before asking questions
- clarify success criteria, UX, scope, data needs, and proof
- propose two or three approaches with tradeoffs when there are meaningful options
- turn the approved direction into one issue or a wave
- avoid implementation dispatch until the direction is intake-ready

## Tie-breakers

- Clear bug with reproduction: compact `issue-raise`, then intake.
- Multiple defects or feedback points: Autonomous Cycle Track and corrective wave.
- Ambiguous product request: Interactive Feature Intake Track.
- Post-merge or PR handoff: `issue-compound` after merge-gate.
