# Test Harness Registry

| Test ID | Layer | Feature/Area | File Path | Trigger Issue | Owner | Status | Notes |
|---|---|---|---|---|---|---|---|
| WEB-SMOKE-001 | smoke | app shell | tests/smoke/app-shell.spec.ts | bootstrap | team | active | |
| WEB-REG-001 | regression | auth login | tests/regression/auth-login.spec.ts | #123 | team | active | |
| APP-GOLDEN-001 | visual | primary button | test/goldens/primary_button_test.dart | #124 | team | active | loads app font set |

## Status values

- `active`
- `flaky`
- `deprecated`
- `replaced`

## Notes

- Every issue that changes behavior should add or update at least one row.
- Prefer behavior or slice names in `Feature/Area` instead of only implementation-layer names.
- If a test is removed, replace the row with a `deprecated` or `replaced` note rather than silently deleting history.
