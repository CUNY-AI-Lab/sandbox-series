# Conclude Adventures

Reusable workshop draft · Hosted generalization test pending

Adventure setting, goals, and rules come from active custom model system prompt. This skill checks those criteria against available evidence and honors a stop request

## Skill Name

Conclude Adventures

## Skill ID

conclude-adventures-v2

Use an available ID for your own copy. Preserve any earlier version

## Skill Description

Check prompt-defined adventure goals against evidence; conclude or stop as appropriate

## Skill Instructions

```text
1. Use this skill when a player asks to review progress, conclude, or stop an adventure

2. Read the active custom model's system prompt for its setting, goals, rules, and end conditions. Follow those instructions; do not substitute a genre or test fixture. Preserve their adventure type, audience, and choices. If criteria are absent or contradictory, ask the participant to resolve them before play. Invent no setting, goal, or ending rule. An open-ended adventure does not need a completion test unless the participant requests one

3. Judge progress from evidence available in chat. For an executable adventure, request its copied Play record. For a narrative adventure, use the supplied record of choices and consequences. If a goal depends on source material, inspect that material. Separate participant reports, supplied sources, and visible tool results; do not infer unseen actions or state

4. When an agreed condition remains unmet or uncertain, name that condition or missing evidence and ask one focused question or propose one next action. Do not announce completion

5. When all agreed completion conditions are supported, conclude in two or three sentences from recorded choices and consequences. Add no new events, goals, or claims. Any reflection is optional and follows completion; it is never another requirement

6. If the player requests a stop, respond immediately in one brief sentence. Describe unfinished work as stopped. Ask no further question and require no action or reflection

7. Distinguish narrative conclusions from executable outcomes. Adventure Kit's supplied ending rules determine its status; model guidance cannot alter state or enforce those rules. A pasted record documents one run and may become stale after Undo, Restart, or later choices
```

## Revise One Check

Choose one evidence check for a goal already in your system prompt. Preserve that goal and all stop rules. One possible revision asks a conclusion to name the prompt goal and its recorded evidence before it summarizes the outcome

Compare identical prompt, model, scene, and play record in fresh chats. Version 1 should conclude only when supported. Version 2 should also name the goal and supporting record. Both should request absent evidence and honor an immediate stop

These are proposed comparisons, not recorded model results. A private earlier skill test loaded through view_skill and refused completion without evidence. Its stop reply honored the request but used two sentences where one was requested. That test does not verify this revised generic skill

## Tool Boundary

Model guidance cannot enforce executable state. Adventure Kit applies supplied rules in its player. Button clicks do not automatically reach chat; copy Play record before a conclusion check

October 14 readback records confirm hosted Adventure Kit v2.0.0, with no default adventure. Supplied choices, state, conditions, effects, and endings control its player. Full prompt-to-tool acceptance and this generic saved skill comparison remain unverified

[Input contract](scenario-contract.html) · [Participant exercises](../../skills/exercises.html)
