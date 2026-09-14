# Prompt sequence review

Compared with `0fb985b5a45f51f3b95e9d373cd2bb66b74f814e`. HTML remains authoritative.

[Full workshop copy](../SLIDES.md) · [Direct diff](prompt-sequence.diff) · [Lesson plan](../WORKSHOP.md)

## Sequence

System prompts are defined before model comparison. Participants save original responses, read sample instructions, locate System Prompt in Controls, add instructions, regenerate each original response, and compare results.

| Current slide | Previous slide | Title |
| --- | --- | --- |
| 1 | 1 | Compose System Prompts |
| 2 | 2 | Workshop Roadmap |
| 3 | 3 | Workshop Agenda |
| 4 | 4 | Request Access |
| 5 | 15 | System Prompts |
| 6 | 5 | Select Models |
| 7 | 6 | Chat Features |
| 8 | 7 | Compare Models |
| 9 | 8 | Who Was Late? |
| 10 | 9 | Examine Assumptions |
| 11 | 10 | Compare Outputs |
| 12 | 11 | Gemma’s Response |
| 13 | 12 | Qwen’s Response |
| 14 | 13 | Compare Models |
| 15 | 17 | Read System Prompt |
| 16 | 16 | Open Chat Controls |
| 17 | 14 | Test System Prompts |
| 18 | Added | Regenerate Responses |
| 19 | 18 | Compare Responses |
| 20 | 19 | Open Workspace |

## Sources

The definition uses role, behavior, and focus from [CUNY AI Lab System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/). [Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/) locates message actions beneath responses. [Open WebUI Chat Parameters](https://docs.openwebui.com/features/chat-conversations/chat-features/chat-params/) identifies System Prompt in Chat Controls. Firefox captures show the current fields and button labels.

## Complete slide revisions

### Slide 3 — Workshop Agenda

**Before**

### Workshop Agenda

- Request individual access and sign in

- Compare responses from small models

- Compare outputs

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse

Before attending, request individual access and sign into Sandbox.

**After**

### Workshop Agenda

- Request individual access and sign in

- Define system prompts

- Compare responses from small models

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse

Before attending, request individual access and sign into Sandbox.

### Slide 5 — System Prompts

**Before**

### System Prompts

A system prompt defines how a model should behave throughout a conversation.

### User Prompts

Questions or tasks you enter in chat.

### System Prompts

Instructions defining model behavior, tone, boundaries, and response style.

Test whether your selected model follows these instructions.

[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/)

[Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

**After**

### System Prompts

A system prompt gives a model instructions for its role, behavior, and focus.

### User Prompts

Questions or tasks you enter in chat.

### System Prompts

Instructions defining model behavior, tone, boundaries, and response style.

Test whether your selected model follows these instructions.

[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/)

[Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

### Slide 7 — Chat Features

**Before**

### Chat Controls

Upload Files (+)

Attach images, PDFs, or documents.

Integrations

Choose tools and skills for this chat.

Message actions

Copy, edit, or regenerate a response. Open More (⋯) for additional actions.

[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

**After**

### Chat Features

Upload Files (+)

Attach images, PDFs, or documents.

Integrations

Choose tools and skills for this chat.

Message actions

Find actions beneath each response to copy, edit, or regenerate it. Open More (⋯) for additional actions.

[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

### Slide 14 — Compare Models

**Before**

### Compare Models

- Send your original question to two models. Save both responses.

- Add system instructions in Chat Controls.

- Regenerate responses to your original prompt. Compare outputs before and after adding instructions.

**After**

### Compare Models

Start a new chat, select two models, and send this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

Save both responses with your question and selected model IDs before adding system instructions.

### Slide 15 — Read System Prompt

**Before**

### Test System Prompts

Add these instructions in System Prompt under Chat Controls. Regenerate responses to your original prompt.

```text
Help the user examine a question before settling on an answer.

Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question.

Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.
```

**After**

### Read System Prompt

Read these instructions. What should change in each model’s response?

```text
Help the user examine a question before settling on an answer.

Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question.

Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.
```

### Slide 16 — Open Chat Controls

**Before**

### Open Chat Controls

![Current chat Controls panel with its System Prompt field](images/current/chat-controls.png)

Enter instructions in System Prompt under Chat Controls.

- Open your chat.

- Select **Controls** at top right.

- Enter sample instructions in **System Prompt**, then regenerate responses to your original prompt.

Use Chat Controls for this exercise. Defaults in Settings apply across chats.

**After**

### Open Chat Controls

![Sandbox logo, message box, and open Controls panel with System Prompt field marked by an arrow](images/current/chat-controls-2026-09-14-annotated.svg)

Open Controls at top right → System Prompt. Add sample instructions, then regenerate original responses.

- Open your chat.

- Select **Controls** at top right.

- Add sample instructions in **System Prompt**. Close Controls, then select **Regenerate** beneath each original response.

Leave your original question unchanged. Use Chat Controls for this exercise; defaults in Settings apply across chats.

### Slide 17 — Test System Prompts

**Before**

### Evaluate Responses

Compare how each model interprets your question and explains its recommendation.

- Which assumptions does each response make?

- Does either response invent information?

- How do outputs change after you edit system instructions?

Save both responses with your prompt and selected model IDs.

**After**

### Test System Prompts

- Copy sample instructions from [Read System Prompt](#15).

- Open **Controls** at top right of your chat. Add instructions in **System Prompt**.

- Close Controls. Select **Regenerate** beneath each original response.

Leave your original question, selected models, and other settings unchanged.

### Slide 18 — Regenerate Responses

**Before**

(No previous slide.)

**After**

### Regenerate Responses

![Original question, model response, and message box with Regenerate button marked by an arrow](images/current/regenerate-2026-09-14-annotated.svg)

After adding system instructions, select Regenerate beneath each original response.

### Slide 19 — Compare Responses

**Before**

### Compare Responses

- Compare responses before and after adding system instructions.

- Check whether each response identifies your goal, states assumptions, and answers without unnecessary questions.

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

Keep base models and other settings unchanged. Record any differences you cannot control.

**After**

### Compare Responses

- Compare responses before and after adding system instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

Keep base models and other settings unchanged. Record any differences you cannot control.

## README.md

**Before**

Participants first compare how two small models interpret a sentence about a nurse and doctor. They then ask whether to walk or drive to a car wash, edit system instructions, and regenerate responses to their original prompt. Participants compare responses, check citations, and test tools in teaching and research tasks. Long disciplinary examples remain available as reference material; the lesson plans identify a shorter path for live sessions.

**After**

Participants learn how user prompts and system prompts differ, then compare how two small models interpret a sentence about a nurse and doctor. They ask whether to walk or drive to a car wash and save both responses. After reading sample system instructions, participants locate System Prompt in Chat Controls, add those instructions, and regenerate responses to their original prompt. Participants compare responses, check citations, and test tools in teaching and research tasks. Long disciplinary examples remain available as reference material; the lesson plans identify a shorter path for live sessions.

## WORKSHOP.md

**Before**

Participants compare responses and test system instructions before saving a custom model for reuse. Begin with two small models interpreting a sentence about a nurse and doctor. Then ask whether to walk or drive to a car wash. Participants edit system instructions in Chat Controls and regenerate responses to their original prompt.

**After**

Participants learn how user prompts and system prompts differ before comparing models. A system prompt gives a model instructions for its role, behavior, and focus. Begin comparisons with two small models interpreting a sentence about a nurse and doctor, then ask whether to walk or drive to a car wash. Participants save both responses, read sample system instructions, locate System Prompt in Chat Controls, and regenerate responses to their original prompt after adding those instructions.

**Before**

- Request individual access and sign in
- Compare responses from small models
- Compare outputs
- Revise in-chat system prompts
- Explore Workspace models
- Save prompts for reuse

**After**

- Request individual access and sign in
- Define system prompts
- Compare responses from small models
- Revise in-chat system prompts
- Explore Workspace models
- Save prompts for reuse

**Before**

| Minutes | Facilitation and participant activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Introduce the series and agenda. Confirm sign-in. Locate the model selector inside the message box, More, Integrations, message actions, and Controls. | Account readiness and selected model names |
| 10–18 | Demonstrate two small models answering the nurse question. Ask participants to read both responses and identify assumptions. | Exact inputs, model identifiers, responses |
| 18–25 | Ask whether to walk or drive to a car wash. Show Gemma’s and Qwen’s responses after comparing models live. Ask participants what they think this person wants to accomplish. | Assumptions and evidence supporting each judgment |
| 25–35 | Ask participants to send this question to two models and save both responses. Introduce System Prompt in Chat Controls. | Original responses and system instructions |
| 35–45 | Add sample instructions through Controls → System Prompt. Regenerate responses to participants’ original prompt without changing base models or other settings. Compare outputs, then revisit our opening question about who was late. | Before-and-after comparison using the same criteria |
| 45–55 | Enable the arranged Workspace access. Participants refresh and inspect a prepared custom model with the facilitator. Read Base Model and System Prompt together, then connect those settings to the in-chat exercise. | Prompt text and model choice to carry forward |
| 55–75 | Discuss one disciplinary progression from the examples page. Participants adapt context, procedure, constraints, tone, and format for one teaching or research task. Keep other examples as reference material. | Draft prompt and private custom model when Workspace access is confirmed |
| 75–85 | Test a normal request, an incomplete request, and a request that conflicts with the intended procedure. Revise one instruction and repeat. | Failure, revision, and retest |
| 85–90 | Share one supported observation. Save prompt versions and comparison notes. Review access needed for Workshop 2. | Next question and access request |

**After**

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

**Before**

Ask “What do you think this person wants to accomplish?” Participants save both original responses, add system instructions in Chat Controls, and regenerate responses to their unchanged prompt. Compare assumptions, explanations, and any change in recommendations.

**After**

Ask “What do you think this person wants to accomplish?” Participants save both original responses and read the sample system prompt before changing settings. Ask what should change in each response. Show Controls at the top right of chat and its System Prompt field alongside the exercise instructions. Participants add the sample instructions, close Controls, and select Regenerate beneath each original response, leaving their question unchanged. Compare assumptions, explanations, and any change in recommendations.

## Verification

- Content checks passed across 119 slides, including retained examples, exact demonstration questions, headings, articles, screenshot hashes, links, and transcripts.
- Nine revised slides checked at 1280×720 and 390×844. No clipped headings, horizontal overflow, missing images, screenshot/footer overlap, or browser warnings and errors.
- Prompt-copy button and link to Read System Prompt verified in browser. Both annotated images open in the expanded screenshot dialog and close with Escape.
- System Prompt and Regenerate annotations visually checked against Firefox screenshots and native control names.
- Original prompt examples remain unchanged. Evaluation questions about assumptions, invented information, goals, and unnecessary questions remain in Compare Responses.

## Added material

One screenshot slide, Regenerate Responses, was added at participant request. A direct copy button on Test System Prompts lets participants copy the existing sample without leaving the exercise. The car wash question is repeated unchanged where participants begin their own comparison. No new prompt example or model-comparison claim was added.
