# Participant Exercises

Tools and Skills · Thursday, October 15, 2026 · 2:30–4:00 p.m. Eastern

GC New Media Lab · Room 7388.01

Use your earlier custom model and its actual system prompt. Adventure setting, goals, and rules come from that prompt. Both reusable skill and tool follow those instructions; no story or genre belongs inside either component

Preparation records: Adventure Kit 2.0.0 save and readback were recorded October 14. Generic skill loading and prompt-to-tool acceptance against the standard STEM configuration remain unverified. Participant access also remains unverified; inspect available version and permissions before class

## Clone or Continue

2:30–2:40 · Slides 1–3

Open New Chat, choose your saved model, and confirm its name below message box. If needed, use Workspace → Models → model menu → Clone and preserve original

Read actual system prompt. Identify its setting, goals, and rules. Open instructions.txt and source passages when that prompt requires them. Ask about absent or contradictory instructions before an adventure draft

| Prompt instruction | Proposed scene or rule | Evidence for outcome |
| --- | --- | --- |
| Setting | | |
| Goal | | |
| Rule or end condition | | |

## Add and Test Skill

2:40–2:50 · Slides 4–5

Read [Conclude Adventures](../examples/adventure-kit/conclude-adventure.html). Identify Trigger, Procedure, and Format. Its procedure reads goals from active system prompt rather than imposing one goal on every adventure

Open Workspace → Skills → Create. Enter your own Skill Name, Skill ID, Description, and complete Skill Instructions. Review Access, then Save & Create. Open New Chat with your saved model and select your copy through Integrations → Skills

Use actual prompt and observed play record for a completion check. Withhold evidence required by one prompt goal and check for a focused question. Ask to stop with unfinished goals and expect one brief acknowledgment with no completion claim or compulsory reflection. When no record exists, test absent evidence and stop only

Record whether saved skill loaded. Pasted instructions test prose guidance; they do not prove a saved resource loaded

## Add and Test Tool

2:50–3:10 · Slides 6–9

Open Integrations → Tools, search Adventure Kit, and select its toggle. Confirm which version is available. Version 2 requires completed schema version 2. Older rooms/flags scenarios need explicit conversion before use

Ask model to read its system prompt, show how each instruction maps into tool input, and ask about absent or contradictory context. Review scene, choices, state, and end conditions before invocation. Add source passages only when prompt goals require them

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

3:10–3:20 · Slide 10

Choose one task after both tests: revise either tool or skill, or create your own tool or skill in this same activity

For a tool revision, open Workspace → Tools → Adventure Kit. Click inside code editor, then Select All and Copy; on this Mac, use ⌘A and ⌘C. Copy complete code and preserve original. For a skill revision, copy complete instructions. For a new item, describe purpose, input, expected result, and constraints

Include active system prompt with your request. It defines adventure behavior; Support does not automatically inherit it or your collection

## Work With Support

3:20–3:40 · Slide 11

Open [CAIL Workspace Support](https://chat.ailab.gc.cuny.edu/?model=cail-workspace-support) and confirm its name below message box

For revision, paste original, observed result, and one requested change. For creation, name one operation or procedure, required input, expected result, and limits. Include actual system prompt and any sources it requires

Request complete content, an explanation, and one test. Reusable tool and skill must derive adventure setting, goals, and rules from active system prompt. Embed no scenario or genre. Ask about missing or contradictory instructions

Copy this Support request and replace bracketed fields

```text
Help me [revise/create] a [tool/skill] for [purpose]. My system prompt defines [setting, goals, rules]. Here are original content, observations, and requested change, or a new task and expected result. Return complete Sandbox content and one test. Reusable components must follow my prompt and embed no story or genre. Ask about missing or contradictory instructions. Label unrun tests
```

One possible skill revision asks a conclusion to name each prompt goal and its recorded evidence. Preserve goals and immediate-stop rules. Compare identical prompt and record across versions. This changes an evidence check rather than inventing a new adventure goal

## Add New Version

3:40–4:00 · Slides 12–13

Use Workspace → Tools → Create or Skills → Create. Enter new Name and ID; preserve original. For a tool, replace all sample code with reviewed complete content. For a skill, paste complete Skill Instructions. Review Access, then Save & Create

Select your new item through Integrations and turn off older version of that item. Use a fresh chat with the same model, system prompt, settings, scene, and record. For a revision, compare identical input. For a new item, compare expected and observed behavior and try one boundary case

| Test | Original or expected result | New result | Evidence |
| --- | --- | --- | --- |
| Prompt goals supported | | | |
| Required evidence absent | Focused question | | |
| Contradictory instructions | Ask before play | | |
| Explicit stop | Immediate acknowledgment, no false completion | | |

Consider your teaching or research more broadly

- What task in your teaching or research could benefit from a skill or tool?
- Across the series, how has your approach to custom models changed?
- What would you develop next with the prompts, knowledge collections, skills, and tools you have explored?

Save both versions and observed results. Mark unrun checks as unrun. Current local engine tests do not establish hosted prompt fidelity or participant-account access

[Slides](index.html) · [Facilitator notes](facilitator.html) · [Navigation guide](navigation.html)
