# Contract Naming

Shared intermediate contracts should be named for their role, not for a vague container metaphor.

## Core rule

A good shared contract name answers three questions at a glance:

- what domain slice it belongs to
- what workflow stage it represents
- what job the data shape does

Prefer:

- `archive-review-summary`
- `retention-decision-note`
- `review-checkpoint`
- `release-handoff`

Avoid:

- `archive-envelope`
- `review-thing`
- `output-bundle`

## Naming heuristics

- Prefer role nouns such as `summary`, `state`, `report`, `receipt`, `manifest`, `ledger`, `checkpoint`, or `note` when they match the shape.
- Use packaging nouns such as `bundle`, `packet`, or `pack` only when the packaging itself is the important idea.
- If the same concept can be described without metaphor, prefer the non-metaphorical name.
- Keep the same stage name across shared, backend, frontend, admin, and docs instead of inventing synonyms.
- If a consumer surface renders a shared contract directly, keep the surface naming close to the contract name.
- When turning review evidence into prep checklists, name the new contract for its attention/checklist job and keep success/failure language conditional until a later result-scoped contract resolves it.

## Builder and serializer rule

- Contract: `EncounterArchiveReviewSummary`
- Builder: `buildEncounterArchiveReviewSummary`
- Serializer: `serializeEncounterArchiveReviewSummary`

Builders and serializers should mirror the contract name exactly.

## Intermediate data rule

For internal intermediate data, optimize for scanability over cleverness.

- Someone should understand the identifier without reading the whole file.
- If the name needs a paragraph to explain, rename it.
- If the container metaphor is not the important part, use a role name instead.

## Escalation rule

When a new shared seam appears, pause and name it deliberately before downstream packages depend on it.
