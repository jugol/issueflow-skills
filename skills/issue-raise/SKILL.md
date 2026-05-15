---
name: issue-raise
description: Use when the user describes a problem, improvement, feature, plan gap, or idea in natural language and wants help turning it into a clean implementation-ready GitHub or local issue through focused clarification.
---

# issue-raise

Turn rough problem statements into durable issues. This skill is conversational on purpose: it should refine the user's intent, not dump a rigid template too early.

## Workflow

1. Start from the user's natural language description.
2. Extract the likely problem, impact, desired outcome, and missing information.
3. Run a fan-out check before drafting a single issue.
4. Ask only the smallest number of focused questions needed to make the issue or wave implementation-ready.
5. Draft the issue using the shared template.
6. If a project plan exists, map the issue to the relevant plan promise, requirement, or constraint.
7. Classify the plan relationship as `aligned`, `extension`, `conflict`, or `deviation`.
8. If the issue extends or conflicts with the plan, require a plan update, decision-log entry, or plan-change note before dispatch.
9. Shape product work as a vertical slice by default: name the user-visible result, the needed domain or contract path, and the proof path.
10. For UI work, capture the experience direction: audience, primary action, first-viewport priority, desired feel, aesthetic bar, copy tone or target language, and anti-dashboard or no-debug-copy constraints.
11. If the issue is support-only or contract-first, name the nearby core slice it enables.
12. Suggest labels, branch slug, and the likely owning implementation or QA skill.
13. If the repo and auth context are available, prepare the issue for GitHub creation or create it directly after user confirmation.
14. If GitHub is not available, write the issue draft into the repo's chosen backlog location without changing the structure of the issue.

If the user report clearly contains multiple distinct failures, split them into separate issues that can be verified independently.

If the work came from `issue-brainstorm`, preserve the approved approach and rejected alternatives. If it came from an autonomous scan, record the origin signal such as failing test, review finding, playtest feedback, or compound-learning trigger.

If a direct coding session already changed files before this step was applied, backfill the issue draft honestly. Mark what was already done, list the proof that now exists, and add a handoff note that future similar work must be raised before implementation.

## Fan-out check

Create multiple issues instead of one when findings differ by user-visible behavior, ownership lane, proof command, dependency order, or rollout risk. Use `../../references/autonomous-wave-generation.md` and `../../templates/PARALLEL-WAVE.template.md` when two or more issues should move together.

## Package resources

- Use `../../templates/ISSUE.template.md` when drafting local issue files.
- Use `../../templates/BRAINSTORM.template.md` when preserving approved approaches and rejected alternatives.
- Use `../../references/plan-alignment.md` when the repo has a project plan or product brief.
- Use `../../references/plan-governance.md` when an issue should update, extend, split, or contradict the plan.
- Use `../../templates/PLAN-CHANGE.template.md` when a plan-changing decision needs a durable note.
- Use `../../references/two-track-routing.md` when deciding whether this came from interactive intake or autonomous cycle work.
- Use `../../references/autonomous-wave-generation.md` when a report should split into a wave.
- Use `../../references/vertical-slice-architecture.md` when deciding whether the issue is `core`, `support`, `internal`, or `deviation`.
- Use `../../references/experience-first-ui.md` when UI, visuals, copy tone, or first-viewport behavior matters.

## Required output

- A concise issue title
- Origin: `brainstorm`, `autonomous-scan`, `review-finding`, `compound-learning`, or `user-request`
- Problem statement with evidence
- Plan alignment note, if a plan exists
- Plan relationship: `aligned`, `extension`, `conflict`, or `deviation`
- Required plan update or no-plan-update rationale
- Slice shape or support reason
- UX or visual direction, if UI is involved
- Aesthetic and native-language copy expectations, if UI or user-facing text is involved
- Acceptance criteria
- Test plan
- Spec file impact, if applicable
- Scope and out-of-scope
- Docs plan
- Handoff notes

GitHub is recommended because it gives durable issue IDs, PR linkage, branch protection, and review history, but the issue structure should still work without GitHub.

For greenfield repos, default to a local numbered issue file until hosted issue infrastructure exists.

## Questioning rules

- Prefer one or two sharp questions over a large questionnaire.
- If the user's intent is already concrete, skip questions and draft immediately.
- If the user requested a broad feature or product behavior and no approved approach exists yet, route to `issue-brainstorm`.
- If evidence is weak, explicitly mark the issue as needing validation before dispatch.
- If the issue does not clearly advance the plan, classify whether it is an extension, conflict, or deviation instead of pretending it is aligned.

## Good defaults

- Use imperative issue titles.
- Keep issue titles short enough to become branch names cleanly.
- If the issue changes behavior, require a test plan before calling it ready.
- Prefer acceptance criteria that describe an end-to-end user path rather than only a technical layer.
- For UI issues, include a first-read or primary-action acceptance criterion before proof-only criteria.
- For UI or copy issues, include an acceptance criterion that the rendered screen looks aesthetically intentional and the visible copy sounds natural to a native speaker in the target language.

## Hand-off

- If the issue is ready: hand off to `issue-intake`.
- If the issue is not ready: return a draft plus the missing items.
