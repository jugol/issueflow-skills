# Compound Learning

Compound learning makes each finished issue improve the next one.

## When to write a solution note

Write or update a `docs/solutions/` note when an issue reveals:

- a recurring bug pattern
- a reusable implementation or testing pattern
- an important failed approach
- a prevention rule for future agents
- a shared contract used by multiple lanes
- a future issue trigger

Skip the note when the work was straightforward and left no reusable lesson. State the no-compound rationale in the handoff.

## Update before creating

Before creating a new note, search existing `docs/solutions/` notes. Update an existing note when the symptom, root cause, and prevention rule substantially overlap.

## Note shape

Keep notes short and searchable:

- title names the symptom or pattern
- context says where it appears
- root cause explains why it happened
- solution summarizes the durable fix
- failed approaches prevent repeat detours
- prevention says what future agents should check
- follow-up triggers name issue-worthy future work

## Follow-up rule

If the solution note names concrete future work, create or update a follow-up issue. Do not leave issue-worthy work only in the solution note.
