# Configuring skills and tools

## Configuring skills and tools — 1

### Configuring skills and tools

Add tools and reusable instructions for teaching and research

CUNY AI Lab Sandbox

Developed by Stefano Morello and Zach Muhlbauer

---

## Configuring skills and tools — 2

### Workshop Agenda

- Confirm Skills and Tools access

- Play STEM Adventure

- Inspect commands and results

- Configure reusable skills

- Create and test tools

- Compare procedural changes

Before attending, confirm individual access and Sandbox sign-in. Creating or editing resources also requires Workspace access. Knowledge access is needed when your task uses a collection.

---

## Configuring skills and tools — 3

### Review Previous Work

Open STEM Adventure Games and review its system prompt.

- Identify instructions for opening Prism Laboratory.

- Review attached STEM Wikipedia Experiments collection.

- Distinguish source material, skill instructions, and tool operations.

Use your own configuration when adapting these examples.

---

## Configuring skills and tools — 4

### Tools & Skills

Skills

Reusable instructions for tasks or procedures.

Tools

Operations such as web search, code execution, or database queries.

Test a request that needs your skill or tool. Check what your model used and whether its response is correct.

[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 5

### Connect Resources

System prompt

Open games and describe how components work together.

Knowledge

Supply scientific and historical sources.

Skill

Guide procedural changes and interpretation.

Tool

Apply game rules and render playable output.

Save each artifact with its tests.

---

## Configuring skills and tools — 6

### Enable Tools

![Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter](../images/current/integrations.png)

Open Integrations beside + to enable tools for this chat.

A tool runs an operation, such as a search, a calculation, or a search within a knowledge collection.

Open **Integrations** beside + to choose tools for this chat. Attach reusable tools under **Tools** in your model editor.

Availability depends on account permissions, configuration, and model support.

[Enable tools in chat or on a model](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 7

### Inspect Game Rules

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](../images/current/stem-game-2026-09-14.png)

STEM Adventure applies rules for rooms, inventory, actions, and completion.

- Enter go north to reach Storeroom.

- Enter take prism to add a prism to inventory.

- Enter help to list available actions.

- Try record result before completing required steps.

[Open game](../examples/adventure/preview.html) · [Read scenario JSON](../examples/adventure/prism.json)

---

## Configuring skills and tools — 8

### Test Game Commands

Check successful and unsuccessful actions.

- Complete [winning command sequence](../examples/adventure/winning-commands.json).

- Try completing an experiment before its prerequisites.

- Pick up an item twice.

- Enter undo, restart, save, and load.

Compare room, inventory, flags, and completion after replay.

---

## Configuring skills and tools — 9

### Discuss Play Records

- Enter **discuss** inside your game.

- Review record in message box, then send it.

- Check how your model explains a failed action.

- Compare programmed observations with historical sources.

A completed game does not establish conceptual understanding.

---

## Configuring skills and tools — 10

### Choose Procedures

Choose one procedure to change or examine.

- Add an aperture comparison to Prism Laboratory.

- Inspect a failed command and its prerequisite.

- Check a historical claim against source material.

Describe expected behavior before testing.

---

## Configuring skills and tools — 11

### Define Skills

Skills contain reusable Markdown instructions for tasks or procedures.

Models receive a skill’s name and description and can load its full instructions when needed.

Describe when to use your skill and which steps to follow.

[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

[Open WebUI Skills](https://docs.openwebui.com/features/workspace/skills/)

---

## Configuring skills and tools — 12

### Write Skills

---

## Configuring skills and tools — 13

Structure

### Structure Skills

Use three parts to draft this skill.

- **Trigger** — When should this skill activate?

- **Procedure** — Which steps should your model follow?

- **Format** — How should responses appear?

---

## Configuring skills and tools — 14

### Define Triggers

Describe when your skill should be used.

- Should it load when users request a procedural change?

- Should it also apply to submitted play records?

- Which requests should leave it unused?

```text
Use this skill when users request an experimental variation in STEM Adventure or ask to examine a submitted play record.
```

---

## Configuring skills and tools — 15

### Write Procedures

Specify how your model should extend an experiment.

```text
1. Identify one experimental decision to change.
2. Check source material for that procedure.
3. Revise scenario JSON within the tool contract.
4. Provide winning and blocked commands, then open the game.
5. Compare a submitted record with expected behavior.
```

---

## Configuring skills and tools — 16

### Specify Format

Keep artifacts and test results distinguishable.

```text
Scenario JSON: [Complete scenario]
Source: [Relevant historical passage]
Invented elements: [Rooms or simplified observations]
Winning commands: [Sequence]
Blocked command: [Command and missing prerequisite]
Observed result: [Fill only after testing]
```

---

## Configuring skills and tools — 17

### Draft Skills

Open Kale Skill Builder to draft reusable instructions.

Select model ID on bottom right of message box.

```text
Draft a skill for STEM Adventure that extends one experimental procedure or examines a submitted play record. Use render_stem_adventure(scenario_json: str = ""). Preserve game rules. Include trigger, 3–5 steps, output, and two proposed tests. Do not invent successful tool calls.
```

[Open Kale Skill Builder](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-skill-builder) · [Read tested skill](../examples/stem-game-skill.md)

---

## Configuring skills and tools — 18

### Write Instructions

Describe when to use your skill, which steps to follow, and when to pause.

```text
Use this skill when [specific request or action].

1. [First step]
2. [Next step]
3. [What to check before continuing]
4. [When to wait for user input]

Format responses as [required structure].
```

---

## Configuring skills and tools — 19

### Create Skills

![Extend STEM Adventures in Workspace Skills, showing its name, description, and Markdown instructions for game play, procedural extensions, and submitted records.](../images/current/stem-skill-2026-09-14.png)

Enter a name, description, and instructions, then select Save & Create.

- Open **Workspace → Skills → Create**.

- Enter a name, identifier, and description that explain when to use it.

- Write instructions, review **Access**, and choose **Save & Create**.

[Create and attach a skill](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 20

### Attach Skills

- Open **Workspace → Models** and edit your model.

- Select your skill under **Skills**.

- Set **Function Calling** to **Native** under **Advanced Parameters**.

- Select **Save & Update** and test a request that uses your skill.

Use a model that supports tool calling.

[Attach skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 21

### Extend Procedures

Attach [Prism Laboratory JSON](../examples/adventure/prism.json), enable Extend STEM Adventures, and request one change.

```text
Add an aperture comparison to Prism Laboratory using Newton: Experimental Variants. Keep existing rooms and actions. Provide scenario JSON, a winning command sequence, and one command that must fail before its prerequisite. Open the revised game.
```

[Read skill instructions](../examples/stem-game-skill.md) · [Download tested scenario](../examples/adventure/aperture.json)

---

## Configuring skills and tools — 22

### Check Interpretations

Use this draft to check an interpretation against a source passage.

```text
When the user asks whether a passage supports a claim, ask for both if either is missing.

1. Quote the relevant passage and identify its source. Do not invent missing metadata.
2. State what the passage directly supports.
3. Identify an inference or competing reading that needs further evidence.
4. Ask one question that would help resolve the difference, then wait.

Keep the quotation separate from your interpretation. If the source is unavailable, explain what cannot be checked.
```

Test it with supported, overstated, and unsupported claims from public or approved material.

---

## Configuring skills and tools — 23

### Test Skills

Repeat an extension request before and after enabling your skill.

- Keep base model, system prompt, sources, and tool unchanged.

- Check whether scenario JSON follows its contract.

- Run winning and blocked commands.

- Compare expected behavior with actual results.

Keep generated scenarios and play records for review.

---

## Configuring skills and tools — 24

### Check Skill Drafts

Ask whether a skill’s test expectations match available evidence.

```text
{"commands":[],"events":[],"result":{"complete":true}}
```

An empty history cannot establish completion. Request a full record or replay.

Return this failure to Kale Skill Builder and inspect its revised instructions.

[Read corrected skill draft](../examples/creators/record-interpreter-skill.md) · [Inspect initial response](../review/live/skill-builder-consistency-failure.md)

---

## Configuring skills and tools — 25

### Create Adventure Tools

Open Tool Creator to draft or revise Python code.

```text
Create a minimalist text adventure tool for Open WebUI. Return an interactive HTMLResponse and a description for the model. Track rooms, inventory, prerequisites, and completion. Use one command line with help, undo, restart, save, load, and discuss commands. Keep scenario JSON separate from executable code.
```

[Open Tool Creator](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-tool-creator) · [Download tested tool](../examples/tools/stem_adventure.py)

---

## Configuring skills and tools — 26

### Install Tool Code

- Open **Workspace → Tools → Create**.

- Enter Name, ID, and Description.

- Paste [STEM Adventure code](../examples/tools/stem_adventure.py) and review it.

- Select **Save & Create**.

- Enable your tool through **Integrations → Tools**.

Use a private copy when changing code.

---

## Configuring skills and tools — 27

### Check Generated Code

Test whether generated code rejects incorrect types.

```text
{"commands":[42],"events":[{"command":42,"valid":false}]}
```

Expected: reject numeric commands. Initial creator output accepted them.

Send observed failure back to Tool Creator, then repeat your tests.

[Read corrected tool](../examples/creators/record-validator.py) · [Review executed tests](../review/live/tool-creator-corrected-tests.json)

---

## Configuring skills and tools — 28

### Inspect Tool Results

Use an available knowledge tool to retrieve a file from STEM Wikipedia Experiments. Check which file and passage it retrieves.

For STEM Adventure Games, retrieve source text and use Check Source Imports to inspect it. Python example is a draft for installation and testing in an approved Workspace.

Inspect tool calls and results. Check whether a tool ran when your model says it inspected a source.

---

## Configuring skills and tools — 29

### Compare Game Records

Compare original and extended procedures.

```text
Review both play records. Which commands and prerequisites changed? Which observations were programmed? Which historical claims can the uploaded sources support?
```

Check your model’s account against commands and source passages. Keep expected and observed results separate.

---

## Configuring skills and tools — 30

### Record Test Results

| Record | Include |
| --- | --- |
| Configuration | Model ID, system prompt, documents, skill instructions, and enabled tools. |
| Action | Request, instructions used, tool calls and results, and final response. |
| Judgment | What you expected, what happened, and any change you plan to test. |

Before sharing, confirm others can access your model, collections, skills, and tools. Repeat relevant tests after updates.

---

## Configuring skills and tools — 31

### Repeat Tests

- Save prompts, sources, skills, and tool settings

- Compare expected and observed behavior

- Revise instructions from recorded failures

- Verify shared access with intended users

- Retest after model or tool updates

[Browse system-prompt examples](../examples.html) · [Return to Composing system prompts](../)
