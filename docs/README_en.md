# Issueflow Skills

Issueflow is a Codex skill pack and plugin for issue-driven software development. It gives AI agents a repeatable operating model for discovering or clarifying work, keeping product plans synchronized, shaping issues or waves, dispatching isolated branches, proving changes, merging safely, and capturing reusable learning.

The core idea is simple: do not let implementation outrun intent, evidence, or integration discipline.

The same `skills/` package is distributed for Codex and Claude Code. Claude Code users install it as a plugin marketplace and invoke namespaced skills such as `/issueflow:issueflow`.

When issueflow creates or updates `PLAN.md`, it should capture the target user goal experience: who the user is, what is difficult before, the primary product moment, what changes afterward, and what proof shows that experience exists.

## Philosophy

Issueflow treats software work as a chain of accountable decisions:

- What problem are we solving?
- Why does it matter now?
- What is explicitly in scope?
- What proof will show that the change works?
- Where should the work branch from?
- When is the branch allowed to merge?
- When is the integrated product allowed to ship?

This is especially important when AI agents are doing substantial implementation work. Agents are fast, but speed can blur boundaries. Issueflow gives agents a shared project memory and a set of gates so they do not silently widen scope, keep working on stale branches, or ship proof that only exists in a chat transcript.

Issueflow is not meant to add paperwork for its own sake. The goal is to keep the smallest durable trail that lets future humans and agents understand what happened, why it happened, how it was proven, and what the next cycle should know.

## Two-Track Planning

Issueflow uses two planning tracks.

The Autonomous Cycle Track is for automation, repeated iterations, post-merge follow-up, failing tests, review findings, and batches of playtest or user feedback. The agent scans durable signals instead of waiting for the user to name every next issue. It should combine related tiny findings into medium vertical-slice issues and create waves when independent lanes exist.

When an automation needs user input, approval, credentials, or a product decision, it should pause the existing automation and record the resume condition instead of deleting it.

The Interactive Feature Intake Track is for user-described features, product behavior changes, UI changes, and broad improvements. The agent inspects repo context first, asks focused questions, resolves imprecise or contradictory wording before implementation-critical assumptions become scope, proposes approaches when tradeoffs matter, and then turns the approved direction into one issue or a wave.

After merge or PR handoff, the compound loop captures reusable learning in `docs/solutions/` when a fix reveals a recurring pattern, failed approach, prevention rule, or follow-up trigger.

Context governance keeps this from becoming a memory pile. Agents should read current-state pointers and indexes first, then search archived issues, old waves, proof logs, and solution notes only when they are relevant. Autonomous cycles preserve macro direction, such as the product promise and current wave goal, separately from micro direction, such as the active issue, proof pointer, branch or worktree, and next action.

`PLAN_ANCHOR.md` and `CURRENT_STATE.md` should stay bounded. Completed issue, wave, and proof details should compact into `docs/history/` or the repo's equivalent archive, leaving only short summaries and archive pointers in active files.

## Plan Governance

Issueflow can start from a single detailed product plan. In a plan-first repo, the plan is not a one-time prompt; it is the product source of truth.

The recommended starting point is:

- `docs/plan/PLAN.md`: the detailed plan
- `docs/plan/PLAN_ANCHOR.md`: the compact summary agents read first

As the project grows, split the plan into `ROADMAP.md`, `DECISIONS.md`, and `areas/<area>.md` only when the single plan becomes too expensive to scan or contains independent domains.

When a user asks for a feature, the agent should classify the request against the plan as `aligned`, `extension`, `conflict`, or `deviation`. Aligned work can become an issue. Extensions and conflicts need a plan update or decision note before dispatch. Planned behavior that is still missing from the product becomes a plan gap, and autonomous cycles can turn plan gaps into issues or waves.

## Project Management Model

Issueflow uses a Git Flow-lite model:

- `main`: production or release truth
- `develop`: integrated work that has passed issue-level proof
- `issue/<n>-<slug>`: one issue-scoped implementation branch
- `release/<version>`: optional release candidate stabilization
- `hotfix/<slug>`: production fix from `main`, back-merged into `develop`

The default lifecycle is:

1. Discover or clarify the work through autonomous scan or interactive brainstorming.
2. Capture the work as one issue or a planned wave.
3. Validate readiness with `issue-intake`.
4. Dispatch from `develop` with `issue-dispatch`.
5. Implement only the approved scope.
6. Add or update durable test coverage.
7. Produce QA proof.
8. Pass `merge-gate`.
9. Merge into `develop`, resolving conflicts on the integration path.
10. Rerun integrated proof on `develop`.
11. Leave the checkout on `develop`.
12. Capture reusable learning with `issue-compound` when useful.
13. Promote through `release-gate` when ready.

This model makes integration explicit. A completed issue branch is not the same thing as a release. `develop` absorbs proven work first; `main` changes only through an intentional release decision.

A branch that has passed proof but has not entered `develop` is merge-ready, not complete. Agents should not start the next issue from that branch.

## Vertical Slice Bias

Issueflow prefers vertical slices for product work. A good product issue should usually deliver one medium user-visible behavior across the necessary domain, contract, runtime, UI, and proof surfaces.

This does not mean every issue should be tiny. It means the issue should be large enough to justify branch, proof, and merge overhead while still pointing toward one real product outcome instead of drifting into isolated layer work.

For autonomous waves, the main agent should act as scheduler and integrator, delegating independent implementation lanes when subagents are explicitly authorized.

Layer-first work is still valid when it is needed, but it should be named honestly:

- `core`: directly advances the user-facing product promise
- `support`: enables a nearby core slice
- `internal`: improves tooling, QA, admin, or review surfaces
- `deviation`: intentionally explores outside the active plan

Support and contract-first issues should name the downstream core slice they unblock.

## Experience-First UI

Issueflow has a strong bias against turning user-facing products into proof dashboards.

For UI-heavy work, the default screen should feel like the intended product or workflow. Diagnostics, raw payloads, QA labels, and evidence panels should live in tests, hidden inspectors, stable attributes, logs, or separate developer surfaces.

Functional proof is required, but it is not enough. A user-facing change is unfinished if the rendered screen looks broken, generic, visually confusing, or if the visible copy sounds unnatural in the target language.

## Durable Proof

Issueflow expects every meaningful change to strengthen the long-lived test harness.

Examples:

- Bug fix: add a regression test.
- Feature: add or extend scenario coverage.
- Web UI: add Playwright-backed proof.
- Flutter UI: add widget, integration, or golden proof.
- Visual change: attach rendered evidence and protect important states.
- Refactor: prove unchanged behavior with existing or tightened tests.

The proof must be rerunnable. A screenshot or manual claim can support evidence, but it should not be the only evidence for behavior that can be automated.

## When To Use Issueflow

Issueflow is a good fit when:

- AI agents are implementing nontrivial product work.
- A project has multiple issues moving in parallel.
- Automated runs should keep finding the next useful issue.
- User-requested features need clarification before implementation.
- User wording is often approximate and agents must actively ask about details that change scope, UX, data, proof, rollout, or plan truth.
- You want stable branch hygiene around `develop` and `main`.
- You need durable proof before merge.
- Bugs, features, and UX feedback should become trackable issues.
- A project plan or product brief needs to stay connected to day-to-day work.
- You want future agents to understand prior decisions without reading old chats.
- You need long-running automation without forcing every agent to read the whole project history.
- Web or Flutter UI work must include real browser/rendered evidence.

It is especially useful for small teams or solo builders who use AI heavily and need lightweight structure without heavyweight ceremony.

## When Not To Use Issueflow

Issueflow may be too much for:

- One-off scripts with no ongoing maintenance.
- Tiny throwaway prototypes.
- Repositories that intentionally use trunk-based development with no issue branches.
- Changes where no durable proof or future context matters.

Even then, parts of the model can still be useful. For example, `issue-raise` can help clarify a vague idea before coding, and `merge-gate` can serve as a pre-merge checklist.

## How The Skills Fit Together

- `issueflow`: routes broad requests into the right workflow skill.
- `issue-brainstorm`: clarifies feature requests before issue creation.
- `repo-bootstrap`: adapts the workflow to a concrete repository.
- `issue-raise`: turns rough ideas or feedback into implementation-ready issues.
- `issue-intake`: decides whether an issue is ready to start.
- `issue-dispatch`: creates isolated branches or worktrees from `develop`.
- `implement-web`: implements approved web issues with durable browser proof.
- `implement-flutter`: implements approved Flutter issues with durable app proof.
- `qa-web-proof`: verifies web changes with Playwright and local checks.
- `qa-flutter-proof`: verifies Flutter changes with widget, integration, and golden tests.
- `merge-gate`: decides whether an issue branch can merge into `develop`.
- `issue-compound`: captures reusable learning and follow-up triggers.
- `release-gate`: decides whether integrated work can promote to `main`.

## Practical Outcome

Using issueflow should make a repository feel calmer:

- Agents know where to start.
- Branches have one owner and one issue.
- Scope drift is caught early.
- Test coverage grows with product scope.
- Releases are deliberate.
- Project direction stays visible.
- Reusable learning compounds across issues.
- Current context stays small even as history grows.

The workflow is intentionally lightweight, but it insists on the few boundaries that keep fast implementation from becoming chaotic implementation.
