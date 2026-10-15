# Configuring skills and tools

## 1. Configuring skills and tools

[![CUNY AI Lab](../images/cail-wordmark-white.png)](https://ailab.gc.cuny.edu/)



New Media Lab · Room 7388.01
CUNY Graduate Center

Thursday, October 15, 2026   2:30–4:00 p.m. Eastern

Developed by Zach Muhlbauer

[https://cuny-ai-lab.github.io/sandbox-series/skills](https://cuny-ai-lab.github.io/sandbox-series/skills)

---

## 2. Choose Your Own Adventure

Continue your saved model or clone it first

Open **Workspace → Models → Edit**
Review your system prompt to identify setting, goals, and rules from last time

Keep this model card open while you add a skill and a tool

Select **Workspace** in left sidebar, then **Models**. Search for **STEM Adventure Games**. Open **⋯** beside it and select **Clone**.

![Workspace Models filtered to STEM Adventure Games, with annotations identifying Workspace in left sidebar and Clone for original model](../images/knowledge-stem-2026-09-28/clone-model.svg)

---

## 3. What Is a Skill?

**Skills** contain plain-text instructions for repeatable tasks

Trigger

Request or condition that starts a procedure

Procedure

Steps, checks, and points that require a question

Output

Required response content and form

---

## 4. What Is a Tool?

When a model calls a **tool**, it is given the ability to execute a function and return its result, usually through a Python script

This is called **tool calling** (aka **function calling**)

Input

Information passed to a function

Execution

Code that applies specified rules

Result

Returned output for a model to inspect

---

## 5. Update Model for Tool Calling

![Model card base-model picker — 1 identifies Base Model; 2 identifies DeepSeek V4 Flash 0731](../images/current/workshop3-deepseek-base-model.svg)

---

## 6. Enable Filter

Enable **Model Bound Tool Enabler** on your model card, which binds assigned tools to the model’s operations.

![Model card filter picker with Model Bound Tool Enabler outlined](../images/current/workshop3-model-bound-filter.svg)

---

## 7. Add Your Skill

In **Workspace → Models → Edit**, find **Skills → Select Skill**

Choose **Adventure Panel Play** and read its saved instructions
Keep this model card open for the tool

![Skills picker with arrow 1 at Select Skill and arrow 2 at Adventure Panel Play.](../images/current/workshop3-panel-skill-select.svg)

---

## 8. Add the ‘Adventure Panel’ tool

In this same model card, open **Tools → Select Tool**
Choose **Adventure Panel** · Keep **Adventure Panel Play** selected
Add the next prompt instruction, then click **Save & Update** before testing

![Tools picker with arrow 1 at Select Tool and arrow 2 at Adventure Panel.](../images/current/workshop3-panel-tool-select.svg)

---

## 9. Model Card Check-In

Confirm **1. Adventure Panel**, **2. Adventure Panel Play**,
and **3. Model Bound Tool Enabler** are selected
Keep your own knowledge collection attached above

![Model card with numbered arrows identifying the checked Adventure Panel tool, Adventure Panel Play skill, and Model Bound Tool Enabler filter.](../images/current/workshop3-panel-check-in.svg)

---

## 10. Add Skill Instructions to the Bottom of Your System Prompt

```text
Load the attached Adventure Panel Play skill (extend-adventure-games) and follow it on every turn. Use show_scene from the Adventure Panel tool to display each scene and its choices. Follow this system prompt’s setting, goals, rules, and source instructions.
```

---

## 11. Test Your Adventure

- Run your updated adventure game

- Verify configured skill and tool are called appropriately

- Then play the rest of your game

---

## 12. Observe Game Results

- Check skill call

- Check tool call

Open details to confirm selected skill

![User-provided live Clone response with numbered callouts for view_skill and show_scene above rendered ADVENTURES panel](../images/current/workshop3-skill-tool-run.svg)

---

## 13. Explore Other Skills

After your first adventure works, try **Adventure Outcomes** or **Conclude Adventure Game**

Read saved instructions · Change one item · Save your model card and compare results

![Skills picker showing Adventure Panel Play, Adventure Outcomes, and Conclude Adventure Game, with arrows at Select Skill and Conclude Adventure Game.](../images/current/workshop3-panel-other-skills.svg)

---

## 14. Choose Your Task

### Revise One Item

Copy complete tool code or skill instructions

Describe an observed problem and one change

### Create Your Own

Choose your own tool or skill

Specify purpose, required input, and expected result

[Copy tool code](navigation.html#tool-copy) · [Skill instructions](navigation.html#skill-copy)

---

## 15. Work With Support

Prompt CAIL Workspace Support to generate a skill and/or tool that continues to support or further extends your adventure game, adapting an existing skill/tool or making your own.

![Fresh live CAIL Workspace Support interface with model identity, description, composer, and Get started suggestion](../images/current/workshop3-support-live-20261015.svg)

---

## 16. Adapt Your Adventure

Introduce a lesson plan, learning outcome, or disciplinary focus to your use of **CAIL Workspace Support** card

Prompted to generate a skill and/or tool that continues to support or further extends your adventure game, either adapting an existing skill or tool, or making your own.

---

## 17. Add Tools or Skills

Copy and paste all code for tools or plain text for skills, then save your item. On your model card, select your new tool or skill, and signpost it in your system prompt.

![Tools Create form with code editor, Access and Save & Create visible; arrows identify relevant steps without changing interface pixels](../images/current/workshop3-arrow-create-tool.svg)

---

## 18. Series Reflections

What task in your teaching or research could benefit from a skill or tool?

Would you be interested in joining our coworking session on October 29,  2–4pm,  to build your adventure into a collection so that we can showcase our work over the course of the series?

What would you develop next with the prompts, knowledge collections, skills, and tools you have explored?
