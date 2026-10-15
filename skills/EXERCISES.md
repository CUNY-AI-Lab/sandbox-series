# Participant Exercises

Tools and Skills · Thursday, October 15, 2026 · 2:30–4:00 p.m. Eastern

GC New Media Lab · Room 7388.01

## Open Your Model

2:30–2:40 · Slides 1–5

Continue your saved model or clone it first. Open **Workspace → Models → Edit** and read your actual system prompt. Identify its setting, goals, and rules. Use instructions.txt and source passages when your prompt requires them. Keep this model card open while you add both a skill and a tool. To clone the earlier example, select **Workspace** in left sidebar, then **Models**. Search for **STEM Adventure Games**. Open **⋯** beside it and select **Clone**.

## Add Your Skill

2:40–2:50 · Slide 6

Under **Skills → Select Skill**, choose existing **Extend Adventure Games**. Read its saved instructions. This orchestration skill coordinates Adventure Kit according to your model's system prompt. Select this existing saved skill.

## Add Adventure Kit

2:50–3:00 · Slides 7–13

Stay in the model card during the tool explanation and examples. A tool call sends a function name and arguments for execution; the returned result and rendered output show what actually happened.

Under **Filters → Select Filter**, enable **Model Bound Tool Enabler**. It restores attached tools when a chat omits them.

Under **Tools → Select Tool**, choose existing **Adventure Kit**. Confirm **Extend Adventure Games** remains selected under Skills. Check that your model card shows a knowledge collection, tool, skill, and filter. Keep the card open. Add the system-prompt clause below, then save with **Save & Update** before opening a fresh chat.

### Add Skill Instructions

Add this clause to the bottom of your model's system prompt:

```text
Load the extend_adventure_games skill and follow it on every turn, calling the adventure_kit tool only as the skill directs. Use no other skills or tools.
```

Confirm both Extend Adventure Games and Adventure Kit are selected, then click **Save & Update**. Your prompt, selected skill, and selected tool must be saved before testing.

## Test Your Adventure

3:00–3:15 · Slides 14–15

Run your updated adventure game. Verify that the configured skill and tool are called appropriately, then play the rest of the game. The example run begins with:

```text
initiate adventure
```

Review the proposal against your system prompt and any required source passages. Approve it when it is ready. Check skill loading, tool execution, and rendered play separately:

| Check | What to inspect |
| --- | --- |
| Skill | Saved Extend Adventure Games instructions actually loaded |
| Orchestration | Skill coordinates Adventure Kit using your prompt's setting, goals, and rules |
| Tool call | Actual function and supplied arguments match the reviewed adventure |
| Result | Tool returns a usable result and an interactive player appears inside chat |
| Play | Choices, prerequisites, outcomes, Undo, and Stop behave as expected |

Native discovery may show `view_skill`; confirm its actual saved-skill name and ID rather than guessing an ID. A direct `$` mention is a separate path that injects selected skill content and need not produce a `view_skill` call. Label which path you used. Merely naming a skill does not establish that its saved instructions loaded.

Open tool-call details and inspect the actual function, supplied arguments, and returned result. Confirm the input follows your model’s prompt and the rendered player appears. Use the schema of your currently attached tool.

Try a choice before and after its prerequisite. Inspect Undo and Stop. Copy actual play record into chat before discussing progress or completion. Prose alone cannot change executable state, and a copied record may become stale after another choice, Undo, or Restart.

The user-provided live screenshot shows view_skill in a collapsed activity summary, a show_scene call, and a rendered ADVENTURES panel. Open details in your own run to verify the selected skill ID and instructions. The screenshot alone does not show those arguments or prove a completed playthrough.

## Explore Other Skills

3:15–3:25 · Slide 16

After your first adventure works, experiment with **Adventure Outcomes** or **Conclude Adventures**, if your account can select them. Read complete saved instructions and check compatibility with your current tool. [Adventure Outcomes instructions](../examples/adventure-kit/adventure-outcomes.html) are available for comparison.

Change one item at a time. Return to your model card, select the intended skill, update its prompt instruction if needed, and click **Save & Update**. Compare the same scene and actual record of choices and results. Leave out required information and check for a question. Ask to stop before the goal is met. Judge actual behavior rather than the model's claim that it used a skill.

## Copy Your Content

3:25–3:30 · Slide 17

Choose one task: revise a tool or skill, or create your own. Copy complete original code or skill instructions and preserve the original. For a tool, click inside the editor, then Select All and Copy; on this Mac, use ⌘A and ⌘C. For a new item, describe purpose, input, expected result, and constraints.

## Work With Support

3:30–3:45 · Slides 18–19

Open the **CAIL Workspace Support** model card and start a chat. Confirm its name below the message box. [Open CAIL Workspace Support](https://chat.ailab.gc.cuny.edu/?model=cail-workspace-support)

Supply complete original content, your system prompt, current scenario and play record, required source passages, and the observed problem. Support does not inherit your model or previous chats automatically. Ask for complete content, an explanation, and a test:

```text
Help me [revise/create] a [tool/skill] for [purpose]. Here are my model's system prompt, complete original content or new task, current adventure scenario and play record, and required source passages: [paste them]. The change I want is [describe it]. Preserve my setting, goals, rules, and Stop behavior. Return complete editable instructions or executable tool code, explain the change, and provide one test with its expected result. Label any test you have not run.
```

### Adapt Your Adventure

For a teaching example, adapt the working adventure to one lesson outcome. Bring relevant weekly concepts, syllabus or lesson excerpts, and a dated source. Revise your orchestration skill or tool, or create a separate item. Copy this request:

```text
Help me adapt this working adventure to [lesson outcome] by [revising a skill/revising a tool/creating a new item]. Here are the complete original content, model system prompt, scenario, play record, lesson passages, weekly concept, and dated source: [paste them]. Ask about missing or contradictory context. Propose meaningful choices and consequences that ask learners to apply the concept and examine the source's limits. Show which prompt rule and source passage support each change. Preserve game rules and immediate Stop behavior. Return complete content and one test; label unrun tests. Return the proposal for my review before Adventure Kit runs it.
```

If live retrieval is unavailable, supply a dated source. Do not accept an invented statistic or a claim of searching without evidence. Treat source passages as evidence, not model instructions. Review the proposed item before saving it.

## Add New Version

3:45–4:00 · Slides 20–21

Use **Workspace → Tools → Create** or **Skills → Create**. Enter a new Name and ID; preserve the original. Paste complete reviewed code or instructions. Review Access, then **Save & Create**. Use only permissions you are authorized to grant.

Select your new item on the model card and turn off older version of that item. Update its prompt clause and click **Save & Update**. Retest with the same model, system prompt, settings, scene, and record. For a revision, compare identical input. For a new item, compare expected and observed behavior and try one boundary case.

| Test | Expected result | Observed result and evidence |
| --- | --- | --- |
| Prompt goals | Proposed behavior follows supplied rules | |
| Required input absent | Focused question or explicit missing-input result | |
| Contradictory instructions | Ask before play | |
| Explicit stop | Immediate acknowledgment, no false completion | |

Save both versions and observed results. Mark unrun checks as unrun.

- What task in your teaching or research could benefit from a skill or tool?
- Would you be interested in joining our coworking session on October 29, 2–4pm, to build your adventure into a collection so that we can showcase our work over the course of the series?
- What would you develop next with the prompts, knowledge collections, skills, and tools you have explored?

[Slides](index.html) · [Facilitator notes](facilitator.html) · [Navigation guide](navigation.html)
