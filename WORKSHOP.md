# Presenter Lesson Plans

The CUNY AI Lab Sandbox supports teaching, research, and experimentation with open-weight models. These workshops introduce its chat interface, custom models, knowledge collections, skills, and tools through demonstrations and guided exercises.

Participants first compare models and test system prompts, then upload documents for models to reference. The final workshop introduces reusable skill instructions and tools for operations such as web search and code execution. Participants compare responses, check citations, and test whether models follow their instructions.

[Present the series](https://cuny-ai-lab.github.io/sandbox-series/) · [Read all slide copy](SLIDES.md) · [Browse system-prompt examples](examples.html) · [Review copy changes](review/README.md)

## Workshop Roadmap

| Workshop | Activity | Required access | Next steps |
| --- | --- | --- | --- |
| Compose System Prompts | Configure model behavior with system prompts | Individual access approval and Sandbox sign-in | Save tested prompts; request Workspace and Knowledge access |
| Curate Knowledge Collections | Upload documents so models can reference them | Workshop 1 access, Workspace, Knowledge collection access | Save retrieval tests; request Skills and Tools access |
| Skills & Tools | Add web search, code execution, and reusable instructions | Workshop 1 access, Skills and Tools access; Workspace authoring for creation and editing | Save configurations; verify shared access; retest after changes |

Workshop 3 needs Knowledge access when the selected procedure retrieves from a collection. Its standalone skill and calculation exercises can be completed without a collection.

## Prepare Workshop Access

For individual access, follow [Getting Started](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/) to the Lab’s [access application](https://ailab.gc.cuny.edu/request-access/). Choose **My own access**, use CUNY Login, complete the application, and check the verified CUNY email for approval. Then enter the [Sandbox](https://chat.ailab.gc.cuny.edu/) through **Continue with CUNY Login**. Participants do not need an API key for these chat exercises.

Workshop 1 requires only individual access and sign-in. The facilitator enables the arranged Workspace access during the midpoint exercise. Participants refresh, inspect a sample custom model, and can save their tested prompt as a private configuration. If access is delayed, participants follow the demonstration and continue testing in chat. Before Workshop 2, arrange Workspace and Knowledge access with the Lab. Before Workshop 3, arrange Skills and Tools access, including authoring permissions for participants who will create or edit resources. Confirm which base models and capabilities are available to the group.

Prepare **Examine Assumptions** as a custom model using [this sample prompt](examples/assumption-check.txt) and a tested base model. Keep a plain-text copy available if the demonstration account cannot open it.

Choose two available small models for the opening demonstration. Record their exact identifiers and settings rather than treating screenshot labels as a current inventory. Check personal defaults, folder instructions, memory, and optional features that may introduce additional context. Keep these consistent during comparisons and document differences you cannot control.

Use documents you are permitted to upload and share for collection and skill exercises. Verify sharing through an ordinary participant account, including access to custom models, base models, and attached resources. Course enrollment has a separate invitation route in the documentation; it is not a prerequisite for Workshop 1.

## Compose System Prompts

Participants learn how user prompts and system prompts differ before comparing models. A system prompt gives a model instructions for its role, behavior, and focus. Begin comparisons with two small models interpreting a sentence about a nurse and doctor, then ask whether to walk or drive to a car wash. Participants save both responses, read sample system instructions, locate System Prompt in Chat Controls, and regenerate responses to their original prompt after adding those instructions.

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
| 25–35 | Ask participants to start a new chat, send the car wash question to two models, and save both responses. Read the sample system prompt and ask what should change in each response. Show Controls at the top right of chat and its System Prompt field before participants add instructions. | Original responses and expected effects of system instructions |
| 35–45 | Keep the control location visible with the exercise steps. Participants open Controls, add the sample instructions in System Prompt, close Controls, and select Regenerate beneath each original response. Leave the original question, selected models, and other settings unchanged. Compare outputs, then revisit the question about who was late. | Before-and-after comparison using the same criteria |
| 45–55 | Enable the arranged Workspace access. Participants refresh and inspect a prepared custom model with the facilitator. Read Base Model and System Prompt together, then connect those settings to the in-chat exercise. | Prompt text and model choice to carry forward |
| 55–75 | Discuss one disciplinary progression from the examples page. Participants adapt context, procedure, constraints, tone, and format for one teaching or research task. Keep other examples as reference material. | Draft prompt and private custom model when Workspace access is confirmed |
| 75–85 | Test a normal request, an incomplete request, and a request that conflicts with the intended procedure. Revise one instruction and repeat. | Failure, revision, and retest |
| 85–90 | Share one supported observation. Save prompt versions and comparison notes. Review access needed for Workshop 2. | Next question and access request |

### Compare Small Models

> The nurse yelled at the doctor because she was late. Who was late?

Send exactly this question to two small models with matching context. Ask which interpretation each response chooses and whether it acknowledges ambiguity. Either person can be the referent of “she”; the sentence does not establish a unique answer. A plausible interpretation is different from information established by the wording. Avoid turning this single item into a claim about model-wide bias or ability.

### Compare Outputs

> The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.

Screenshot provenance and inconsistent Qwen labels are documented in [source history](review/showcase-sources.json). Discuss these responses without treating screenshot labels or timings as reliable model identifiers or comparative measurements.

Ask “What do you think this person wants to accomplish?” Participants save both original responses and read the sample system prompt before changing settings. Ask what should change in each response. Show Controls at the top right of chat and its System Prompt field alongside the exercise instructions. Participants add the sample instructions, close Controls, and select Regenerate beneath each original response, leaving their question unchanged. Compare assumptions, explanations, and any change in recommendations.

| Criterion | Model A evidence | Model B evidence |
| --- | --- | --- |
| Identify stated goal or acknowledge missing purpose | | |
| Distinguish stated facts from assumptions | | |
| Give reasons that support recommendation | | |
| Compare outputs after changing system instructions | | |

For the in-chat system-prompt exercise, use [Examine Assumptions](examples/assumption-check.txt). It asks the model to examine facts and assumptions without prescribing either demonstration answer. Check whether the added instructions help, cause unnecessary questions, or fail on the second task. Save original responses before changing system instructions.

## Curate Knowledge Collections

Participants upload documents to a knowledge collection and attach it to a custom model. They ask questions about those materials and check whether the model retrieves relevant passages and cites them accurately. Course examples use assignments and readings; research examples compare claims and methods across source documents.

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
| 20–35 | Discuss one collection progression. Compare what each source contributes to the task. Offer the research collection as an alternative context. | Proposed source list with reasons |
| 35–55 | Create a private collection. Upload a few documents, wait for processing, and inspect extracted text. | Document versions and extraction problems |
| 55–65 | Attach the collection under Knowledge in the model editor and use Save & Update. Keep the model and system prompt fixed. | Collection and custom model settings |
| 65–80 | Test a question answered by one source, one requiring two sources, and one absent from the collection. Open cited passages and verify them. | Retrieved passages, responses, and judgments |
| 80–90 | Diagnose one failure and make one change. Check dependency access with the intended audience. Review Skills and Tools access for the next session. | Retest, access check, and next procedure |

Use the [system-prompt examples](examples.html) when a participant needs a starting configuration. Teaching participants can curate an assignment, a methodological framework, and readings. Research participants can curate a research question, codebook or protocol, and a few approved excerpts. Participants should know the sources well enough to judge the model’s claims independently.

A generic or incorrect answer can arise from processing, retrieval, access, instructions, or interpretation. Check the actual evidence before diagnosing the cause. File length alone does not determine retrieval quality. Scanned or multi-column PDFs deserve particular attention during text extraction.

### Next steps

- Save source lists and retrieval tests
- Request Skills and Tools access
- Choose recurring teaching or research procedures
- Review system-prompt examples
- Continue to Skills & Tools

## Skills & Tools

Participants write reusable Markdown instructions for a teaching or research procedure, attach the skill to a model, and test whether the model loads and follows it. They then enable an available tool for web search or code execution, inspect its results, and check the final response.

### Workshop Agenda

- Confirm Skills and Tools access
- Choose recurring procedures
- Write skill instructions
- Attach skills to models
- Inspect tool calls and results
- Test models with skills and tools

### Lesson Plan

| Minutes | Facilitation and participant activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Confirm sign-in, Skills and Tools access, authoring permissions, and a usable custom model. Confirm Knowledge access only when the chosen task requires a collection. | Available resources and original response |
| 10–25 | Explain skills and tools. Demonstrate the Skill editor, model attachment, native function calling, and chat Integrations. | Trigger and capability requirements |
| 25–40 | Discuss one retained disciplinary procedure. Use Check Interpretations when relevant. | Procedure and success criteria |
| 40–60 | Draft trigger, procedure, and format. Create the skill, attach it, set Function Calling → Native, and save the model. | Skill version and model settings |
| 60–72 | Test a matching request, a follow-up, and an unrelated request. Inspect skill loading and whether the model pauses or continues as instructed. | Evidence of followed or missed instructions |
| 72–82 | Demonstrate an available search or code tool. For the included median task, inspect execution and check the expected answer, 8. | Tool call, result, and final response |
| 82–90 | Revise one component, repeat its test, and verify dependency access before sharing. | Retest and unresolved case |

The small calculation uses invented values `[3, 8, 8, 12, 19]`. It introduces a result participants can verify independently. It does not establish general numerical reliability. If Code Interpreter is unavailable, use an approved search capability and verify a returned page, or follow the facilitator’s demonstration.

The cinematic-image skill includes a necessary correction to the older instructions. A vision-capable model needs the actual image. Text retrieval from a knowledge collection should not be assumed to deliver an original visual for inspection.

### Next steps

- Save prompts, sources, skills, and tool settings
- Compare expected and observed behavior
- Revise instructions from recorded failures
- Verify shared access with intended users
- Retest after model or tool updates

## Source Documentation

Interface instructions draw on the published [Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/), especially [Getting Started](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/), [Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/), [Models](https://ailab.gc.cuny.edu/sandbox-docs/models/), [Knowledge Bases](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/), [Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/), and [Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/).

The live interface was inspected in Firefox on September 13, 2026. [Screenshot provenance](review/screenshot-sources.json) records source hashes and crop coordinates. [Showcase provenance](review/showcase-sources.json) distinguishes archival comparison excerpts from current interface instructions. The unrelated fourth screenshot is excluded.

Provider requests are described in the docs as configured for zero retention with training use prohibited. Sandbox history can still be stored and visible to administrators or its shared audience. Retrieved passages enter the model request and may appear in its response. Use materials appropriate for those conditions.

Open WebUI’s [Models](https://docs.openwebui.com/features/workspace/models/), [Knowledge](https://docs.openwebui.com/features/workspace/knowledge/), and [Skills](https://docs.openwebui.com/features/workspace/skills/) documentation supports the descriptions of custom configurations, retrieval, and skill loading. The Sandbox docs govern local access and sign-in instructions.
