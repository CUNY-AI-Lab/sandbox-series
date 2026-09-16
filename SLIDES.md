# Sandbox Workshops

## Composing system prompts — 1

Workshop 1 of 3

### Composing system prompts

Compare and configure models for teaching and research

CUNY AI Lab Sandbox

Developed by Zach Muhlbauer

---

## Composing system prompts — 2

### Workshop Roadmap

- **Composing system prompts** Configure model behavior with system prompts.

- **Curating knowledge collections** Upload documents so models can reference them.

- **Configuring skills and tools** Add web search, code execution, and reusable instructions.

[Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/)

---

## Composing system prompts — 3

### Workshop Agenda

- Request individual access and sign in

- Define system prompts

- Compare responses from small models

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse

Before attending, request individual access and sign into Sandbox.

---

## Composing system prompts — 4

### Request Access

[ailab.gc.cuny.edu/request-access/](https://ailab.gc.cuny.edu/request-access/)

- Choose **My own access** and sign in with **CUNY Login**.

- Complete your details, select **CAIL Sandbox**, and submit your application.

- After approval, open [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/) and select **Continue with CUNY Login**.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Composing system prompts — 5

### System Prompts

A system prompt gives a model instructions for its role, behavior, and focus.

### User Prompts

Questions or tasks you enter in chat.

### Base Models

A base model generates responses. A custom model adds instructions and resources without training a new base model.

[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/) · [Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

---

## Composing system prompts — 6

### Select Models

![Sandbox chat with CUNY AI Lab logo, message box, and open model selector; enlarged detail shows model choices with model ID outlined and marked by an arrow](images/current/model-selector-hidpi-2026-09-16.svg)

**Alt text:** Sandbox chat with CUNY AI Lab logo, message box, and open model selector; enlarged detail shows model choices with model ID outlined and marked by an arrow

Select model ID on bottom right of message box. Type a request, send it, then ask a follow-up. Open New Chat to start without earlier messages.

---

## Composing system prompts — 7

### Chat Features

Upload Files (+)

Attach images, PDFs, or documents.

Integrations

Enable tools that perform operations and skills that give reusable instructions.

Message actions

Find actions beneath each response to copy, edit, or regenerate it. Open More (⋯) for additional actions.

[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

---

## Composing system prompts — 8

### Compare Models

![Sandbox logo, message box, and open model selector; enlarged detail shows Compare button beside search field outlined and marked by an arrow](images/current/model-selector-compare-hidpi-2026-09-16.svg)

**Alt text:** Sandbox logo, message box, and open model selector; enlarged detail shows Compare button beside search field outlined and marked by an arrow

Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two small models. If Compare is unavailable, send identical prompts in separate new chats.

---

## Composing system prompts — 9

### Who Was Late?

Compare how two small models interpret this sentence.

```text
The nurse yelled at the doctor because she was late. Who was late?
```

Send this question to both models.

---

## Composing system prompts — 10

### Examine Assumptions

“She” could refer to either person. This sentence does not establish who was late.

- Does each model acknowledge ambiguity?

- What assumption supports its answer?

- Does either explanation add information absent from this sentence?

---

## Composing system prompts — 11

### Compare Outputs

Consider this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

What do you think this person wants to accomplish?

---

## Composing system prompts — 12

### Gemma’s Response

You should **walk** to the car wash.

[View original response](images/showcase/car-wash-gemma.png)

---

## Composing system prompts — 13

### Qwen’s Response

You should **take the car**.

[View original response](images/showcase/car-wash-qwen.png)

---

## Composing system prompts — 14

### Compare Models

Start a new chat, select two models, and send this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

Save both responses with your question and selected model IDs before adding system prompt instructions.

---

## Composing system prompts — 15

### Add System Prompt

Copy these instructions for in-chat **System Prompt**.

```text
Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer briefly without inventing context.
```

---

## Composing system prompts — 16

### Open Chat Controls

![Sandbox logo, message box, and open Controls panel with System Prompt field marked by an arrow](images/current/chat-controls-2026-09-14-annotated.svg)

**Alt text:** Sandbox logo, message box, and open Controls panel with System Prompt field marked by an arrow

Select Controls at top right. Paste copied instructions into System Prompt, then close Controls.

---

## Composing system prompts — 17

### Regenerate Responses

![Original question, Gemma response, and message box with Regenerate button marked by an arrow](images/current/regenerate-gemma-2026-09-14-annotated.svg)

**Alt text:** Original question, Gemma response, and message box with Regenerate button marked by an arrow

Select Regenerate beneath each original response, then choose Try Again. Keep your original question, selected models, and other settings unchanged.

---

## Composing system prompts — 18

### Compare Responses

- Compare responses before and after adding system prompt instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

---

## Composing system prompts — 19

### Open Workspace

![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](images/current/workspace-sidebar-2026-09-15-annotated.svg)

**Alt text:** Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar

Select Workspace in left sidebar.

---

## Composing system prompts — 20

### Review Custom Models

Choose **Models** and open a custom model shared with you.

Review **Base Model** and **System Prompt**, then compare its instructions with your tested prompt.

Continue in chat if Workspace is unavailable.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Composing system prompts — 21

### Model Configuration

![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.](images/current/model-create-hidpi-2026-09-16.svg)

**Alt text:** New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.

Select Create in Models. Enter a recognizable name, choose a tested base model, and add your tested system prompt.

---

## Composing system prompts — 22

### Add Prompt Suggestions

Add a description and prompt suggestions for tasks your model should support.

Users select your custom model to use its instructions and resources.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Composing system prompts — 23

Examples

### Situating System Prompts

---

## Composing system prompts — 24

### Select STEM Games

![Model Selector filtered to STEM Adventure Games, with CUNY AI Lab logo and message box visible.](images/current/stem-selector-2026-09-14.png)

**Alt text:** Model Selector filtered to STEM Adventure Games, with CUNY AI Lab logo and message box visible.

Select model ID on bottom right of message box. Search for STEM Adventure Games and select it.

---

## Composing system prompts — 25

### STEM Adventure Games

![STEM Adventure Games presents a short scene and numbered choices directly in Sandbox chat.](images/current/stem-chat-play-hidpi-2026-09-16.png)

**Alt text:** STEM Adventure Games presents a short scene and numbered choices directly in Sandbox chat.

Type Start an adventure. Choose an experiment, then reply with a number or describe what you want to do.

---

## Composing system prompts — 26

### Inspect System Prompt

![STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.](images/current/stem-chat-model-hidpi-2026-09-16.svg)

**Alt text:** STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.

Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt.

---

## Composing system prompts — 27

### Read Game Instructions

```text
End each scene with three numbered choices. Accept a number or an action in ordinary language, such as looking around, examining an object, or asking for a hint. Wait for a response before continuing.
```

What should happen after you choose an action?

[Read full system prompt](examples.html#stem-chat)

---

## Composing system prompts — 28

### Adapt Research Prompts

You can adapt this exercise to a research task, such as comparing article abstracts or documenting a method.

- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.

Save your source material, prompt, response, and assessment together.

---

## Composing system prompts — 29

### Draft System Prompts

---

## Composing system prompts — 30

### Define Prompt Components

Choose one component to change.

- **Context** — Experiment, historical setting, and intended users.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Tone and format** — Language, length, and presentation.

---

## Composing system prompts — 31

### Define Context

Describe what your model should help users do.

- Who will use this model?

- Which experiment or research question will they explore?

- What prior knowledge can you assume?

```text
Guide a short text adventure about light and colour.
Help players explore how a prism changes a beam of sunlight.
```

---

## Composing system prompts — 32

### Write Procedures

What should happen before and after each choice?

```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer three numbered choices and wait.
4. Describe observations after players choose.
```

---

## Composing system prompts — 33

### Set Constraints

Specify how your model should handle missing evidence.

```text
Do not invent historical details when sources are missing.
Distinguish documented events from choices created for the game.
If a source is unavailable, explain what cannot be checked.
```

Test a request that asks for a detail absent from your sources.

---

## Composing system prompts — 34

### Set Tone

Describe how your model should address players.

```text
Address the player as “you.”
Use concise language for scenes and choices.
Explain unfamiliar scientific terms when they first appear.
```

Which terms need explanation for your intended users?

---

## Composing system prompts — 35

### Specify Format

Specify how scenes and choices should appear.

```text
Write a short scene followed by three numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```

---

## Composing system prompts — 36

Refine

### Refine Instructions

---

## Composing system prompts — 37

### Extend Instructions

- Specify what happens when a player asks for a hint.

- Explain how to revisit an earlier decision.

- Require source checks when players ask about historical claims.

- Test how your model responds when evidence is missing.

---

## Composing system prompts — 38

Watch Out

### Review Common Problems

### Prioritize Instructions

Check instructions for conflicts. Prioritize essential steps and test whether your model follows them.

### Resolve Contradictions

Check whether requested detail fits your length limit. Revise requirements that cannot be met together.

### Test Player Requests

Test game choices, requests for hints, and questions about sources.

### Retest Revised Prompts

Save each prompt version with its responses. Revise when a test reveals a problem, then repeat that test.

---

## Composing system prompts — 39

### Save Prompts

Save your tested prompt in a private custom model. Choose a base model, review **Access**, and select **Save & Create**. Reuse this model when adding documents in Workshop 2.

---

## Composing system prompts — 40

### Share Custom Models

- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and any attached collections.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Composing system prompts — 41

### Record Comparisons

Save your prompt, model settings, and responses.

| Item | Record |
| --- | --- |
| Configuration | Custom model name, base model, system prompt, settings, and date. |
| Test | User request, enabled features, saved response. |
| Judgment | What you checked, evidence from each response, and any change you plan to test. |

Use materials you are permitted to upload and share. Sandbox chats may be stored and accessible to administrators or people you share them with.

[Privacy and chat history](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Composing system prompts — 42

### Prepare Source Documents

- Save prompt versions and comparison notes

- Request Workspace and Knowledge collection access

- Select public or approved source documents

- Review [system-prompt examples](examples.html)

- Continue to [Curating knowledge collections](knowledge/)


## Curating knowledge collections — 1

### Curating knowledge collections

Upload documents for models to reference in teaching and research

CUNY AI Lab Sandbox

Developed by Zach Muhlbauer

---

## Curating knowledge collections — 2

### Workshop Agenda

- Confirm Workspace and Knowledge access

- Select source documents

- Create knowledge collections

- Attach collections to custom models

- Check source citations

- Choose procedures for skills

Before attending, confirm individual access, Sandbox sign-in, Workspace access, and Knowledge collection access.

---

## Curating knowledge collections — 3

### Knowledge Collections

A knowledge collection contains uploaded documents that a model can search when responding to questions.

Collections support PDFs, Markdown, and plain text. Attach a collection to a custom model under **Knowledge**.

[Knowledge Bases](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

[Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/)

---

## Curating knowledge collections — 4

### Choose Questions

Choose a question your documents can answer.

Bring course materials, research papers, or other documents you know well enough to check.

Use [system-prompt examples](examples.html) if you need a prompt to begin.

---

## Curating knowledge collections — 5

### Open Workspace

![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](images/current/workspace-sidebar-2026-09-15-annotated.svg)

**Alt text:** Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar

Select Workspace in left sidebar. Choose Models and open your custom model.

---

## Curating knowledge collections — 6

### Review Model Settings

![STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.](images/current/stem-chat-model-hidpi-2026-09-16.svg)

**Alt text:** STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.

Review **Base Model** and **System Prompt** in your custom model. Use [STEM Adventure Games instructions](examples.html#stem-chat) from Workshop 1. Leave Skills and Tools unselected.

---

## Curating knowledge collections — 7

### Save Initial Response

Start a new chat. Select model ID on bottom right of message box. Choose your custom model.

Ask your document question and save its response before attaching documents. Record any sources it uses.

---

## Curating knowledge collections — 8

### Retrieve Source Passages

- Uploaded documents are divided into passages and indexed for search.

- Retrieval finds passages relevant to a question.

- Your model can use retrieved passages in its response.

Which passages did your model use, and do they support its claims?

[Open WebUI retrieval](https://docs.openwebui.com/features/workspace/knowledge/)

---

## Curating knowledge collections — 9

### Open STEM Collection

![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, Newton’s optical experiments, procedural variations, and software checks.](images/current/stem-knowledge-2026-09-14.png)

**Alt text:** STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, Newton’s optical experiments, procedural variations, and software checks.

Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments.

---

## Curating knowledge collections — 10

### Review Source Roles

Use sources for different questions.

Newton’s optical experiments

Check apparatus, procedures, and observations.

Scientific method

Examine hypotheses, measurement, and revision.

Women in science

Investigate collaboration, recognition, and institutions.

Check whether a scene follows its sources or adds invented details.

---

## Curating knowledge collections — 11

### Inspect Imported Text

Open each file and compare its contents with its source page.

- Confirm article text is present.

- Check headings, missing passages, and extraction errors.

- Record article title, source URL, and revision date.

On September 14, 2026, List of experiments contained a Wikimedia rate-limit error instead of article text. Its filename alone did not establish usable content.

---

## Curating knowledge collections — 12

### Review Attached Knowledge

![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.](images/current/knowledge-chat-attachments-hidpi-2026-09-16.svg)

**Alt text:** STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.

Select STEM Wikipedia Experiments under Knowledge in your custom model and choose Save & Update. Skills and Tools are added in Workshop 3.

---

## Curating knowledge collections — 13

### Check Game Sources

In your custom model, start an adventure about light and colour. Choose one action, then ask about its historical sources.

```text
Which objects in this scene appear in Newton: Light and Colour? Quote a relevant passage. Which details were invented for this game?
```

Open cited material. Does it support your model’s response?

[Read Newton source summary](examples/knowledge/newton-light-colour.md) · [Read Newton’s account](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006)

---

## Curating knowledge collections — 14

### Select Documents

Begin with a few documents you know well enough to check.

- Course materials, such as syllabi, readings, or assignment instructions

- Research papers, methods, or annotated bibliographies

Use Markdown, plain text, or readable PDFs. Name files clearly and use headings to separate sections.

Check scanned or complex PDFs before uploading. Convert them to text if needed.

[Document formats](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

[Explore source examples](knowledge/reference.html)

---

## Curating knowledge collections — 15

### Build Knowledge Collections

Choose documents that explain your course or research project and describe what you want to examine.

---

## Curating knowledge collections — 16

### Choose Reference Materials

Choose source documents that help players investigate an experiment.

- Use [Newton: Light and Colour](examples/knowledge/newton-light-colour.md) for apparatus and observations.

- Use [Newton: Experimental Variants](examples/knowledge/newton-experimental-variants.md) for changes to experimental procedures.

Read entries before uploading. Distinguish these summaries from original historical accounts.

[Download Light and Colour](examples/knowledge/newton-light-colour.md) · [Download Experimental Variants](examples/knowledge/newton-experimental-variants.md)

---

## Curating knowledge collections — 17

### Create Knowledge Collections

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](images/current/knowledge-create-hidpi-2026-09-16.png)

**Alt text:** Current Create a knowledge base form with name, description, Private access, and Create Knowledge

Open Workspace → Knowledge → Create. Enter a name and description, keep access Private, then select Create Knowledge.

---

## Curating knowledge collections — 18

### Attach Knowledge Collections

- Open Workspace → Knowledge → your collection. Use Add Content to upload documents, then wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your custom model, and replace STEM Wikipedia Experiments with your collection under **Knowledge**.

- Choose **Save & Update**, then start a new chat with your custom model.

[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating knowledge collections — 19

### Test Retrieval

- Ask a question answered by one source. Verify each answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask about something absent from your documents. Check whether your model acknowledges missing information.

Repeat your saved question after attaching documents. Keep base model and system prompt unchanged. Compare responses and check which source passages were used.

---

## Curating knowledge collections — 20

### Check Retrieval Problems

| Observation | Next check |
| --- | --- |
| No relevant source appears | Check whether files finished processing, are attached, and are accessible. Review your search query. |
| A source is present but misread | Read cited passages in full and revise instructions. |
| A response invents a citation | Open cited documents and verify quotations and page numbers. |

Save unsuccessful responses before revising anything.

---

## Curating knowledge collections — 21

### Share Knowledge Collections

Share your collection with people who will use your custom model.

- Use **Add Access** to grant users or groups **Read** access.

- Ask someone you shared with to check access to your model and collection.

- Choose **Public** only for documents intended for all signed-in Sandbox users.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Curating knowledge collections — 22

### Prepare Skill Instructions

- Save source lists and retrieval tests

- Request Skills and Tools access

- Choose recurring teaching or research procedures

- Review [system-prompt examples](examples.html)

- Continue to [Configuring skills and tools](skills)


## Configuring skills and tools — 1

### Configuring skills and tools

Add tools and reusable instructions for teaching and research

CUNY AI Lab Sandbox

Developed by Zach Muhlbauer

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

### Tools & Skills

Skills

Reusable instructions for tasks or procedures.

Tools

Operations such as web search, code execution, or database queries.

Test a request that needs your skill or tool. Check what your model used and whether its response is correct.

[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 4

### Review Previous Work

Continue from your chat adventure and source collection. Workshop 3 adds tools and skills. Select STEM Adventure Games — Advanced and review its system prompt.

- Identify instructions for opening Prism Laboratory.

- Review attached STEM Wikipedia Experiments collection.

- Distinguish source material, skill instructions, and tool operations.

Use a private copy when adapting this configuration.

---

## Configuring skills and tools — 5

### Connect Resources

System prompt

Tell your model when to open a game or consult sources.

Knowledge

STEM Wikipedia Experiments contains scientific and historical sources.

Skill

Extend STEM Adventures describes how to change experimental procedures.

Tool

STEM Adventure opens a game and applies its rules.

Use provided game files to describe rooms, objects, and rules.

---

## Configuring skills and tools — 6

### Enable Tools

![STEM Adventure Games — Advanced with full message box and Tools menu open; white outlines and arrows identify Integrations and enabled STEM Adventure tool.](images/current/integrations-advanced-hidpi-2026-09-16.svg)

**Alt text:** STEM Adventure Games — Advanced with full message box and Tools menu open; white outlines and arrows identify Integrations and enabled STEM Adventure tool.

With STEM Adventure Games — Advanced selected, open Integrations beside +. Under Tools, confirm STEM Adventure is enabled for this chat.

---

## Configuring skills and tools — 7

### Inspect Game Rules

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](images/current/stem-game-2026-09-14.png)

**Alt text:** Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.

Send Begin Prism Laboratory to your selected model. Enter help inside its command box, then go north and take prism. [Open game](examples/adventure/preview.html) · [Read game file](examples/adventure/prism.json)

---

## Configuring skills and tools — 8

### Test Game Commands

- Enter **restart**, then try **record result** before completing required steps.

- Follow [winning command sequence](skills/reference.html#game-commands). Immediately after take prism, repeat take prism and check its response.

- Enter **save** to download your play record.

- Enter **restart**, then **load** and choose your saved file.

- Enter **inventory**. Check restored items, room, and completion. Enter **undo** to reverse your last move.

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

- Change size of an opening that admits light, called an aperture.

- Inspect a failed command and its prerequisite.

- Check a historical claim against source material.

Describe expected behavior before testing.

---

## Configuring skills and tools — 11

### Define Skills

Skills contain reusable Markdown instructions for tasks or procedures.

Models can load attached skills when needed. Enable a skill under Integrations → Skills to include its full instructions in this chat.

Markdown is plain text with formatting such as headings and lists.

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

[Read blank template](skills/reference.html#write-instructions)

[Read complete skill](examples/stem-game-skill.md)

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

Specify one change to your experiment. Use fields listed in [scenario instructions](examples/stem-game-skill.md) when editing your game file.

```text
1. Identify one experimental decision to change.
2. Check source material for that procedure.
3. Revise scenario JSON using fields listed in attached instructions.
4. List commands that complete your game and one command that should fail, then open your game.
5. Compare a submitted record with expected behavior.
```

---

## Configuring skills and tools — 16

### Specify Format

Separate your game file, source evidence, and test results.

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

### Clone Custom Models

![Workspace Models filtered to STEM Adventure Games — Advanced with More menu open; white outline and arrow identify Clone.](images/current/model-clone-advanced-hidpi-2026-09-16.svg)

**Alt text:** Workspace Models filtered to STEM Adventure Games — Advanced with More menu open; white outline and arrow identify Clone.

In Workspace → Models, open ⋯ beside STEM Adventure Games — Advanced and choose Clone.

---

## Configuring skills and tools — 18

### Save Private Copy

![Access Control on an unsaved STEM Adventure Games copy shows Private and No access grants. Private to you.](images/current/model-private-2026-09-16-annotated.svg)

**Alt text:** Access Control on an unsaved STEM Adventure Games copy shows Private and No access grants. Private to you.

Rename model and ID. Open Access, keep Private, and remove copied users or groups from Access List. Close Access and choose Save & Create.

---

## Configuring skills and tools — 19

### Draft Skills

Kale Skill Builder is a custom model that drafts skills for tasks you describe.

Select model ID on bottom right of message box. Choose Kale Skill Builder.

Attach [scenario instructions](examples/stem-game-skill.md) before sending this example.

```text
Draft a skill for adding an aperture comparison to STEM Adventure. Use attached scenario instructions and preserve existing game rules. Include when to use it, 3–5 steps, expected output, and two proposed tests. Do not claim unrun tests passed.
```

[Open Kale Skill Builder](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-skill-builder) · [Read tested skill](examples/stem-game-skill.md)

[Review draft evaluation](skills/reference.html#check-skill-drafts)

[Download skill instructions](examples/stem-game-skill.md)

---

## Configuring skills and tools — 20

### Create Skills

![Create Skill form in Workspace with empty name, identifier, description, and Instructions fields; outline marks Instructions.](images/current/skill-create-2026-09-16-annotated.svg)

**Alt text:** Create Skill form in Workspace with empty name, identifier, description, and Instructions fields; outline marks Instructions.

Open Workspace → Skills → Create. Name your skill and add an identifier and description. Paste your saved draft into Instructions, review Access, and choose Save & Create.

---

## Configuring skills and tools — 21

### Attach Skills

- Open your private copy under **Workspace → Models**.

- Replace Extend STEM Adventures with your saved draft under **Skills**. Update System Prompt to name your skill.

- Set **Function Calling** to **Native** under **Advanced Parameters**.

- Select **Save & Update** and test a request that uses your skill.

Native function calling lets your model call tools and load attached skill instructions.

[Attach skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 22

### Extend Procedures

Open your private copy. Attach [Prism Laboratory JSON](examples/adventure/prism.json) and enable your saved draft under **Integrations → Skills**. Send this request.

```text
Add an aperture comparison to Prism Laboratory using Newton: Experimental Variants. Keep existing rooms and actions. Provide scenario JSON, a winning command sequence, and one command that must fail before its prerequisite. Open the revised game.
```

[Read skill instructions](examples/stem-game-skill.md) · [Download tested scenario](examples/adventure/aperture.json)

[Download Prism Laboratory](examples/adventure/prism.json)

---

## Configuring skills and tools — 23

### Test Skills

Use your private copy for both tests. Remove any additional skills from this copy before comparing your draft.

- Remove your skill under **Workspace → Models → Skills**. Save, start a new chat, and confirm it is off under **Integrations → Skills**. Repeat your extension request with Prism Laboratory JSON attached.

- Attach your skill again, save, and repeat that request in another new chat. Attach Prism Laboratory JSON and enable your saved draft under Integrations → Skills.

- Keep base model, system prompt, sources, and tool unchanged.

- Run winning and blocked commands. Compare expected and observed results.

Save generated scenarios and play records.

---

## Configuring skills and tools — 24

### Create Adventure Tools

Tool Creator is a custom model that drafts Python tools for tasks you describe. Save its output as a draft for review and testing. Use tested STEM Adventure code for installation in this workshop.

```text
Create a minimalist text adventure tool for Open WebUI. Return an interactive HTMLResponse and a description for the model. Track rooms, inventory, prerequisites, and completion. Use one command line with help, undo, restart, save, load, and discuss commands. Keep scenario JSON separate from executable code.
```

[Open Tool Creator](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-tool-creator) · [Download tested tool](examples/tools/stem_adventure.py)

[Review code evaluation](skills/reference.html#check-generated-code)

[Read tested code](examples/tools/stem_adventure.py)

---

## Configuring skills and tools — 25

### Install Tool Code

- Open **Workspace → Tools → Create**.

- Enter Name, ID, and Description.

- Paste and review [tested STEM Adventure code](examples/tools/stem_adventure.py). Keep your creator draft separate.

- Select **Save & Create**.

- Enable your tool through **Integrations → Tools**.

Use a private copy when changing code. Attach reusable tools under Tools in your model editor.

---

## Configuring skills and tools — 26

### Inspect Tool Results

Start a new chat with your private model. Under Integrations → Tools, select only your installed adventure tool. Send Begin Prism Laboratory, then open its tool-call details.

- Check which scenario was passed to render_stem_adventure.

- Compare returned result with your request.

- Confirm displayed game matches that scenario.

Save any error before revising your request.

---

## Configuring skills and tools — 27

### Compare Game Records

Attach saved play records from original and revised games, then send this request.

```text
Review both play records. Which commands and prerequisites changed? Which observations were programmed? Which historical claims can the uploaded sources support?
```

Check your model’s account against commands and source passages. Keep expected and observed results separate.

---

## Configuring skills and tools — 28

### Record Test Results

| Record | Include |
| --- | --- |
| Configuration | Model ID, system prompt, documents, skill instructions, and enabled tools. |
| Action | Request, instructions used, tool calls and results, and final response. |
| Judgment | What you expected, what happened, and any change you plan to test. |

Before sharing, confirm others can access your model, collections, skills, and tools. Repeat relevant tests after updates.

---

## Configuring skills and tools — 29

### Repeat Tests

- Save prompts, sources, skills, and tool settings

- Compare expected and observed behavior

- Revise instructions from recorded failures

- Verify shared access with intended users

- Retest after model or tool updates

[Browse system-prompt examples](examples.html) · [Return to Composing system prompts](.)
