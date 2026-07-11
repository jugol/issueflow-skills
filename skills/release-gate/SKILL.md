---
name: release-gate
description: Approve or block promotion from develop to main after integrated release proof. Use to bundle completed issues, validate the release candidate, and record ship, rollback, or hotfix decisions.
---

# release-gate

Govern `develop -> release/* -> main`, or approved direct `develop -> main` for a small release.

## Gate

- Release set is known, merged into green `develop`, and free of blocked issues.
- Integrated regression and high-value smoke paths pass; do not rely only on isolated branch proof.
- Visual baselines are intentional; changed UI/copy passes human aesthetic and target-language review.
- Canonical local checks, docs, changelog/release notes, risk, and rollback are ready.

Return release summary, integrated proof, `ship` or `no-ship`, and follow-up/rollback notes.

Production hotfixes branch from `main`, merge to `main`, then back-merge to `develop`. Load `../../OPERATING-MODEL.md` only when the full release/hotfix model is needed.
