# Vertical Slice Architecture

Issueflow recommends vertical slice architecture as the default architecture and delivery style for product work.

## Why it fits issueflow

- An issue names one behavior or outcome.
- An issue branch isolates the work needed for that outcome.
- The harness proves the outcome through the real user path.
- The merge gate checks that the slice still works after integration.

This keeps product value, code ownership, and proof tied together instead of letting separate layers drift.

## Slice shape

A `core` issue should usually include the thinnest useful path through:

- domain rule, use case, or state transition
- data model, fixture, schema, or shared contract when needed
- adapter, API, event, or runtime boundary when needed
- user-facing screen, interaction, or product surface
- durable automated proof and any required visual evidence

The slice does not need to finish every internal layer. It should make one concrete user-visible result real enough to verify.

For UI slices, "user-visible" means the intended product experience, not a proof dashboard. Pair this reference with [experience-first-ui.md](./experience-first-ui.md) when a slice includes screens, flows, or visual polish.

## Issue shaping

Ask:

- What can a user do or understand after this closes?
- Which domain behavior must exist for that to be true?
- Which UI or product surface proves it?
- Which test or smoke path will keep it from regressing?

Prefer acceptance criteria that describe the user path and observable result. Avoid layer-only titles such as "add service layer" or "build API endpoint" unless the issue also names the downstream slice it enables.

## Support and contract-first work

Support issues are allowed, but they should stay attached to a nearby vertical slice.

Use `contract-first` when one issue must define a shared schema, payload, fixture grammar, or helper before consumer slices can safely proceed. In that case:

- name the downstream core slice or consumer lanes
- prove the contract directly
- require consumer lanes to revalidate after the contract lands or restacks
- avoid building broad infrastructure without a ready consumer path

## Repo topology

When the repo's conventions allow it, prefer feature or slice ownership over strict technical-layer ownership. A slice can own its UI, state/use-case code, fixtures, and tests close together.

Do not force a folder migration just to look like vertical slice architecture. In an existing layered repo, use vertical slices as the issue, branch, and proof boundary first. Move files only when it reduces real coupling or matches established local patterns.

Share code after a second slice needs it, or when a cross-slice contract is already clear. Avoid extracting shared abstractions from the first slice just because a future slice might need them.

## Dispatch and parallelism

- Prefer one issue branch per vertical slice.
- Parallelize separate slices when ownership is disjoint.
- Serialize or restack when slices share a new contract, root wrapper, generated fixture, or visual baseline.
- Avoid horizontal waves made only of data, API, UI shell, or QA paperwork unless each lane points to a named core slice.

## Proof

Proof should tell the slice story:

- the behavior was exercised through the real user path
- the important boundary or contract was tested directly
- the user-facing surface visibly reflects the result
- the harness registry names the behavior or slice, not only the implementation layer

For UI work, screenshots or goldens should show the primary product surface, not a debug-only shell.
