# Issue Sizing and Scheduling

Use this when an autonomous cycle, feedback batch, plan gap scan, or dispatch decision is producing issues that are too small, too serial, or too dependent on the main agent doing all implementation work.

## Intent

Issueflow should avoid both extremes:

- atomized issues that each change one tiny detail and waste branch, proof, and merge overhead
- oversized issues that hide independent outcomes, ownership lanes, or proof paths

Default to a medium vertical slice: one meaningful user-visible or support outcome with one proof story, worth a branch but small enough for one focused lane.

## Main agent role

In autonomous wave work, the main agent is primarily the scheduler, issue creator, dispatcher, reviewer, and integrator. Its first responsibility is to actively maximize safe parallelism: find as many non-overlapping lanes as safely practical, assign them to subagents when allowed, and reserve direct implementation for single-lane work or blocking coordination.

It should:

- scan plan anchor, current state, backlog, feedback, failing proof, and solution triggers
- combine related tiny findings; split independent outcomes
- create waves when two or more issues can move together
- assign lanes, worktrees, proof commands, merge order, and worker handoffs
- track lane summaries, review proofs, manage restacks, run merge-gate, and run compound handoff
- while workers run, scan for next non-overlapping candidates without editing root checkout or active worker-owned paths

The main agent may implement directly when there is only one real lane, no subagent support, or a blocking coordination contract; record that rationale. `Serialized` means dependency or merge-order control unless marked fully serialized, and does not by itself prohibit worker implementation.

Subagents implement assigned lanes. A subagent should receive one issue, one worktree or branch, owned paths, out-of-scope boundaries, proof command, and expected summary; it should not reshape the wave.

Every worker prompt must state that the worker is not alone in the codebase, must work only in the assigned worktree, must not touch the root `develop` checkout, and must not revert or overwrite other workers' changes. If the lane needs a root checkout, shared registry, shared schema, fixture, or baseline change outside its ownership, the worker should stop and report the coordination need.

Default worker reasoning effort to `high` for implementation, QA, review, merge-risk, intake, scope-investigation, or scheduling-influencing lanes, even when the task is read-only. Use `medium` only for trivial documentation, mechanical edits, simple lookup, or narrowly scoped low-risk lanes that cannot change issue shape or wave scheduling.

## Good issue size

A good issue has:

- one product outcome, defect fix, prevention rule, or support contract
- one owner lane/package group, one proof story, explicit boundaries
- enough work to justify branch, proof, and merge overhead

For `core` work, an issue may cross domain, runtime, UI, and test files when they serve the same user-visible result. Do not split a coherent vertical slice just because it touches multiple layers.

For `support` or `contract-first` work, keep the issue tied to a named downstream core slice or consumer lane.

## Too small

Merge tiny candidates together when they share the same outcome, files, owner, and proof path.

An issue is probably too small when it is only a cosmetic tweak, rename, copy edit, constant/selector/fixture tweak, or setup step with no independent product meaning.

Keep tiny issues only when they unblock several lanes, carry high risk, require separate review, or must be reverted independently.

## Too large

Split an issue or turn it into a wave when it contains two or more user-visible outcomes, unrelated defects/feedback, separate packages or ownership lanes, independent proof commands, shared contract plus separable consumers, or rollout/migration/visual-baseline risk that deserves isolated review.

## Wave sizing

Autonomous cycles should prefer a wave when at least two independent candidate issues exist. A one-issue wave is usually a scheduling failure: either make it a single issue, scan for additional non-overlapping candidates, or record a concrete no-wave rationale.

A useful wave usually has two to five active lanes. Group larger batches by dependency, package, milestone, or user goal.

If a scan finds only one tiny candidate, look once for adjacent plan gaps, proof gaps, feedback items, or compound-learning triggers that can form a meaningful medium issue or a small wave. Do not fabricate work just to fill a wave.

Every product-facing wave should include at least one `core` issue unless it is explicitly a stabilization wave.

## Scheduling policy

Use worktree-first scheduling when two or more lanes have disjoint ownership and separable proof commands.

During a wave, keep the root checkout on `develop` for scheduling and integration. Each implementation lane gets its own worktree and `issue/*` branch.

When subagents are allowed, give each worker issue id, worktree/branch path, owned paths, out-of-scope boundaries, root-checkout prohibition, other-worker context, reasoning effort, proof command, dependency/restack notes, and expected summary format.

The main agent should keep a scheduler board for the wave and avoid waiting on a single lane when other lanes can proceed independently.

While subagents are running, the main agent should do read-only next-issue discovery: scan plan gaps, backlog, recent proof, feedback, and solution triggers for candidates that do not overlap active lanes. It may draft candidates or a next-wave proposal, but must not dispatch or edit files that conflict with active worker ownership until the current merge order is clear.

Serialize instead of parallelizing when lanes touch the same file, root registry, shared schema, generated fixture, golden baseline, root proof wrapper, or unresolved shared contract.
