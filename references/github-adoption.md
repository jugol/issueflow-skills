# GitHub Adoption

GitHub is recommended, not mandatory.

## Why recommend GitHub

- Durable issue IDs
- PR linkage to issues
- Review history
- Branch protection
- Required checks
- Release notes and milestones if the team wants them

## What to add when GitHub is available

- `.github/ISSUE_TEMPLATE/` form or templates
- `.github/PULL_REQUEST_TEMPLATE.md`
- Optional workflow that calls the repo's local check entrypoint
- Branch protection for `develop` and `main`

## What not to do

- Do not invent CI-only commands that contributors cannot run locally
- Do not make hosted checks the only way to know whether the branch is healthy
- Do not force GitHub-only workflow wording into non-GitHub repos

## Recommended rule

Treat GitHub as the collaboration and audit layer, while the repository's own scripts and commands remain the execution layer.
