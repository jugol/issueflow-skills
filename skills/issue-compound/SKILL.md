---
name: issue-compound
description: Capture reusable learning after an issue merges, enters a PR/merge queue, or reveals recurring implementation knowledge. Use to update docs/solutions, record failed approaches and prevention rules, and raise follow-up issues when completion reveals future work.
---

# issue-compound

Use this after `merge-gate`, PR handoff, or a significant debugging/review cycle.

## Workflow

1. Inspect the linked issue, proof summary, changed behavior, failed approaches, and follow-up notes.
2. Decide whether the work produced reusable knowledge:
   - recurring bug or prevention rule
   - reusable implementation pattern
   - important failed approach
   - cross-lane contract or worktree coordination lesson
   - future issue trigger
3. If it overlaps strongly with an existing `docs/solutions/` note, update that note instead of creating a duplicate.
4. Otherwise create a concise solution note using `../../templates/SOLUTION.template.md`.
5. If the learning implies future product, QA, cleanup, or prevention work, hand off to `issue-raise`.
6. If no solution note or follow-up is needed, state the concrete no-compound rationale.

## Rules

- Do not treat compound notes as release notes. They are future-agent memory.
- Keep notes short, searchable, and tied to symptoms or triggers.
- Prefer updating an existing solution when the root cause, affected surface, and prevention rule are substantially the same.
- Never call an issue complete while known follow-up work is only mentioned in chat.

## Package resources

- `../../references/compound-learning.md` for solution-note policy
- `../../templates/SOLUTION.template.md` for the standard note shape
- `../../references/autonomous-wave-generation.md` when follow-up work should become a wave

## Output

- Solution note created, updated, or skipped with rationale
- Follow-up issue ids or explicit no-follow-up rationale
- Any repo docs or agent instructions that should point to `docs/solutions/`
