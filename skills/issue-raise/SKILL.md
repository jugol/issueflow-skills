---
name: issue-raise
description: Use when the user describes a problem, improvement, feature, plan gap, or idea in natural language and wants help turning it into a clean implementation-ready GitHub or local issue through focused clarification.
---

# issue-raise

Turn rough problem statements into durable issues. This skill is conversational on purpose: it should refine the user's intent, not dump a rigid template too early.

## Workflow

1. Extract problem, impact, desired outcome, missing information, and evidence from the user's wording.
2. Run fan-out and precision checks before drafting: vague referents, undefined product terms, missing actors/states, contradictions, hidden multi-issue scope, and unclear proof.
3. Ask the fewest focused questions needed to remove implementation-blocking ambiguity; ask more than one when answers can materially change scope, UX, data, proof, or plan truth.
4. Map to the active plan when present and classify: `aligned`, `extension`, `conflict`, or `deviation`. For `extension`/`conflict`, require plan update, decision entry, or plan-change note before dispatch.
5. Shape product work as a medium vertical slice: target goal experience, user-visible result, domain/contract path, and proof path. For support/contract-first work, name the downstream core slice.
6. For UI work, capture audience, primary action, first-viewport priority, desired feel, aesthetic bar, copy tone/target language, and anti-dashboard or no-debug-copy constraints.
7. Draft with the shared template, suggest labels, branch slug, owner skill, and QA skill.
8. Create the GitHub issue after confirmation when available; otherwise write the same structure into the repo's local backlog.

If the user report clearly contains multiple distinct failures, split them into separate issues that can be verified independently. If the report contains several tiny findings that share the same outcome, owner, and proof command, combine them into one medium issue instead of creating atomized issue overhead.

If the work came from `issue-brainstorm`, preserve the approved approach and rejected alternatives. If it came from an autonomous scan, record the origin signal such as failing test, review finding, playtest feedback, or compound-learning trigger.

If a direct coding session already changed files before this step was applied, backfill the issue draft honestly. Mark what was already done, list the proof that now exists, and add a handoff note that future similar work must be raised before implementation.

## Fan-out check

Create multiple issues instead of one when findings differ by user-visible behavior, ownership lane, proof command, dependency order, or rollout risk. Keep one issue when multiple edits belong to the same user outcome and proof story. Use `../../references/autonomous-wave-generation.md`, `../../references/issue-sizing-and-scheduling.md`, and `../../templates/PARALLEL-WAVE.template.md` when two or more issues should move together.

## Package resources

- Templates: `../../templates/ISSUE.template.md`, `../../templates/BRAINSTORM.template.md`, `../../templates/PLAN-CHANGE.template.md`
- Plan and experience: `../../references/plan-alignment.md`, `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`
- Track and wave shape: `../../references/two-track-routing.md`, `../../references/autonomous-wave-generation.md`, `../../references/issue-sizing-and-scheduling.md`
- Product shape and UI quality: `../../references/vertical-slice-architecture.md`, `../../references/experience-first-ui.md`

## Required output

- Title, origin, problem/evidence, acceptance criteria, test plan, scope/out-of-scope, docs plan, and handoff notes.
- Plan alignment, relationship, required update or no-plan-update rationale.
- Slice shape, support reason, target goal experience, and likely owner/QA skill.
- UI direction, aesthetic bar, and native-language copy expectations when relevant.

GitHub is recommended because it gives durable issue IDs, PR linkage, branch protection, and review history, but the issue structure should still work without GitHub.

For greenfield repos, default to a local numbered issue file until hosted issue infrastructure exists.

## Questioning rules

- Prefer one or two sharp questions at a time.
- Ask actively when wording is imprecise, contradictory, missing success criteria, or uses repo-undefined product terms.
- Infer only low-risk details; ask before deciding scope, proof, UX, data, rollout, or plan truth.
- Skip questions only when intent is concrete and low-risk.
- Route broad feature/product behavior to `issue-brainstorm` when no approved approach exists.
- Mark weak evidence as needing validation before dispatch.
- Classify plan extension/conflict/deviation instead of pretending alignment.

## Good defaults

- Use short imperative titles that become clean branch names.
- Behavior changes need a test plan before readiness.
- Acceptance criteria should describe an end-to-end user path, not only a technical layer.
- UI/copy issues need first-read or primary-action criteria plus aesthetic and native-copy criteria.

## Hand-off

- If the issue is ready: hand off to `issue-intake`.
- If the issue is not ready: return a draft plus the missing items.
