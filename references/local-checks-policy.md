# Local Checks Policy

Local checks are the canonical proof entrypoints for the repository.

## Why

- They are cheap to run during iteration
- They reduce dependency on hosted CI minutes
- They let humans and AI agents validate changes before opening a PR
- They keep CI honest by mirroring the same commands

## Good shape

- `npm run test`
- `npm run check`
- `pnpm test`
- `flutter test`
- `dart test`
- `scripts/check-local.sh`
- `scripts/check-local.ps1`

## Recommended layering

- Fast checks: lint, typecheck, smoke, focused tests
- Full checks: full regression, integration, visual, performance where applicable

Package-local entrypoints are encouraged when the repo has multiple apps or services. A root wrapper can compose them, but each package should still be able to prove its own health directly.

## Policy

- The repo should expose one obvious local command path
- PRs should report which local commands passed
- Hosted workflows should call the same local commands where practical
- If stack-specific commands differ across packages, add a wrapper script
- In monorepos, each package or service should also expose its own proof command so issue branches can validate just their lane during iteration

## Wrapper design notes

- Wrapper scripts should not depend on a specific current working directory when they can avoid it
- Prefer direct script execution for simple validation tasks
- Use package-manager commands when they are the real canonical test entrypoint for that package, not just out of habit
- For schema-heavy work, prefer `schema + sample fixture + validator test` over prose-only definitions
- Treat edits to root wrappers, root registries, or proof manifests as shared-contract changes that may force merge restacking for other in-flight branches
