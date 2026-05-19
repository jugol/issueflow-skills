---
name: issueflow
description: Umbrella entrypoint for the issueflow pack. Use when the user wants to adopt or follow Git Flow-lite issue-driven work, continue or iterate an autonomous cycle, schedule parallel subagent/worktree lanes, dispatch next issues, govern a plan-first project, or run issue discovery, proof, merge, and compound learning without naming a narrower sub-skill.
---

# issueflow

This is the front door to the pack.

## Main-thread delegation contract

In autonomous implementation cycles, the main thread is the scheduler, reviewer, integrator, and merge-gate owner. Before editing issue code, either delegate a bounded lane to a worker when subagents are explicitly authorized, or record a no-safe-delegation rationale. `Serialized` controls merge/dependency order; it is not permission for main-thread implementation.

`issueflow parallel` is the short explicit authorization to use subagents and worktrees for independent non-overlapping lanes. Do not infer that permission from plain `issueflow`. For a simple single-lane request, proceed normally without parallel mode. For multi-spec, multi-surface, or long-running goal work, first attempt parallel shaping with a non-overlap scan and wave/lane plan; ask the user to run or confirm `issueflow parallel` only when worker authorization is the blocker that would otherwise force main-thread or serialized implementation.

After dispatching workers, do not idle by default. Keep doing read-only scheduler work: update the wave board/current-state, scan for non-overlapping next-issue candidates, and prepare follow-up lanes. Use `wait_agent` only when the next main-thread action is blocked on worker output. Do not dispatch extra lanes until subagent authorization, active-lane budget, and non-overlap with current worker ownership are explicit.

Before calling `wait_agent` while any worker is running, record a before-wait scheduler scan: non-overlapping candidates found, dispatch decision, and one reason if no dispatch happened: `no-candidate`, `overlaps-active-lane`, `active-lane-budget-full`, or `blocked-on-worker-output`.

## Routing

- New repo or adopting the workflow in an existing repo -> `repo-bootstrap`
- User-requested feature, product behavior, UI change, or ambiguous improvement -> `issue-brainstorm`
- Rough problem statement that should become an issue -> `issue-raise`
- Existing issue needs readiness review -> `issue-intake`
- Ready issue needs branching and ownership -> `issue-dispatch`
- Web implementation work -> `implement-web`
- Flutter implementation work -> `implement-flutter`
- Web QA proof before merge -> `qa-web-proof`
- Flutter QA proof before merge -> `qa-flutter-proof`
- Merge decision for `issue/* -> develop` -> `merge-gate`
- Post-merge learning, prevention notes, or follow-up capture -> `issue-compound`
- Release decision for `develop -> main` -> `release-gate`

## Shared package resources

Load package-level references only when the task needs deeper guidance. Paths are relative to this `SKILL.md`:

- Operating model: `../../OPERATING-MODEL.md` only for full workflow design, onboarding docs, or unresolved policy conflicts
- Plan truth: `../../references/plan-alignment.md`, `../../references/plan-governance.md`, `../../references/goal-experience-planning.md`
- Track/intake: `../../references/two-track-routing.md`, `../../references/interactive-brainstorming.md`
- Autonomous scheduling: `../../references/autonomous-wave-generation.md`, `../../references/issue-sizing-and-scheduling.md`, `../../references/parallel-delivery.md`
- Lifecycle safety: `../../references/automation-governance.md`, `../../references/branch-lifecycle.md`, `../../references/compound-learning.md`
- Context control: `../../references/context-governance.md`, `../../references/history-compaction.md`
- Product shape: `../../references/vertical-slice-architecture.md`, `../../references/experience-first-ui.md`
- Durable artifacts: `../../templates/`

## Default behavior

If the user asks broadly how to use the workflow in a repo, start with `repo-bootstrap`.

## Track routing

- Autonomous Cycle: continue, iterate, resume, process failures, process review/playtest feedback, or choose next work. Scan durable signals and create issues or waves; do not wait for the user to name every task.
- Interactive Feature Intake: feature, product behavior, UI change, or ambiguous improvement. Use `issue-brainstorm` before `issue-raise` unless the request is already concrete and low-risk.
- Concrete bug or product feedback: use `issue-raise`; split independent findings into a corrective wave.
- Existing issue link/body: use `issue-intake`.
- If code was already changed before routing, backfill the issue/wave/proof trail honestly before final handoff.

## Autonomous cycle rules

- Read macro then micro context: current-state pointer, plan anchor summary, current wave/issue, recent proof, active branch/worktree, next action, then matching solution-index entries.
- Keep active context small. Search archives before opening them; never bulk-load completed issues, old waves, superseded brainstorms, old proof logs, or all solution notes.
- Keep `PLAN_ANCHOR.md` and `CURRENT_STATE.md` bounded: short summaries and links only; move completed issue, wave, and proof detail to `docs/history/` or equivalent.
- Prefer medium vertical-slice issues and wave-first scheduling. Avoid one tiny issue at a time; use `issue-sizing-and-scheduling.md` when sizing or delegation is unclear.
- For complex work, attempt read-only parallel shaping before settling for one lane. In automations, worker authorization must come from `issueflow parallel` in the user/automation prompt or a current-state handoff quoting that approval. If lanes are technically independent but authorization is missing, ask or pause for `issueflow parallel`; if lanes overlap, serialize with overlap rationale.
- Before waiting on active workers, update the current-state or wave board with the latest before-wait scheduler scan.
- If automation needs user input, approval, credentials, or product/policy choice, pause the existing automation instead of deleting it. Record blocker, question, active work, branch/worktree, proof pointer, resume condition, and next step.

## Plan and product truth

- A plan-only project can start: bootstrap `docs/plan/PLAN.md` or the repo's chosen plan, extract the target user goal experience, create a compact plan anchor, and generate the first issue wave from unimplemented gaps.
- Treat an existing plan as active truth. New issues and waves must cite or classify their relationship to it: `aligned`, `extension`, `conflict`, or `deviation`.
- Require a target user goal experience in plan work: user/situation, before state, primary product moment, after state, and user-visible proof.
- For `extension` or `conflict`, update the plan or record a plan-change decision before dispatch. Do not let implementation silently change product truth.

## Issue shape and UI quality

- Ask focused questions when implementation-critical details are vague: actor, target screen, state, data ownership, proof, rollout, or plan relationship. Infer only low-risk details and record the assumption.
- Default product work to a vertical slice: one user-visible outcome through the needed domain, contract, UI, and proof path. Split or form a wave only when outcomes, owners, proof commands, dependencies, or rollout risks are independent.
- For support or contract-first work, name the downstream core slice it enables.
- For UI, build the intended product experience, not proof dashboards by default. Screens must look aesthetically intentional, visible copy must sound natural to a fluent native speaker, and diagnostics should stay hidden/test-only unless the product is operational tooling.
- For non-icon scene or product assets, use generated or captured JPG/PNG raster imagery; keep SVG/CSS/canvas drawing for icons and controls.

## Branch, finish, and compound

- Before concrete changes, check branch state. If on `issue/*`, continue only for that issue; otherwise merge, park, or dispatch fresh from `develop`.
- An issue is not complete until integrated into `develop` or handed to the repo's PR/merge queue, and the checkout has returned to `develop`.
- After integration or PR handoff, update the issue note, backlog/wave board, latest proof pointer, and automation/run memory so completed work is not selected again.
- Create/update follow-up issues when defects, polish, or next slices are discovered; otherwise record a concrete no-follow-up rationale.
- Run `issue-compound` when work produced reusable learning, prevention rules, failed approaches, follow-up triggers, plan gaps, or active-context drift. History compaction is part of that conditional handoff.
