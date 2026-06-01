# Parallel Wave: <wave-id>

## Goal

Short description of why these issues can move together.

## Plan Context

- Plan anchor:
- Target user goal experience:
- Plan gaps addressed:
- Plan relationship: `aligned` / `extension` / `conflict` / `deviation`
- Plan update or decision note:

## Status

planned

## Issues

- `<issue-id>` `<title>` origin: `<brainstorm | autonomous-scan | review-finding | compound-learning | user-request>`
- `<issue-id>` `<title>` origin: `<brainstorm | autonomous-scan | review-finding | compound-learning | user-request>`

## Ownership Lanes

- `<issue-id>` -> `<owned paths or package>`
- `<issue-id>` -> `<owned paths or package>`

## Scheduler Plan

- Main agent role: scheduler / integrator. Direct implementation only with no-safe-delegation rationale.
- Non-overlap lane scan:
- Main-agent direct implementation exception rationale, if any:
- Why this is a wave instead of one serial issue:
- One-issue wave rationale, if applicable:
- Serialization scope: `merge-order` / `dependency-order` / `fully-serialized`
- Tiny findings combined before dispatch:
- Oversized candidates split before dispatch:
- Target active lane count:
- Active lane budget before adding more workers:

## Worktree Plan

- Scheduler checkout path:
- Scheduler checkout remains on `develop`: `yes` / `no`
- Base `develop` snapshot:
- Default worktree root:
- Worktree ignored or repo-approved: `yes` / `no`
- Worker prompt guardrail: assigned worktree only, no root checkout edits, no other-worker reversions
- Worker reasoning effort: `high` default / `medium` only with trivial-lane and no-scope-impact rationale
- `<issue-id>` -> `<worktree path or serialize>`
- Subagent authorization: `explicitly-allowed` / `not-allowed` / `needs-user-approval`
- Authorization source: `issueflow parallel in user request` / `issueflow parallel in automation prompt` / `current-state handoff quoting issueflow parallel`
- Parallel trigger present: `issueflow parallel` / `none`
- `<issue-id>` -> `<subagent assignment or no-delegation rationale>`
- `<issue-id>` -> `<subagent assignment or no-delegation rationale>`

## Slice Boundaries

- `<issue-id>` -> `<vertical slice or support/contract-first reason>`
- `<issue-id>` -> `<vertical slice or support/contract-first reason>`

## Shared Contracts

- `<root wrapper, schema, registry, fixture, or baseline path>`
- Consumer slice:

## Dependencies and Restack

- Dependency order:
- Restack trigger:
- Serialization reason, if any:

## Proof Commands

- `<issue-id>` -> `<local proof command>`
- `<issue-id>` -> `<local proof command>`

## Merge Notes

- Queue or restack rule:
- Revalidation trigger:

## Follow-up Scan

- Main-agent wait-time discovery:
- Before-wait sources checked:
- Candidate overlap with active lanes:
- Before-wait scheduler scan recorded: `yes` / `no`
- No-dispatch reason: `no-candidate-after-minimum-scan` / `overlaps-active-lane` / `active-lane-budget-full` / `blocked-on-worker-output`
- Wait condition, if blocked on worker output:
- Signals to re-check after merge:
- Follow-up issue rule:
