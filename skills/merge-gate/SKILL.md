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
- User-facing UI changes have been judged for human aesthetic quality and native-language copy naturalness, not only functionality
- Risk and rollback notes exist
- The proof was produced against a current or revalidated `develop` base

## Reject merge when

- Proof is manual-only
- Hosted checks are green but the local canonical checks are unknown or skipped
- The branch widened scope without issue updates
- The branch contains unrelated work for a later issue
- Acceptance criteria changed but the issue was not updated
- The harness should have grown but did not
- Visual changes landed without visual proof
- Screenshots or rendered proof show an ugly, broken, generic, visually confusing, or unpolished in-app screen
- User-facing copy sounds stiff, translated, uncommon, or unnatural to a fluent native speaker
- `develop` moved in a way that invalidates the branch's proof and the branch was not revalidated
- Another in-flight branch changed a shared root proof contract and this branch was not revalidated against it

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

## Hand-off

- If `merge-approved` and repo policy allows local integration, check out `develop`, update or verify it, merge the issue branch, resolve conflicts, rerun integrated proof, and leave the checkout on `develop`.
- If repo policy requires PR or merge queue, open or update that path and still return the local checkout to `develop`.
- Do not call the issue complete while the active checkout remains on `issue/*`.
- Batched, approved work moves toward `release-gate`
