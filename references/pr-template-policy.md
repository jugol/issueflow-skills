# PR Template Policy

PR templates should be partly fixed and partly flexible.

## Fixed core

These sections should stay stable across projects because the workflow depends on them:

- Summary
- Linked Issue
- Scope
- Proof
- Risk Review
- Docs

## Flexible extension

Projects may append custom sections after the core:

- rollout plan
- screenshots gallery
- database migration notes
- analytics impact
- API compatibility notes

## Recommendation

Do not let projects replace the core with a fully custom PR template. That weakens merge-gate consistency.

The right model is:

- enforce the core
- allow project-specific appendices
