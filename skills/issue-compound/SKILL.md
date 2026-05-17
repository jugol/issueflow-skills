---
name: issue-compound
description: Capture reusable learning after an issue merges, enters a PR/merge queue, or reveals recurring implementation knowledge. Use to update docs/solutions, record failed approaches and prevention rules, and raise follow-up issues when completion reveals future work.
---

# issue-compound

Use this after `merge-gate`, PR handoff, or a significant debugging/review cycle. This is the post-completion lifecycle step; history compaction is only one conditional cleanup action inside it.

## Workflow

1. Inspect the linked issue, proof summary, changed behavior, failed approaches, and follow-up notes.
2. Decide whether the work produced reusable knowledge:
   - recurring bug or prevention rule
   - reusable implementation pattern
   - important failed approach
   - cross-lane contract or worktree coordination lesson
   - future issue trigger
   - plan truth change or plan gap that future cycles should see
3. If it overlaps strongly with an existing `docs/solutions/` note, update that note instead of creating a duplicate.
4. Update `docs/solutions/INDEX.md` or the repo's equivalent solution index before expecting future agents to discover the note.
5. Otherwise create a concise solution note using `../../templates/SOLUTION.template.md`.
6. If the learning implies future product, QA, cleanup, or prevention work, hand off to `issue-raise`.
7. If the learning changes product direction, hand off to plan governance or record the required plan update.
8. If the completed issue changed next-cycle context or left completed issue details in `PLAN_ANCHOR.md`, `CURRENT_STATE.md`, backlog boards, or wave notes, run or require cycle/history compaction as part of this compound handoff.
9. If no solution note, follow-up, plan update, or completion cleanup is needed, state the concrete no-compound rationale.

## Rules

- Do not treat compound notes as release notes. They are future-agent memory.
- Keep notes short, searchable, and tied to symptoms or triggers.
- Prefer updating an existing solution when the root cause, affected surface, and prevention rule are substantially the same.
- Search the solution index before reading or creating full solution notes.
- Never bulk-load every solution note just to decide whether one applies.
- Never call an issue complete while known follow-up work is only mentioned in chat.
- Never leave completed issue details appended to active context files after completion handoff; compact them to history and keep pointers.

## Package resources

- `../../references/compound-learning.md` for solution-note policy
- `../../references/context-governance.md` for index-first reading and compaction rules
- `../../references/history-compaction.md` for moving completed issue, wave, and proof detail out of active files
- `../../references/plan-governance.md` when reusable learning changes product truth or reveals plan gaps
- `../../templates/SOLUTION.template.md` for the standard note shape
- `../../templates/SOLUTION-INDEX.template.md` for index scaffolding
- `../../templates/CYCLE-COMPACTION.template.md` when compounding changes the next-cycle context
- `../../templates/HISTORY-INDEX.template.md` when completed details move to history
- `../../references/autonomous-wave-generation.md` when follow-up work should become a wave

## Output

- Solution note created, updated, or skipped with rationale
- Solution index updated or no-index rationale
- Current-state or cycle compaction update, when the next issue selection changed
- History compaction update, when completed detail moved out of active files
- Plan update or plan-gap handoff, when product truth changed
- Follow-up issue ids or explicit no-follow-up rationale
- Any repo docs or agent instructions that should point to `docs/solutions/`
