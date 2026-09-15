# Presenter Lesson Plans

The CUNY AI Lab Sandbox supports teaching, research, and experimentation with open-weight models. These workshops introduce its chat interface, custom models, knowledge collections, skills, and tools through demonstrations and guided exercises.

Participants first compare models and test system prompts, then upload documents for models to reference. The final workshop configures a playable text adventure, a complementary skill for experimental variations, and a creator model for Python tools. Participants compare responses, check citations, and test whether models follow their instructions.

[Present the series](https://cuny-ai-lab.github.io/sandbox-series/) · [Read all slide copy](SLIDES.md) · [Browse system-prompt examples](examples.html) · [Review copy changes](review/README.md)

## Workshop Roadmap

| Workshop | Activity | Required access | Next steps |
| --- | --- | --- | --- |
| Composing system prompts | Configure model behavior with system prompts | Individual access approval and Sandbox sign-in | Save tested prompts; request Workspace and Knowledge access |
| Curating knowledge collections | Upload documents so models can reference them | Workshop 1 access, Workspace, Knowledge collection access | Save retrieval tests; request Skills and Tools access |
| Configuring skills and tools | Configure an adventure tool and reusable instructions | Workshop 1 access, Skills and Tools access; Workspace authoring for creation and editing | Save configurations; verify shared access; retest after changes |

Workshop 3 needs Knowledge access when the selected procedure retrieves from a collection. The STEM exercise uses its attached collection for historical claims. The game itself runs from a self-contained scenario without retrieval or a network connection.

## Prepare Workshop Access

For individual access, follow [Getting Started](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/) to the Lab’s [access application](https://ailab.gc.cuny.edu/request-access/). Choose **My own access**, use CUNY Login, complete the application, and check the verified CUNY email for approval. Then enter the [Sandbox](https://chat.ailab.gc.cuny.edu/) through **Continue with CUNY Login**. Participants do not need an API key for these chat exercises.

Workshop 1 requires only individual access and sign-in. The facilitator enables the arranged Workspace access during the midpoint exercise. Participants refresh, inspect a sample custom model, and can save their tested prompt as a private configuration. If access is delayed, participants follow the demonstration and continue testing in chat. Before Workshop 2, arrange Workspace and Knowledge access with the Lab. Before Workshop 3, arrange Skills and Tools access, including authoring permissions for participants who will create or edit resources. Confirm which base models and capabilities are available to the group.

Prepare **Examine Assumptions** using [this sample prompt](examples/assumption-check.txt) and a tested base model. Confirm access to **STEM Adventure Games** and **STEM Wikipedia Experiments** for the later demonstration. The [observed system prompt](examples/stem-system-prompt.txt) is available as a reference.

Choose two available small models for the opening demonstration. Record their exact identifiers and settings rather than treating screenshot labels as a current inventory. Check personal defaults, folder instructions, memory, and optional features that may introduce additional context. Keep these consistent during comparisons and document differences you cannot control.

Use documents you are permitted to upload and share for collection and skill exercises. Verify sharing through an ordinary participant account, including access to custom models, base models, and attached resources. Course enrollment has a separate invitation route in the documentation; it is not a prerequisite for Workshop 1.

## Composing system prompts

Participants learn how user prompts and system prompts differ before comparing models. A system prompt gives a model instructions for its role, behavior, and focus. Begin comparisons with two small models interpreting a sentence about a nurse and doctor, then ask whether to walk or drive to a car wash. Participants save both responses, read sample system prompt instructions, locate System Prompt in Chat Controls, and regenerate responses to their original prompt after adding those instructions.

### Workshop Agenda

- Request individual access and sign in
- Define system prompts
- Compare responses from small models
- Revise in-chat system prompts
- Explore Workspace models
- Save prompts for reuse

### Lesson Plan

| Minutes | Facilitation and participant activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Introduce the series and agenda. Confirm sign-in. Define system prompts through model role, behavior, and focus, and distinguish them from user questions or tasks. Locate the model selector inside the message box, Integrations, and message actions. | Account readiness and distinction between user and system prompts |
| 10–18 | Demonstrate two small models answering the nurse question. Ask participants to read both responses and identify assumptions. | Exact inputs, model identifiers, responses |
| 18–25 | Ask whether to walk or drive to a car wash. Show Gemma’s and Qwen’s responses after comparing models live. Ask participants what they think this person wants to accomplish. | Assumptions and evidence supporting each judgment |
| 25–35 | Ask participants to start a new chat, send the car wash question to two models, and save both responses. Read the sample system prompt and ask what should change in each response. Show Controls at the top right of chat and its System Prompt field before participants add instructions. | Original responses and expected effects of system prompt instructions |
| 35–45 | Keep the control location visible with the exercise steps. Participants open Controls, add the sample instructions in System Prompt, close Controls, and select Regenerate beneath each original response, then choose Try Again. Leave the original question, selected models, and other settings unchanged. Compare outputs, then revisit the question about who was late. | Before-and-after comparison using the same criteria |
| 45–55 | Enable the arranged Workspace access. Participants refresh and inspect a prepared custom model with the facilitator. Read Base Model and System Prompt together, then connect those settings to the in-chat exercise. | Prompt text and model choice to carry forward |
| 55–75 | Open STEM Adventure Games in Model Selector, then inspect its base model and system prompt in Workspace. Read its game rules, run two commands in Prism Laboratory, and choose one instruction to adapt. Use the component templates to draft a private variant. | Draft prompt and private custom model when Workspace access is confirmed |
| 75–85 | Test a normal request, an incomplete request, and a request that conflicts with the intended procedure. Revise one instruction and repeat. | Failure, revision, and retest |
| 85–90 | Share one supported observation. Save prompt versions and comparison notes. Review access needed for Workshop 2. | Next question and access request |

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

Participants upload documents to a knowledge collection and attach it to a custom model. They ask questions about those materials and check whether the model retrieves relevant passages and cites them accurately. STEM Wikipedia Experiments provides a concrete collection for checking historical claims, scientific methods, and the limits of imported sources.

### Workshop Agenda

- Confirm Workspace and Knowledge access
- Select source documents
- Create knowledge collections
- Attach collections to custom models
- Check source citations
- Choose procedures for skills

### Lesson Plan

| Minutes | Facilitation and participant activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Confirm individual sign-in, Workspace, Knowledge access, and a custom model or prompt from Workshop 1. Save a response before adding sources. | Original model settings and response |
| 10–20 | Explain extraction, passages, retrieval, and response context. Demonstrate the current Knowledge creation form. | Question about a document and expected passage |
| 20–35 | Open STEM Wikipedia Experiments. Inspect the original Wikipedia imports and the added Newton entries. Contrast a failed import, a historical source summary, and software documentation. Compare game apparatus with Newton’s account. | Proposed source list with reasons |
| 35–55 | Create a private collection. Upload a few documents, wait for processing, and inspect extracted text. | Document versions and extraction problems |
| 55–65 | Attach the collection under Knowledge in the model editor and use Save & Update. Keep the model and system prompt fixed. | Collection and custom model settings |
| 65–80 | Test a question answered by one source, one requiring two sources, and one absent from the collection. Open cited passages and verify them. | Retrieved passages, responses, and judgments |
| 80–90 | Diagnose one failure and make one change. Check dependency access with the intended audience. Review Skills and Tools access for the next session. | Retest, access check, and next procedure |

Use the [STEM system prompt and drafts](examples.html) as starting configurations. Participants can build a small collection for another experiment or adapt the procedure to their own teaching or research. They should know the source material well enough to check model claims independently.

A generic or incorrect answer can arise from processing, retrieval, access, instructions, or interpretation. Check the actual evidence before diagnosing the cause. File length alone does not determine retrieval quality. Scanned or multi-column PDFs deserve particular attention during text extraction.

### Next steps

- Save source lists and retrieval tests
- Request Skills and Tools access
- Choose recurring teaching or research procedures
- Review system-prompt examples
- Continue to Configuring skills and tools

## Configuring skills and tools

Participants use STEM Adventure to play a deterministic text adventure, inspect commands and prerequisites, and export a play record. They attach Extend STEM Adventures to guide a source-based procedural change, test the resulting scenario, and examine how a model interprets the run. Kale Skill Builder and Tool Creator accept participants’ own requirements. Their system prompts and starter suggestions are general-purpose. STEM Adventure is a submitted workshop example. Tool Creator produces a reviewable Python draft with explicit tests. Each participant retains a skill, tool, scenario, and record of expected and observed behavior.

### Workshop Agenda

- Confirm Skills and Tools access
- Play STEM Adventure
- Inspect commands and results
- Configure reusable skills
- Create and test tools
- Compare procedural changes

### Lesson Plan

| Minutes | Facilitation and participant activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Confirm sign-in and resource access. Revisit STEM Adventure Games, its system prompt, and source collection. Identify what a skill describes and what a tool executes. | Model, source, skill, and tool versions |
| 10–23 | Open Prism Laboratory through STEM Adventure. Explore rooms, take objects, try a blocked action, and enter help. Run the prepared winning sequence. | Commands and expected prerequisites |
| 23–33 | Enter undo and restart, then save and load a play record. Enter discuss and send the resulting record. Check the model’s account against recorded commands. | Exported record and interpretation |
| 33–48 | Open Kale Skill Builder and read Extend STEM Adventures. Identify trigger, procedure, and output. Examine the supplied draft’s unsupported completion claim and its correction. Create a private copy, attach it to a model, and use native function calling. | Skill instructions and attachment |
| 48–63 | Attach Prism Laboratory JSON and request an aperture comparison using Newton: Experimental Variants. Compare generated scenario JSON with the prepared example. Run a winning sequence and a blocked action. | Scenario, source passage, expected and actual results |
| 63–78 | Open Tool Creator. Request a bounded operation, review its Python code, and inspect the numeric-command validation failure and correction. Distinguish proposed tests from executed tests. Inspect the supplied STEM Adventure implementation, then install a private copy when authoring access is available. | Tool artifact and test cases |
| 78–86 | Repeat one request with and without the skill while holding other settings fixed. Revise one instruction from observed behavior. | Before/after responses and retest |
| 86–90 | Save artifacts and check access from a participant account before sharing. Identify one unresolved historical or procedural question. | Skill, tool, scenario, play record, next question |

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

The live interface was inspected in Firefox on September 13–14, 2026. [Screenshot provenance](review/screenshot-sources.json) records source hashes and crop coordinates. [Showcase provenance](review/showcase-sources.json) distinguishes archival comparison excerpts from current interface instructions. The unrelated fourth screenshot is excluded.

Provider requests are described in the docs as configured for zero retention with training use prohibited. Sandbox history can still be stored and visible to administrators or its shared audience. Retrieved passages enter the model request and may appear in its response. Use materials appropriate for those conditions.

Open WebUI’s [Models](https://docs.openwebui.com/features/workspace/models/), [Knowledge](https://docs.openwebui.com/features/workspace/knowledge/), and [Skills](https://docs.openwebui.com/features/workspace/skills/) documentation supports the descriptions of custom configurations, retrieval, and skill loading. The Sandbox docs govern local access and sign-in instructions.

## STEM Configuration

Inspected and updated in Firefox on September 14, 2026. STEM Adventure Games uses DeepSeek V4 Pro 0813, STEM Wikipedia Experiments, STEM Adventure, and Extend STEM Adventures. Native function calling is selected. The revised system prompt describes each component and requires a submitted play record before interpreting game actions.

The original collection contained three Wikipedia imports. Scientific method and Women in science contained article text; List of experiments contained a Wikimedia 429 error and was only 369 bytes. The failed import is identified in the source register and system prompt so it is not treated as evidence. Additional entries provide Newton’s optical experiments, procedural variants, software evaluation guidance, and a source register. Inspect processing and retrieval before using newly added material.

### Additional Knowledge Entries

| Entry | Use |
| --- | --- |
| [Newton: Light and Colour](examples/knowledge/newton-light-colour.md) | Check apparatus and distinguish historical claims from game simplifications |
| [Newton: Experimental Variants](examples/knowledge/newton-experimental-variants.md) | Support an aperture comparison with a specific source |
| [Evaluate Game Procedures](examples/knowledge/game-procedure-evaluation.md) | Check commands, prerequisites, replay, and interpretation limits |
| [STEM Source Register](examples/knowledge/source-register.md) | Track provenance and identify the failed Wikipedia import |

The Newton entries summarize primary accounts from the [Newton Project](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006). They identify their sources and limits; they are not full article imports. Web Search remains available, so verify whether cited evidence came from uploaded entries or external pages.
