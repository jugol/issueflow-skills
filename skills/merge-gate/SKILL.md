---
name: merge-gate
description: Approve or block issue/* integration into develop by checking scope, proof, plan truth, durable completion state, and branch readiness. Use after implementation and QA.
---

# merge-gate

Treat this as the `issue/* -> develop` integration gate.

## Approval requirements

- Issue, branch, scope, and acceptance criteria match.
- Proof and canonical checks pass against current or revalidated `develop`; required harness, visual, aesthetic, and native-copy evidence exists.
- Plan truth, risk/rollback notes, and any shared contract/restack requirements are current.
- Completion state prevents reselection: issue note, backlog/wave board, proof/current-state pointer, and automation memory are updated.
- Follow-up, compound, and context/history-compaction decisions are explicit.
- Blocked automation is paused with a resume condition, not deleted.

Missing or stale evidence, unrecorded scope/plan drift, manual-only proof, unrevalidated shared contracts, append-only active context, or an unresolved completion decision blocks merge.

## Parallel integration

Branches may prepare in parallel but enter `develop` through a controlled queue. Rebase/restack and rerun affected checks when `develop` or shared wrappers, registries, schemas, fixtures, or proof contracts change. Load `../../references/branch-lifecycle.md` and `../../references/parallel-delivery.md` when order is unclear.

## Output

Return `merge-approved` or `merge-blocked` with missing evidence, drift, required fixes, queue/restack decision, conflict/integrated-proof status, completion/compound/compaction decisions, next dispatch, and automation continuation/pause/retirement rationale.

## Integration contract

- When approved and local policy allows, switch to `develop`, update it, merge, resolve conflicts, rerun integrated proof, update durable state, and leave root on `develop`.
- Under PR/merge-queue policy, open/update that path and still return local root to `develop`.
- Do not call the issue complete while root remains on `issue/*` or durable completion state is missing.
- Run `issue-compound` when its triggers apply; then route a release batch to `release-gate`.
