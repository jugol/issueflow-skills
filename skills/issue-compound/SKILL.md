---
name: issue-compound
description: Turn completed or reviewed work into reusable future-agent memory, follow-up issues, plan updates, and bounded active context. Use after merge/PR handoff or significant debugging when lessons or cleanup may compound.
---

# issue-compound

Run after `merge-gate`, PR handoff, or a significant debugging/review cycle. Compaction is a conditional cleanup inside compound, not its sole purpose.

## Workflow

1. Inspect the issue, proof, changed behavior, failed approaches, follow-ups, plan effects, and active-context drift.
2. Search the solution index. Update an existing overlapping note; otherwise create a concise note only for reusable patterns, prevention rules, meaningful failures, coordination lessons, or future triggers.
3. Update the solution index before expecting future agents to discover the note.
4. Raise product/QA/cleanup/prevention follow-ups as issues; route product-direction changes to plan governance.
5. Compact completed issue/wave/proof detail out of `PLAN_ANCHOR.md`, `CURRENT_STATE.md`, boards, and wave notes when it no longer guides the next cycle.
6. Remove stale plan gaps, superseded drafts, closed lanes, dead follow-ups, outdated next actions, and old automation notes. Archive only useful history.
7. If no note, follow-up, plan update, or cleanup applies, record a concrete no-compound rationale.

## Rules

- Solution notes are short searchable future-agent memory, not release notes.
- Search index-first; never bulk-load all solution/history files.
- Never leave known follow-up only in chat or completed detail in active context.
- Treat active planning files as bounded working memory, not append-only history.

## Output

Report solution/index action, follow-up issues or rationale, plan action, current-state/history compaction, obsolete-content cleanup, and any discoverability updates.

Load only what applies: `../../references/compound-learning.md`, `../../references/context-governance.md`, `../../references/history-compaction.md`, `../../references/plan-governance.md`, and `../../references/autonomous-wave-generation.md`. Use the matching solution/index/compaction/history template under `../../templates/`.
