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

A base model generates responses. A custom model adds instructions and resources to a chosen base model.

Test whether your selected model follows these instructions.

[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/)

[Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

---

## Composing system prompts — 6

### Select Models

![Sandbox chat with model ID at bottom right of message box](images/current/chat-page.png)

**Alt text:** Sandbox chat with model ID at bottom right of message box

Select model ID on bottom right of message box.

Type a request, send it, then ask a follow-up. Open **New Chat** when you want to begin with fresh conversation history.

[Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/)

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

![Sandbox logo, message box, and model selector with Compare button marked by an arrow](images/current/model-selector-compare-2026-09-14.svg)

**Alt text:** Sandbox logo, message box, and model selector with Compare button marked by an arrow

Start a new chat. Select Compare beside search field, then choose two models.

Select model ID on bottom right of message box.

Select **Compare** beside search field, then choose two small models.

If Compare is unavailable, send identical prompts in separate new chats.

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

Ask both models this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

What do you think this person wants to accomplish?

---

## Composing system prompts — 12

### Gemma’s Response

![Gemma recommends walking to a car wash](images/showcase/car-wash-gemma.png)

**Alt text:** Gemma recommends walking to a car wash

---

## Composing system prompts — 13

### Qwen’s Response

![Qwen recommends driving to a car wash](images/showcase/car-wash-qwen.png)

**Alt text:** Qwen recommends driving to a car wash

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

![Current model creation form showing Name, Base Model, and System Prompt](images/current/model-editor.png)

**Alt text:** Current model creation form showing Name, Base Model, and System Prompt

Select Create in Models. Choose a name and base model, then enter your system prompt.

- **Name** — Use a name that students or colleagues will recognize.

- **Base Model** — Choose a model you have tested.

- **System Prompt** — Add instructions you tested in chat.

A custom model combines these choices. Creating it does not train a new base model.

[Model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Composing system prompts — 22

### Create Custom Models

Custom models combine a base model with instructions, documents, and tools.

- Enter a name and description that students or colleagues will recognize.

- Select a base model and add your tested system prompt.

- Add prompt suggestions for tasks your model should support.

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

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](images/current/stem-game-2026-09-14.png)

**Alt text:** Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.

Send Begin Prism Laboratory to open this game. Enter help inside its command box to list available commands.

Enter commands inside Prism Laboratory. Type help to list commands, including save, load, and discuss.

---

## Composing system prompts — 26

### Inspect System Prompt

![STEM Adventure Games model editor showing DeepSeek V4 Pro 0813 under Base Model and opening system prompt instructions.](images/current/stem-model-2026-09-14.png)

**Alt text:** STEM Adventure Games model editor showing DeepSeek V4 Pro 0813 under Base Model and opening system prompt instructions.

Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt. Base model shown here was selected on September 14, 2026.

---

## Composing system prompts — 27

### Read Game Instructions

Read this excerpt from STEM Adventure Games.

```text
When a user asks to begin or play, call render_stem_adventure with scenario_json empty. This opens Prism Laboratory inside chat.

STEM Adventure controls rooms, inventory, prerequisites, observations, and completion. Moves inside its interface do not automatically enter model context.
```

Which instructions guide model behavior? Which actions require a tool?

[Read full system prompt](examples.html#stem-system)

---

## Composing system prompts — 28

### Test Game Instructions

Send Begin Prism Laboratory, then enter help and go north inside your game.

- Does your command change rooms or inventory?

- Does help list available actions?

- Which observations come from programmed rules?

- Which historical claims require source checks?

Type discuss inside your game to place your run in chat, then send it.

---

## Composing system prompts — 29

### Adapt Research Prompts

Choose a research task, such as comparing article abstracts, checking how you coded a passage, or documenting a method.

- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.

Save your source material, prompt, response, and assessment together.

---

## Composing system prompts — 30

### Draft System Prompts

---

## Composing system prompts — 31

### Define Prompt Components

Adapt STEM Adventure Games through these components.

- **Context** — Experiment, historical setting, and intended users.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Tone and format** — Language, length, and presentation.

---

## Composing system prompts — 32

### Define Context

Describe what your model should help users do.

- Who will use this model?

- Which experiment or research question will they explore?

- What prior knowledge can you assume?

```text
Guide an interactive adventure about [experiment].
Users will explore [question] through [available choices or methods].
Use [source material] for historical context.
```

---

## Composing system prompts — 33

### Write Procedures

Write numbered steps for your model to follow.

- What information should users provide first?

- Which steps must happen before your model responds?

- How should your model respond to different requests?

```text
1. Open Prism Laboratory when users ask to play.
2. Let users enter commands inside the game.
3. Ask users to send a play record before interpreting their choices.
4. Check relevant sources before making historical claims.
```

---

## Composing system prompts — 34

### Set Constraints

Specify how your model should handle missing evidence.

```text
Do not invent historical details when sources are missing.
Distinguish documented events from choices created for the game.
If a source is unavailable, explain what cannot be checked.
```

Test a request that asks for a detail absent from your sources.

---

## Composing system prompts — 35

### Set Tone

Describe how your model should address players.

```text
Address the player as “you.”
Use concise language for scenes and choices.
Explain unfamiliar scientific terms when they first appear.
```

Which terms need explanation for your intended users?

---

## Composing system prompts — 36

### Specify Format

Specify how your model should discuss a submitted record.

```text
Observed decision: [Command and result]
Prerequisite: [Condition required for that action]
Source comparison: [What historical evidence supports]
Question: [One limitation to examine]
```

---

## Composing system prompts — 37

Refine

### Refine Instructions

---

## Composing system prompts — 38

### Extend Instructions

- Specify what happens when a player asks for a hint.

- Explain how to revisit an earlier decision.

- Require source checks when players ask about historical claims.

- Test how your model responds when evidence is missing.

---

## Composing system prompts — 39

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

## Composing system prompts — 40

### Save Prompts

- Save your prompt text, model ID, and responses.

- Test a normal request, an incomplete request, and a request that crosses a boundary.

- Revise one instruction and repeat your test in a new chat.

Save your tested prompt in a private custom model. Choose a base model, review **Access**, and select **Save & Create**. Reuse this model when adding documents in Workshop 2.

---

## Composing system prompts — 41

### Share Custom Models

- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and attached collections, skills, and tools.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Composing system prompts — 42

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

## Composing system prompts — 43

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

### Review Custom Models

Choose a question about documents you want your custom model to use.

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

![Current model editor showing base model, system prompt, and Knowledge](images/current/model-editor.png)

**Alt text:** Current model editor showing base model, system prompt, and Knowledge

Review Base Model and System Prompt before attaching documents.

Review **Base Model (From)** and **System Prompt**. Start a new chat. Select model ID on bottom right of message box. Choose your custom model.

Ask a question about your source material. Save this response before attaching documents.

[Model configuration](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Curating knowledge collections — 7

### Select Documents

Choose documents with clear headings and readable text.

- Course syllabi, readings, or assignment instructions

- Research papers, methods, or annotated bibliographies

- Markdown, plain text, or well-formatted PDFs

Check scans and complex PDFs before uploading. Convert them to text if necessary.

[Document formats](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating knowledge collections — 8

### Retrieve Source Passages

- Uploaded documents are divided into passages and indexed for search.

- Retrieval finds passages relevant to a question.

- Your model uses retrieved passages to generate a response.

Check whether retrieved passages address your question and support claims in each response.

[Open WebUI retrieval](https://docs.openwebui.com/features/workspace/knowledge/)

---

## Curating knowledge collections — 9

### Open STEM Collection

![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, Newton’s optical experiments, procedural variations, and software checks.](images/current/stem-knowledge-2026-09-14.png)

**Alt text:** STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, Newton’s optical experiments, procedural variations, and software checks.

Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments. Inspect each file before using it as evidence.

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

Keep source summaries and game documentation distinguishable.

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

![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge, STEM Adventure enabled under Tools, and Extend STEM Adventures enabled under Skills.](images/current/stem-attachments-2026-09-14.png)

**Alt text:** STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge, STEM Adventure enabled under Tools, and Extend STEM Adventures enabled under Skills.

Open Workspace → Models → STEM Adventure Games. Scroll to Knowledge and review its attached collection. For your own model, select a collection and choose Save & Update.

---

## Curating knowledge collections — 13

### Check Game Sources

Compare Prism Laboratory with Newton’s account.

```text
Which apparatus details from Newton’s account does Prism Laboratory simplify? Identify the uploaded source and quote a relevant passage. If it is unavailable, say so.
```

Open cited material. Does it support your model’s response?

[Read Newton source entry](examples/knowledge/newton-light-colour.md) · [Review source register](examples/knowledge/source-register.md)

---

## Curating knowledge collections — 14

### Check Citations

Check a response from STEM Adventure Games against its cited passage.

- Which apparatus did Newton describe?

- Which experimental changes did he examine?

Open each citation. Compare quoted wording and interpretation with source text.

---

## Curating knowledge collections — 15

### Compare Research Methods

Build a collection from research papers or methods you want to compare.

- Identify a question that requires consulting those sources.

- Ask your model to compare specific claims or methods.

- Check its citations against your uploaded documents.

[Knowledge collections for research](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating knowledge collections — 16

### Organize Documents

Begin with a few documents and test how your model uses them.

- Name files so students or colleagues can identify them.

- Use headings to distinguish sections.

- Check whether your model retrieves relevant passages before adding more documents.

---

## Curating knowledge collections — 17

### Check Retrieval Problems

| Observation | Next check |
| --- | --- |
| No relevant source appears | Check whether files finished processing, are attached, and are accessible. Review your search query. |
| A source is present but misread | Read cited passages in full and revise instructions. |
| A response invents a citation | Open cited documents and verify quotations and page numbers. |

Save unsuccessful responses before revising anything.

---

## Curating knowledge collections — 18

### Build Knowledge Collections

Choose documents that explain your course or research project and describe what you want to examine.

---

## Curating knowledge collections — 19

### Choose Reference Materials

Add sources that support your adventure.

- Use [Newton: Light and Colour](examples/knowledge/newton-light-colour.md) for apparatus and observations.

- Use [Newton: Experimental Variants](examples/knowledge/newton-experimental-variants.md) for procedural changes.

- Use [Evaluate Game Procedures](examples/knowledge/game-procedure-evaluation.md) for software checks.

Download entries you want your model to use. Create your own collection after reviewing these materials.

---

## Curating knowledge collections — 20

### Describe Experimental Context

Separate documented experiments from invented game settings.

- Which question motivated an experiment?

- Which instruments and materials appear in its source?

- Which rooms or actions were created for play?

Prism Laboratory simplifies an apparatus with two boards and two prisms.

---

## Curating knowledge collections — 21

### Describe Scientific Methods

An aperture is an opening that admits light. Compare procedures before changing its size in your game.

- Which variable changes when an aperture narrows?

- Which conditions stay fixed?

- What would a changed observation support?

[Read experimental variants](examples/knowledge/newton-experimental-variants.md)

---

## Curating knowledge collections — 22

### Identify Historical Sources

Use Women in science to examine contributors, institutions, and recognition.

- Who performed or supported this work?

- Which barriers affected participation?

- What can these sources establish about a particular experiment?

---

## Curating knowledge collections — 23

### Select Research Materials

Describe your research project and identify sources your model should use.

Research context

Describe your question, scope, and method.

Instructions

Include a codebook, protocol, or criteria for comparing sources.

Sources

Identify documents and passages you want to examine.

---

## Curating knowledge collections — 24

### Create Knowledge Collections

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](images/current/knowledge-create.png)

**Alt text:** Current Create a knowledge base form with name, description, Private access, and Create Knowledge

Enter a collection name and description, set access, and select Create Knowledge.

- Open **Workspace → Knowledge → Create**.

- Name your collection and describe its contents and purpose.

- Keep it **Private** while building, then choose **Create Knowledge**.

[Create and manage collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating knowledge collections — 25

### Attach Knowledge Collections

- Open Workspace → Knowledge → your collection. Use Add Content to upload documents, then wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your custom model, and select your collection under **Knowledge**.

- Choose **Save & Update**, then start a new chat with your custom model.

[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating knowledge collections — 26

### Test Retrieval

- Ask a question answered by one source. Verify each answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask about something absent from your documents. Check whether your model acknowledges missing information.

Repeat your first question without changing models or system prompts. Record which documents you used, which passages were retrieved, and whether those passages support your model’s response.

---

## Curating knowledge collections — 27

### Share Knowledge Collections

Share your collection with people who will use your custom model.

- Use **Add Access** to grant users or groups **Read** access.

- Ask someone you shared with to check access to your model and collection.

- Choose **Public** only for documents intended for all signed-in Sandbox users.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Curating knowledge collections — 28

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

STEM Adventure Games is a custom model. Prism Laboratory is its starting game. Open this model and review its system prompt.

- Identify instructions for opening Prism Laboratory.

- Review attached STEM Wikipedia Experiments collection.

- Distinguish source material, skill instructions, and tool operations.

Use your own configuration when adapting these examples.

---

## Configuring skills and tools — 5

### Connect Resources

System prompt

Tell STEM Adventure Games when to open a game or consult sources.

Knowledge

STEM Wikipedia Experiments contains scientific and historical sources.

Skill

Extend STEM Adventures describes how to change experimental procedures.

Tool

STEM Adventure opens a game and applies its rules.

Scenario JSON is a text file describing rooms, items, actions, and rules.

---

## Configuring skills and tools — 6

### Enable Tools

![Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter](images/current/integrations.png)

**Alt text:** Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter

Open Integrations beside +. Under Tools, confirm STEM Adventure is enabled for this chat.

A tool runs an operation, such as a search, a calculation, or a search within a knowledge collection.

Open **Integrations** beside + to choose tools for this chat. Attach reusable tools under **Tools** in your model editor.

Availability depends on account permissions, configuration, and model support.

[Enable tools in chat or on a model](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 7

### Inspect Game Rules

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](images/current/stem-game-2026-09-14.png)

**Alt text:** Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.

Send Begin Prism Laboratory to STEM Adventure Games. Enter help inside its command box.

STEM Adventure applies rules for rooms, inventory, actions, and completion.

- Enter go north to reach Storeroom.

- Enter take prism to add a prism to inventory.

- Enter help to list available actions.

- Try record result before completing required steps.

[Open game](examples/adventure/preview.html) · [Read scenario JSON](examples/adventure/prism.json)

---

## Configuring skills and tools — 8

### Test Game Commands

- Enter **restart**, then try **record result** before completing required steps.

- Follow [winning command sequence](examples/adventure/winning-commands.json). Try taking an item twice.

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

Specify how your model should change an experiment. Follow [supported fields](examples/stem-game-skill.md) when editing scenario JSON.

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

Kale Skill Builder is a custom model that drafts skills for tasks you describe.

Select model ID on bottom right of message box.

Attach [scenario instructions](examples/stem-game-skill.md) before sending this example.

```text
Draft a skill for STEM Adventure that extends one experimental procedure or examines a submitted play record. Use render_stem_adventure(scenario_json: str = ""). Preserve game rules. Include trigger, 3–5 steps, output, and two proposed tests. Do not invent successful tool calls.
```

[Open Kale Skill Builder](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-skill-builder) · [Read tested skill](examples/stem-game-skill.md)

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

![Extend STEM Adventures in Workspace Skills, showing its name, description, and Markdown instructions for game play, procedural extensions, and submitted records.](images/current/stem-skill-2026-09-14.png)

**Alt text:** Extend STEM Adventures in Workspace Skills, showing its name, description, and Markdown instructions for game play, procedural extensions, and submitted records.

Use this saved example when creating your own skill. Review its name, description, and instructions.

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

Native function calling lets your model call tools and load attached skill instructions.

[Attach skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Configuring skills and tools — 21

### Extend Procedures

Open STEM Adventure Games. Attach [Prism Laboratory JSON](examples/adventure/prism.json) and enable Extend STEM Adventures under **Integrations → Skills**. Send this request.

```text
Add an aperture comparison to Prism Laboratory using Newton: Experimental Variants. Keep existing rooms and actions. Provide scenario JSON, a winning command sequence, and one command that must fail before its prerequisite. Open the revised game.
```

[Read skill instructions](examples/stem-game-skill.md) · [Download tested scenario](examples/adventure/aperture.json)

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

Use a private model copy for this comparison.

- Remove your skill under **Workspace → Models → Skills**. Save and run your extension request in a new chat.

- Attach your skill again, save, and repeat that request in another new chat.

- Keep base model, system prompt, sources, and tool unchanged.

- Run winning and blocked commands. Compare expected and observed results.

Save generated scenarios and play records.

---

## Configuring skills and tools — 24

### Check Skill Drafts

This example has no commands or events but reports completion. Can a skill establish that play occurred?

```text
{"commands":[],"events":[],"result":{"complete":true}}
```

An empty history cannot establish completion. Request a full record or replay.

Send this example to Kale Skill Builder with your skill draft. Check whether revised instructions flag missing evidence.

[Read corrected skill draft](examples/creators/record-interpreter-skill.md) · [Inspect initial response](review/live/skill-builder-consistency-failure.md)

---

## Configuring skills and tools — 25

### Create Adventure Tools

Tool Creator is a custom model that drafts Python tools for tasks you describe.

```text
Create a minimalist text adventure tool for Open WebUI. Return an interactive HTMLResponse and a description for the model. Track rooms, inventory, prerequisites, and completion. Use one command line with help, undo, restart, save, load, and discuss commands. Keep scenario JSON separate from executable code.
```

[Open Tool Creator](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-tool-creator) · [Download tested tool](examples/tools/stem_adventure.py)

---

## Configuring skills and tools — 26

### Install Tool Code

- Open **Workspace → Tools → Create**.

- Enter Name, ID, and Description.

- Paste [STEM Adventure code](examples/tools/stem_adventure.py) and review it.

- Select **Save & Create**.

- Enable your tool through **Integrations → Tools**.

Use a private copy when changing code.

---

## Configuring skills and tools — 27

### Check Generated Code

This recorded test checks a separate draft tool that validates play records. Each command must be text.

```text
{"commands":[42],"events":[{"command":42,"valid":false}]}
```

Expected behavior is to reject numeric commands. Initial creator output accepted them.

Send observed failure back to Tool Creator, then repeat your tests.

[Inspect original draft](review/live/record-validator-before.py) · [Read corrected tool](examples/creators/record-validator.py) · [Review executed tests](review/live/tool-creator-corrected-tests.json)

---

## Configuring skills and tools — 28

### Inspect Tool Results

Ask STEM Adventure Games to quote from Newton: Light and Colour and identify its source.

- Open tool-call details in its response.

- Check which file was retrieved and what text was returned.

- Open cited passages and compare them with your model’s claims.

A claim to have searched is not evidence that a tool ran. Inspect recorded calls and results.

---

## Configuring skills and tools — 29

### Compare Game Records

Attach saved play records from original and revised games, then send this request.

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

[Browse system-prompt examples](examples.html) · [Return to Composing system prompts](.)
