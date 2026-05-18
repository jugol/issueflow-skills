---
name: merge-gate
description: Decide whether an issue branch is allowed to merge into develop by checking scope discipline, QA evidence, durable harness updates, and branch readiness. Use after implementation and QA but before merge.
---

# merge-gate

This skill is the approval and integration stop for `issue/* -> develop`.

## Merge requirements

- Linked issue, branch name, and scope match.
- Branch targets `develop`; proof was produced against current or revalidated `develop`.
- Repo-local proof and required checks pass; QA evidence matches acceptance criteria.
- Harness updates landed when behavior, UI, or risk required them.
- Product plan truth is current: implemented gaps, changed scope, or deviations are reflected in plan/decision notes.
- UI changes have aesthetic and native-language copy review, not only functional proof.
- Risk/rollback notes exist.
- Completion handoff prevents the completed issue from being selected again: issue note, backlog/wave board, latest proof pointer, and automation/run memory are updated.
- Follow-up decision exists: new/updated issue, explicit defer, or explicit no-follow-up rationale.
- Compound decision exists: `issue-compound` note/update or explicit no-compound rationale.
- Active context stays bounded: completed details move to history or summaries; `PLAN_ANCHOR.md` and `CURRENT_STATE.md` keep pointers, not append-only history.
- Continuing automation has macro direction, micro direction, and next cycle decision; blocked automation is paused with a resume condition, not deleted.

## Reject merge when

- Proof is manual-only, local canonical checks are skipped/unknown, or `develop` moved without revalidation.
- Scope, acceptance criteria, or branch contents no longer match the issue.
- Product behavior diverged from plan without plan update, decision entry, or deviation rationale.
- Harness, visual proof, aesthetic review, or native-copy review is missing when required.
- Shared proof contracts changed in another branch and this branch was not revalidated.
- Post-merge notes, backlog pointers, wave notes, or automation memory can still select the completed issue.
- Follow-up, compound, context compaction, or history compaction decisions are missing.
- A user-blocked automation was deleted instead of paused without an explicit retirement reason.

## Parallel merge rule

Independent branches may become merge-ready in parallel, but `develop` should absorb them through a controlled queue rather than blind simultaneous merging.

Preferred order:

1. each branch reaches `merge-approved`
2. auto-merge or merge queue rebases each branch against current `develop`
3. required checks rerun if the base changed materially
4. merge proceeds only while the branch remains green

Parallel preparation is the speed advantage; queue-controlled merge is the safety mechanism. Shared wrapper, registry, schema, or repo-wide proof contract changes require dependent branches to restack or rerun proof.

Use `../../references/branch-lifecycle.md` and `../../references/parallel-delivery.md` when branch ownership, merge order, or restacking is unclear.

## Output

- `merge-approved` or `merge-blocked`
- Missing evidence or scope drift
- Required fixes before merge
- Whether queue merge or restack is required
- Integration action: direct merge, PR, merge queue, or blocked
- Conflict status and integrated proof result on `develop`, unless PR-only policy blocks local integration
- Post-merge branch action and return-to-`develop` status
- Completion handoff, follow-up, plan, compound, context, and history-compaction decisions
- Next dispatch recommendation or no-next-work rationale
- Automation continuation: continue, pause existing automation with resume condition, or retire/delete with rationale

## Hand-off

- If `merge-approved` and repo policy allows local integration, check out `develop`, update or verify it, merge the issue branch, resolve conflicts, rerun integrated proof, and leave the checkout on `develop`.
- If repo policy requires PR or merge queue, open or update that path and still return the local checkout to `develop`.
- Do not call the issue complete while the active checkout remains on `issue/*`.
- Do not call the issue complete until the handoff is durable: issue note, backlog/wave board, latest proof/current-state pointer, automation/run memory, follow-up decision, plan decision, compound decision, and bounded active context.
- If active context files have grown from completed history, move details to history and leave summaries plus pointers before recommending the next dispatch.
- If the issue closes an automation cycle or leaves stale pointers, perform cycle compaction before recommending next work.
- Batched, approved work moves toward `release-gate`
