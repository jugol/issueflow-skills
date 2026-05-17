# Changelog

## Unreleased

- No changes yet.

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
