# Context Governance

Issueflow projects accumulate issues, waves, brainstorms, proof, and solution notes. That is useful memory, but it must not become the default context for every run.

## Core rule

Read current pointers first. Search archives before reading them. Never bulk-load all completed issues, old waves, or all solution notes.

## Default context set

For normal work, load only:

- backlog board or current-state pointer
- active issue or current wave
- plan anchor summary, not the full long plan unless needed
- current plan gaps when they are named in the anchor or current-state pointer
- relevant test harness registry rows
- solution index matches for the current symptom, not every solution note
- recent proof pointer for the active issue
- paused automation blocker and resume condition, when a run is waiting for the user

## Autonomous cycle entry

At the start of every autonomous cycle, load in this order:

1. current-state pointer or backlog board current context
2. plan anchor summary and current plan gaps for macro direction
3. active issue or current wave for micro direction
4. recent proof pointer for the active lane
5. solution index matches only
6. archived issue, old wave, proof log, or full solution note only if the current pointer or index requires it

If the current-state pointer is missing, stale, contradictory, or too broad, do a cycle compaction before choosing the next issue.

## Archive policy

Completed issues, old brainstorm notes, old waves, and previous proof details should move out of the active set. Keep summaries and links in the board or current-state note.

Use search to retrieve archived details only when:

- the current issue references them
- the same symptom appears again
- a solution index entry points to them
- merge or release proof needs a specific past result

## Solution index

When `docs/solutions/` exists, keep a short `docs/solutions/INDEX.md` or equivalent index.

Each row should include:

- title
- symptom keywords
- affected area
- prevention rule
- follow-up trigger, if any

Agents should search the index before reading solution notes. Read a full note only when its keywords or affected area match the active issue.

## Brainstorm lifecycle

Brainstorm notes are temporary decision records. After an issue or wave is created:

- copy the approved direction and rejected approaches into the issue or wave
- move the brainstorm note to archive, or mark it superseded
- do not keep old brainstorms in the active working set

## Cycle compaction

Every few autonomous cycles, at automation resume, after merge handoff, or whenever the active set feels noisy:

- move done issues out of active
- close or defer stale draft issues
- update the backlog board current-state summary
- update the compact plan anchor if plan gaps or product direction changed
- update wave status and next-lane pointer
- update `docs/solutions/INDEX.md`
- record which active issue or wave should be picked next
- preserve paused automation identity and resume conditions when the next cycle is waiting for user input

If no next issue should start, record a concrete no-next-work rationale.

Use `CYCLE-COMPACTION.template.md` when the project keeps durable compaction notes.
