# Autonomous Wave Generation

Use this when issueflow is continuing an automated cycle, processing feedback, or deciding what to do after a merge.

## Signals to scan

- plan anchor drift or missing core promise
- unimplemented plan gaps from the compact plan anchor or relevant area plan
- active backlog and stale issues
- failing tests or flaky proof
- review comments and QA findings
- playtest or user feedback batches
- recent merge-gate handoff notes
- `docs/solutions/` prevention rules and future issue triggers

## Candidate rules

Create candidate issues when the signal names a concrete behavior, defect, prevention rule, product gap, or proof gap.

If a plan gap is promised in `PLAN.md` or an area plan but absent from the live product or harness, treat it as a first-class autonomous candidate.

Do not create an issue for vague discomfort unless it can be turned into:

- a user-visible outcome
- a support/contract slice with a downstream consumer
- a durable proof improvement
- a named investigation with a success criterion

## Fan-out rule

Make multiple issues when findings differ by:

- user-visible behavior
- ownership lane or package
- proof command
- dependency order
- risk or rollout path

Make one issue when the work is one inseparable vertical slice.

## Wave rule

Use a wave when two or more issues can be planned together. A wave should record:

- goal
- issue list and origin
- ownership lanes
- worktree plan
- dependencies and restack triggers
- proof commands
- merge order
- follow-up scan expectations

Default to at least one `core` issue. Allow internal-only waves only with an explicit stabilization reason.
