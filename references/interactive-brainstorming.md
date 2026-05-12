# Interactive Brainstorming

Use this when a user asks for a new feature, major UI change, or ambiguous product behavior.

## Ground first

Before asking questions, inspect likely sources of truth:

- plan anchor or product brief
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

## Keep decisions

Record rejected approaches briefly in the issue or brainstorm note so the next agent does not reopen the same decision without new evidence.
