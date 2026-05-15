# Interactive Brainstorming

Use this when a user asks for a new feature, major UI change, or ambiguous product behavior.

## Ground first

Before asking questions, inspect likely sources of truth:

- plan anchor or product brief
- relevant `docs/plan/` file if the repo uses plan governance
- backlog and active issues
- related screens, routes, tests, schemas, or fixtures
- existing design and copy patterns

## Ask narrowly

Ask only questions that change the implementation direction:

- user/audience and primary job
- first visible action or state
- acceptance criteria and non-goals
- data ownership or persistence
- proof surface and local commands
- rollout or compatibility constraints

Prefer one or two questions at a time. If the answer can be inferred safely from repo context, infer it and record the assumption.

## Offer approaches

When multiple paths are viable, present two or three options:

- smallest vertical slice
- richer product slice
- support-first or contract-first path

Name the tradeoff and recommend one. After the user accepts or adjusts the direction, hand off to `issue-raise`.

## Plan relationship

Classify the request before issue creation:

- `aligned`: implements the current plan
- `extension`: adds compatible scope that should be written into the plan
- `conflict`: changes existing plan direction and needs an approved plan-change decision
- `deviation`: intentional exploration outside the plan

Do not dispatch implementation for `extension` or `conflict` work until the required plan update or decision note is recorded.

## Keep decisions

Record rejected approaches briefly in the issue or brainstorm note so the next agent does not reopen the same decision without new evidence.
