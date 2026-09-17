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

Keep the system prompt from your chosen model in Workshop 1. The [adventure prompt](examples.html#stem-chat) and [research prompt](examples.html#wikipedia-revisions) remain available for comparison. The [source-checking instructions](examples.html#stem-sources) can extend the adventure prompt when participants ask about evidence. Keep Skills and Tools unselected. Participants can build a small collection for another experiment or adapt the procedure to their own teaching or research. They should know the source material well enough to check model claims independently.

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

The original collection contained three Wikipedia imports. List of experiments initially contained a Wikimedia error; complete article text was restored on September 17, 2026, as documented in the [repair record](review/prompt-style-2026-09-16/knowledge-repair/README.md). Scientific method and Women in science remain alongside it. Additional entries cover Newton’s optical experiments, procedural variants, and software checks. Verify retrieval separately from successful text import.

### Additional Knowledge Entries

| Entry | Use |
| --- | --- |
| [Newton: Light and Colour](examples/knowledge/newton-light-colour.md) | Check apparatus and distinguish historical claims from game simplifications |
| [Newton: Experimental Variants](examples/knowledge/newton-experimental-variants.md) | Support an aperture comparison with a specific source |
| [Evaluate Game Procedures](examples/knowledge/game-procedure-evaluation.md) | Check commands, prerequisites, replay, and interpretation limits |
| [STEM Source Register](examples/knowledge/source-register.md) | Track provenance and document the repaired Wikipedia import |

The Newton entries summarize primary accounts from the [Newton Project](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006). They identify their sources and limits; they are not full article imports. Keep Web Search unchanged during comparisons and record whether evidence came from uploaded entries or external pages.

## Optional References

[Source examples](knowledge/reference.html) preserve research and historical alternatives. [Skill and tool examples](skills/reference.html) preserve the blank template, source interpretation exercise, creator failures, corrections, and test labels. These ordinary pages contain no hidden notes.
