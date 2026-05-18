# Autonomous Wave Generation

Use this when issueflow is continuing an automated cycle, processing feedback, or deciding what to do after a merge.

## Signals to scan

- plan anchor drift or missing core promise
- missing or stale target user goal experience
- unimplemented plan gaps from the compact plan anchor or relevant area plan
- active backlog and stale issues
- failing tests or flaky proof
- review comments and QA findings
- playtest or user feedback batches
- recent merge-gate handoff notes
- `docs/solutions/` prevention rules and future issue triggers

## Candidate rules

Create candidate issues when the signal names a concrete behavior, target experience gap, defect, prevention rule, product gap, or proof gap.

If a plan gap is promised in `PLAN.md` or an area plan but absent from the live product or harness, treat it as a first-class autonomous candidate.

Do not create an issue for vague discomfort unless it can be turned into:

- a user-visible outcome
- a support/contract slice with a downstream consumer
- a durable proof improvement
- a named investigation with a success criterion

Avoid atomized candidates. Combine tiny findings that share the same user outcome, ownership lane, and proof command into one medium issue.

## Fan-out rule

Make multiple issues when findings differ by:

- user-visible behavior
- ownership lane or package
- proof command
- dependency order
- risk or rollout path

Make one issue when the work is one inseparable vertical slice.

## Wave rule

Use a wave when two or more issues can be planned together. In autonomous cycles, this is the preferred path when independent lanes exist; do not default to a single serial issue if a small wave is available.

Do not create a one-issue wave by default. If only one candidate exists after scanning, treat it as a single issue or record why no additional safe lane exists.

A useful wave usually has two to five active lanes. Larger candidate batches should be grouped by dependency, package, milestone, or user goal; keep overflow candidates drafted until active-lane budget and merge order are clear.

A wave should record:

- goal
- issue list and origin
- ownership lanes
- worktree plan
- dependencies and restack triggers
- proof commands
- merge order
- follow-up scan expectations

Default to at least one `core` issue. Allow internal-only waves only with an explicit stabilization reason.

## Scheduler rule

For a wave, the main agent should first ask which issues can run without overlap, then create as many safe lanes as practical and schedule them instead of serially implementing one lane while other independent lanes remain undispatched.

While scheduled workers are running, use the wait time for read-only discovery of the next non-overlapping issue candidates. Do not dispatch or edit overlapping work until active lane results and merge order are clear, and do not add workers past the active-lane budget. Use `wait_agent` only after safe scheduler work is exhausted or blocked.

Use [issue-sizing-and-scheduling.md](./issue-sizing-and-scheduling.md) when deciding whether to combine tiny candidates, split oversized work, or delegate multiple lanes.
