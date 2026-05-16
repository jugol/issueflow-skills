---
name: repo-bootstrap
description: Apply the issueflow workflow to a concrete repository by scaffolding plan governance, local-first check entrypoints, issue and PR templates, optional GitHub forms, vertical-slice-oriented issue shaping, and workflow notes that match the shared Git Flow-lite process.
---

# repo-bootstrap

This skill takes the shared pack and adapts it to a real repository.

## Goals

- Make the workflow easy to follow in a specific repo
- Keep local verification as the canonical truth
- Add GitHub integration naturally when the repo uses GitHub
- Avoid hard-coding one stack's commands into every project
- Convert a product plan or rough project brief into the first executable issue wave
- Preserve the original product direction while the repo grows
- Establish plan governance so product docs stay synchronized with implementation
- Recommend vertical slice architecture as the default shape for product work
- Make branch lifecycle visible so agents do not keep working on stale issue branches
- Keep the first user-facing screen aligned with the intended experience instead of a proof dashboard
- Make UI-heavy repos judge screens by human aesthetic quality and native-language copy naturalness, not only by functional proof

## What to scaffold

- Issue template or GitHub issue form
- PR template with required core sections
- Local backlog board when GitHub is not attached yet
- Current-state pointer so agents do not scan the entire backlog by default
- Cycle compaction note template or location for long-running automation
- Automation pause policy for user-blocked runs
- Local check entrypoints for the current stack
- Test harness registry
- Brainstorm and wave note locations for durable planning
- `docs/plan/` or equivalent plan governance location when the repo has durable product intent
- Primary plan, compact plan anchor, roadmap, decision log, and optional area-plan locations
- `docs/solutions/` or equivalent solution-note directory for compound learning
- `docs/solutions/INDEX.md` or equivalent solution index for index-first reading
- Branch lifecycle notes or checklist for `develop`, `issue/*`, merge, and return-to-`develop`
- Worktree ignore policy such as `.worktrees/` when the repo will use local parallelism
- Optional GitHub Actions that call the same local commands
- Stack and repo-topology decision record when the project is still greenfield

## Package resources

Use these package resources when the repo needs more than the core checklist:

- `../../OPERATING-MODEL.md` for the complete workflow model
- `../../references/greenfield-bootstrap.md` for plan-only or empty repos
- `../../references/plan-governance.md` for plan-first starts, plan changes, plan gaps, and plan splitting
- `../../references/github-adoption.md` for hosted issue and PR setup
- `../../references/local-backlog-policy.md` for repos without GitHub
- `../../references/local-checks-policy.md` for local proof entrypoints
- `../../references/two-track-routing.md` for autonomous cycle vs interactive intake routing
- `../../references/interactive-brainstorming.md` for feature-request clarification
- `../../references/autonomous-wave-generation.md` for issue fan-out and waves
- `../../references/automation-governance.md` for pause-vs-delete behavior in long-running automations
- `../../references/compound-learning.md` for `docs/solutions/` notes
- `../../references/context-governance.md` for active-set, archive, and compaction rules
- `../../references/pr-template-policy.md` for PR proof sections
- `../../references/stack-selection.md` for early stack decisions
- `../../references/harness-governance.md` for durable test registry policy
- `../../templates/` for reusable issue, PR, backlog, plan, harness, and local-check scaffolds

## Local-first rule

If the repo already has stable local commands like `npm run test`, `pnpm test`, or `flutter test`, reuse them.

If it does not, create a thin local wrapper script rather than teaching contributors to copy-paste long command lists.

Wrapper scripts should be:

- cwd-robust
- platform-aware
- as direct as possible for simple validation tasks

Do not add package-manager indirection for checks that can be expressed as one deterministic script call.

## GitHub rule

If the repo uses GitHub, recommend:

- issue forms
- PR template
- branch protection on `develop` and `main`
- required checks that mirror the local commands
- PR or merge process that returns the working checkout to `develop` before the next issue starts

If the repo does not use GitHub, keep the same issue and proof structure in local files.

## Greenfield rule

If the project begins with only a plan document:

- pick or create the primary plan file, preferably `docs/plan/PLAN.md` when the repo has no stronger convention
- extract a compact plan summary or anchor note
- create or identify `docs/plan/PLAN_ANCHOR.md` as the first context file agents read
- create `docs/plan/DECISIONS.md` and `docs/plan/ROADMAP.md` when sequencing or plan-change history will matter
- defer `docs/plan/areas/` until the plan has distinct areas or becomes expensive to scan
- choose and record the first stack decision
- choose and record repo topology
- create the first issue or wave from unimplemented plan gaps
- create a durable brainstorm or strategy note when the plan leaves major product choices open
- create a current-state note that points to the active issue, current wave, and plan anchor summary
- create a cycle compaction location or note that records macro direction, micro direction, archive moves, and next cycle decision
- create a local proof entrypoint before starting product code
- record the branch lifecycle rule before the first issue branch is created
- make the first product issue a thin vertical slice whenever possible
- capture a compact UX or visual direction before scaffolding UI-heavy work

The anchor summary should capture at least:

- core product promise
- non-negotiable UX or art targets
- target-language copy tone and native-language naturalness requirements
- first-viewport or primary-action experience
- MVP boundaries
- explicit anti-goals or "not this" constraints

When creating the first issue wave, tag each issue mentally or explicitly as `core`, `support`, `internal`, or `deviation`.

If a later user request extends or conflicts with the plan, route it through plan governance before dispatch: update `PLAN.md`, add a `DECISIONS.md` entry, or create a plan-change note, then raise implementation issues.

For `core` issues, prefer vertical slices that expose one user-facing behavior through the needed domain, UI, and proof path. For `support` or `contract-first` issues, name the downstream core slice they unblock.

For UI-heavy plans, make the first product slice experience-first. Do not use a dashboard, proof board, setup console, or admin shell as the default first screen unless the plan explicitly asks for that kind of product. The first slice should also name what makes the screen aesthetically acceptable and what makes its visible copy sound native in the target language.

Do not let a greenfield repo spend multiple waves on internal proof layers while the core product promise is still absent.

## PR template rule

Keep the core required sections stable across projects:

- summary
- linked issue
- scope
- proof
- risk review
- docs

Project-specific sections may be appended below the core. Do not let custom sections replace the core proof structure.

## Output

- Files to scaffold
- Plan governance structure, primary plan file, compact summary path, roadmap or decision-log paths, if applicable
- Existing repo commands to reuse
- New local wrapper commands, if needed
- Optional GitHub files to add
- Initial issue wave, if starting from a project plan
- Brainstorm, wave, and solution-note locations
- Current-state pointer and context-governance expectations
- Cycle compaction trigger and artifact location
- Automation pause policy and resume handoff location
- Branch lifecycle expectations for dispatch, merge, and return-to-`develop`
- Worktree policy and default local worktree path, if parallel issue delivery is expected
- Vertical slice recommendation or support-first rationale for the first wave
- Experience-first recommendation for the first user-facing UI slice
- Aesthetic and native-language copy review expectations for UI-heavy work
- Follow-up skills to use next
