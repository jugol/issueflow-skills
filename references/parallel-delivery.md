# Parallel Delivery

The major speed advantage of the workflow is parallel issue execution, not unsafe simultaneous branch integration.

## What can happen in parallel

- issue refinement
- implementation
- package-local tests
- QA proof collection
- PR preparation

## What needs control

- merging into the same long-lived integration branch
- visual baseline updates that touch the same files
- schema changes that alter another issue's base assumptions
- shared generated files

## Recommended model

- one issue branch per issue
- one medium vertical slice per product issue when possible
- worktree-first local parallelism when two or more lanes are independent
- root checkout stays on `develop` as the scheduler/integration checkout during a wave
- disjoint ownership when possible
- merge queue or auto-merge with revalidation into `develop`
- optional wave record that lists issue ids, owned paths, proof commands, and merge notes
- never reuse one `issue/*` branch for later issues

For autonomous waves, the main agent schedules and integrates from the root `develop` checkout rather than becoming the sole implementation lane. Delegate independent lanes when subagents are explicitly authorized by user or project policy.

## Strong pattern for monorepos

- split work by package or service lane when the ownership is naturally disjoint
- keep a package-local proof command for each lane
- let the root wrapper compose those checks
- assign each independent lane to a worktree unless the repo policy says otherwise
- treat edits to the root wrapper, shared schemas, or shared registries as cross-lane coordination points

Before creating worktrees, verify the repo's worktree root, commonly `.worktrees/`, is ignored or otherwise approved. If it is not, serialize or ask for the repo policy instead of scattering local directories.

If one lane exists mainly to define a shared contract, make that lane explicit:

- mark it `contract-first`
- name the consumer vertical slice or slices it enables
- let consumer lanes proceed in parallel if useful
- require consumer lanes to revalidate after the contract lane lands or restacks

If the contract needs to look like a real client payload, do not jump straight to a frontend-only model.

Prefer:

- reusable contract or domain payload shape
- thin backend adapter that packages it
- frontend or admin surfaces that consume it

This keeps "sample transport" logic from being duplicated in multiple lanes.

## Rule of thumb

If two branches both target `develop`, do not trust "green once" as enough after the base moves.

Trust this instead:

- green on owned branch
- green again after rebase or queue reconciliation
- checkout returns to `develop` before the next issue dispatch

## When true parallel merge is unsafe

- both branches touch the same file
- both branches rewrite the same fixture or golden baseline
- both branches depend on the same schema evolution
- one branch changes shared local proof commands
- one branch changes a root wrapper or registry that other branches rely on

In those cases, serialize.
