# Operating Model

This pack uses Git Flow-lite, not `main`-only GitHub Flow.

## Plan anchor rule

If the repo has a project plan, product brief, spec, or other durable requirements document, treat it as a plan anchor.

Before bootstrapping or dispatching work:

- identify the primary plan anchor file
- extract the core product promise
- extract the target user goal experience
- extract any non-negotiable UX, art, or platform constraints
- keep a compact plan summary close to the backlog so active work can be checked against it quickly

Do not treat the plan as a one-time bootstrap input.

When the repo is plan-driven, prefer a small plan governance structure:

- `docs/plan/PLAN.md` for the detailed product plan or index
- `docs/plan/PLAN_ANCHOR.md` for the compact summary agents read first
- `docs/plan/ROADMAP.md` for sequencing when needed
- `docs/plan/DECISIONS.md` for approved plan changes when needed
- `docs/plan/areas/` only after the plan has independent areas or becomes expensive to scan

Re-check it:

- before the first issue wave
- before each new wave
- before a major refactor or architecture push
- whenever internal tooling starts growing faster than user-visible product value

When a user request differs from the active plan, classify it as `aligned`, `extension`, `conflict`, or `deviation`. Extensions and conflicts must update the plan or record a decision before implementation dispatch. If the plan promises behavior that is still missing from the live product, treat that as a plan gap and turn it into an issue or wave during autonomous cycles.

A complete plan must describe the target user goal experience, not only a feature list. Capture who the user is, what is painful before, the primary product moment, what changes afterward, and what user-visible proof shows the experience exists.

## Why this model

- Issue work stays isolated.
- Multiple issue branches can merge into `develop` without forcing a release.
- QA can verify a realistic integrated state on `develop`.
- Promotion to `main` becomes an explicit release decision instead of an accidental side effect of finishing one issue.

## Two-track planning loop

Issueflow is not only a single-issue executor. It is an issue discovery, planning, proof, merge, and learning loop.

Use the Autonomous Cycle Track when automation, a user, or a completed merge asks the agent to continue. Scan the plan anchor, current plan gaps, backlog, failing tests, review findings, playtest feedback, recent proof, and `docs/solutions/`. Create follow-up issues or waves when concrete next work is visible; record a no-follow-up rationale when it is not.

Autonomous cycles should avoid one tiny issue per run. Prefer medium vertical-slice issues and wave-first scheduling; the main agent should first look for non-overlapping lanes to delegate before doing implementation itself.

When an automation cannot continue without user input, approval, credentials, or a product/policy decision, pause the existing automation instead of deleting it. Record the blocker, question, current issue or wave, branch/worktree, proof pointer, resume condition, and next step in the current-state or cycle compaction artifact.

Use the Interactive Feature Intake Track when a user describes a feature, product behavior, UI change, or ambiguous improvement. Ground in the repo first, ask focused questions, resolve imprecise or contradictory wording before it becomes issue scope, present two or three approaches when tradeoffs matter, and turn the approved direction into one issue or a wave before implementation.

After merge or PR handoff, run the compound loop when reusable learning exists, follow-up triggers are visible, or active context needs completion cleanup. Update or create `docs/solutions/` notes for recurring failures, reusable patterns, failed approaches, prevention rules, and follow-up triggers. When the completed work left historical detail in active files, the compound loop owns the history compaction handoff.

Govern context continuously. Start from current-state pointers, search indexes before archives, and keep completed issues, old waves, superseded brainstorms, old proof logs, and unrelated solution notes out of the default context.

For autonomous cycles, always preserve two levels of context:

- macro direction: plan anchor summary, product promise, current wave goal, and drift warning
- micro direction: active issue, recent proof pointer, active branch or worktree, next recommended action, and relevant solution index entries

Keep active context files bounded. `PLAN_ANCHOR.md` and `CURRENT_STATE.md` should not become append-only issue history. Archive completed issue, wave, and proof details to `docs/history/` or the repo's equivalent history folder, update a searchable history index, and keep only short completed summaries and pointers in active files.

## Lifecycle

1. Discover the next work through autonomous scan or interactive brainstorming.
2. Capture the work as one issue or a planned wave.
3. Refine issues until they are implementation-ready.
4. Confirm the checkout is on `develop` or an explicitly separate worktree from `develop`.
5. Branch from `develop`.
6. Implement only the approved issue scope.
7. Update the durable test harness with the change.
8. Produce QA evidence.
9. Pass `merge-gate`.
10. Merge the branch into `develop`, resolving conflicts on the integration path.
11. Rerun the required integrated proof on `develop`.
12. Return the working checkout to `develop`.
13. If repo policy requires PR-only integration, open or update the PR and make the pending merge explicit.
14. Run compound learning and completion cleanup when reusable knowledge, follow-up triggers, plan gaps, or active-context history drift exist.
15. Bundle approved issues into a release candidate.
16. Promote to `main`.

## Session guardrail

When a user gives a direct implementation request, first check whether the repo uses issueflow artifacts such as `backlog/BOARD.md`, numbered local issues, `TEST-HARNESS-REGISTRY.md`, or this skill pack.

If it does, do not treat the request as "just code". Route it through `issue-raise`, `issue-intake`, `issue-dispatch`, the relevant implementation skill, and the matching QA proof skill. For small fixes, this can be compact, but it should still produce or reference a durable issue and proof trail.

If the direct request is a feature, product behavior, UI change, or ambiguous improvement, route through `issue-brainstorm` before `issue-raise` unless the direction is already concrete and low-risk.

If the request contains vague referents, undefined product terms, contradictory statements, missing success criteria, hidden multi-issue scope, or unclear proof, ask targeted clarification questions before marking an issue ready. Infer only low-risk details from repo context and write down the assumption.

If the request is to continue, iterate, process feedback, handle test failures, or choose the next cycle, scan for follow-up issues or a wave instead of waiting for the user to name the next task.

Before routing a new concrete change, check the current branch. If the checkout is already on `issue/*`, continue only when the new request belongs to that same issue. Otherwise stop and finish, merge, or explicitly park that branch before dispatching a new issue from `develop`.

If work has already started outside issueflow, pause before the final answer and repair the trace:

- create or update the local/GitHub issue
- classify plan alignment
- record the dispatch ownership and wave context when the request contains multiple failures
- update the harness registry for durable tests
- attach the local proof commands and visual evidence

This repair does not make issue-free implementation acceptable; it only prevents the repository history from losing the reason and proof for the change.

If work for later issues accumulated on an older issue branch, treat it as branch lifecycle repair. Identify the unrelated work, stop adding to that branch, and move or replay the work onto the correct issue branch from `develop`.

## Branch lifecycle guard

Every issue branch must have a visible lifecycle:

- dispatch from `develop`
- one issue scope only
- implementation and proof on that branch
- `merge-gate` before integration
- merge into `develop` by default
- PR or merge queue only when repo policy requires it
- conflict resolution and integrated proof happen before the issue is called complete
- checkout returns to `develop` before the next issue starts

Block dispatch when the current checkout is an unrelated `issue/*` branch. Do not make `issue/001-*` or any other issue branch the default workspace for later work.

Use [branch-lifecycle.md](./references/branch-lifecycle.md) when a repo has stale issue branches, unclear branch ownership, or repeated work landing on the wrong branch.

When multiple independent issues exist, group them into an explicit parallel wave record so ownership, proof commands, scheduler role, delegation plan, and merge order are visible.

If one feedback pass reveals several separate failures, do not hide them inside one oversized issue.

Instead:

1. split the failures into explicit sibling issues
2. group them into one corrective wave
3. parallelize the disjoint lanes
4. keep the corrective wave open until all sibling issues are resolved and verified

## Drift stop rule

Pause and realign if any of these become true:

- the current issue cannot point to the plan clause or promise it advances
- several consecutive issues only improve meta tooling, QA paperwork, or admin views while the primary user-facing promise is still missing
- the repo has strong review artifacts but weak usable product surfaces
- the visual or interaction target in the plan is clearly absent from the live product path

In that case, create or prioritize a corrective issue wave that restores product-direction alignment before adding more supporting layers.

Corrective waves should be especially aggressive when live playtests expose user-facing confusion. Do not downgrade that feedback into a vague future polish note.

## Value sequencing rule

Classify issues as one of:

- `core`: directly advances the main user-facing product promise
- `support`: enables or sharpens a nearby core slice
- `internal`: improves tooling, QA, admin, or review layers
- `deviation`: intentionally explores outside the current plan

Until the first genuinely usable slice exists, every wave should include at least one `core` issue.

After that, avoid long runs of `internal`-only waves unless the wave is explicitly justified as stabilization.

When a support or shared-contract issue unblocks a ready core user-facing issue in the same wave, prefer continuing into the dependent product slice after the contract proof is green. Do not report support-only progress as sufficient product progress when the ready downstream issue is what makes the feature visible to a user.

## Vertical slice architecture recommendation

Use vertical slice architecture as the default product-delivery shape.

For `core` work, prefer issues that carry one thin user-visible behavior through the required domain, contract, runtime, UI, and proof surfaces. The goal is not to finish every layer completely; the goal is to make one real outcome visible, executable, and regression-protected.

Do not make issues microscopic by splitting every layer into its own branch. A single issue may include multiple files and layers when they all serve the same user-visible result and proof story. Combine nearby tiny findings when they share one outcome, owner, and proof command.

Layer-first work is allowed when it is genuinely needed, but it should be classified as `support`, `internal`, or `contract-first` and should name the nearby core slice it enables. Avoid broad data-only, API-only, UI-shell-only, or QA-paperwork waves unless each lane points back to a concrete vertical slice.

When a repo already has a layered folder structure, do not force an architecture migration before delivering value. Use vertical slices as the issue, branch, ownership, and proof boundary first. Move files toward feature or slice ownership only when it reduces real coupling or matches local conventions.

Use [vertical-slice-architecture.md](./references/vertical-slice-architecture.md) when shaping a new issue wave, evaluating support-only work, or planning a major architecture push.

## Experience-first UI rule

For user-facing UI, proof must support the product experience instead of defining the visible screen.

Do not let issueflow turn the first product surface into a dashboard, QA board, debug console, evidence table, or admin shell unless that is the product being built. The default screen should communicate the intended user promise through the primary interaction, scene, object, or workflow.

Diagnostics should live in stable data attributes, automated assertions, hidden inspectors, collapsed details, logs, or test helpers. If a proof surface is needed, keep it separate from the default user path.

Screen judgment must include a human aesthetic and native-language review. Correct implementation is not enough if the in-app screen looks ugly, broken, generic, visually confusing, or amateur, or if user-facing copy sounds stiff, translated, uncommon, or unnatural to a fluent native speaker. Treat those as product failures, not optional polish.

When bootstrapping or raising UI work, capture a compact UX direction: audience, primary action, first-viewport priority, desired visual language, copy tone or target language, and anti-goals such as "not a dashboard". Use [experience-first-ui.md](./references/experience-first-ui.md) when a screen keeps drifting toward dashboard-like proof UI or when screenshots/copy pass tests but still feel bad to a human viewer.

## Durable harness policy

The project must grow its permanent test surface as it grows product scope.

- Bug fix: add a regression test.
- Feature: add or update a scenario/spec test.
- UI change: add or update visual coverage.
- Refactor: prove unchanged behavior with existing or tightened tests.
- Removed behavior: remove tests only when the issue explicitly removes the feature.

The harness is a first-class artifact, not cleanup work.

For browser proof that validates carryover from a previous resolved state, provide a direct proof seed or harness path for that resolved contract in addition to any long end-to-end scenario. Long workflows can otherwise hide the target surface and make a stable contract look flaky.

## Shared contract naming

When a new intermediate shared contract appears, prefer a role-first name.

- good: `archive-review-summary`
- bad: `archive-envelope`

Use [contract-naming.md](./references/contract-naming.md) when naming a new shared seam.

When one issue introduces a payload, recommendation, or explainability contract that multiple lanes will consume, prefer this shape:

- shared or reusable contract first
- thin backend adapter second
- frontend or admin consumer surfaces after that

This keeps transport-shaped logic from drifting into multiple packages.

## Evidence-history contracts

When a feature turns resolved events into a history, ledger, or review surface, keep it evidence-only by default.

- Derive history rows only from previous resolved receipts, outcomes, or evidence links.
- Keep the current user action or selection receipt as the source of truth unless the issue explicitly asks to change it.
- Add tests that prove unresolved current state cannot precompute resolved success or failure confidence.
- Surface target-vs-selected evidence rather than overwriting user choices with a learned recommendation.
- If a prior state is no longer directly available, carry stable linked evidence ids and compact review readouts instead of pretending the new surface can inspect unavailable details.

## Minimal repo expectations

- Issue form with acceptance criteria and test plan
- Plan governance files when a durable project plan exists
- PR template with proof section
- Test harness registry
- Brainstorm and wave note location
- `docs/solutions/` or equivalent solution-note location
- Current-state pointer and solution index
- History archive and history index
- Cycle compaction artifact or location for long-running automation
- Automation pause policy for user-blocked runs
- Stable local entrypoint for fast checks and full checks
- Package-local proof entrypoints for each app or service in a multi-package repo
- Optional GitHub Actions that mirror the same local commands instead of inventing different CI-only logic
- Protected `develop` and `main`

For greenfield projects that do not have GitHub wired yet, replace the GitHub issue layer with a local backlog board and numbered issue documents until the repo is ready to attach hosted collaboration.

If a plan anchor exists, also keep a compact plan summary or anchor note in the repo so agents do not need to reload the full long-form plan every time.

## Local-first verification

The canonical checks should live in the repo itself, not only in GitHub Actions.

- Prefer project-local commands such as `npm run test`, `npm run check`, `pnpm test`, or `flutter test`
- If a wrapper script exists, prefer one stable entrypoint such as `scripts/check-local.sh` or `scripts/check-local.ps1`
- GitHub Actions should call the same local commands whenever possible
- In multi-package repos, each package should also expose its own `check` or equivalent proof command

This keeps the workflow usable for local iteration and keeps hosted CI from becoming the only source of truth.

## Greenfield baseline rule

In a brand-new project, "baseline is green" does not mean full product tests already exist.

It means:

- the scaffold is structurally valid
- the issue ledger is valid
- the local proof entrypoint runs successfully
- the first project slices can start without hidden setup drift

## Merge intent

- `issue/* -> develop`: implementation complete and proven
- `develop -> release/*`: release candidate stabilization
- `release/* -> main`: approved ship
- `main -> develop`: back-merge after release
- `hotfix/*`: branch from `main`, merge to `main`, then back-merge to `develop`

An issue branch that passed local proof but has not entered `develop` is merge-ready, not complete. Do not start the next issue from it.

## Parallel delivery rule

Independent issues should be implemented in parallel whenever ownership is truly disjoint.

The default autonomous wave shape is scheduling-first: the root checkout stays on `develop`, the main agent coordinates from there, and implementation lanes run in separate worktrees when the environment and project policy permit.

Their merge path should still be controlled:

- parallel implementation
- parallel QA readiness
- queue-managed merge into `develop`

This avoids false confidence from two branches that both passed against different `develop` snapshots.

## Parallel wave record

For multi-issue waves, capture:

- wave id or name
- issue ids
- owned paths or owned areas
- worktree lane or serialization decision
- shared contracts that may force restacking
- proof commands per lane
- queue or restack note for merge
- follow-up scan expectations

Use [PARALLEL-WAVE.template.md](./templates/PARALLEL-WAVE.template.md) when the repo benefits from an explicit wave ledger.

## Compound learning record

For reusable learning, capture a concise `docs/solutions/` note:

- symptom or trigger
- root cause
- durable solution
- failed approaches
- prevention checks
- follow-up issue triggers

Use [compound-learning.md](./references/compound-learning.md) and [SOLUTION.template.md](./templates/SOLUTION.template.md) when the same lesson should help future agents.

## Context compaction rule

Every few autonomous cycles, or whenever the active set feels noisy:

- archive completed issues and superseded brainstorms
- move completed issue, wave, and proof detail out of active files into history
- update the backlog board and current-state pointer
- update the history index
- update wave status and next-lane pointer
- update `docs/solutions/INDEX.md`
- record the next issue, next wave, or concrete no-next-work rationale
- preserve macro direction and micro direction separately

Use [context-governance.md](./references/context-governance.md) when deciding what should be loaded, archived, indexed, or summarized.
