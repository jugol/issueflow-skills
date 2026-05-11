---
name: repo-bootstrap
description: Apply the issueflow workflow to a concrete repository by scaffolding local-first check entrypoints, issue and PR templates, optional GitHub forms, vertical-slice-oriented issue shaping, and workflow notes that match the shared Git Flow-lite process.
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
- Recommend vertical slice architecture as the default shape for product work
- Make branch lifecycle visible so agents do not keep working on stale issue branches
- Keep the first user-facing screen aligned with the intended experience instead of a proof dashboard
- Make UI-heavy repos judge screens by human aesthetic quality and native-language copy naturalness, not only by functional proof

## What to scaffold

- Issue template or GitHub issue form
- PR template with required core sections
- Local backlog board when GitHub is not attached yet
- Local check entrypoints for the current stack
- Test harness registry
- Branch lifecycle notes or checklist for `develop`, `issue/*`, merge, and return-to-`develop`
- Optional GitHub Actions that call the same local commands
- Stack and repo-topology decision record when the project is still greenfield

## Package resources

Use these package resources when the repo needs more than the core checklist:

- `../../OPERATING-MODEL.md` for the complete workflow model
- `../../references/greenfield-bootstrap.md` for plan-only or empty repos
- `../../references/github-adoption.md` for hosted issue and PR setup
- `../../references/local-backlog-policy.md` for repos without GitHub
- `../../references/local-checks-policy.md` for local proof entrypoints
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

- pick the primary plan anchor file
- extract a compact plan summary or anchor note
- choose and record the first stack decision
- choose and record repo topology
- create the first issue wave from the plan
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
- Plan anchor file and compact summary path, if applicable
- Existing repo commands to reuse
- New local wrapper commands, if needed
- Optional GitHub files to add
- Initial issue wave, if starting from a project plan
- Branch lifecycle expectations for dispatch, merge, and return-to-`develop`
- Vertical slice recommendation or support-first rationale for the first wave
- Experience-first recommendation for the first user-facing UI slice
- Aesthetic and native-language copy review expectations for UI-heavy work
- Follow-up skills to use next
