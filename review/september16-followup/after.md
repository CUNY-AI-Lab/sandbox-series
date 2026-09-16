# Composing system prompts

## Slide 1: Composing system prompts

Workshop 1 of 3

### Composing system prompts

Compare and configure models for teaching and research

CUNY AI Lab Sandbox

Developed by Zach Muhlbauer

---

## Slide 2: Workshop Roadmap

### Workshop Roadmap

- **Composing system prompts** Configure model behavior with system prompts.

- **Curating knowledge collections** Upload documents so models can reference them.

- **Configuring skills and tools** Add web search, code execution, and reusable instructions.

[Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/)

---

## Slide 3: Workshop Agenda

### Workshop Agenda

- Request individual access and sign in

- Define system prompts

- Compare responses from small models

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse

Before attending, request individual access and sign into Sandbox.

---

## Slide 4: Request Access

### Request Access

[ailab.gc.cuny.edu/request-access/](https://ailab.gc.cuny.edu/request-access/)

- Choose **My own access** and sign in with **CUNY Login**.

- Complete your details, select **CAIL Sandbox**, and submit your application.

- After approval, open [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/) and select **Continue with CUNY Login**.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Slide 5: System Prompts

### System Prompts

System prompts are setup instructions that describe how a model should behave.

### User Prompts

Questions or tasks you enter in chat.

### Custom Models

You create a custom model by choosing a base model, such as Gemma, and adding instructions and documents for it to use.

[Basic Concepts](https://ailab.gc.cuny.edu/sandbox-docs/basic-concepts/) · [Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Slide 6: Select Models

### Select Models

![Sandbox logo, message box, and Gateway model selector; enlarged detail shows current model choices with model ID outlined and marked by an arrow.](images/current/gateway-selector-hidpi-2026-09-16.svg)

Select model ID on bottom right of message box. Choose Gateway from filters, then select Gemma 4 26B A4B IT.

---

## Slide 7: Chat Features

### Chat Features

Upload Files (+)

Attach images, PDFs, or documents.

Integrations

Enable tools that perform operations and skills that give reusable instructions.

Message actions

Find actions beneath each response to copy, edit, or regenerate it. Open More (⋯) for additional actions.

[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

---

## Slide 8: Compare Models

### Compare Models

![Sandbox logo, message box, and Gateway model selector; enlarged detail shows Compare beside search field outlined and marked by an arrow.](images/current/gateway-selector-compare-hidpi-2026-09-16.svg)

Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two Gateway models. If Compare is unavailable, send identical prompts in separate new chats.

---

## Slide 9: Who Was Late?

### Who Was Late?

Compare how two small models interpret this sentence.

```text
The nurse yelled at the doctor because she was late. Who was late?
```

Send this question to both models.

---

## Slide 10: Winograd Schema Challenge

### Winograd Schema Challenge

This challenge tests how models interpret ambiguous pronouns using context and common-sense knowledge. Changing one or two words between paired sentences changes who a pronoun refers to.

In our question, either person could be late.

- Which person does each model choose?

- What assumption supports its answer?

[Levesque, Davis, and Morgenstern (2012)](https://www.cs.nyu.edu/faculty/davise/papers/WSKR2012.pdf)

---

## Slide 11: Compare Outputs

### Compare Outputs

Consider this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

What do you think this person wants to accomplish?

---

## Slide 12: Compare Outputs

### Compare Outputs

### Gemma’s Response

![Gemma 3 27B response recommending walking, with model name and generation time.](images/showcase/car-wash-gemma-response.png)

### Qwen’s Response

![Qwen3.5 27B response recommending driving, with model name and generation time.](images/showcase/car-wash-qwen-response.png)

---

## Slide 13: Compare Models

### Compare Models

Start a new chat, select two models, and send this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

Save both responses with your question and selected model IDs before adding system prompt instructions.

---

## Slide 14: Add System Prompt

### Add System Prompt

![Sandbox logo, message box, and open Controls panel; white annotations identify Controls button and System Prompt field.](images/current/chat-controls-instructions-2026-09-16.svg)

Select **Controls** at top right of chat. Paste these instructions into **System Prompt**, then close Controls.

```text
Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer briefly without inventing context.
```

---

## Slide 15: Regenerate Responses

### Regenerate Responses

![Mistral Large 3 response recommending walking, with original question and message box; enlarged recommendation and response controls show Regenerate outlined and marked by an arrow.](images/current/regenerate-mistral-gateway-hidpi-2026-09-16.svg)

Select Regenerate beneath each original response, then choose Try Again. Keep your original question, selected models, and other settings unchanged.

---

## Slide 16: Compare Responses

### Compare Responses

- Compare responses before and after adding system prompt instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

---

## Slide 17: Open Workspace

### Open Workspace

![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](images/current/workspace-sidebar-2026-09-15-annotated.svg)

Select Workspace in left sidebar.

---

## Slide 18: Review Custom Models

### Review Custom Models

Choose **Models** and open a custom model shared with you.

Review **Base Model** and **System Prompt**, then compare its instructions with your tested prompt.

Continue in chat if Workspace is unavailable.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Slide 19: Model Configuration

### Model Configuration

![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.](images/current/model-create-hidpi-2026-09-16.svg)

Select Create in Models. Enter a recognizable name, choose a tested base model, and add your tested system prompt.

---

## Slide 20: Add Prompt Suggestions

### Add Prompt Suggestions

Add a description and prompt suggestions for tasks your model should support.

Users select your custom model to use its instructions and resources.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Slide 21: Situating System Prompts

Examples

### Situating System Prompts

---

## Slide 22: Select STEM Games

### Select STEM Games

![Model Selector filtered to STEM Adventure Games, with CUNY AI Lab logo and message box visible.](images/current/stem-selector-2026-09-14.png)

Select model ID on bottom right of message box. Search for STEM Adventure Games and select it.

---

## Slide 23: STEM Adventure Games

### STEM Adventure Games

![STEM Adventure Games presents a short scene and numbered choices directly in Sandbox chat.](images/current/stem-chat-play-hidpi-2026-09-16.png)

Type Start an adventure. Choose an experiment, then reply with a number or describe what you want to do.

---

## Slide 24: Inspect System Prompt

### Inspect System Prompt

![STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.](images/current/stem-chat-model-hidpi-2026-09-16.svg)

Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt.

---

## Slide 25: Read Game Instructions

### Read Game Instructions

```text
End each scene with three numbered choices. Accept a number or an action in ordinary language, such as looking around, examining an object, or asking for a hint. Wait for a response before continuing.
```

What should happen after you choose an action?

[Read full system prompt](examples.html#stem-chat)

---

## Slide 26: Adapt Research Prompts

### Adapt Research Prompts

You can adapt this exercise to a research task, such as comparing article abstracts or documenting a method.

- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.

Save your source material, prompt, response, and assessment together.

---

## Slide 27: Draft System Prompts

### Draft System Prompts

---

## Slide 28: Define Prompt Components

### Define Prompt Components

Choose one component to change.

- **Context** — Experiment, historical setting, and intended users.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Tone and format** — Language, length, and presentation.

---

## Slide 29: Define Context

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

## Slide 30: Write Procedures

### Write Procedures

What should happen before and after each choice?

```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer three numbered choices and wait.
4. Describe observations after players choose.
```

---

## Slide 31: Set Constraints

### Set Constraints

Specify how your model should handle missing evidence.

```text
Do not invent historical details when sources are missing.
Distinguish documented events from choices created for the game.
If a source is unavailable, explain what cannot be checked.
```

Test a request that asks for a detail absent from your sources.

---

## Slide 32: Set Tone

### Set Tone

Describe how your model should address players.

```text
Address the player as “you.”
Use concise language for scenes and choices.
Explain unfamiliar scientific terms when they first appear.
```

Which terms need explanation for your intended users?

---

## Slide 33: Specify Format

### Specify Format

Specify how scenes and choices should appear.

```text
Write a short scene followed by three numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```

---

## Slide 34: Refine Instructions

Refine

### Refine Instructions

---

## Slide 35: Extend Instructions

### Extend Instructions

- Specify what happens when a player asks for a hint.

- Explain how to revisit an earlier decision.

- Require source checks when players ask about historical claims.

- Test how your model responds when evidence is missing.

---

## Slide 36: Review Common Problems

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

## Slide 37: Save Prompts

### Save Prompts

Save your tested prompt in a private custom model. Choose a base model, review **Access**, and select **Save & Create**. Reuse this model when adding documents in Workshop 2.

---

## Slide 38: Share Custom Models

### Share Custom Models

- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and any attached collections.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Slide 39: Record Comparisons

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

## Slide 40: Prepare Source Documents

### Prepare Source Documents

- Save prompt versions and comparison notes

- Request Workspace and Knowledge collection access

- Select public or approved source documents

- Review [system-prompt examples](examples.html)

- Continue to [Curating knowledge collections](knowledge/)
