# Changelog

## Unreleased

- No changes yet.

## 0.3.9 - 2026-07-12

- Compact all skill prompts while preserving delegation, scheduling, planning, proof, merge, and compound hard gates.
- Add prompt-budget validation to prevent skill context from growing past 700 words per skill or 4,500 words across the pack.
- Tighten Codex marketplace metadata with repository links, a composer icon, and schema-compliant starter prompts.

## 0.3.8 - 2026-06-01

- Tighten before-wait `no-candidate` handling so Ready/Active-only scans are invalid and minimum scan sources must be recorded.

## 0.3.7 - 2026-05-19

- Add a before-wait scheduler scan gate so main agents must look for non-overlapping next work before waiting on active workers.
- Require compound cleanup to prune obsolete plan gaps, stale drafts, closed lanes, outdated next actions, and dead follow-up candidates from active context files.
- Add `issueflow parallel` as the short explicit trigger for worker/worktree authorization, while still requiring complex work to attempt parallel shaping before asking for that trigger.

## 0.3.6 - 2026-05-19

- Clarify that the main thread keeps doing read-only scheduler work after worker dispatch and should call `wait_agent` only when blocked.
- Tighten trigger metadata, subagent authorization records, wave direct-implementation exceptions, brainstorm handoff, current-state naming, and active-lane budget controls.

## 0.3.5 - 2026-05-18

- Clarify main-thread delegation as a hard gate before issue code edits, including implementation-skill guards and serialized-vs-delegated wave wording.
- Keep `high` as the default worker effort for scheduling-influencing lanes and add wait-time discovery for next non-overlapping issue candidates.
- Compact high-traffic skill and reference documents so critical routing, planning, dispatch, and merge rules are harder to miss.

## 0.3.4 - 2026-05-18

- Add worker prompt guardrails, default delegated implementation workers to high reasoning effort, and discourage one-issue waves unless explicitly justified.

## 0.3.3 - 2026-05-18

- Clarify that the main agent must scan for non-overlapping lanes and delegate implementation to subagents before doing direct work in autonomous waves.

## 0.3.2 - 2026-05-18

- Add issue sizing and scheduler guidance so autonomous cycles prefer medium vertical-slice issues, wave-first worktree dispatch, and subagent delegation when independent lanes exist.
- Add compound decision fields to issue and PR handoff templates.

## 0.3.1 - 2026-05-17

- Add target user goal experience planning to plan governance, anchors, issue shaping, and intake.
- Add history compaction so `PLAN_ANCHOR.md` and `CURRENT_STATE.md` stay bounded while completed issue detail moves to history.
- Clarify `issue-compound` as the post-completion lifecycle step, with history compaction handled as conditional completion cleanup inside the compound handoff.

## 0.3.0 - 2026-05-17

- Strengthen active clarification rules for imprecise, contradictory, or underspecified user requests.
- Add automation governance so user-blocked automations pause instead of being deleted.
- Add Claude Code plugin and marketplace metadata for dual Codex/Claude distribution.

## 0.2.0 - 2026-05-15

- Add two-track planning with autonomous cycle routing and interactive feature intake.
- Add `issue-brainstorm` and `issue-compound` skills.
- Add autonomous wave generation, interactive brainstorming, compound learning, and routing references.
- Add brainstorm and solution templates, and expand wave/issue templates for origins, worktrees, and follow-up scans.
- Add context governance, current-state, and solution-index guidance to prevent context bloat in long-running projects.
- Add autonomous cycle entry and cycle compaction guidance for macro direction and micro direction.
- Add plan governance for plan-first starts, plan updates, plan gaps, and request-vs-plan conflict handling.

## 0.1.0 - 2026-05-12

- Package issueflow as a Codex plugin.
- Add marketplace metadata for Codex plugin discovery.
- Add validation for skill frontmatter, plugin metadata, marketplace metadata, and local-only content.
- Add GitHub maintenance templates and validation workflow.
- Add release tooling and cross-machine update documentation.
- Tighten issue branch completion rules so resolved issues merge or PR into `develop`, rerun integrated proof, and return checkout to `develop`.
