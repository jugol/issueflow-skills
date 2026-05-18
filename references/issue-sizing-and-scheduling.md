# Issue Sizing and Scheduling

Use this when an autonomous cycle, feedback batch, plan gap scan, or dispatch decision is producing issues that are too small, too serial, or too dependent on the main agent doing all implementation work.

## Intent

Issueflow should avoid both extremes:

- atomized issues that each change one tiny detail and waste branch, proof, and merge overhead
- oversized issues that hide independent outcomes, ownership lanes, or proof paths

The default target is a medium vertical slice: one meaningful user-visible outcome or support outcome with a clear proof story, large enough to be worth an issue branch, but still small enough for one focused implementation lane to complete and prove.

## Main agent role

In autonomous wave work, the main agent is primarily the scheduler, issue creator, dispatcher, reviewer, and integrator. It should:

- scan the plan anchor, current state, backlog, feedback, failing proof, and solution triggers
- group related tiny findings into medium issues when they share one outcome, ownership lane, and proof command
- split genuinely independent outcomes into separate issues
- create a wave when two or more issues can move together
- assign lanes, worktrees, proof commands, and merge order
- delegate implementation lanes to subagents when the environment and user or project policy allow it
- track lane summaries, review proofs, manage restacks, run merge-gate, and run compound handoff

The main agent may implement directly when there is only one real lane, no subagent support, or a blocking coordination contract. It should not serially implement one lane while other independent lanes remain undispatched.

## Good issue size

A good issue has:

- one product outcome, defect fix, prevention rule, or support contract
- one primary owner lane or package group
- one proof story
- explicit in-scope and out-of-scope boundaries
- enough work to justify branch, proof, and merge overhead

For `core` work, an issue may cross domain, runtime, UI, and test files when they serve the same user-visible result. Do not split a coherent vertical slice just because it touches multiple layers.

For `support` or `contract-first` work, keep the issue tied to a named downstream core slice or consumer lane.

## Too small

Merge tiny candidates together when they share the same outcome, files, owner, and proof path.

An issue is probably too small when it is only:

- a cosmetic tweak, rename, copy edit, constant change, selector update, or fixture tweak with no independent product meaning
- a setup step that can safely live in the first consumer slice

Keep tiny issues only when they unblock several lanes, carry high risk, require separate review, or must be reverted independently.

## Too large

Split an issue or turn it into a wave when it contains:

- two or more user-visible outcomes
- unrelated defects or feedback points
- separate packages or ownership lanes
- proof commands that can run independently
- a shared contract plus multiple consumers that can proceed as separate lanes
- rollout, migration, or visual-baseline risk that deserves isolated review

## Wave sizing

Autonomous cycles should prefer a wave when at least two independent candidate issues exist.

A useful wave usually has two to five active lanes. Group larger batches by dependency, package, milestone, or user goal.

If a scan finds only one tiny candidate, look once for adjacent plan gaps, proof gaps, feedback items, or compound-learning triggers that can form a meaningful medium issue or a small wave. Do not fabricate work just to fill a wave.

Every product-facing wave should include at least one `core` issue unless it is explicitly a stabilization wave.

## Scheduling policy

Use worktree-first scheduling when two or more lanes have disjoint ownership and separable proof commands.

During a wave, keep the root checkout on `develop` for scheduling and integration. Each implementation lane gets its own worktree and `issue/*` branch.

When subagents are available and policy allows them, give each implementation subagent:

- issue id and branch or worktree path
- owned paths or owned area
- out-of-scope boundaries
- required proof command
- dependency and restack notes
- expected summary format with files changed, proof run, risks, and follow-up candidates

The main agent should keep a scheduler board for the wave and avoid waiting on a single lane when other lanes can proceed independently.

Serialize instead of parallelizing when lanes touch the same file, root registry, shared schema, generated fixture, golden baseline, root proof wrapper, or unresolved shared contract.
