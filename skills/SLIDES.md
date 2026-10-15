# Configuring skills and tools

## Configuring skills and tools — 1

[![CUNY AI Lab](../images/cail-wordmark-white.png)](https://ailab.gc.cuny.edu/)

### Configuring skills and tools

New Media Lab · Room 7388.01
CUNY Graduate Center

Thursday, October 15, 2026   2:30–4:00 p.m. Eastern

Developed by Zach Muhlbauer

[https://cuny-ai-lab.github.io/sandbox-series/skills](https://cuny-ai-lab.github.io/sandbox-series/skills)

---

## Configuring skills and tools — 2

### Choose Your Own Adventure

Continue your saved model or clone it first

Open **Workspace → Models → Edit**
Read your actual system prompt
Identify setting, goals, and rules

Keep this model card open while you add a skill and a tool

Select **Workspace** in left sidebar, then **Models**. Search for **STEM Adventure Games**. Open **⋯** beside it and select **Clone**.

![Workspace Models filtered to STEM Adventure Games, with annotations identifying Workspace in left sidebar and Clone for original model](../images/knowledge-stem-2026-09-28/clone-model.svg)

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

### Extend Adventure Games

Follow a saved adventure procedure

Call Adventure Kit as directed by the skill

Read the saved instructions in **Workspace → Skills**

---

## Configuring skills and tools — 5

### Add Your Skill

In **Workspace → Models → Edit**, find **Skills → Select Skill**

Choose existing **Extend Adventure Games**

Read its saved instructions
Keep this model card open for Adventure Kit

![User-supplied model card with step 1 outlining Skills → Select Skill and step 2 outlining checked Extend Adventure Games](../images/current/workshop3-add-skill-current.svg)

---

## Configuring skills and tools — 6

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

## Configuring skills and tools — 7

### Tool Examples

Workspace → Tools
Examples from the host’s catalog. Your list depends on access

![Selected tools — Adventure Kit, Chat Export, Instructional Toolset, Pronunciation and Translation Tool, and ChartJS once](../images/current/workshop3-selected-tools.svg)

---

## Configuring skills and tools — 8

### Update Model for Tool Calling

![Model card base-model picker — 1 identifies Base Model; 2 identifies DeepSeek V4 Flash 0731](../images/current/workshop3-deepseek-base-model.svg)

---

## Configuring skills and tools — 9

### Enable Filter

Enable **Model Bound Tool Enabler** on your model card.
Why: It restores attached tools when a chat omits them.

![Model card filter picker with Model Bound Tool Enabler outlined](../images/current/workshop3-model-bound-filter.svg)

---

## Configuring skills and tools — 10

### Add the ‘Adventure Kit’ tool

In this same model card, open **Tools → Select Tool**
Choose **Adventure Kit** · Confirm **Extend Adventure Games** remains selected
Add next prompt instruction, then click **Save & Update** before testing

![Model editor — 1 identifies Select Tool; 2 identifies saved Adventure Kit entry](../images/skills-2026-10-15/adventure-kit-select.svg)

---

## Configuring skills and tools — 11

### Model Card Check-In

Ensure that your model card has a knowledge collection, tool, skill, and filter configured like the image below.

![Model card showing a knowledge collection, Adventure Kit tool, Extend Adventure Games skill, and Model Bound Tool Enabler filter selected](../images/current/workshop3-model-card-status.png)

---

## Configuring skills and tools — 12

### Add Skill Instructions to the Bottom of Your System Prompt

```text
Load the extend_adventure_games skill and follow it on every turn, calling the adventure_kit tool only as the skill directs. Use no other skills or tools.
```

---

## Configuring skills and tools — 13

### Test Your Adventure

Run your updated adventure game
Verify configured skill and tool are called appropriately
Then play the rest of your game

---

## Configuring skills and tools — 14

### Observe Game Results

① Check skill call
② Check tool call

Open details to confirm selected skill

![User-provided live Clone response with numbered callouts for view_skill and show_scene above rendered ADVENTURES panel](../images/current/workshop3-skill-tool-run.svg)

---

## Configuring skills and tools — 15

### Explore Other Skills

After your first adventure works, try **Adventure Outcomes** or **Conclude Adventure Game** if available

Read saved instructions · Change one item · Save your model card and compare results

![Fresh model-card skill picker — 1 identifies Select Skill; 2 identifies Conclude Adventure Game. Captured October 15, 2026.](../images/current/workshop3-conclude-skill-current.svg)

---

## Configuring skills and tools — 16

### Choose Your Task

### Revise One Item

Copy complete tool code or skill instructions

Describe an observed problem and one change

### Create Your Own

Choose your own tool or skill

Specify purpose, required input, and expected result

[Copy tool code](navigation.html#tool-copy) · [Skill instructions](navigation.html#skill-copy)

---

## Configuring skills and tools — 17

### Work With Support

Open **CAIL Workspace Support**
Paste original content or your new task, system prompt, and required sources
Request complete content, an explanation, and one test · [Copy request](exercises.html#work-with-support)

![CAIL Workspace Support model identity with surrounding sidebar](../images/current/workshop3-clean-support.png)

---

## Configuring skills and tools — 18

### Adapt Your Adventure

Introduce a lesson plan, learning outcome, or disciplinary focus to your use of **CAIL Workspace Support** card

Prompted to generate a skill and/or tool that continues to support or further extends your adventure game, either adapting an existing skill or tool, or making your own.

---

## Configuring skills and tools — 19

### Add Tools or Skills

Copy and paste all code, then save your item.

On your model card, select your new tool or skill.

Update the system prompt to tell the model which tool to use and when. Save the model card.

![Tools Create form with code editor, Access and Save & Create visible; arrows identify relevant steps without changing interface pixels](../images/current/workshop3-arrow-create-tool.svg)

---

## Configuring skills and tools — 20

### Series Reflections

What task in your teaching or research could benefit from a skill or tool?

Would you be interested in joining our coworking session on October 29,  2–4pm,  to build your adventure into a collection so that we can showcase our work over the course of the series?

What would you develop next with the prompts, knowledge collections, skills, and tools you have explored?
