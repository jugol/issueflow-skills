# Plan Governance

Use this reference when a project plan should be the durable product source of truth, not only a bootstrap note.

## Core rule

The plan is a living contract between product intent and implementation.

If the repo has a plan, issueflow should:

- start from it for first issues and autonomous gap scans
- extract target user goal experience, not only feature scope
- check new work against it before implementation
- update it when approved direction changes
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

- `PLAN.md`: top-level truth, product promise, current scope, links
- `PLAN_ANCHOR.md`: macro direction, target goal experience, current gaps
- `ROADMAP.md`: milestones, waves, sequencing, deferred work
- `DECISIONS.md`: approved changes and reversals
- `areas/<area>.md`: detailed feature/domain/UX/data/platform plan for one area

Split a single plan when it becomes too expensive to scan, usually when it exceeds a few hundred lines, contains independent product areas, or agents repeatedly need only one section.

## Plan-first start

If the repo begins with only a detailed plan:

1. Put or keep the plan at `docs/plan/PLAN.md` unless the user chose another primary file.
2. Extract `docs/plan/PLAN_ANCHOR.md` from the plan.
3. Extract the target user goal experience: user, situation, before state, primary product moment, after state, and proof of success.
4. Identify the first implementable product promise.
5. Create the first issue or wave from unimplemented plan gaps.
6. Ensure the first wave includes at least one `core` user-visible issue unless the plan explicitly requires stabilization first.
7. Record stack, topology, proof entrypoint, and current-state pointers before dispatch.

Do not require a full backlog before starting. The plan and anchor are enough to create the first wave.

Use [goal-experience-planning.md](./goal-experience-planning.md) when a plan describes features but not the user's target experience.

## User requests vs plan

Before turning a user-requested feature into implementation work, classify its relationship to the active plan:

- `aligned`: directly implements an existing plan promise or requirement
- `extension`: compatible with the plan but not currently written down
- `conflict`: changes, replaces, or contradicts existing plan direction
- `deviation`: intentionally explores outside the plan without changing it yet

For `aligned` work, cite the plan section and proceed through normal issue shaping.

For `extension`, update the plan or add a plan-change note before dispatch. For `conflict`, do not implement first; run interactive brainstorming, approve direction, then update `PLAN.md`, an area file, or `DECISIONS.md`. For `deviation`, record why it is worth doing now, how it is contained, and what would make it graduate into the plan.

## Plan gaps

A plan gap is a promised behavior, target user experience, UX target, domain rule, platform constraint, or proof expectation that is present in the plan but absent from the live product or durable harness.

Autonomous cycles should scan for plan gaps from `PLAN_ANCHOR.md`, current wave goal, active area plan, backlog board, recent proof, failing tests, and review findings.

When one gap is clear, raise one issue.

When two or more gaps are independent by user outcome, ownership lane, or proof command, create a wave instead of one broad issue.

## Plan change notes

Use a plan-change note when:

a user request conflicts with the plan, implementation disproves a planned approach, milestone/scope changes, an area plan is split out, or a deviation becomes official direction.

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

- planned item implemented -> mark the gap satisfied or update current-state
- scope changed -> update the plan or record a decision
- future plan work revealed -> raise follow-up issues or wave candidates
- reusable implementation knowledge produced -> capture through `issue-compound`

Implementation that silently diverges from the plan is not complete.
