---
name: merge-gate
description: Decide whether an issue branch is allowed to merge into develop by checking scope discipline, QA evidence, durable harness updates, and branch readiness. Use after implementation and QA but before merge.
---

# merge-gate

This skill is the approval and integration stop for `issue/* -> develop`.

## Merge requirements

- Linked issue exists and is still the right scope
- Branch targets `develop`
- Branch name matches the linked issue id and slug closely enough to prove scope ownership
- Repo-local proof commands pass
- Required checks are green
- QA evidence exists and matches the issue acceptance criteria
- Harness updates landed with the change
- Docs plan was honored
- Product plan truth is current: implemented plan gaps are marked, changed scope is reflected in the plan or decision log, and plan-divergent work has an explicit rationale
- User-facing UI changes have been judged for human aesthetic quality and native-language copy naturalness, not only functionality
- Risk and rollback notes exist
- The proof was produced against a current or revalidated `develop` base
- Completion handoff is recorded before the issue is called complete: issue note, backlog or wave board, latest proof pointer, and any automation/run memory no longer identify the completed issue as active work
- Follow-up work discovered during implementation or QA has a durable decision: new issue(s) created or updated, explicit defer note, or explicit `no follow-up issue` rationale
- Compound learning decision is recorded: `issue-compound` note created or updated, or explicit no-compound rationale
- Context governance is preserved: active pointers are updated, completed artifacts are archived or summarized, and future agents are not required to bulk-load old issues or solution notes
- If automation will continue, current-state records macro direction, micro direction, and next cycle decision

## Reject merge when

- Proof is manual-only
- Hosted checks are green but the local canonical checks are unknown or skipped
- The branch widened scope without issue updates
- The branch contains unrelated work for a later issue
- Acceptance criteria changed but the issue was not updated
- Product behavior diverged from the active plan but no plan update, decision entry, or deviation rationale exists
- A planned feature was implemented but the plan gap or current-state pointer still makes it look unimplemented
- The harness should have grown but did not
- Visual changes landed without visual proof
- Screenshots or rendered proof show an ugly, broken, generic, visually confusing, or unpolished in-app screen
- User-facing copy sounds stiff, translated, uncommon, or unnatural to a fluent native speaker
- `develop` moved in a way that invalidates the branch's proof and the branch was not revalidated
- Another in-flight branch changed a shared root proof contract and this branch was not revalidated against it
- Post-merge notes, backlog pointers, wave notes, or automation memory can still cause the completed issue to be selected again as current work
- Known follow-up work exists but no next issue, updated existing issue, defer note, or no-follow-up rationale is recorded
- Reusable learning or recurring prevention knowledge exists but no `docs/solutions/` update or no-compound rationale is recorded
- Completed issue, wave, brainstorm, or proof artifacts still remain in the active context set without a reason

## Parallel merge rule

Independent branches may become merge-ready in parallel, but `develop` should absorb them through a controlled queue rather than blind simultaneous merging.

Preferred order:

1. each branch reaches `merge-approved`
2. auto-merge or merge queue rebases each branch against current `develop`
3. required checks rerun if the base changed materially
4. merge proceeds only after the branch is still green

Practical meaning: parallel preparation is the speed advantage, queue-controlled merge is the safety mechanism.

If the branch changes a shared wrapper, registry, schema root, or other repo-wide proof contract, expect dependent in-flight branches to restack or rerun proof before they merge.

Use `../../references/branch-lifecycle.md` and `../../references/parallel-delivery.md` when branch ownership, merge order, or restacking is unclear.

## Output

- `merge-approved` or `merge-blocked`
- Missing evidence or scope drift
- Required fixes before merge
- Whether queue merge or restack is required
- Integration action taken or required: direct merge, PR, merge queue, or blocked
- Conflict resolution performed or still required
- Integrated proof result on `develop`, unless a PR-only policy blocks local integration
- Post-merge branch action: return checkout to `develop`, and delete/archive the issue branch only according to repo policy
- Completion handoff updates made: issue note, backlog or wave board, latest proof pointer, and automation/run memory if present
- Follow-up issue decision: issue ids created or updated, explicit defer note, or explicit no-follow-up rationale
- Plan update decision: plan gap satisfied, plan changed, decision logged, or explicit no-plan-update rationale
- Compound decision: solution note created or updated, or explicit no-compound rationale
- Context governance updates: current-state pointer, archive move, summary, or solution index update
- Cycle compaction performed or skipped with rationale
- Next dispatch recommendation, or a clear statement that no next issue should start yet

## Hand-off

- If `merge-approved` and repo policy allows local integration, check out `develop`, update or verify it, merge the issue branch, resolve conflicts, rerun integrated proof, and leave the checkout on `develop`.
- If repo policy requires PR or merge queue, open or update that path and still return the local checkout to `develop`.
- Do not call the issue complete while the active checkout remains on `issue/*`.
- Do not call the issue complete until the forward handoff is durable: update the issue note, backlog or wave board, latest proof/current-state pointer, and any automation/run memory so the next run cannot continue the completed issue by mistake.
- If the completed issue reveals future work, raise or update follow-up issues before final handoff; if it does not, state the explicit no-follow-up rationale.
- If the completed issue changed product truth, update `docs/plan/PLAN.md`, `PLAN_ANCHOR.md`, `DECISIONS.md`, the relevant area plan, or record why no plan update is needed.
- Run `issue-compound` when the work produced reusable implementation knowledge, a failed approach worth remembering, a prevention rule, or follow-up triggers.
- Update current-state and archive pointers so the next agent reads the active set instead of the full history.
- If the issue closes an automation cycle or leaves many stale pointers, perform cycle compaction before recommending the next dispatch.
- Batched, approved work moves toward `release-gate`
