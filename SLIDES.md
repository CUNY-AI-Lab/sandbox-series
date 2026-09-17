# Sandbox Workshops

## Composing system prompts — 1

### Getting Started with the CUNY AI Lab Sandbox

Sandbox Workshop Series  Part 1/3

Developed and led by  Zach Muhlbauer

New Media Lab · Room 7388.01
CUNY Graduate Center

Thursday, September 17, 2026   2:30–4:00 p.m.

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

- Review Workspace model cards

- Choose teaching or research examples

- Clone model cards and test revisions

Check monthly usage at [Model Access](https://tools.ailab.gc.cuny.edu/model-access).

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

System prompts are setup instructions that describe how a model should behave.

### User Prompts

Questions or tasks you enter in chat.

### Custom Models

You create a custom model by choosing a base model, such as Gemma, and adding instructions and documents for it to use.

[Basic Concepts](https://ailab.gc.cuny.edu/sandbox-docs/basic-concepts/) · [Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Composing system prompts — 6

### Select Models

![Sandbox logo, message box, and Gateway model selector; enlarged detail shows current model choices with model ID outlined and marked by an arrow.](images/current/gateway-selector-hidpi-2026-09-16.svg)

**Alt text:** Sandbox logo, message box, and Gateway model selector; enlarged detail shows current model choices with model ID outlined and marked by an arrow.

Select model ID on bottom right of message box. Choose Gateway from filters, then select Gemma 4 26B A4B IT.

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

![Sandbox logo, message box, and Gateway model selector; enlarged detail shows Compare beside search field outlined and marked by an arrow.](images/current/gateway-selector-compare-hidpi-2026-09-16.svg)

**Alt text:** Sandbox logo, message box, and Gateway model selector; enlarged detail shows Compare beside search field outlined and marked by an arrow.

Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two Gateway models. If Compare is unavailable, send identical prompts in separate new chats.

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

### Winograd Schema Challenge

This challenge tests how models interpret ambiguous pronouns using context and common-sense knowledge. Changing one or two words between paired sentences changes who a pronoun refers to.

In our question, either person could be late.

- Which person does each model choose?

- What assumption supports its answer?

[Levesque, Davis, and Morgenstern (2012)](https://www.cs.nyu.edu/faculty/davise/papers/WSKR2012.pdf)

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

### Compare Outputs

### Gemma’s Response

![Gemma 3 27B response recommending walking, with model name and generation time.](images/showcase/car-wash-gemma-response.png)

**Alt text:** Gemma 3 27B response recommending walking, with model name and generation time.

### Qwen’s Response

![Qwen3.5 27B response recommending driving, with model name and generation time.](images/showcase/car-wash-qwen-response.png)

**Alt text:** Qwen3.5 27B response recommending driving, with model name and generation time.

---

## Composing system prompts — 13

### Compare Models

Start a new chat, select two models, and send this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

Save both responses with your question and selected model IDs before adding system prompt instructions.

---

## Composing system prompts — 14

### Add System Prompt

![Sandbox logo, message box, and open Controls panel; white annotations identify Controls button and System Prompt field.](images/current/chat-controls-instructions-2026-09-16.svg)

**Alt text:** Sandbox logo, message box, and open Controls panel; white annotations identify Controls button and System Prompt field.

Select **Controls** at top right of chat. Paste these instructions into **System Prompt**, then close Controls.

```text
Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer briefly without inventing context.
```

---

## Composing system prompts — 15

### Regenerate Responses

![Mistral Large 3 response recommending walking, with original question and message box; enlarged recommendation and response controls show Regenerate outlined and marked by an arrow.](images/current/regenerate-mistral-gateway-hidpi-2026-09-16.svg)

**Alt text:** Mistral Large 3 response recommending walking, with original question and message box; enlarged recommendation and response controls show Regenerate outlined and marked by an arrow.

Select Regenerate beneath each original response, then choose Try Again. Keep your original question, selected models, and other settings unchanged.

---

## Composing system prompts — 16

### Compare Responses

- Compare responses before and after adding system prompt instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

---

## Composing system prompts — 17

### Open Workspace

![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](images/current/workspace-sidebar-2026-09-15-annotated.svg)

**Alt text:** Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar

Select Workspace in left sidebar.

---

## Composing system prompts — 18

### Review Custom Models

Choose **Models** to find custom model cards. Each combines a base model with setup instructions and any attached resources.

Review **Base Model** and **System Prompt** before choosing a card to adapt.

Continue in chat if Workspace is unavailable.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Composing system prompts — 19

### Model Configuration

![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.](images/current/model-create-hidpi-2026-09-16.svg)

**Alt text:** New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.

Review Model Name, Base Model, and System Prompt when configuring your copy.

---

## Composing system prompts — 20

### Choose Examples

**Teaching**

[STEM Adventure Games](https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games)

Explore scientific experiments through a text adventure with numbered choices.

**Research**

[Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions)

Compare passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.

Choose either model for your own work.

---

## Composing system prompts — 21

### Clone Model Cards

- In Workspace → Models, find your chosen model and open ⋯ → **Clone**.

- Rename your copy and give it a unique ID.

- Read **System Prompt** and identify one instruction to revise.

- Review **Access**, keep Private, remove copied access grants, and select **Save & Create**.

Save an initial response before changing instructions.

[Model management](https://docs.openwebui.com/features/workspace/models/)

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

### STEM Adventure Games

![STEM Adventure Games presents Pasteur’s flask experiment with four numbered choices, CUNY AI Lab icon, and message box visible.](images/current/stem-original-play-clean-2026-09-17.png)

**Alt text:** STEM Adventure Games presents Pasteur’s flask experiment with four numbered choices, CUNY AI Lab icon, and message box visible.

For STEM Adventure Games, type Start an adventure. Choose an experiment, then reply with a number or describe what you want to do.

---

## Composing system prompts — 25

### Read Game Instructions

```text
Simulate an interactive game-based learning experience through Choose Your Own STEM Adventure games featuring historically significant scientific experiments.

Each stage presents 4 numbered choices based on historically accurate experimental decisions.

After each choice, briefly state what the player observes, what the result suggests, and what question remains open.
```

What should happen after you choose an action?

[Read full system prompt](examples.html#stem-chat)

---

## Composing system prompts — 26

### Adapt Research Prompts

For [Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions), paste one pair from [sample revisions](examples/research/sample-revisions.md) into your copy.

- Ask it to classify one change and quote evidence.

- Check quotations against both passages.

- Identify an instruction to revise if its classification is unclear.

[Read full system prompt](examples.html#wikipedia-revisions)

---

## Composing system prompts — 27

### Draft System Prompts

---

## Composing system prompts — 28

### Define Prompt Components

Use either example. Choose one component to change in your cloned model.

- **Purpose** — What your model should help users do.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Format** — Length and presentation.

---

## Composing system prompts — 29

### Define Purpose

Describe what your model should help users do.

- Who will use this model?

- Which task or question will they explore?

- What prior knowledge can you assume?

```text
Guide a short text adventure in which players explore how a prism changes a beam of sunlight.
```

For research, name your question, source material, and intended users.

---

## Composing system prompts — 30

### Write Procedures

Which steps should your model follow?

```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer four numbered choices and wait.
4. Describe what players observe after each choice.
```

For research, check inputs, quote changed passages, then classify changes.

---

## Composing system prompts — 31

### Set Constraints

Specify how your model should handle missing evidence.

```text
Do not invent historical details when sources are missing.
Distinguish documented events from invented scenes and choices.
If a source is unavailable, explain what cannot be checked.
```

For research, request missing excerpts and mark uncertain classifications.

Test a request that asks for a detail absent from your sources.

---

## Composing system prompts — 32

### Specify Format

Specify response structure and length.

```text
Write a short scene followed by four numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```

For research, use Before and After quotations, categories, and brief explanations.

---

## Composing system prompts — 33

Refine

### Refine Instructions

---

## Composing system prompts — 34

### Extend Instructions

Specify what your model should do when a request needs additional guidance.

- **Teaching** — Explain how to offer a hint or revisit an earlier choice.

- **Research** — Explain when to request missing passages or mark a classification uncertain.

Select Save & Update, then test that condition in a new chat. After revising, save again and repeat your request.

---

## Composing system prompts — 35

Watch Out

### Review Common Problems

### Prioritize Instructions

Check instructions for conflicts. Prioritize essential steps and test whether your model follows them.

### Resolve Contradictions

Check whether requested detail fits your length limit. Revise requirements that cannot be met together.

### Test User Requests

Test likely requests, including questions about missing evidence.

### Retest Revised Prompts

Save each prompt version with its responses. Revise when a test reveals a problem, then repeat that test.

---

## Composing system prompts — 36

### Save Prompts

Save changes to your cloned model. Review **Access** and select **Save & Update**. Reuse this model when adding documents in Workshop 2.

---

## Composing system prompts — 37

### Share Custom Models

- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and any attached collections.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Composing system prompts — 38

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

## Composing system prompts — 39

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

Open your private copy of **STEM Adventure Games** or **Compare Wikipedia Edits**.

Review **Base Model** and **System Prompt**. Keep instructions from Workshop 1. Leave Skills and Tools unselected.

[Review system prompts](examples.html)

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

![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, List of experiments, procedural variations, and software checks.](images/current/stem-knowledge-2026-09-14.png)

**Alt text:** STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, List of experiments, procedural variations, and software checks.

Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments.

---

## Curating knowledge collections — 10

### Review Source Roles

Use sources for different questions.

List of experiments

Choose experiments, scientists, and questions to investigate.

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

List of experiments once imported a Wikimedia rate-limit error. Article text was restored on September 17, 2026. Check contents after every import.

---

## Curating knowledge collections — 12

### Review Attached Knowledge

![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.](images/current/knowledge-attachments-3x-2026-09-16.svg)

**Alt text:** STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.

In your STEM copy, select STEM Wikipedia Experiments under Knowledge and choose Save & Update. Skills and Tools are added in Workshop 3.

---

## Curating knowledge collections — 13

### Check Game Sources

In your STEM copy, start an adventure about light and colour. Choose one action, then ask about its historical sources.

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

Choose documents for your teaching or research task.

- Use [Newton: Light and Colour](examples/knowledge/newton-light-colour.md) for apparatus and observations.

- Use [Newton: Experimental Variants](examples/knowledge/newton-experimental-variants.md) for changes to experimental procedures.

For Compare Wikipedia Edits, use [sample revision excerpts](examples/research/sample-revisions.md) and [classification criteria](examples/research/system-prompt.txt). Read documents before uploading; distinguish summaries from original accounts.

[Download Light and Colour](examples/knowledge/newton-light-colour.md) · [Download Experimental Variants](examples/knowledge/newton-experimental-variants.md)

---

## Curating knowledge collections — 17

### Create Knowledge Collections

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](images/current/knowledge-create-3x-2026-09-16.png)

**Alt text:** Current Create a knowledge base form with name, description, Private access, and Create Knowledge

Open Workspace → Knowledge → Create. Enter a name and description, keep access Private, then select Create Knowledge.

---

## Curating knowledge collections — 18

### Attach Knowledge Collections

- Open Workspace → Knowledge → your collection. Use Add Content to upload documents, then wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your chosen custom model, and select your collection under **Knowledge**. Remove collections unrelated to your question.

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

Review your model and source collection. This example builds on our chat adventure and source collection. Workshop 3 adds tools and skills. Select STEM Adventure Games — Advanced and review its system prompt.

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

![STEM Adventure Games — Advanced with CUNY AI Lab logo, message box, and Integrations menu showing Tools and Skills.](images/current/integrations-advanced-2026-09-17.png)

**Alt text:** STEM Adventure Games — Advanced with CUNY AI Lab logo, message box, and Integrations menu showing Tools and Skills.

With STEM Adventure Games — Advanced selected, open Integrations beside +. Under Tools, confirm STEM Adventure is enabled for this chat.

---

## Configuring skills and tools — 7

### Inspect Game Rules

![Prism Laboratory running in STEM Adventure Games — Advanced, with room description, move status, command box, and chat message box.](images/current/stem-advanced-clean-2026-09-17.png)

**Alt text:** Prism Laboratory running in STEM Adventure Games — Advanced, with room description, move status, command box, and chat message box.

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

![Workspace Models filtered to STEM Adventure Games — Advanced, with More menu open and Clone visible.](images/current/model-clone-advanced-2026-09-17.png)

**Alt text:** Workspace Models filtered to STEM Adventure Games — Advanced, with More menu open and Clone visible.

In Workspace → Models, open ⋯ beside STEM Adventure Games — Advanced and choose Clone.

---

## Configuring skills and tools — 18

### Save Private Copy

![Access Control on an unsaved STEM Adventure Games copy shows Private and No access grants. Private to you.](images/current/model-private-3x-2026-09-16.svg)

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

![Create Skill form in Workspace with empty name, identifier, description, and Instructions fields; outline marks Instructions.](images/current/skill-create-3x-2026-09-16.svg)

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

CAIL Tool Creator is a custom model that drafts Python tools for tasks you describe. Save its output as a draft for review and testing. Use tested STEM Adventure code for installation in this workshop.

```text
Create a minimalist text adventure tool for Open WebUI. Return an interactive HTMLResponse and a description for the model. Track rooms, inventory, prerequisites, and completion. Use one command line with help, undo, restart, save, load, and discuss commands. Keep scenario JSON separate from executable code.
```

[Open CAIL Tool Creator](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-tool-creator) · [Download tested tool](examples/tools/stem_adventure.py)

[Review code evaluation](skills/reference.html#check-generated-code)

---

## Configuring skills and tools — 25

### Install Tool Code

- Open **Workspace → Tools → Create**.

- Enter a unique Name and ID, then add a Description.

- Paste provided [tested STEM Adventure code](examples/tools/stem_adventure.py). Save your creator draft for separate review.

- Select **Save & Create**.

- In your private model, replace STEM Adventure under **Tools** with your installed copy. Update System Prompt to name it and select **Save & Update**.

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
