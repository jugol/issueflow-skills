# Automation Governance

Use this when issueflow runs as a recurring or long-running automation.

## Core rule

Pause automations that are waiting for the user. Do not delete them.

Deleting an automation loses its identity, schedule, workspace association, and resume trail. A user-blocked automation should keep those intact so it can continue after the user answers.

## Pause when user input is required

Set the existing automation to `PAUSED` or the platform's equivalent when the run cannot continue without user input, approval, credentials, policy choice, or product direction.

Before pausing, record:

- blocking question or requested user action
- why the automation cannot safely continue
- current issue, wave, branch, or worktree
- latest proof or failure pointer
- resume condition
- next command or workflow step after the user answers

Prefer the repo's current-state pointer or cycle compaction note for this handoff.

## Do not delete by default

Only delete an automation when:

- the user explicitly asks to delete it
- it is a duplicate of another active automation
- its repository or workspace no longer exists
- it is unsafe or misconfigured and cannot be repaired by pausing and updating it
- the project is intentionally shutting down the automation

When deleting, record why deletion is correct and what replaces the automation, if anything.

## Resume behavior

When the user answers, resume the same automation if possible. Before setting it active again:

- update the issue, wave, plan, or decision note with the user's answer
- refresh current-state pointers
- confirm the branch or worktree is still valid
- rerun required context and proof checks before continuing implementation

Do not create a new automation for the same cycle unless the old one is gone, unrecoverable, or intentionally replaced.

## User-facing wording

When stopping to ask, be explicit:

- state the blocker
- ask the smallest useful question
- say the automation has been paused, not deleted
- state what will resume after the answer
