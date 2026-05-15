# Plan Governance

Use this reference when a project plan should be the durable product source of truth, not only a bootstrap note.

## Core rule

The plan is a living contract between product intent and implementation.

If the repo has a plan, issueflow should:

- start from it when creating the first issues
- check new work against it before implementation
- update it when approved product direction changes
- mine it for unimplemented plan gaps during autonomous cycles
- keep a compact anchor so agents do not reload the full plan by default

## Recommended structure

Start small:

```text
docs/plan/
  PLAN.md
  PLAN_ANCHOR.md
```

Use `PLAN.md` as the long-form product plan and `PLAN_ANCHOR.md` as the compact summary agents read first.

When the plan grows, split into:

```text
docs/plan/
  PLAN.md
  PLAN_ANCHOR.md
  ROADMAP.md
  DECISIONS.md
  areas/
    <area>.md
```

- `PLAN.md`: top-level source of truth, product promise, current scope, links to detail files
- `PLAN_ANCHOR.md`: compact macro direction and current plan gaps
- `ROADMAP.md`: milestones, waves, sequencing, deferred work
- `DECISIONS.md`: approved plan changes and reversals
- `areas/<area>.md`: detailed feature, domain, UX, data, or platform plan for one area

Split a single plan when it becomes too expensive to scan, usually when it exceeds a few hundred lines, contains independent product areas, or agents repeatedly need only one section.

## Plan-first start

If the repo begins with only a detailed plan:

1. Put or keep the plan at `docs/plan/PLAN.md` unless the user chose another primary file.
2. Extract `docs/plan/PLAN_ANCHOR.md` from the plan.
3. Identify the first implementable product promise.
4. Create the first issue or wave from unimplemented plan gaps.
5. Ensure the first wave includes at least one `core` user-visible issue unless the plan explicitly requires stabilization first.
6. Record stack, topology, proof entrypoint, and current-state pointers before dispatch.

Do not require a full backlog before starting. The plan and anchor are enough to create the first wave.

## User requests vs plan

Before turning a user-requested feature into implementation work, classify its relationship to the active plan:

- `aligned`: directly implements an existing plan promise or requirement
- `extension`: compatible with the plan but not currently written down
- `conflict`: changes, replaces, or contradicts existing plan direction
- `deviation`: intentionally explores outside the plan without changing it yet

For `aligned` work, cite the plan section and proceed through normal issue shaping.

For `extension` work, update the plan or add a plan-change note before dispatch so future agents do not treat the feature as accidental scope.

For `conflict` work, do not implement first. Run interactive brainstorming, state the conflict plainly, get an approved direction, then update `PLAN.md`, an area file, or `DECISIONS.md` before creating implementation issues.

For `deviation` work, record why it is worth doing now, what would make it graduate into the plan, and how it will be contained.

## Plan gaps

A plan gap is a promised behavior, UX target, domain rule, platform constraint, or proof expectation that is present in the plan but absent from the live product or durable harness.

Autonomous cycles should scan for plan gaps from:

- `PLAN_ANCHOR.md`
- current wave goal
- active area plan
- backlog board
- recent proof
- failing tests or review findings

When one gap is clear, raise one issue.

When two or more gaps are independent by user outcome, ownership lane, or proof command, create a wave instead of one broad issue.

## Plan change notes

Use a plan-change note when:

- a user request conflicts with the current plan
- implementation proves a planned approach is wrong
- a milestone or scope boundary changes
- an area plan is split out of the top-level plan
- a deviation becomes official product direction

Small compatible edits can update `PLAN.md` directly, but the change should still be visible in `DECISIONS.md` or the issue/wave note when it affects sequencing or scope.

## Context hygiene

Agents should read plan artifacts in this order:

1. `PLAN_ANCHOR.md`
2. `CURRENT-STATE.md`
3. relevant section of `PLAN.md`
4. relevant `areas/<area>.md`
5. `ROADMAP.md` or `DECISIONS.md` only when sequencing or plan-change history matters

Do not bulk-load every area plan by default.

If `PLAN_ANCHOR.md` is stale, update it before creating the next issue or wave.

## Merge and compound loop

At merge or PR handoff, check whether the completed work changed product truth:

- If it implemented a planned item, mark the plan gap as satisfied or update the current-state pointer.
- If it changed scope, update the plan or record a decision.
- If it revealed future plan work, raise follow-up issues or wave candidates.
- If it produced reusable implementation knowledge, capture that through `issue-compound`.

Implementation that silently diverges from the plan is not complete.
