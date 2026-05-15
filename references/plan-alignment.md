# Plan Alignment

Use this reference when a repository has a long-lived project plan, product brief, or spec that should actively constrain execution.

## Core idea

A plan document is not just bootstrap input. It is a durable source of intent.

If the repo has a file such as:

- `project_plan.md`
- `product_plan.md`
- `SPEC.md`
- a product brief in `docs/`

pick one primary plan anchor and keep checking work against it.

Use [plan-governance.md](./plan-governance.md) when the plan should be created, split, updated, or treated as the product source of truth for user requests and autonomous plan-gap discovery.

## What to extract

Capture these four things in a compact summary:

1. Core product promise
2. Non-negotiable UX, art, or interaction targets
3. MVP boundaries
4. Explicit anti-goals

Example:

- core promise: a usable collaboration tool for planning and tracking work
- non-negotiable target: fast capture, clear ownership, and low-friction review
- MVP boundary: one complete create-to-close workflow, not every reporting view
- anti-goal: do not spend weeks on admin analytics before the primary workflow is usable

## When to re-check the plan

- before the first issue wave
- before each new wave
- after every few completed issues
- before major architecture or tooling expansions
- whenever product output starts feeling unlike the plan

## Issue classification

Classify each issue as:

- `core`: directly advances the main user-facing promise
- `support`: enables a nearby core slice
- `internal`: tooling, QA, admin, or review support
- `deviation`: intentional exploration outside the current plan

Also classify the request's relationship to the plan as `aligned`, `extension`, `conflict`, or `deviation` before dispatch. Extensions and conflicts need a visible plan update or plan-change decision; they should not silently become implementation scope.

This is not bureaucracy. It is a drift detector.

For interactive products, each `core` issue should name the concrete user action or visible state it improves. Examples: creating an item, changing a setting, reviewing a recommendation, completing a checkout step, or understanding an error. If the issue cannot name a user action or product state, it is probably `support` or `internal`.

Prefer shaping `core` issues as vertical slices: one thin path through the needed domain behavior, product surface, and proof. If an issue is intentionally layer-first, name the nearby vertical slice it enables and classify it honestly.

When a plan names a domain concept, do not stop at visual labels. Important nouns in the plan should usually become executable rules, UI affordances, data contracts, and tests. If a user would expect the concept to affect decisions, model that decision pressure in the system.

When a plan names a visual or interaction target, do not treat themed copy as delivery. The issue must prove that the live product surface moved toward that target. For web work, inspect an actual browser screenshot and check whether primary objects, controls, and important state can be understood without reading raw debug text.

When a plan or user feedback concerns screen quality, treat aesthetics and language as product requirements. The live surface should look intentionally designed to a human viewer, and visible text should sound like fluent, common native-language product or story copy. Do not count technically correct but ugly screens, broken-looking images, awkward localization, or stiff translated prose as plan-aligned delivery.

Do not substitute a review dashboard, proof board, or diagnostic table for a user-facing plan promise. If the plan is a consumer app, creative tool, or polished product flow, the active issue should name the first-read experience and visual language it is trying to create. Use [experience-first-ui.md](./experience-first-ui.md) when the implementation keeps drifting toward admin UI.

For reference-driven visual work, preserve the reference grammar as explicit implementation contracts instead of translating it into vague labels. The issue should name the visible traits, states, or variants that matter and prove them in the same surface where users will encounter them.

## Drift signals

Stop and realign if:

- there is no live product surface that resembles the plan
- multiple waves improved proof, review, or admin artifacts but not the primary product
- the current issue cannot point to a plan promise or justified deviation
- the visual or interaction target in the plan is still absent after many completed issues
- completed UI issues keep passing tests while users still describe the screens as ugly, visually confusing, or linguistically unnatural

## Corrective action

When drift is detected:

1. Write down the mismatch plainly.
2. Create a corrective wave that restores alignment.
3. Prioritize at least one `core` issue in that wave.
4. Delay new internal layers unless they unblock the corrective slice directly.

## Practical rule

If a human opened the app today, would they recognize the product promise from the plan?

If the answer is no, the next wave should probably be `core`.
