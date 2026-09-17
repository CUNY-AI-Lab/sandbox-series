# Cycle 1 changes

## index.html — Compare Outputs

### Before

### Compare Outputs



### Gemma’s Response



![Gemma 3 27B response recommending walking, with model name and generation time.](images/showcase/car-wash-gemma-response.png)



### Qwen’s Response



![Qwen3.5 27B response recommending driving, with model name and generation time.](images/showcase/car-wash-qwen-response.png)

### After

### Compare Outputs



Consider this question.



```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```



What do you think this person wants to accomplish?

## index.html — Compare Models

### Before

### Compare Models



Start a new chat, select two models, and send this question.



```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```



Save both responses with your question and selected model IDs before adding system prompt instructions.

### After

### Compare Models



![Sandbox logo, message box, and Gateway model selector; enlarged detail shows Compare beside search field outlined and marked by an arrow.](images/current/gateway-selector-compare-hidpi-2026-09-16.svg)



Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two Gateway models. If Compare is unavailable, send identical prompts in separate new chats.

## index.html — Review Custom Models

### Before

### Review Custom Models



Choose **Models** to find custom model cards. Each combines a base model with setup instructions and any attached resources.



Review **Base Model** and **System Prompt**, then compare its instructions with your tested prompt.



Continue in chat if Workspace is unavailable.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### After

### Review Custom Models



Choose **Models** to find custom model cards. Each combines a base model with setup instructions and any attached resources.



Review **Base Model** and **System Prompt** before choosing a card to adapt.



Continue in chat if Workspace is unavailable.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

## index.html — Clone Model Cards

### Before

### Clone Model Cards



- In Workspace → Models, find your chosen model and open ⋯ → **Clone**.

- Rename your copy and give it a unique ID.

- Adjust **System Prompt** for your intended users or research question.

- Review **Access**, keep Private, remove copied access grants, and select **Save & Create**.



Test your copy in chat, then revise its instructions.



[Model management](https://docs.openwebui.com/features/workspace/models/)

### After

### Clone Model Cards



- In Workspace → Models, find your chosen model and open ⋯ → **Clone**.

- Rename your copy and give it a unique ID.

- Read **System Prompt** and identify one instruction to revise.

- Review **Access**, keep Private, remove copied access grants, and select **Save & Create**.



Save an initial response before changing instructions.



[Model management](https://docs.openwebui.com/features/workspace/models/)

## index.html — Model Configuration

### Before

### Model Configuration



![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.](images/current/model-create-hidpi-2026-09-16.svg)



Use Model Name, Base Model, and System Prompt to review and adjust your copy. This blank form identifies those fields.

### After

### Model Configuration



![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.](images/current/model-create-hidpi-2026-09-16.svg)



Review Model Name, Base Model, and System Prompt when configuring your copy.

## index.html — Select STEM Games

### Before

### Select STEM Games



![Model Selector filtered to STEM Adventure Games, with CUNY AI Lab logo, message box, and starter prompts visible.](images/current/stem-original-selector-2026-09-17.png)



Select model ID on bottom right of message box. Search for STEM Adventure Games and select it.

### After

Removed repeated navigation slide.

## index.html — STEM Adventure Games

### Before

### STEM Adventure Games



![STEM Adventure Games presents a short scene and numbered choices directly in Sandbox chat.](images/current/stem-chat-play-hidpi-2026-09-16.png)



Type Start an adventure. Choose an experiment, then reply with a number or describe what you want to do.

### After

### STEM Adventure Games



![STEM Adventure Games presents a short scene and numbered choices directly in Sandbox chat.](images/current/stem-chat-play-hidpi-2026-09-16.png)



For STEM Adventure Games, type Start an adventure. Choose an experiment, then reply with a number or describe what you want to do.

## index.html — Inspect System Prompt

### Before

### Inspect System Prompt



![STEM Adventure Games model editor with CUNY AI Lab icon, DeepSeek V4 Flash 0731 as Base Model, and System Prompt showing Purpose and Wikipedia source instructions.](images/current/stem-original-framework-2026-09-17.png)



Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt.

### After

Removed repeated navigation slide.

## index.html — Adapt Research Prompts

### Before

### Adapt Research Prompts



For [Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions), use [sample revisions](examples/research/sample-revisions.md) to test your copy.



- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.



Save your source material, prompt, response, and assessment together.

### After

### Adapt Research Prompts



For [Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions), paste one pair from [sample revisions](examples/research/sample-revisions.md) into your copy.



- Ask it to classify one change and quote evidence.

- Check quotations against both passages.

- Identify an instruction to revise if its classification is unclear.



[Read full system prompt](examples.html#wikipedia-revisions)

## index.html — Define Prompt Components

### Before

### Define Prompt Components



Choose one component to change.



- **Purpose** — What your model should help users do.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Format** — Length and presentation.

### After

### Define Prompt Components



Use either example. Choose one component to change in your cloned model.



- **Purpose** — What your model should help users do.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Format** — Length and presentation.

## index.html — Define Purpose

### Before

### Define Purpose



Describe what your model should help users do.



- Who will use this model?

- Which experiment or research question will they explore?

- What prior knowledge can you assume?



```text
Guide a short text adventure in which players explore how a prism changes a beam of sunlight.
```

### After

### Define Purpose



Describe what your model should help users do.



- Who will use this model?

- Which task or question will they explore?

- What prior knowledge can you assume?



```text
Guide a short text adventure in which players explore how a prism changes a beam of sunlight.
```



For research, name your question, source material, and intended users.

## index.html — Write Procedures

### Before

### Write Procedures



What should happen before and after each choice?



```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer four numbered choices and wait.
4. Describe what players observe after each choice.
```

### After

### Write Procedures



Which steps should your model follow?



```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer four numbered choices and wait.
4. Describe what players observe after each choice.
```



For research, check inputs, quote changed passages, then classify changes.

## index.html — Set Constraints

### Before

### Set Constraints



Specify how your model should handle missing evidence.



```text
Do not invent historical details when sources are missing.
Distinguish documented events from invented scenes and choices.
If a source is unavailable, explain what cannot be checked.
```



Test a request that asks for a detail absent from your sources.

### After

### Set Constraints



Specify how your model should handle missing evidence.



```text
Do not invent historical details when sources are missing.
Distinguish documented events from invented scenes and choices.
If a source is unavailable, explain what cannot be checked.
```



For research, request missing excerpts and mark uncertain classifications.



Test a request that asks for a detail absent from your sources.

## index.html — Specify Format

### Before

### Specify Format



Specify how scenes and choices should appear.



```text
Write a short scene followed by four numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```

### After

### Specify Format



Specify response structure and length.



```text
Write a short scene followed by four numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```



For research, use Before and After quotations, categories, and brief explanations.

## index.html — Extend Instructions

### Before

### Extend Instructions



- Specify what happens when a player asks for a hint.

- Explain how to revisit an earlier decision.

- Require source checks when players ask about historical claims.

- Test how your model responds when evidence is missing.

### After

### Extend Instructions



Specify what your model should do when a request needs additional guidance.



- **Teaching** — Explain how to offer a hint or revisit an earlier choice.

- **Research** — Explain when to request missing passages or mark a classification uncertain.



Test that condition in your copy, revise one instruction, and repeat your request.

## index.html — Review Common Problems

### Before

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

### After

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

## knowledge/index.html — Review Model Settings

### Before

### Review Model Settings



![STEM Adventure Games model editor with CUNY AI Lab icon, DeepSeek V4 Flash 0731 as Base Model, and System Prompt showing Purpose and Wikipedia source instructions.](../images/current/stem-original-framework-2026-09-17.png)



Review **Base Model** and **System Prompt** in your custom model. Use [STEM Adventure Games instructions](../examples.html#stem-chat) from Workshop 1. Leave Skills and Tools unselected.

### After

### Review Model Settings



Open your private copy of **STEM Adventure Games** or **Compare Wikipedia Edits**.



Review **Base Model** and **System Prompt**. Keep instructions from Workshop 1. Leave Skills and Tools unselected.



[Review system prompts](../examples.html)

## knowledge/index.html — Open STEM Collection

### Before

### Open STEM Collection



![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, Newton’s optical experiments, procedural variations, and software checks.](../images/current/stem-knowledge-2026-09-14.png)



Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments.

### After

### Open STEM Collection



![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, List of experiments, procedural variations, and software checks.](../images/current/stem-knowledge-2026-09-14.png)



Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments.

## knowledge/index.html — Review Source Roles

### Before

### Review Source Roles



Use sources for different questions.



Newton’s optical experiments



Check apparatus, procedures, and observations.



Scientific method



Examine hypotheses, measurement, and revision.



Women in science



Investigate collaboration, recognition, and institutions.



Check whether a scene follows its sources or adds invented details.

### After

### Review Source Roles



Use sources for different questions.



List of experiments



Choose experiments, scientists, and questions to investigate.



Scientific method



Examine hypotheses, measurement, and revision.



Women in science



Investigate collaboration, recognition, and institutions.



Check whether a scene follows its sources or adds invented details.

## knowledge/index.html — Review Attached Knowledge

### Before

### Review Attached Knowledge



![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.](../images/current/knowledge-attachments-3x-2026-09-16.svg)



Select STEM Wikipedia Experiments under Knowledge in your custom model and choose Save & Update. Skills and Tools are added in Workshop 3.

### After

### Review Attached Knowledge



![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.](../images/current/knowledge-attachments-3x-2026-09-16.svg)



For STEM Adventure Games, select STEM Wikipedia Experiments under Knowledge and choose Save & Update. Skills and Tools are added in Workshop 3.

## knowledge/index.html — Check Game Sources

### Before

### Check Game Sources



In your custom model, start an adventure about light and colour. Choose one action, then ask about its historical sources.



```text
Which objects in this scene appear in Newton: Light and Colour? Quote a relevant passage. Which details were invented for this game?
```



Open cited material. Does it support your model’s response?



[Read Newton source summary](../examples/knowledge/newton-light-colour.md) · [Read Newton’s account](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006)

### After

### Check Game Sources



In STEM Adventure Games, start an adventure about light and colour. Choose one action, then ask about its historical sources.



```text
Which objects in this scene appear in Newton: Light and Colour? Quote a relevant passage. Which details were invented for this game?
```



Open cited material. Does it support your model’s response?



[Read Newton source summary](../examples/knowledge/newton-light-colour.md) · [Read Newton’s account](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006)

## knowledge/index.html — Choose Reference Materials

### Before

### Choose Reference Materials



Choose source documents that help players investigate an experiment.



- Use [Newton: Light and Colour](../examples/knowledge/newton-light-colour.md) for apparatus and observations.

- Use [Newton: Experimental Variants](../examples/knowledge/newton-experimental-variants.md) for changes to experimental procedures.



Read entries before uploading. Distinguish these summaries from original historical accounts.



[Download Light and Colour](../examples/knowledge/newton-light-colour.md) · [Download Experimental Variants](../examples/knowledge/newton-experimental-variants.md)

### After

### Choose Reference Materials



Choose documents for your teaching or research task.



- Use [Newton: Light and Colour](../examples/knowledge/newton-light-colour.md) for apparatus and observations.

- Use [Newton: Experimental Variants](../examples/knowledge/newton-experimental-variants.md) for changes to experimental procedures.



For Compare Wikipedia Edits, use saved revision excerpts and your classification criteria. Read documents before uploading; distinguish summaries from original accounts.



[Download Light and Colour](../examples/knowledge/newton-light-colour.md) · [Download Experimental Variants](../examples/knowledge/newton-experimental-variants.md)

## knowledge/index.html — Attach Knowledge Collections

### Before

### Attach Knowledge Collections



- Open Workspace → Knowledge → your collection. Use Add Content to upload documents, then wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your custom model, and replace STEM Wikipedia Experiments with your collection under **Knowledge**.

- Choose **Save & Update**, then start a new chat with your custom model.



[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

### After

### Attach Knowledge Collections



- Open Workspace → Knowledge → your collection. Use Add Content to upload documents, then wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your chosen custom model, and select your collection under **Knowledge**. Remove collections unrelated to your question.

- Choose **Save & Update**, then start a new chat with your custom model.



[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

## skills/index.html — Review Previous Work

### Before

### Review Previous Work



Continue from your chat adventure and source collection. Workshop 3 adds tools and skills. Select STEM Adventure Games — Advanced and review its system prompt.



- Identify instructions for opening Prism Laboratory.

- Review attached STEM Wikipedia Experiments collection.

- Distinguish source material, skill instructions, and tool operations.



Use a private copy when adapting this configuration.

### After

### Review Previous Work



Review your model and source collection. This example builds on our chat adventure and source collection. Workshop 3 adds tools and skills. Select STEM Adventure Games — Advanced and review its system prompt.



- Identify instructions for opening Prism Laboratory.

- Review attached STEM Wikipedia Experiments collection.

- Distinguish source material, skill instructions, and tool operations.



Use a private copy when adapting this configuration.

## skills/index.html — Create Adventure Tools

### Before

### Create Adventure Tools



Tool Creator is a custom model that drafts Python tools for tasks you describe. Save its output as a draft for review and testing. Use tested STEM Adventure code for installation in this workshop.



```text
Create a minimalist text adventure tool for Open WebUI. Return an interactive HTMLResponse and a description for the model. Track rooms, inventory, prerequisites, and completion. Use one command line with help, undo, restart, save, load, and discuss commands. Keep scenario JSON separate from executable code.
```



[Open Tool Creator](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-tool-creator) · [Download tested tool](../examples/tools/stem_adventure.py)



[Review code evaluation](reference.html#check-generated-code)



[Read tested code](../examples/tools/stem_adventure.py)

### After

### Create Adventure Tools



CAIL Tool Creator is a custom model that drafts Python tools for tasks you describe. Save its output as a draft for review and testing. Use tested STEM Adventure code for installation in this workshop.



```text
Create a minimalist text adventure tool for Open WebUI. Return an interactive HTMLResponse and a description for the model. Track rooms, inventory, prerequisites, and completion. Use one command line with help, undo, restart, save, load, and discuss commands. Keep scenario JSON separate from executable code.
```



[Open CAIL Tool Creator](https://chat.ailab.gc.cuny.edu/?model=cail-sandbox-tool-creator) · [Download tested tool](../examples/tools/stem_adventure.py)



[Review code evaluation](reference.html#check-generated-code)



[Read tested code](../examples/tools/stem_adventure.py)

## skills/index.html — Install Tool Code

### Before

### Install Tool Code



- Open **Workspace → Tools → Create**.

- Enter Name, ID, and Description.

- Paste and review [tested STEM Adventure code](../examples/tools/stem_adventure.py). Keep your creator draft separate.

- Select **Save & Create**.

- Enable your tool through **Integrations → Tools**.



Use a private copy when changing code. Attach reusable tools under Tools in your model editor.

### After

### Install Tool Code



- Open **Workspace → Tools → Create**.

- Enter Name, ID, and Description.

- Paste and review [tested STEM Adventure code](../examples/tools/stem_adventure.py). Keep your creator draft separate.

- Select **Save & Create**.

- In your private model, replace STEM Adventure under **Tools** with your installed copy. Update System Prompt to name it and select **Save & Update**.



Give your installed tool a unique name and ID so you can select it for testing.

## WORKSHOP.md

### Before

# Presenter Lesson Plans

The CUNY AI Lab Sandbox supports teaching, research, and experimentation with open-weight models. These workshops introduce its chat interface, custom models, knowledge collections, skills, and tools through demonstrations and guided exercises.

Participants first compare models and test system prompts through a text adventure played in chat. Workshop 2 adds source documents and checks how they inform scenes and explanations. Workshop 3 introduces a separate game tool, a skill for changing experiments, and a creator model for Python tools. Participants compare responses, check citations, and test whether models follow their instructions.

[Present the series](https://cuny-ai-lab.github.io/sandbox-series/) · [Read all slide copy](SLIDES.md) · [Browse system-prompt examples](examples.html) · [Review copy changes](review/README.md)

## Workshop Roadmap

| Workshop | Activity | Required access | Next steps |
| --- | --- | --- | --- |
| Composing system prompts | Configure model behavior with system prompts | Individual access approval and Sandbox sign-in | Save tested prompts; request Workspace and Knowledge access |
| Curating knowledge collections | Upload documents so models can reference them | Workshop 1 access, Workspace, Knowledge collection access | Save retrieval tests; request Skills and Tools access |
| Configuring skills and tools | Configure an adventure tool and reusable instructions | Workshop 1 access, Skills and Tools access; Workspace authoring for creation and editing | Save configurations; verify shared access; retest after changes |

Workshop 3 needs Knowledge access when a procedure retrieves from a collection. Its advanced STEM example uses an attached collection for historical claims, while a separate tool runs game commands. Workshops 1 and 2 use scenes and choices generated in chat without attached skills or tools.

## Prepare Workshop Access

For individual access, follow [Getting Started](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/) to the Lab’s [access application](https://ailab.gc.cuny.edu/request-access/). Choose **My own access**, use CUNY Login, complete the application, and check the verified CUNY email for approval. Then enter the [Sandbox](https://chat.ailab.gc.cuny.edu/) through **Continue with CUNY Login**. Participants do not need an API key for these chat exercises.

Workshop 1 requires only individual access and sign-in. Workspace access is arranged for the midpoint exercise. Participants refresh, inspect a sample custom model, and can save their tested prompt as a private configuration. If access is delayed, participants follow the demonstration and continue testing in chat. Before Workshop 2, arrange Workspace and Knowledge access with the Lab. Before Workshop 3, arrange Skills and Tools access, including authoring permissions for participants who will create or edit resources. Confirm which base models and capabilities are available to the group.

Prepare **Examine Assumptions** using [this sample prompt](examples/assumption-check.txt) and a tested base model. For Workshops 1 and 2, configure **STEM Adventure Games** with [instructions for an adventure played in chat](examples/stem-chat-system-prompt.txt). Leave Skills and Tools unselected. Confirm access to **STEM Wikipedia Experiments** for Workshop 2. Set Function Calling to Legacy under Advanced Params when preparing automatic knowledge retrieval; this setting is covered in [Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/). Save the tool-based configuration as **STEM Adventure Games — Advanced** for Workshop 3, using its [separate system prompt](examples/stem-system-prompt.txt).

Choose two available small models for the opening demonstration. Record their exact identifiers and settings rather than treating screenshot labels as a current inventory. Check personal defaults, folder instructions, memory, and optional features that may introduce additional context. Keep these consistent during comparisons and document differences you cannot control.

Use documents you are permitted to upload and share for collection and skill exercises. Verify sharing through an ordinary participant account, including access to custom models, base models, and attached resources. Course enrollment has a separate invitation route in the documentation; it is not a prerequisite for Workshop 1.

## Composing system prompts

Participants learn how user prompts and system prompts differ before comparing models. System prompts are setup instructions that describe how a model should behave. Begin comparisons with two small models interpreting a sentence about a nurse and doctor, then ask whether to walk or drive to a car wash. Participants save both responses, read sample system prompt instructions, locate System Prompt in Chat Controls, and regenerate responses to their original prompt after adding those instructions.

### Workshop Agenda

- Request individual access and sign in
- Define system prompts
- Compare responses from small models
- Revise in-chat system prompts
- Explore Workspace models
- Save prompts for reuse

### Lesson Plan

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Introduce the series, confirm sign-in, define system prompts, and locate the model selector. | Account readiness and prompt distinction |
| 10–25 | Demonstrate small models on the nurse question and car-wash question. Examine assumptions before showing the saved responses. | Exact inputs, model IDs, and responses |
| 25–45 | Compare the car-wash responses, paste the short in-chat system prompt, then choose Regenerate → Try Again on each original response. Keep the question and other settings unchanged. | Original and regenerated responses |
| 45–65 | Inspect Workspace models and play two or three turns in STEM Adventure Games. Read its system prompt, then create a private configuration. | Base model, system prompt, and game responses |
| 65–85 | Change one instruction, such as how the game offers hints. Test a choice and a request for help, revise one instruction, and repeat. | Failure, revision, and retest |
| 85–90 | Save the tested prompt and identify source documents for Workshop 2. | Private model and source question |

### Compare Small Models

> The nurse yelled at the doctor because she was late. Who was late?

Send exactly this question to two small models with matching context. Ask which interpretation each response chooses and whether it acknowledges ambiguity. Either person can be the referent of “she”; the sentence does not establish a unique answer. A plausible interpretation is different from information established by the wording. Avoid turning this single item into a claim about model-wide bias or ability.

### Compare Outputs

> The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.

Screenshot provenance and inconsistent Qwen labels are documented in [source history](review/showcase-sources.json). Discuss these responses without treating screenshot labels or timings as reliable model identifiers or comparative measurements.

Ask “What do you think this person wants to accomplish?” Participants save both original responses and read the sample system prompt before changing settings. Ask what should change in each response. Show Controls at the top right of chat and its System Prompt field alongside the exercise instructions. Participants add the sample instructions, close Controls, and select Regenerate beneath each original response and choose Try Again, leaving their question unchanged. Compare assumptions, explanations, and any change in recommendations.

| Criterion | Model A evidence | Model B evidence |
| --- | --- | --- |
| Identify stated goal or acknowledge missing purpose | | |
| Distinguish stated facts from assumptions | | |
| Give reasons that support recommendation | | |
| Compare outputs after changing system prompt instructions | | |

For the in-chat system-prompt exercise, use [Examine Assumptions](examples/assumption-check.txt). It asks the model to examine facts and assumptions without prescribing either demonstration answer. Check whether the added instructions help, cause unnecessary questions, or fail on the second task. Save original responses before changing system prompt instructions.

## Curating knowledge collections

Participants add source documents to the adventure they played in Workshop 1. They ask about objects and events in a scene, then check whether cited passages support the model’s explanation. STEM Wikipedia Experiments provides material for checking historical claims and scientific procedures. Scenes and choices continue in chat; skills and tools begin in Workshop 3.

### Workshop Agenda

- Confirm Workspace and Knowledge access
- Select source documents
- Create knowledge collections
- Attach collections to custom models
- Check source citations
- Choose procedures for skills

### Lesson Plan

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–15 | Confirm access, choose a document question, and save its initial response. Record any sources already used. Keep Skills and Tools unselected. | Question, settings, and initial response |
| 15–35 | Inspect STEM Wikipedia Experiments and check imports. Play a short adventure about light and colour, then compare objects in its scene with Newton’s account. Distinguish the uploaded summary from its historical source. | Game scene, cited passages, and supported claims |
| 35–55 | Select a few readable documents, create a private collection, upload files, wait for processing, and attach it to the same custom model. | Documents, collection, and saved model |
| 55–80 | Repeat the saved question with base model and system prompt unchanged. Check cited passages, try questions requiring two sources or missing information, and diagnose one failure. | Before/after responses and source checks |
| 80–90 | Retest one change, check sharing, and choose a procedure for Workshop 3. | Retest and next procedure |

Use the same [adventure system prompt](examples.html#stem-chat) from Workshop 1. The [source-checking instructions](examples.html#stem-sources) can extend that prompt when participants ask about evidence. Keep Skills and Tools unselected. Participants can build a small collection for another experiment or adapt the procedure to their own teaching or research. They should know the source material well enough to check model claims independently.

A generic or incorrect answer can arise from processing, retrieval, access, instructions, or interpretation. Check the actual evidence before diagnosing the cause. File length alone does not determine retrieval quality. Scanned or multi-column PDFs deserve particular attention during text extraction.

### Next steps

- Save source lists and retrieval tests
- Request Skills and Tools access
- Choose recurring teaching or research procedures
- Review system-prompt examples
- Continue to Configuring skills and tools

## Configuring skills and tools

Participants use STEM Adventure to play a deterministic text adventure, inspect commands and prerequisites, and export a play record. They draft a skill, attach it to a private copy of STEM Adventure Games — Advanced, test one procedural change, and examine how a model interprets the run. Kale Skill Builder and Tool Creator accept participants’ own requirements. Their system prompts and starter suggestions are general-purpose. STEM Adventure is a submitted workshop example. Tool Creator produces a reviewable Python draft with explicit tests. Each participant retains a skill draft, creator output, an installed copy of the tested tool, a scenario, and a play record. Creator output remains a draft until reviewed and tested.

### Workshop Agenda

- Confirm Skills and Tools access
- Play STEM Adventure
- Inspect commands and results
- Configure reusable skills
- Create and test tools
- Compare procedural changes

### Lesson Plan

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–25 | Open STEM Adventure Games — Advanced, test commands, save and reload a play record, and submit it with discuss. | Commands, failed prerequisite, and play record |
| 25–45 | Clone STEM Adventure Games — Advanced, remove inherited access grants, and save a private copy. Use Kale Skill Builder to draft one skill, save it, replace the existing attached skill, and update the private system prompt to name the draft. | Private model and saved skill |
| 45–65 | Attach Prism Laboratory JSON and request one aperture comparison. Run the resulting scenario. Compare the same request with and without the saved skill, keeping other settings and inputs fixed. | Generated scenarios, test results, and records |
| 65–83 | Request a Python draft from Tool Creator and save it for review. Install the provided tested adventure code separately, enable that copy, open a game, and inspect its actual call and result. | Creator draft, installed tested code, and tool result |
| 83–90 | Save artifacts, compare game records with source evidence, and identify a next test. | Artifacts, observed result, and next question |

The primary artifacts are [STEM Adventure](examples/tools/stem_adventure.py), [Extend STEM Adventures](examples/stem-game-skill.md), [Prism Laboratory](examples/adventure/prism.json), [Aperture Test](examples/adventure/aperture.json), and [winning commands](examples/adventure/winning-commands.json). The [local preview](examples/adventure/preview.html) allows practice before Sandbox access is ready. It does not establish that a participant has permission to call the installed tool.

The tool returns an interactive HTMLResponse with explicit model context. Its engine owns game state. The skill guides a procedural change and interpretation of a record; it cannot change state through prose. The discuss command fills the chat message box for review and sending. The save and load commands preserve progress after reloads; clicks inside the iframe do not automatically reach the model.

Evaluate source use separately from game correctness. A deterministic winning sequence establishes software behavior. It does not validate a historical interpretation or establish a learning effect. The aperture extension is a scripted comparison based on a particular account, not a general optical simulation.

### Next steps

- Save prompts, sources, skills, and tool settings
- Compare expected and observed behavior
- Revise instructions from recorded failures
- Verify shared access with intended users
- Retest after model or tool updates

## Source Documentation

Interface instructions draw on the published [Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/), especially [Getting Started](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/), [Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/), [Models](https://ailab.gc.cuny.edu/sandbox-docs/models/), [Knowledge Bases](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/), [Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/), and [Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/).

The live interface was inspected in Firefox on September 13–16, 2026. Creation, Clone, and access controls were checked in an administrator account. Participant-account checks remain with Zach before delivery. [Screenshot provenance](review/screenshot-sources.json) records source hashes and crop coordinates. [Showcase provenance](review/showcase-sources.json) distinguishes archival comparison excerpts from current interface instructions. The unrelated fourth screenshot is excluded.

Provider requests are described in the docs as configured for zero retention with training use prohibited. Sandbox history can still be stored and visible to administrators or its shared audience. Retrieved passages enter the model request and may appear in its response. Use materials appropriate for those conditions.

Open WebUI’s [Models](https://docs.openwebui.com/features/workspace/models/), [Knowledge](https://docs.openwebui.com/features/workspace/knowledge/), and [Skills](https://docs.openwebui.com/features/workspace/skills/) documentation supports the descriptions of custom configurations, retrieval, and skill loading. The Sandbox docs govern local access and sign-in instructions.

## STEM Configuration

**STEM Adventure Games** is the introductory model for Workshops 1 and 2. Its system prompt asks for short scenes, three numbered choices, and responses to actions typed in ordinary language. The model uses attached sources when discussing historical evidence. It has no attached skills or tools.

**STEM Adventure Games — Advanced** is reserved for Workshop 3. It uses STEM Adventure and Extend STEM Adventures with native function calling. Its system prompt describes those components and requires a submitted play record before interpreting actions taken inside the game interface.

The original collection contained three Wikipedia imports. Scientific method and Women in science contained article text; List of experiments contained a Wikimedia 429 error and was only 369 bytes. The failed import is identified in the source register and system prompt so it is not treated as evidence. Additional entries provide Newton’s optical experiments, procedural variants, software evaluation guidance, and a source register. Inspect processing and retrieval before using newly added material.

### Additional Knowledge Entries

| Entry | Use |
| --- | --- |
| [Newton: Light and Colour](examples/knowledge/newton-light-colour.md) | Check apparatus and distinguish historical claims from game simplifications |
| [Newton: Experimental Variants](examples/knowledge/newton-experimental-variants.md) | Support an aperture comparison with a specific source |
| [Evaluate Game Procedures](examples/knowledge/game-procedure-evaluation.md) | Check commands, prerequisites, replay, and interpretation limits |
| [STEM Source Register](examples/knowledge/source-register.md) | Track provenance and identify the failed Wikipedia import |

The Newton entries summarize primary accounts from the [Newton Project](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006). They identify their sources and limits; they are not full article imports. Web Search remains available, so verify whether cited evidence came from uploaded entries or external pages.

## Optional References

[Source examples](knowledge/reference.html) preserve research and historical alternatives. [Skill and tool examples](skills/reference.html) preserve the blank template, source interpretation exercise, creator failures, corrections, and test labels. These ordinary pages contain no hidden notes.

### After

# Presenter Lesson Plans

The CUNY AI Lab Sandbox supports teaching, research, and experimentation with open-weight models. These workshops introduce its chat interface, custom models, knowledge collections, skills, and tools through demonstrations and guided exercises.

Participants first compare models, then choose STEM Adventure Games for teaching or Compare Wikipedia Edits for research and revise a private copy. Workshop 2 adds source documents and checks how they inform scenes and explanations. Workshop 3 introduces a separate game tool, a skill for changing experiments, and a creator model for Python tools. Participants compare responses, check citations, and test whether models follow their instructions.

[Present the series](https://cuny-ai-lab.github.io/sandbox-series/) · [Read all slide copy](SLIDES.md) · [Browse system-prompt examples](examples.html) · [Review copy changes](review/README.md)

## Workshop Roadmap

| Workshop | Activity | Required access | Next steps |
| --- | --- | --- | --- |
| Composing system prompts | Configure model behavior with system prompts | Individual access approval and Sandbox sign-in | Save tested prompts; request Workspace and Knowledge access |
| Curating knowledge collections | Upload documents so models can reference them | Workshop 1 access, Workspace, Knowledge collection access | Save retrieval tests; request Skills and Tools access |
| Configuring skills and tools | Configure an adventure tool and reusable instructions | Workshop 1 access, Skills and Tools access; Workspace authoring for creation and editing | Save configurations; verify shared access; retest after changes |

Workshop 3 needs Knowledge access when a procedure retrieves from a collection. Its advanced STEM example uses an attached collection for historical claims, while a separate tool runs game commands. Workshops 1 and 2 use scenes and choices generated in chat without attached skills or tools.

## Prepare Workshop Access

For individual access, follow [Getting Started](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/) to the Lab’s [access application](https://ailab.gc.cuny.edu/request-access/). Choose **My own access**, use CUNY Login, complete the application, and check the verified CUNY email for approval. Then enter the [Sandbox](https://chat.ailab.gc.cuny.edu/) through **Continue with CUNY Login**. Participants do not need an API key for these chat exercises.

Workshop 1 requires only individual access and sign-in. Workspace access is arranged for the midpoint exercise. Participants refresh, review model cards, choose a teaching or research example, and clone it as a private configuration. If access is delayed, participants follow the demonstration and continue testing in chat. Before Workshop 2, arrange Workspace and Knowledge access with the Lab. Before Workshop 3, arrange Skills and Tools access, including authoring permissions for participants who will create or edit resources. Confirm which base models and capabilities are available to the group.

Prepare **Examine Assumptions** using [this sample prompt](examples/assumption-check.txt) and a tested base model. For Workshops 1 and 2, configure **STEM Adventure Games** with [instructions for an adventure played in chat](examples/stem-chat-system-prompt.txt). Leave Skills and Tools unselected. Confirm access to **STEM Wikipedia Experiments** for Workshop 2. Set Function Calling to Legacy under Advanced Params when preparing automatic knowledge retrieval; this setting is covered in [Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/). Save the tool-based configuration as **STEM Adventure Games — Advanced** for Workshop 3, using its [separate system prompt](examples/stem-system-prompt.txt).

Choose two available small models for the opening demonstration. Record their exact identifiers and settings rather than treating screenshot labels as a current inventory. Check personal defaults, folder instructions, memory, and optional features that may introduce additional context. Keep these consistent during comparisons and document differences you cannot control.

Use documents you are permitted to upload and share for collection and skill exercises. Verify sharing through an ordinary participant account, including access to custom models, base models, and attached resources. Course enrollment has a separate invitation route in the documentation; it is not a prerequisite for Workshop 1.

## Composing system prompts

Participants learn how user prompts and system prompts differ before comparing models. System prompts are setup instructions that describe how a model should behave. Begin comparisons with two small models interpreting a sentence about a nurse and doctor, then ask whether to walk or drive to a car wash. Participants save both responses, read sample system prompt instructions, locate System Prompt in Chat Controls, and regenerate responses to their original prompt after adding those instructions.

### Workshop Agenda

- Request individual access and sign in
- Define system prompts
- Compare responses from small models
- Revise in-chat system prompts
- Review Workspace model cards
- Choose teaching or research examples
- Clone model cards and test revisions

### Lesson Plan

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Introduce the series, confirm sign-in, define system prompts, and locate the model selector. | Account readiness and prompt distinction |
| 10–25 | Demonstrate small models on the nurse question and car-wash question. Examine assumptions before showing the saved responses. | Exact inputs, model IDs, and responses |
| 25–45 | Compare the car-wash responses, paste the short in-chat system prompt, then choose Regenerate → Try Again on each original response. Keep the question and other settings unchanged. | Original and regenerated responses |
| 45–65 | Review Workspace model cards, compare teaching and research options, and clone one privately. Save an initial response from a game choice or a provided Wikipedia edit. | Base model, system prompt, and initial response |
| 65–85 | Revise one component using Purpose, Procedure, Constraints, and Format. Test a hint request or an uncertain classification, check the response, and repeat after one revision. | Failure, revision, and retest |
| 85–90 | Save the tested prompt and identify source documents for Workshop 2. | Private model and source question |

### Compare Small Models

> The nurse yelled at the doctor because she was late. Who was late?

Send exactly this question to two small models with matching context. Ask which interpretation each response chooses and whether it acknowledges ambiguity. Either person can be the referent of “she”; the sentence does not establish a unique answer. A plausible interpretation is different from information established by the wording. Avoid turning this single item into a claim about model-wide bias or ability.

### Compare Outputs

> The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.

Screenshot provenance and inconsistent Qwen labels are documented in [source history](review/showcase-sources.json). Discuss these responses without treating screenshot labels or timings as reliable model identifiers or comparative measurements.

Ask “What do you think this person wants to accomplish?” Participants save both original responses and read the sample system prompt before changing settings. Ask what should change in each response. Show Controls at the top right of chat and its System Prompt field alongside the exercise instructions. Participants add the sample instructions, close Controls, and select Regenerate beneath each original response and choose Try Again, leaving their question unchanged. Compare assumptions, explanations, and any change in recommendations.

| Criterion | Model A evidence | Model B evidence |
| --- | --- | --- |
| Identify stated goal or acknowledge missing purpose | | |
| Distinguish stated facts from assumptions | | |
| Give reasons that support recommendation | | |
| Compare outputs after changing system prompt instructions | | |

For the in-chat system-prompt exercise, use [Examine Assumptions](examples/assumption-check.txt). It asks the model to examine facts and assumptions without prescribing either demonstration answer. Check whether the added instructions help, cause unnecessary questions, or fail on the second task. Save original responses before changing system prompt instructions.

## Curating knowledge collections

Participants add source documents to their chosen teaching or research model from Workshop 1. They ask about objects and events in a scene, then check whether cited passages support the model’s explanation. STEM Wikipedia Experiments provides material for checking historical claims and scientific procedures. Scenes and choices continue in chat; skills and tools begin in Workshop 3.

### Workshop Agenda

- Confirm Workspace and Knowledge access
- Select source documents
- Create knowledge collections
- Attach collections to custom models
- Check source citations
- Choose procedures for skills

### Lesson Plan

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–15 | Confirm access, choose a document question, and save its initial response. Record any sources already used. Keep Skills and Tools unselected. | Question, settings, and initial response |
| 15–35 | Inspect STEM Wikipedia Experiments and check imports. Play a short adventure about light and colour, then compare objects in its scene with Newton’s account. Distinguish the uploaded summary from its historical source. | Game scene, cited passages, and supported claims |
| 35–55 | Select a few readable documents, create a private collection, upload files, wait for processing, and attach it to the same custom model. | Documents, collection, and saved model |
| 55–80 | Repeat the saved question with base model and system prompt unchanged. Check cited passages, try questions requiring two sources or missing information, and diagnose one failure. | Before/after responses and source checks |
| 80–90 | Retest one change, check sharing, and choose a procedure for Workshop 3. | Retest and next procedure |

Keep the system prompt from your chosen model in Workshop 1. The [adventure prompt](examples.html#stem-chat) and [research prompt](examples.html#wikipedia-revisions) remain available for comparison. The [source-checking instructions](examples.html#stem-sources) can extend that prompt when participants ask about evidence. Keep Skills and Tools unselected. Participants can build a small collection for another experiment or adapt the procedure to their own teaching or research. They should know the source material well enough to check model claims independently.

A generic or incorrect answer can arise from processing, retrieval, access, instructions, or interpretation. Check the actual evidence before diagnosing the cause. File length alone does not determine retrieval quality. Scanned or multi-column PDFs deserve particular attention during text extraction.

### Next steps

- Save source lists and retrieval tests
- Request Skills and Tools access
- Choose recurring teaching or research procedures
- Review system-prompt examples
- Continue to Configuring skills and tools

## Configuring skills and tools

Participants use STEM Adventure to play a deterministic text adventure, inspect commands and prerequisites, and export a play record. They draft a skill, attach it to a private copy of STEM Adventure Games — Advanced, test one procedural change, and examine how a model interprets the run. Kale Skill Builder and CAIL Tool Creator accept participants’ own requirements. Their system prompts and starter suggestions are general-purpose. STEM Adventure is a submitted workshop example. CAIL Tool Creator produces a reviewable Python draft with explicit tests. Each participant retains a skill draft, creator output, an installed copy of the tested tool, a scenario, and a play record. Creator output remains a draft until reviewed and tested.

### Workshop Agenda

- Confirm Skills and Tools access
- Play STEM Adventure
- Inspect commands and results
- Configure reusable skills
- Create and test tools
- Compare procedural changes

### Lesson Plan

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–25 | Open STEM Adventure Games — Advanced, test commands, save and reload a play record, and submit it with discuss. | Commands, failed prerequisite, and play record |
| 25–45 | Clone STEM Adventure Games — Advanced, remove inherited access grants, and save a private copy. Use Kale Skill Builder to draft one skill, save it, replace the existing attached skill, and update the private system prompt to name the draft. | Private model and saved skill |
| 45–65 | Attach Prism Laboratory JSON and request one aperture comparison. Run the resulting scenario. Compare the same request with and without the saved skill, keeping other settings and inputs fixed. | Generated scenarios, test results, and records |
| 65–83 | Request a Python draft from CAIL Tool Creator and save it for review. Install provided tested code separately, attach that copy to the private model, update its system prompt to name it, and inspect an actual call and result. | Creator draft, installed tested code, and tool result |
| 83–90 | Save artifacts, compare game records with source evidence, and identify a next test. | Artifacts, observed result, and next question |

The primary artifacts are [STEM Adventure](examples/tools/stem_adventure.py), [Extend STEM Adventures](examples/stem-game-skill.md), [Prism Laboratory](examples/adventure/prism.json), [Aperture Test](examples/adventure/aperture.json), and [winning commands](examples/adventure/winning-commands.json). The [local preview](examples/adventure/preview.html) allows practice before Sandbox access is ready. It does not establish that a participant has permission to call the installed tool.

The tool returns an interactive HTMLResponse with explicit model context. Its engine owns game state. The skill guides a procedural change and interpretation of a record; it cannot change state through prose. The discuss command fills the chat message box for review and sending. The save and load commands preserve progress after reloads; clicks inside the iframe do not automatically reach the model.

Evaluate source use separately from game correctness. A deterministic winning sequence establishes software behavior. It does not validate a historical interpretation or establish a learning effect. The aperture extension is a scripted comparison based on a particular account, not a general optical simulation.

### Next steps

- Save prompts, sources, skills, and tool settings
- Compare expected and observed behavior
- Revise instructions from recorded failures
- Verify shared access with intended users
- Retest after model or tool updates

## Source Documentation

Interface instructions draw on the published [Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/), especially [Getting Started](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/), [Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/), [Models](https://ailab.gc.cuny.edu/sandbox-docs/models/), [Knowledge Bases](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/), [Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/), and [Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/).

The live interface was inspected in Firefox on September 13–16, 2026. Creation, Clone, and access controls were checked in an administrator account. Participant-account checks remain with Zach before delivery. [Screenshot provenance](review/screenshot-sources.json) records source hashes and crop coordinates. [Showcase provenance](review/showcase-sources.json) distinguishes archival comparison excerpts from current interface instructions. The unrelated fourth screenshot is excluded.

Provider requests are described in the docs as configured for zero retention with training use prohibited. Sandbox history can still be stored and visible to administrators or its shared audience. Retrieved passages enter the model request and may appear in its response. Use materials appropriate for those conditions.

Open WebUI’s [Models](https://docs.openwebui.com/features/workspace/models/), [Knowledge](https://docs.openwebui.com/features/workspace/knowledge/), and [Skills](https://docs.openwebui.com/features/workspace/skills/) documentation supports the descriptions of custom configurations, retrieval, and skill loading. The Sandbox docs govern local access and sign-in instructions.

## STEM Configuration

**STEM Adventure Games** is the introductory model for Workshops 1 and 2. Its system prompt opens with three or four adventures, then presents four numbered choices at each stage and responds to actions typed in ordinary language. The model uses attached sources when discussing historical evidence. It has no attached skills or tools.

**STEM Adventure Games — Advanced** is reserved for Workshop 3. It uses STEM Adventure and Extend STEM Adventures with native function calling. Its system prompt describes those components and requires a submitted play record before interpreting actions taken inside the game interface.

The original collection contained three Wikipedia imports. Scientific method and Women in science contained article text; List of experiments contained a Wikimedia 429 error and was only 369 bytes. The failed import is identified in the source register and system prompt so it is not treated as evidence. Additional entries provide Newton’s optical experiments, procedural variants, software evaluation guidance, and a source register. Inspect processing and retrieval before using newly added material.

### Additional Knowledge Entries

| Entry | Use |
| --- | --- |
| [Newton: Light and Colour](examples/knowledge/newton-light-colour.md) | Check apparatus and distinguish historical claims from game simplifications |
| [Newton: Experimental Variants](examples/knowledge/newton-experimental-variants.md) | Support an aperture comparison with a specific source |
| [Evaluate Game Procedures](examples/knowledge/game-procedure-evaluation.md) | Check commands, prerequisites, replay, and interpretation limits |
| [STEM Source Register](examples/knowledge/source-register.md) | Track provenance and identify the failed Wikipedia import |

The Newton entries summarize primary accounts from the [Newton Project](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006). They identify their sources and limits; they are not full article imports. Keep Web Search unchanged during comparisons and record whether evidence came from uploaded entries or external pages.

## Optional References

[Source examples](knowledge/reference.html) preserve research and historical alternatives. [Skill and tool examples](skills/reference.html) preserve the blank template, source interpretation exercise, creator failures, corrections, and test labels. These ordinary pages contain no hidden notes.

## README.md

### Before

# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Composing system prompts begins the series. Use **Outline** to move to Curating knowledge collections and Configuring skills and tools. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](SLIDES.md)
- [Presenter lesson plans and access requirements](WORKSHOP.md)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Latest copy refinements and before/after](review/streamline-review.md)
- [Source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

Participants learn how user prompts and system prompts differ, then compare how two small models interpret a sentence about a nurse and doctor. They ask whether to walk or drive to a car wash and save both responses. After reading sample system prompt instructions, participants locate System Prompt in Chat Controls, add those instructions, and regenerate responses to their original prompt. Participants compare responses, check citations, and test tools in teaching and research tasks. STEM Adventure Games connects the workshops through its system prompt, STEM Wikipedia Experiments collection, and a playable adventure tool with a complementary skill for experimental variations.

## Workshop Artifacts

- [STEM Adventure tool](examples/tools/stem_adventure.py) and [playable preview](examples/adventure/preview.html)
- [Extend STEM Adventures skill](examples/stem-game-skill.md)
- [System prompt](examples/stem-system-prompt.txt)
- [Prism Laboratory scenario](examples/adventure/prism.json), [aperture variation](examples/adventure/aperture.json), and [winning commands](examples/adventure/winning-commands.json)
- [Additional knowledge entries](WORKSHOP.md#additional-knowledge-entries)
- [Skill Creator instructions](examples/creators/skill-creator-system-prompt.txt) and [Tool Creator instructions](examples/creators/tool-creator-system-prompt.txt)

Both creators accept requirements for any suitable task. STEM Adventure is a workshop request, not a default in either creator.

The engine checks moves, inventory, and prerequisites. Exported records can be restored by replaying commands. Type `discuss` to place a run in the Sandbox message box for review and sending. A game’s programmed observations are distinct from historical evidence.

## Development

Static HTML, CSS, and JavaScript. No build step or runtime dependencies.

```sh
python3 -m http.server 8766
python3 scripts/check_series.py
python3 scripts/test_copy_regressions.py
node scripts/test_deck_interactions.cjs
node examples/adventure/test-engine.cjs
python3 examples/adventure/test-validation.py
```

After changing game sources, run `python3 examples/adventure/build_tool.py` to rebuild the Open WebUI tool and preview. After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, the slider, or **Outline** to navigate. On mobile, the slider occupies a full row above the navigation buttons. Text selection does not advance slides. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Outline** links to each workshop, prompt examples, and the complete transcript, including screenshot instructions. Presenter lesson plans remain available through this README.

## Sources

Developed by Zach Muhlbauer from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools). Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. Reused comparison screenshots exclude obsolete controls. Capture provenance and source limitations remain in review files.

### After

# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Composing system prompts begins the series. Use **Outline** to move to Curating knowledge collections and Configuring skills and tools. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](SLIDES.md)
- [Presenter lesson plans and access requirements](WORKSHOP.md)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Latest copy refinements and before/after](review/streamline-review.md)
- [Source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

Participants learn how user prompts and system prompts differ, then compare how two small models interpret a sentence about a nurse and doctor. They ask whether to walk or drive to a car wash and save both responses. After reading sample system prompt instructions, participants locate System Prompt in Chat Controls, add those instructions, and regenerate responses to their original prompt. Participants compare responses, check citations, and test tools in teaching and research tasks. After reviewing Workspace model cards, participants choose [STEM Adventure Games](https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games) for teaching or [Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions) for research, clone it, and revise its instructions. Workshop 2 adds source documents. Workshop 3 uses a separate advanced game to examine tools and skills.

## Workshop Artifacts

- [STEM Adventure tool](examples/tools/stem_adventure.py) and [playable preview](examples/adventure/preview.html)
- [Extend STEM Adventures skill](examples/stem-game-skill.md)
- [System prompt](examples/stem-system-prompt.txt)
- [Prism Laboratory scenario](examples/adventure/prism.json), [aperture variation](examples/adventure/aperture.json), and [winning commands](examples/adventure/winning-commands.json)
- [Additional knowledge entries](WORKSHOP.md#additional-knowledge-entries)
- [Skill Creator instructions](examples/creators/skill-creator-system-prompt.txt) and [Tool Creator instructions](examples/creators/tool-creator-system-prompt.txt)

Both creators accept requirements for any suitable task. STEM Adventure is a workshop request, not a default in either creator.

The engine checks moves, inventory, and prerequisites. Exported records can be restored by replaying commands. Type `discuss` to place a run in the Sandbox message box for review and sending. A game’s programmed observations are distinct from historical evidence.

## Development

Static HTML, CSS, and JavaScript. No build step or runtime dependencies.

```sh
python3 -m http.server 8766
python3 scripts/check_series.py
python3 scripts/test_copy_regressions.py
node scripts/test_deck_interactions.cjs
node examples/adventure/test-engine.cjs
python3 examples/adventure/test-validation.py
```

After changing game sources, run `python3 examples/adventure/build_tool.py` to rebuild the Open WebUI tool and preview. After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, the slider, or **Outline** to navigate. On mobile, the slider occupies a full row above the navigation buttons. Text selection does not advance slides. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Outline** links to each workshop, prompt examples, and the complete transcript, including screenshot instructions. Presenter lesson plans remain available through this README.

## Sources

Developed by Zach Muhlbauer from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools). Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. Reused comparison screenshots exclude obsolete controls. Capture provenance and source limitations remain in review files.
