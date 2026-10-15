# Configuring skills and tools

## Configuring skills and tools — 1

[![CUNY AI Lab](../images/cail-wordmark-white.png)](https://ailab.gc.cuny.edu/)

### Configuring skills and tools

New Media Lab · Room 7388.01
CUNY Graduate Center

Thursday, October 15, 2026   2:30–4:00 p.m. Eastern

[https://cuny-ai-lab.github.io/sandbox-series/skills](https://cuny-ai-lab.github.io/sandbox-series/skills)

---

## Configuring skills and tools — 2

### Choose Your Own Adventure

Continue your saved model, or clone **STEM Adventure Games**
Read its system prompt for setting, goals, and rules
[Clone instructions](navigation.html#clone) · [Adventure example](../examples/stem-chat-system-prompt.html)

![Saved model in chat with model selector below message box](../images/current/workshop3-clean-continue.png)

---

## Configuring skills and tools — 3

### What Is a Skill?

**Skills** contain plain-text instructions for repeatable tasks

Trigger

Request or condition that starts a procedure

Procedure

Steps, checks, and points that require a question

Output

Required response content and form

---

## Configuring skills and tools — 4

### Skill Examples

Workspace → Skills · 1 of 3
Examples from the host’s catalog. Your list depends on access

![Current skills catalog entries including History Of Ideas Abstract Critique, Historical Context Abstract Critique, Extend STEM Adventures, ChartJS Visualization. Interface screenshot captured October 15, 2026.](../images/current/workshop3-catalog-skills-1.png)

---

## Configuring skills and tools — 5

### Skill Examples

Workspace → Skills · 2 of 3
Examples from the host’s catalog. Your list depends on access

![Current skills catalog entries including Response Features, Error Handling, Language Adjustment, Writing-Support-Opener. Interface screenshot captured October 15, 2026.](../images/current/workshop3-catalog-skills-2.png)

---

## Configuring skills and tools — 6

### Skill Examples

Workspace → Skills · 3 of 3
Examples from the host’s catalog. Your list depends on access

![Current skills catalog entries including Conversational Etiquette, Native Orthography, One-Step Dialogue. Interface screenshot captured October 15, 2026.](../images/current/workshop3-catalog-skills-3.png)

---

## Configuring skills and tools — 7

### Add Your Skill

Open **Workspace → Models**, then choose **Edit** from your model card’s menu
① Under **Skills**, click **Select Skill** · ② Choose your skill
Click **Save & Update** to save your model

![Model card Skills menu with blue numbered callouts for 1 Select Skill, 2 choose a saved skill. Adventure Outcomes is shown selected.](../images/current/workshop3-model-skill-select.svg)

---

## Configuring skills and tools — 8

### Add Skill Instructions

Add this clause with the saved skill’s task, name, and ID · [Copy clause](exercises.html#add-skill-instructions)

When I ask for [TASK], load [SKILL_NAME] (ID: [SKILL_ID]). Follow its saved instructions using this system prompt’s goals and rules and the latest information I have supplied. Ask about missing or conflicting details before deciding. Acknowledge a request to stop immediately, without requiring another action or reflection.

Save your model, then check that the saved skill loads and follows its instructions

---

## Configuring skills and tools — 9

### Test Your Skill

Ask your model to use the selected skill for its stated task

Use an actual record of choices and results
Leave out required information and check for a question
Ask to stop before the goal is met

Which task in your teaching or research needs a repeatable procedure?

---

## Configuring skills and tools — 10

### What Is a Tool?

When a model calls a **tool**, Sandbox executes a function and returns its result

**Tool calling**, otherwise known as **function calling**, sends a function name and arguments for execution

Input

Arguments supplied to a function

Execution

Code that applies specified rules

Result

Returned output for a model to inspect

---

## Configuring skills and tools — 11

### Tool Examples

Workspace → Tools · 1 of 4
Examples from the host’s catalog. Your list depends on access

![Current tools catalog entries including Adventure Kit, Chat Export, Instructor Rubric. Interface screenshot captured October 15, 2026.](../images/current/workshop3-catalog-tools-1.png)

---

## Configuring skills and tools — 12

### Tool Examples

Workspace → Tools · 2 of 4
Examples from the host’s catalog. Your list depends on access

![Current tools catalog entries including OCR reader, Instructional Toolset, Pronunciation and Translation Tool. Interface screenshot captured October 15, 2026.](../images/current/workshop3-catalog-tools-2.png)

---

## Configuring skills and tools — 13

### Tool Examples

Workspace → Tools · 3 of 4
Examples from the host’s catalog. Your list depends on access

![Current tools catalog entries including Graphing, PhysicsPY, ChartJS, Charts (v1). Interface screenshot captured October 15, 2026.](../images/current/workshop3-catalog-tools-3.png)

---

## Configuring skills and tools — 14

### Tool Examples

Workspace → Tools · 4 of 4
Examples from the host’s catalog. Your list depends on access

![Current tools catalog entries including Preflight Student Input, Kale GitHub, Whisper CUDA, cloudflare_whisper_tool. Interface screenshot captured October 15, 2026.](../images/current/workshop3-catalog-tools-4.png)

---

## Configuring skills and tools — 15

### Check Tool Binding

**Model Bound Tool Enabler** is a filter that restores model-attached tools when a chat request omits them

If an attached tool is missing from call details, use this existing filter on your private model and repeat your test

It restores availability; execution still requires a valid tool call

[Configuration checks and evidence record](tool-calling.html)

---

## Configuring skills and tools — 16

### Add the ‘Adventure Kit’ tool

Open **Integrations → Tools**
Search **Adventure Kit** and select its toggle

![Chat Integrations Tools menu with Adventure Kit toggle; arrows identify relevant steps without changing interface pixels](../images/current/workshop3-arrow-kit-select.svg)

---

## Configuring skills and tools — 17

### Prepare Your Adventure

Design your adventure from your system prompt

Instruct your model to map its setting, goals, and rules into scenes, choices, and end conditions

Resolve missing or contradictory instructions
Review proposed input for **Adventure Kit**

[Copy preparation and run requests](exercises.html#add-and-test-tool)

---

## Configuring skills and tools — 18

### Add Tool Instructions

Add this clause to your model’s system prompt · [Copy clause](exercises.html#add-tool-instructions)

After the player approves an adventure, call the attached Adventure Kit tool’s **render_adventure** function with the reviewed schema-version-2 JSON in **scenario_json**. Derive content and rules from this system prompt; resolve missing or conflicting instructions first. Read the returned result, resolve errors before play, and use the player’s copied Play record when discussing progress or completion.

Save your model, then verify tool attachment, provider support, and the actual result

---

## Configuring skills and tools — 19

### Test Your Tool

Run your reviewed adventure, then compare its scene and choices with your prompt

Try a choice before and after its prerequisite
Inspect Undo and Stop
Copy actual play record into chat

Which step in your teaching or research needs an executable operation?

---

## Configuring skills and tools — 20

### Choose Your Task

### Revise One Item

Copy complete tool code or skill instructions

Describe an observed problem and one change

### Create Your Own

Choose your own tool or skill

Specify purpose, required input, and expected result

[Copy tool code](navigation.html#tool-copy) · [Skill instructions](navigation.html#skill-copy)

---

## Configuring skills and tools — 21

### Work With Support

Open **CAIL Workspace Support**
Paste original content or your new task, system prompt, and required sources
Request complete content, an explanation, and one test · [Copy request](exercises.html#work-with-support)

![CAIL Workspace Support model identity with surrounding sidebar](../images/current/workshop3-clean-support.png)

---

## Configuring skills and tools — 22

### Add Tools or Skills

Create a new **tool** or **skill**, or save a revised copy
Use **Workspace → Tools → Create** or [**Skills → Create**](navigation.html#create-skill)
Enter new Name and ID; paste complete reviewed content

Review **Access**, then **Save & Create** · [Select and test your item](exercises.html#add-new-version)

![Tools Create form with code editor, Access and Save & Create visible; arrows identify relevant steps without changing interface pixels](../images/current/workshop3-arrow-create-tool.svg)

---

## Configuring skills and tools — 23

### Series Reflections

What task in your teaching or research could benefit from a skill or tool?

Would you be interested in joining our coworking session on October 29,  2–4pm,  to build your adventure into a collection so that we can showcase our work over the course of the series?

What would you develop next with the prompts, knowledge collections, skills, and tools you have explored?
