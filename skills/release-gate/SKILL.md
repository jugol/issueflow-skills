---
name: release-gate
description: Control promotion from develop to main in a Git Flow-lite issue-driven workflow. Use when bundling completed issues into a release candidate and verifying the integrated state before shipping.
---

# release-gate

This skill governs `develop -> release/* -> main`, or direct `develop -> main` when the project intentionally skips a release branch.

## Preconditions

- Target issues for the release are known
- All included issues are already merged into `develop`
- Integrated baseline on `develop` is green
- Required docs and release notes are ready

## Release checks

- No blocked issue remains in the release set
- Regression suite is green
- High-value smoke paths are green
- Visual baselines are intentionally updated
- Changed user-facing screens still pass a human aesthetic scan, and changed visible copy still sounds natural to a fluent native speaker in the target language
- Changelog or release notes reflect the shipped scope
- The local canonical checks for the repo still pass in the integrated state

If the release bundle came from several independent issue branches, confirm the integrated state after all queue merges rather than relying on each branch's isolated proof alone.

Use `../../OPERATING-MODEL.md` when the project needs the full release, hotfix, or back-merge model.

## Promotion options

- Standard: `develop -> release/<version> -> main`
- Lightweight: `develop -> main` for very small releases with explicit approval

## Required output

- Release set summary
- Integrated proof summary
- Ship or no-ship verdict
- Follow-up or rollback notes

## Hotfix rule

Production fixes branch from `main`, merge back to `main`, then back-merge to `develop` so the integration branch never forgets the fix.
