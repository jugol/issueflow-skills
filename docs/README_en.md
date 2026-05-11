# Issueflow Skills

Issueflow is a Codex skill pack and plugin for issue-driven software development. It gives AI agents a repeatable operating model for turning ideas, bugs, and product feedback into scoped issues, isolated branches, durable proof, and controlled releases.

The core idea is simple: do not let implementation outrun intent, evidence, or integration discipline.

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

Issueflow is not meant to add paperwork for its own sake. The goal is to keep the smallest durable trail that lets future humans and agents understand what happened, why it happened, and how it was proven.

## Project Management Model

Issueflow uses a Git Flow-lite model:

- `main`: production or release truth
- `develop`: integrated work that has passed issue-level proof
- `issue/<n>-<slug>`: one issue-scoped implementation branch
- `release/<version>`: optional release candidate stabilization
- `hotfix/<slug>`: production fix from `main`, back-merged into `develop`

The default lifecycle is:

1. Capture the work as an issue.
2. Validate readiness with `issue-intake`.
3. Dispatch from `develop` with `issue-dispatch`.
4. Implement only the approved scope.
5. Add or update durable test coverage.
6. Produce QA proof.
7. Pass `merge-gate`.
8. Merge into `develop`, resolving conflicts on the integration path.
9. Rerun integrated proof on `develop`.
10. Leave the checkout on `develop`.
11. Promote through `release-gate` when ready.

This model makes integration explicit. A completed issue branch is not the same thing as a release. `develop` absorbs proven work first; `main` changes only through an intentional release decision.

A branch that has passed proof but has not entered `develop` is merge-ready, not complete. Agents should not start the next issue from that branch.

## Vertical Slice Bias

Issueflow prefers vertical slices for product work. A good product issue should usually deliver one thin user-visible behavior across the necessary domain, contract, runtime, UI, and proof surfaces.

This does not mean every issue must be large. It means the issue should point toward a real product outcome instead of drifting into isolated layer work.

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
- You want stable branch hygiene around `develop` and `main`.
- You need durable proof before merge.
- Bugs, features, and UX feedback should become trackable issues.
- A project plan or product brief needs to stay connected to day-to-day work.
- You want future agents to understand prior decisions without reading old chats.
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
- `repo-bootstrap`: adapts the workflow to a concrete repository.
- `issue-raise`: turns rough ideas or feedback into implementation-ready issues.
- `issue-intake`: decides whether an issue is ready to start.
- `issue-dispatch`: creates isolated branches or worktrees from `develop`.
- `implement-web`: implements approved web issues with durable browser proof.
- `implement-flutter`: implements approved Flutter issues with durable app proof.
- `qa-web-proof`: verifies web changes with Playwright and local checks.
- `qa-flutter-proof`: verifies Flutter changes with widget, integration, and golden tests.
- `merge-gate`: decides whether an issue branch can merge into `develop`.
- `release-gate`: decides whether integrated work can promote to `main`.

## Practical Outcome

Using issueflow should make a repository feel calmer:

- Agents know where to start.
- Branches have one owner and one issue.
- Scope drift is caught early.
- Test coverage grows with product scope.
- Releases are deliberate.
- Project direction stays visible.

The workflow is intentionally lightweight, but it insists on the few boundaries that keep fast implementation from becoming chaotic implementation.
