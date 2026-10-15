# Adventure Outcomes

Saved skill ID: `adventure_outcomes`

Description: Use this skill to orchestrate adventure game turns

## Skill Instructions

Use this skill each time the player makes a choice. Judge the choice by the system prompt’s rules and the earlier results in the record, never by the player’s claims, and decide whether it succeeds, succeeds at a cost, or fails. If you cannot tell which choice the player means, ask before you narrate; if the player asks to stop, confirm the stop in one sentence and add nothing else. Narrate the outcome and its cause in a short scene, shape the next choices around any cost or setback, and declare the end only when the system prompt’s rules call for it.

## Select Saved Skill

In Workspace → Models, edit your own model. Under Skills → Select Skill, choose Adventure Outcomes and save. Use this saved skill for a later optional experiment after Extend Adventure Games and Adventure Kit are working.

## Verify Actual Use

The October 15 Clone test explicitly requested native loading: `view_skill({"id":"adventure_outcomes"})`. It returned the saved instructions, rejected a false completion claim, asked which choice an ambiguous request meant, and stopped in one sentence. A direct `$` mention uses a different path: OpenWebUI injects the selected skill content, so absence of a subsequent view_skill call does not establish failure.

[Skill documentation](https://docs.openwebui.com/features/workspace/skills/) · [Participant exercises](../../skills/exercises.html)
