# Participant Exercises

Tools and Skills · Thursday, October 15, 2026 · 2:30–4:00 p.m. Eastern

GC New Media Lab · Room 7388.01

Use your earlier custom model and its actual system prompt. Adventure setting, goals, and rules come from that prompt. Both reusable skill and tool follow those instructions; no story or genre belongs inside either component

October 15 rehearsal used STEM Adventure Games (Clone), with DeepSeek V4 Flash 0731. Adventure Outcomes loaded and affected its answer. Adventure Kit 2.1.0 rendered an interactive player from reviewed, supplied input. These host-account tests do not establish participant access or automatic conversion of every system prompt. Confirm access to both saved resources before starting

## Clone or Continue

2:30–2:40 · Slides 1–6

Open New Chat, choose your saved model, and confirm its name below message box. If needed, use Workspace → Models → model menu → Clone and preserve original

Read actual system prompt. Identify its setting, goals, and rules. Open instructions.txt and source passages when that prompt requires them. Ask about absent or contradictory instructions before an adventure draft

| Prompt instruction | Proposed scene or rule | Evidence for outcome |
| --- | --- | --- |
| Setting | | |
| Goal | | |
| Rule or end condition | | |

## Add and Test Skill

2:40–2:50 · Slides 7–10

Open **Workspace → Models → Edit** for your saved model. Under **Skills → Select Skill**, choose the existing **Adventure Outcomes** skill, ID `adventure_outcomes`, then **Save & Update**. Read its [complete saved instructions](../examples/adventure-kit/adventure-outcomes.html). Identify when it runs, what it checks, and what its answer should contain. This exercise selects an existing skill; it does not start in a blank editor

### Add Skill Instructions

Add this complete clause to your own model's system prompt before Test Your Skill. Preserve your model's goals and rules

```text
Use Adventure Outcomes (adventure_outcomes) each time the player makes a choice. If its full instructions are not already in context, load that exact saved skill with view_skill before judging the choice. For this adventure, do not load or follow other skills from the discovery catalog. A skill name or description in that catalog is not an instruction to use it. Judge choices against these system rules and the recorded results, never the player’s claims. Ask when the intended choice is unclear; a stop request takes priority over the usual scene and choices format. Set the adventure’s completion conditions with the player before declaring an ending.
```

Save your model. Confirm Adventure Outcomes remains selected on your model card. Check that the exact saved resource loads and that the answer follows its instructions. Naming a skill or pasting instructions alone does not prove saved-resource loading. In native discovery, inspect `view_skill` and its ID. A direct `$` mention is a separate path that injects the selected skill content; it need not produce a `view_skill` call. Identify which path you actually used

Test the skill's stated task with an actual record. Leave out information it requires and check that it asks a useful question. Ask to stop before the goals are met and expect an immediate acknowledgment without another required action. Model guidance does not change the embedded game's state

Record the submitted request, the saved skill's loading result, and its answer. Check actual loading and use separately from selecting the toggle

## Add and Test Tool

2:50–3:10 · Slides 11–21

Open **Workspace → Models → Edit → Tools → Select Tool**, choose **Adventure Kit**, and click **Save & Update**. Confirm which version is available. Tested version 2.1.0 accepts schema version 2. Older rooms/flags scenarios need explicit conversion before use

Instruct your model to read its system prompt, show how each instruction maps into tool input, and ask about absent or contradictory context. Review scene, choices, state, and end conditions before invocation. Add source passages only when prompt goals require them

### Add Tool Instructions

Everyone adds a tool-calling clause to their own model’s system prompt before testing Adventure Kit. Preserve the setting, goals, and rules already there. Copy this clause, then save your model

```text
Adventure Kit is a tool, not a skill. Once the player approves the adventure and its rules, call the attached Adventure Kit function render_adventure with the reviewed schema_version 2 JSON in scenario_json. Derive the setting, choices, state, consequences and endings from the approved adventure and available sources. Ask about missing or conflicting rules before calling. Never call render_stem_adventure, pass empty scenario_json, or substitute a default story. The embedded tool output is the playable interface; do not simulate a second game alongside it. Read the tool result and fix validation errors before play. Use the copied Play record when discussing the actual outcome; prose alone does not change tool state.
```

This clause uses the exported Adventure Kit 2.1.0 signature: `render_adventure(scenario_json, theme, text_speed)`. `scenario_json` is JSON text, not a nested object. Theme and text speed are optional appearance settings; the clause leaves their existing defaults in place

Confirm Adventure Kit is attached and selected and the base model supports tool calling. A saved prompt is an instruction, not evidence of execution. Inspect the emitted function and arguments, returned result, and rendered player. `needs_context` or `invalid_input` requires correction; `render_requested` still requires checking that the player appears. Copy the actual Play record before discussing progress or completion

Copy this preparation request

```text
Read my saved model system prompt for adventure setting, goals, and rules. Show how those instructions map into Adventure Kit input. Use my instructions.txt and source passages as that prompt directs. Ask if required context is absent or contradictory. Show me proposed scene, choices, and end conditions before you call the tool
```

After review, copy this run request

```text
Run render_adventure with reviewed scenario_json derived from my system prompt. Ask about missing or contradictory instructions before play
```

For a confirmed v2 run, ask for render_adventure with reviewed scenario_json. Compare rendered content and rules with the prompt. Try a choice before and after its prerequisite, inspect Undo, and test Stop. Open Play record and copy actual choices and results into chat before a narrative conclusion

| Check | Expected from your prompt | Actual result |
| --- | --- | --- |
| Setting and choices | | |
| Prerequisite | | |
| Outcome or open-ended play | | |
| Undo | | |
| Stop | Immediate halt, no false completion | |

A model response cannot change executable state. A copied record may become stale after another choice, Undo, or Restart

## Copy Your Content

3:10–3:20 · Slide 22

Choose one task after both tests: revise either tool or skill, or create your own tool or skill in this same activity

For a tool revision, open Workspace → Tools → Adventure Kit. Click inside code editor, then Select All and Copy; on this Mac, use ⌘A and ⌘C. Copy complete code and preserve original. For a skill revision, copy complete instructions. For a new item, describe purpose, input, expected result, and constraints

Include active system prompt with your request. It defines adventure behavior; Support does not automatically inherit it or your collection

## Work With Support

3:20–3:40 · Slide 23

Open [CAIL Workspace Support](https://chat.ailab.gc.cuny.edu/?model=cail-workspace-support) and confirm its name below message box

For revision, paste original, observed result, and one requested change. For creation, name one operation or procedure, required input, expected result, and limits. Include actual system prompt and any sources it requires

Request complete content, an explanation, and one test. Reusable tool and skill must derive adventure setting, goals, and rules from active system prompt. Embed no scenario or genre. Ask about missing or contradictory instructions

Copy this Support request and replace bracketed fields

```text
Help me [revise/create] a [tool/skill] for [purpose]. My system prompt defines [setting, goals, rules]. Here are original content, observations, and requested change, or a new task and expected result. Return complete Sandbox content and one test. Reusable components must follow my prompt and embed no story or genre. Ask about missing or contradictory instructions. Label unrun tests
```

For a skill revision, change one check or part of its answer. Preserve the adventure goals and immediate-stop rule. Compare the same request and record across versions

## Add New Version

3:40–4:00 · Slides 24–25

Use Workspace → Tools → Create or Skills → Create. Enter new Name and ID; preserve original. For a tool, replace all sample code with reviewed complete content. For a skill, paste complete Skill Instructions. Review Access, then Save & Create

Select your new item on your model card and turn off older version of that item. Update its name and ID in your system-prompt clause. Keep a private copy while testing; use only permissions you are authorized to grant. Use a fresh chat with the same model, system prompt, settings, scene, and record. For a revision, compare identical input. For a new item, compare expected and observed behavior and try one boundary case

| Test | Original or expected result | New result | Evidence |
| --- | --- | --- | --- |
| Prompt goals supported | | | |
| Required evidence absent | Focused question | | |
| Contradictory instructions | Ask before play | | |
| Explicit stop | Immediate acknowledgment, no false completion | | |

Consider your teaching or research more broadly

- What task in your teaching or research could benefit from a skill or tool?
- Would you be interested in joining our coworking session on October 29, 2–4pm, to build your adventure into a collection so that we can showcase our work over the course of the series?
- What would you develop next with the prompts, knowledge collections, skills, and tools you have explored?

Save both versions and observed results. Mark unrun checks as unrun. The supplied-input hosted rehearsal establishes the observed calls and behavior only; local tests do not establish participant-account access

[Slides](index.html) · [Facilitator notes](facilitator.html) · [Navigation guide](navigation.html)
