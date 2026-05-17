# History Compaction

Use this when `PLAN_ANCHOR.md`, `CURRENT_STATE.md`, backlog boards, or wave notes are growing because completed issues keep being appended.

## Core rule

Active context files are bounded pointers, not full history logs.

`PLAN_ANCHOR.md` and `CURRENT_STATE.md` should contain only:

- current macro direction
- target user goal experience
- current plan gaps
- active issue or wave
- recent proof pointer
- active branch or worktree
- next recommended action
- short summaries of recently completed work
- links or paths to archived detail

Do not append every completed issue into these files.

## Suggested archive structure

Use the repo's existing convention when one exists. Otherwise prefer:

```text
docs/history/
  INDEX.md
  issues/
    2026-05.md
  waves/
    2026-05.md
  proof/
    2026-05.md
```

Local backlog repos may use `backlog/history/` instead, but keep one index file that future agents can search first.

## Active file budget

Keep active context small enough to read at the start of every cycle.

Suggested limits:

- `PLAN_ANCHOR.md`: stable product direction plus current gaps; no completed issue log
- `CURRENT_STATE.md`: current wave, current issue, latest proof, next step, paused automation state, and last few completions
- backlog board: active and ready items only, plus links to done/history
- wave note: open lanes and merge order only; archive completed lane details after the wave closes

When an active file grows past roughly `150-250` lines or starts listing many completed issues, run compaction.

## Compaction triggers

Compact when:

- a wave closes
- every `5-10` completed issues
- automation resumes and active context feels noisy
- `PLAN_ANCHOR.md` or `CURRENT_STATE.md` contains many completed issue details
- an agent needs to read old issue history just to find the current task
- merge-gate or release-gate notices stale completed work in active pointers

## Compaction process

1. Identify active facts that must remain visible.
2. Move completed issue, wave, proof, and old decision details to `docs/history/` or the repo's equivalent archive.
3. Preserve a short summary for each completed item:
   - issue id or wave id
   - one-line outcome
   - proof pointer
   - merge or PR status
   - follow-up decision
4. Update `docs/history/INDEX.md`.
5. Update `PLAN_ANCHOR.md` and `CURRENT_STATE.md` with only current direction, current gaps, active work, recent summaries, and archive pointers.
6. Record the compaction in `CYCLE-COMPACTION`.

## Reading policy

Agents should search the history index before opening historical detail.

Read archived details only when:

- the current issue references that history
- the same symptom reappears
- merge or release proof needs a specific past result
- a plan or solution note points to that archived decision

Do not bulk-load old issue archives during normal autonomous cycles.
