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

Prefer one or two questions at a time. If several uncertainties block the same decision, group them into one concise question. If the answer can be inferred safely from repo context, infer it and record the assumption.

## Precision check

Actively ask when the user's wording is imprecise enough to change scope, behavior, UX, data, proof, or plan alignment.

Common triggers:

- vague referents such as "this", "that flow", "make it better", or "fix the weird part"
- missing actor, target screen, state, input, or output
- success criteria that could mean different behaviors
- contradictory statements between the request, plan, issue, and current product
- product terms that are not defined in the repo plan or domain model
- broad requests that hide multiple independent issues
- user-visible changes with no audience, copy tone, visual bar, or proof expectation

For each blocking ambiguity, ask a concrete question that names the decision it unlocks. Good questions compare the most likely options instead of asking the user to restate everything.

Examples:

- "Should theme selection be per user account or only local to this browser? That decides whether this issue touches persistence and auth."
- "When you say dashboard, do you mean the operator admin view or the end-user home screen? Those should become separate issues if both change."
- "The plan says onboarding stays single-step, but this request adds a wizard. Should this be a plan change or a deviation?"

Do not proceed to dispatch with hidden assumptions for implementation-critical details. Either get the answer, record an explicit assumption for low-risk details, or return `needs-clarification`.

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
