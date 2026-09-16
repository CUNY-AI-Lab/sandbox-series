# Workshop readability and game progression

Workshops 1 and 2 use STEM Adventure Games through scenes and numbered choices in chat. Workshop 3 uses STEM Adventure Games — Advanced with its separate tool and skill. Introductory slides omit game records, scenario files, and code. Each lesson plan still totals 90 minutes.

Slide 5 groups related definitions and combines source links. Slides 12 and 13 typeset the exact recommendations visible in the original screenshots and link those images. Those crops contain no further reasoning to transcribe. Slide 27 shows a short excerpt of the introductory prompt. Participants then adapt context, procedure, constraints, tone, and format through ordinary instructions.

The revision applies humanizer, no-ai-slop, and milwrite-style in that order. Short sentences and numbered instructions are necessary here for projected workshop slides. Definitions and controls follow Sandbox and Open WebUI documentation. The introductory prompt preserves the prior menu, choices, Unicode headings, and source grounding; rooms, objects, exploration, and hints draw on classic text-adventure conventions.

Sources consulted

- [Sandbox custom models](https://ailab.gc.cuny.edu/sandbox-docs/models/)
- [Open WebUI models](https://docs.openwebui.com/features/workspace/models/)
- [Open WebUI knowledge](https://docs.openwebui.com/features/workspace/knowledge/)
- [Zork instruction manual, pages 3–4](https://www.ifarchive.org/if-archive/infocom/demos/ztuu.pdf)
- [Previous STEM system prompt](../live/stem-system-prompt-before.txt)

The Zork manual supports rooms, examining objects, ordinary-language commands, and help. Its characters, setting, and prose are not reused. The new scientific scenes remain model-generated fiction, with source checks for historical claims.

Complete edited passages follow. `copy-before.md`, `copy-after.md`, and `copy.diff` retain the full examples page and lesson plan as well as every changed slide.

## index.html · 5 · System Prompts

### Before

### System Prompts



A system prompt gives a model instructions for its role, behavior, and focus.



### User Prompts



Questions or tasks you enter in chat.



### Base Models



A base model generates responses. A custom model adds instructions and resources to a chosen base model.



Test whether your selected model follows these instructions.



[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/)



[Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)



Creating a custom model does not train a new base model.

### After

### System Prompts



A system prompt gives a model instructions for its role, behavior, and focus.



### User Prompts



Questions or tasks you enter in chat.



### Base Models



A base model generates responses. A custom model adds instructions and resources without training a new base model.



[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/) · [Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)


## index.html · 6 · Select Models

### Before

### Select Models



![Sandbox chat with CUNY AI Lab logo, message box, and open model selector showing search and model choices; arrow marks model ID at bottom right of message box](images/current/model-selector-open-2026-09-16.svg)



Select model ID on bottom right of message box. Type a request, send it, then ask a follow-up. Open New Chat to start without earlier messages.

### After

### Select Models



![Sandbox chat with CUNY AI Lab logo, message box, and open model selector; enlarged detail shows model choices with model ID outlined and marked by an arrow](images/current/model-selector-hidpi-2026-09-16.svg)



Select model ID on bottom right of message box. Type a request, send it, then ask a follow-up. Open New Chat to start without earlier messages.


## index.html · 8 · Compare Models

### Before

### Compare Models



![Sandbox logo, message box, and model selector with Compare button marked by an arrow](images/current/model-selector-compare-2026-09-14.svg)



Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two small models. If Compare is unavailable, send identical prompts in separate new chats.

### After

### Compare Models



![Sandbox logo, message box, and open model selector; enlarged detail shows Compare button beside search field outlined and marked by an arrow](images/current/model-selector-compare-hidpi-2026-09-16.svg)



Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two small models. If Compare is unavailable, send identical prompts in separate new chats.


## index.html · 12 · Gemma’s Response

### Before

### Gemma’s Response



![Gemma recommends walking to a car wash](images/showcase/car-wash-gemma.png)

### After

### Gemma’s Response



You should **walk** to the car wash.



[View original response](images/showcase/car-wash-gemma.png)


## index.html · 13 · Qwen’s Response

### Before

### Qwen’s Response



![Qwen recommends driving to a car wash](images/showcase/car-wash-qwen.png)

### After

### Qwen’s Response



You should **take the car**.



[View original response](images/showcase/car-wash-qwen.png)


## index.html · 21 · Model Configuration

### Before

### Model Configuration



![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields; outlines identify each field.](images/current/model-create-2026-09-16-annotated.svg)



Select Create in Models. Enter a recognizable name, choose a tested base model, and add your tested system prompt.

### After

### Model Configuration



![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.](images/current/model-create-hidpi-2026-09-16.svg)



Select Create in Models. Enter a recognizable name, choose a tested base model, and add your tested system prompt.


## index.html · 25 · STEM Adventure Games

### Before

### STEM Adventure Games



![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](images/current/stem-game-2026-09-14.png)



Preview Prism Laboratory. Configure and run this game in Workshop 3.

### After

### STEM Adventure Games



![STEM Adventure Games presents a short scene and numbered choices directly in Sandbox chat.](images/current/stem-chat-play-hidpi-2026-09-16.png)



Type Start an adventure. Choose an experiment, then reply with a number or describe what you want to do.


## index.html · 26 · Inspect System Prompt

### Before

### Inspect System Prompt



![STEM Adventure Games model editor showing DeepSeek V4 Pro 0813 under Base Model and opening system prompt instructions.](images/current/stem-model-2026-09-14.png)



Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt.

### After

### Inspect System Prompt



![STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.](images/current/stem-chat-model-hidpi-2026-09-16.svg)



Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt.


## index.html · 27 · Read Game Instructions

### Before

### Read Game Instructions



Read instructions for game commands and submitted records, used in Workshop 3.



```text
STEM Adventure controls rooms, inventory, prerequisites, observations, and completion.

Ask users to type discuss inside the game, review the message box, and send their record before interpreting their choices.
```



Which part runs game commands? What must users send before discussing their choices?



[Read full system prompt](examples.html#stem-system)

### After

### Read Game Instructions



```text
End each scene with three numbered choices. Accept a number or an action in ordinary language, such as looking around, examining an object, or asking for a hint. Wait for a response before continuing.
```



What should happen after you choose an action?



[Read full system prompt](examples.html#stem-chat)


## index.html · 28 · Adapt Research Prompts

### Before

### Adapt Research Prompts



Choose a research task, such as comparing article abstracts, checking how you coded a passage, or documenting a method.



- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.



Save your source material, prompt, response, and assessment together.

### After

### Adapt Research Prompts



You can adapt this exercise to a research task, such as comparing article abstracts or documenting a method.



- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.



Save your source material, prompt, response, and assessment together.


## index.html · 30 · Define Prompt Components

### Before

### Define Prompt Components



Adapt STEM Adventure Games through these components.



- **Context** — Experiment, historical setting, and intended users.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Tone and format** — Language, length, and presentation.

### After

### Define Prompt Components



Choose one component to change.



- **Context** — Experiment, historical setting, and intended users.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Tone and format** — Language, length, and presentation.


## index.html · 31 · Define Context

### Before

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

### After

### Define Context



Describe what your model should help users do.



- Who will use this model?

- Which experiment or research question will they explore?

- What prior knowledge can you assume?



```text
Guide a short text adventure about light and colour.
Help players explore how a prism changes a beam of sunlight.
```


## index.html · 32 · Write Procedures

### Before

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

### After

### Write Procedures



What should happen before and after each choice?



```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer three numbered choices and wait.
4. Describe observations after players choose.
```


## index.html · 35 · Specify Format

### Before

### Specify Format



Specify how your model should discuss a submitted record.



```text
Observed decision: [Command and result]
Prerequisite: [Condition required for that action]
Source comparison: [What historical evidence supports]
Question: [One limitation to examine]
```

### After

### Specify Format



Specify how scenes and choices should appear.



```text
Write a short scene followed by three numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```


## index.html · 40 · Share Custom Models

### Before

### Share Custom Models



- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and attached collections, skills, and tools.



[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

### After

### Share Custom Models



- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and any attached collections.



[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)


## knowledge/index.html · 6 · Review Model Settings

### Before

### Review Model Settings



![Custom model for STEM source questions with a selected base model and source-checking System Prompt; outlines identify both fields.](../images/current/model-review-2026-09-16-annotated.svg)



Review Base Model and System Prompt in your custom model. Use [source-checking instructions](../examples.html#stem-sources) for this example. Leave Skills and Tools unselected. Under Advanced Params, set Function Calling to Legacy for this workshop.

### After

### Review Model Settings



![STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.](../images/current/stem-chat-model-hidpi-2026-09-16.svg)



Review **Base Model** and **System Prompt** in your custom model. Use [STEM Adventure Games instructions](../examples.html#stem-chat) from Workshop 1. Leave Skills and Tools unselected.


## knowledge/index.html · 10 · Review Source Roles

### Before

### Review Source Roles



Use sources for different questions.



Newton’s optical experiments



Check apparatus, procedures, and observations.



Scientific method



Examine hypotheses, measurement, and revision.



Women in science



Investigate collaboration, recognition, and institutions.



Keep source summaries and game documentation distinguishable.

### After

### Review Source Roles



Use sources for different questions.



Newton’s optical experiments



Check apparatus, procedures, and observations.



Scientific method



Examine hypotheses, measurement, and revision.



Women in science



Investigate collaboration, recognition, and institutions.



Check whether a scene follows its sources or adds invented details.


## knowledge/index.html · 12 · Review Attached Knowledge

### Before

### Review Attached Knowledge



![Custom model with STEM Wikipedia Experiments attached under Knowledge and no Skills or Tools selected; outline marks Knowledge.](../images/current/knowledge-attachments-2026-09-16-annotated.svg)



Select STEM Wikipedia Experiments under Knowledge in your custom model and choose Save & Update. Skills and Tools are added in Workshop 3.

### After

### Review Attached Knowledge



![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.](../images/current/knowledge-chat-attachments-hidpi-2026-09-16.svg)



Select STEM Wikipedia Experiments under Knowledge in your custom model and choose Save & Update. Skills and Tools are added in Workshop 3.


## knowledge/index.html · 13 · Check Game Sources

### Before

### Check Game Sources



Attach [Prism Laboratory scenario](../examples/adventure/prism-scenario.md) to chat. Compare this document with Newton: Light and Colour, a summary of Newton’s account.



```text
Using Newton: Light and Colour, identify apparatus details simplified in the attached Prism Laboratory scenario. Quote a relevant passage and identify this entry as a source summary. If it is unavailable, say so.
```



Open cited material. Does it support your model’s response?



[Read Newton source entry](../examples/knowledge/newton-light-colour.md) · [Review source register](../examples/knowledge/source-register.md)



[Read Newton’s account](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006) · [Read scenario](reference.html#prism-laboratory)

### After

### Check Game Sources



In your custom model, start an adventure about light and colour. Choose one action, then ask about its historical sources.



```text
Which objects in this scene appear in Newton: Light and Colour? Quote a relevant passage. Which details were invented for this game?
```



Open cited material. Does it support your model’s response?



[Read Newton source summary](../examples/knowledge/newton-light-colour.md) · [Read Newton’s account](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006)


## knowledge/index.html · 16 · Choose Reference Materials

### Before

### Choose Reference Materials



Choose documents for your collection.



- Use [Newton: Light and Colour](../examples/knowledge/newton-light-colour.md) for apparatus and observations.

- Use [Newton: Experimental Variants](../examples/knowledge/newton-experimental-variants.md) for procedural changes.

- Use [Evaluate Game Procedures](../examples/knowledge/game-procedure-evaluation.md) for software checks.



Download entries you want your model to use. Review their contents before uploading.



[Download Light and Colour](../examples/knowledge/newton-light-colour.md) · [Download Experimental Variants](../examples/knowledge/newton-experimental-variants.md) · [Download Game Procedures](../examples/knowledge/game-procedure-evaluation.md)

### After

### Choose Reference Materials



Choose source documents that help players investigate an experiment.



- Use [Newton: Light and Colour](../examples/knowledge/newton-light-colour.md) for apparatus and observations.

- Use [Newton: Experimental Variants](../examples/knowledge/newton-experimental-variants.md) for changes to experimental procedures.



Read entries before uploading. Distinguish these summaries from original historical accounts.



[Download Light and Colour](../examples/knowledge/newton-light-colour.md) · [Download Experimental Variants](../examples/knowledge/newton-experimental-variants.md)


## knowledge/index.html · 17 · Create Knowledge Collections

### Before

### Create Knowledge Collections



![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../images/current/knowledge-create.png)



Open Workspace → Knowledge → Create. Enter a name and description, keep access Private, then select Create Knowledge.

### After

### Create Knowledge Collections



![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../images/current/knowledge-create-hidpi-2026-09-16.png)



Open Workspace → Knowledge → Create. Enter a name and description, keep access Private, then select Create Knowledge.


## Lesson-plan revision

### Before

Participants first compare models and test system prompts, then upload documents for models to reference. The final workshop configures a playable text adventure, a complementary skill for experimental variations, and a creator model for Python tools. Participants compare responses, check citations, and test whether models follow their instructions.

### After

Participants first compare models and test system prompts through a text adventure played in chat. Workshop 2 adds source documents and checks how they inform scenes and explanations. Workshop 3 introduces a separate game tool, a skill for changing experiments, and a creator model for Python tools. Participants compare responses, check citations, and test whether models follow their instructions.


## Lesson-plan revision

### Before

Workshop 3 needs Knowledge access when the selected procedure retrieves from a collection. The STEM exercise uses its attached collection for historical claims. The game itself runs from a self-contained scenario without retrieval or a network connection.

### After

Workshop 3 needs Knowledge access when a procedure retrieves from a collection. Its advanced STEM example uses an attached collection for historical claims, while a separate tool runs game commands. Workshops 1 and 2 use scenes and choices generated in chat without attached skills or tools.


## Lesson-plan revision

### Before

Prepare **Examine Assumptions** using [this sample prompt](examples/assumption-check.txt) and a tested base model. Confirm access to **STEM Adventure Games** and **STEM Wikipedia Experiments** for later examples. Workshop 2 uses a source-checking custom model with the collection and no attached skills or tools. Set Function Calling to Legacy under Advanced Params for automatic knowledge retrieval; Native mode requires model-called knowledge tools. See [Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/). Reserve the playable STEM configuration for Workshop 3. The [complete game system prompt](examples/stem-system-prompt.txt) is a Workshop 3 reference.

### After

Prepare **Examine Assumptions** using [this sample prompt](examples/assumption-check.txt) and a tested base model. For Workshops 1 and 2, configure **STEM Adventure Games** with [instructions for an adventure played in chat](examples/stem-chat-system-prompt.txt). Leave Skills and Tools unselected. Confirm access to **STEM Wikipedia Experiments** for Workshop 2. Set Function Calling to Legacy under Advanced Params when preparing automatic knowledge retrieval; this setting is covered in [Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/). Save the tool-based configuration as **STEM Adventure Games — Advanced** for Workshop 3, using its [separate system prompt](examples/stem-system-prompt.txt).


## Lesson-plan revision

### Before

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Introduce the series, confirm sign-in, define system prompts, and locate the model selector. | Account readiness and prompt distinction |
| 10–25 | Demonstrate small models on the nurse question and car-wash question. Examine assumptions before showing the saved responses. | Exact inputs, model IDs, and responses |
| 25–45 | Compare the car-wash responses, paste the short in-chat system prompt, then choose Regenerate → Try Again on each original response. Keep the question and other settings unchanged. | Original and regenerated responses |
| 45–65 | Inspect Workspace models, create a private configuration, and review STEM prompt excerpts. Preview the game that participants will configure in Workshop 3. | Base model and system prompt |
| 65–85 | Adapt one system prompt. Test an ordinary request and an incomplete or conflicting request. Revise one instruction and repeat. | Failure, revision, and retest |
| 85–90 | Save the tested prompt and identify source documents for Workshop 2. | Private model and source question |

### After

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Introduce the series, confirm sign-in, define system prompts, and locate the model selector. | Account readiness and prompt distinction |
| 10–25 | Demonstrate small models on the nurse question and car-wash question. Examine assumptions before showing the saved responses. | Exact inputs, model IDs, and responses |
| 25–45 | Compare the car-wash responses, paste the short in-chat system prompt, then choose Regenerate → Try Again on each original response. Keep the question and other settings unchanged. | Original and regenerated responses |
| 45–65 | Inspect Workspace models and play two or three turns in STEM Adventure Games. Read its system prompt, then create a private configuration. | Base model, system prompt, and game responses |
| 65–85 | Change one instruction, such as how the game offers hints. Test a choice and a request for help, revise one instruction, and repeat. | Failure, revision, and retest |
| 85–90 | Save the tested prompt and identify source documents for Workshop 2. | Private model and source question |


## Lesson-plan revision

### Before

Participants upload documents to a knowledge collection and attach it to a custom model. They ask questions about those materials and check whether the model retrieves relevant passages and cites them accurately. This workshop adds knowledge only; skills and adventure tools begin in Workshop 3. STEM Wikipedia Experiments provides a concrete collection for checking historical claims, scientific methods, and the limits of imported sources.

### After

Participants add source documents to the adventure they played in Workshop 1. They ask about objects and events in a scene, then check whether cited passages support the model’s explanation. STEM Wikipedia Experiments provides material for checking historical claims and scientific procedures. Scenes and choices continue in chat; skills and tools begin in Workshop 3.


## Lesson-plan revision

### Before

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–15 | Confirm access, choose a document question, and save its initial response. Record any sources already used. Keep Skills and Tools unselected. | Question, settings, and initial response |
| 15–35 | Inspect STEM Wikipedia Experiments. Check imports and distinguish source summaries from historical texts. Attach the readable Prism Laboratory scenario and compare its apparatus with the Newton summary. | Source passages and supported claims |
| 35–55 | Select a few readable documents, create a private collection, upload files, wait for processing, and attach it to the same custom model. | Documents, collection, and saved model |
| 55–80 | Repeat the saved question with base model and system prompt unchanged. Check cited passages, try questions requiring two sources or missing information, and diagnose one failure. | Before/after responses and source checks |
| 80–90 | Retest one change, check sharing, and choose a procedure for Workshop 3. | Retest and next procedure |

Use the [source-checking system prompt](examples.html#stem-sources) for the Workshop 2 example. Keep Skills and Tools unselected. Participants examine the [Prism Laboratory scenario](examples/adventure/prism-scenario.md) as a document; running the game begins in Workshop 3. Participants can build a small collection for another experiment or adapt the procedure to their own teaching or research. They should know the source material well enough to check model claims independently.

### After

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–15 | Confirm access, choose a document question, and save its initial response. Record any sources already used. Keep Skills and Tools unselected. | Question, settings, and initial response |
| 15–35 | Inspect STEM Wikipedia Experiments and check imports. Play a short adventure about light and colour, then compare objects in its scene with Newton’s account. Distinguish the uploaded summary from its historical source. | Game scene, cited passages, and supported claims |
| 35–55 | Select a few readable documents, create a private collection, upload files, wait for processing, and attach it to the same custom model. | Documents, collection, and saved model |
| 55–80 | Repeat the saved question with base model and system prompt unchanged. Check cited passages, try questions requiring two sources or missing information, and diagnose one failure. | Before/after responses and source checks |
| 80–90 | Retest one change, check sharing, and choose a procedure for Workshop 3. | Retest and next procedure |

Use the same [adventure system prompt](examples.html#stem-chat) from Workshop 1. The [source-checking instructions](examples.html#stem-sources) can extend that prompt when participants ask about evidence. Keep Skills and Tools unselected. Participants can build a small collection for another experiment or adapt the procedure to their own teaching or research. They should know the source material well enough to check model claims independently.


## Lesson-plan revision

### Before

Participants use STEM Adventure to play a deterministic text adventure, inspect commands and prerequisites, and export a play record. They draft a skill, attach it to a private copy of STEM Adventure Games, test one procedural change, and examine how a model interprets the run. Kale Skill Builder and Tool Creator accept participants’ own requirements. Their system prompts and starter suggestions are general-purpose. STEM Adventure is a submitted workshop example. Tool Creator produces a reviewable Python draft with explicit tests. Each participant retains a skill draft, creator output, an installed copy of the tested tool, a scenario, and a play record. Creator output remains a draft until reviewed and tested.

### After

Participants use STEM Adventure to play a deterministic text adventure, inspect commands and prerequisites, and export a play record. They draft a skill, attach it to a private copy of STEM Adventure Games — Advanced, test one procedural change, and examine how a model interprets the run. Kale Skill Builder and Tool Creator accept participants’ own requirements. Their system prompts and starter suggestions are general-purpose. STEM Adventure is a submitted workshop example. Tool Creator produces a reviewable Python draft with explicit tests. Each participant retains a skill draft, creator output, an installed copy of the tested tool, a scenario, and a play record. Creator output remains a draft until reviewed and tested.


## Lesson-plan revision

### Before

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–25 | Open the playable STEM configuration, test commands, save and reload a play record, and submit it with discuss. | Commands, failed prerequisite, and play record |
| 25–45 | Clone STEM Adventure Games, remove inherited access grants, and save a private copy. Use Kale Skill Builder to draft one skill, save it, replace the existing attached skill, and update the private system prompt to name the draft. | Private model and saved skill |
| 45–65 | Attach Prism Laboratory JSON and request one aperture comparison. Run the resulting scenario. Compare the same request with and without the saved skill, keeping other settings and inputs fixed. | Generated scenarios, test results, and records |
| 65–83 | Request a Python draft from Tool Creator and save it for review. Install the provided tested adventure code separately, enable that copy, open a game, and inspect its actual call and result. | Creator draft, installed tested code, and tool result |
| 83–90 | Save artifacts, compare game records with source evidence, and identify a next test. | Artifacts, observed result, and next question |

### After

| Minutes | Activity | Evidence to retain |
| --- | --- | --- |
| 0–25 | Open STEM Adventure Games — Advanced, test commands, save and reload a play record, and submit it with discuss. | Commands, failed prerequisite, and play record |
| 25–45 | Clone STEM Adventure Games — Advanced, remove inherited access grants, and save a private copy. Use Kale Skill Builder to draft one skill, save it, replace the existing attached skill, and update the private system prompt to name the draft. | Private model and saved skill |
| 45–65 | Attach Prism Laboratory JSON and request one aperture comparison. Run the resulting scenario. Compare the same request with and without the saved skill, keeping other settings and inputs fixed. | Generated scenarios, test results, and records |
| 65–83 | Request a Python draft from Tool Creator and save it for review. Install the provided tested adventure code separately, enable that copy, open a game, and inspect its actual call and result. | Creator draft, installed tested code, and tool result |
| 83–90 | Save artifacts, compare game records with source evidence, and identify a next test. | Artifacts, observed result, and next question |


## Lesson-plan revision

### Before

Inspected and updated in Firefox on September 14, 2026. STEM Adventure Games uses DeepSeek V4 Pro 0813, STEM Wikipedia Experiments, STEM Adventure, and Extend STEM Adventures. Native function calling is selected. The revised system prompt describes each component and requires a submitted play record before interpreting game actions.

### After

**STEM Adventure Games** is the introductory model for Workshops 1 and 2. Its system prompt asks for short scenes, three numbered choices, and responses to actions typed in ordinary language. The model uses attached sources when discussing historical evidence. It has no attached skills or tools.

**STEM Adventure Games — Advanced** is reserved for Workshop 3. It uses STEM Adventure and Extend STEM Adventures with native function calling. Its system prompt describes those components and requires a submitted play record before interpreting actions taken inside the game interface.


## Introductory system prompt

New file `examples/stem-chat-system-prompt.txt`

```text
Guide a short text adventure about a scientific experiment. Players explore a setting, examine objects, and choose what to do by typing in chat.

◉ CHOOSE AN ADVENTURE ◉

List three experiments in plain language and wait for a choice. Use names that describe each experiment, without invented titles or introductory slogans. If a player names an experiment, begin with its opening scene.

▣ PLAY ▣

Describe where players are, what they can see, and what they need to find out. Use a few connected rooms or locations with objects they can examine or use. Keep locations and objects consistent with the chosen experiment.

For light and colour, begin in a darkened room with sunlight entering through a small opening, a prism, and a screen. Ask how players want to investigate coloured light.

End each scene with three numbered choices. Accept a number or an action in ordinary language, such as looking around, examining an object, or asking for a hint. Wait for a response before continuing.

After each action, describe what changes and offer next choices. Remember previous choices, objects, and observations. Allow players to revisit places and try another approach. Give one hint at a time when asked.

◈ SOURCES ◈

Use attached sources for historical details and experimental procedures. Distinguish documented events from invented characters, dialogue, and puzzles. If sources do not support a detail, say so when asked about it. When players ask about sources, pause the game. Quote a relevant passage exactly and identify which scene details it supports. Identify invented details separately. If retrieved text does not contain evidence, say so. Resume play when asked.

▣ STYLE ▣

Address players as “you.” Keep each scene under 100 words, followed by choices. Explain unfamiliar terms when they first appear. Use simple Unicode headings without bordered boxes or tables. Present scenes and choices directly in chat.
```
