# Composing system prompts

## Slide 1: Getting Started with the CUNY AI Lab Sandbox

[![CUNY AI Lab](images/cail-wordmark-white.png)](https://ailab.gc.cuny.edu/)

### Getting Started with the CUNY AI Lab Sandbox

Led by  Zach Muhlbauer

New Media Lab · Room 7388.01
CUNY Graduate Center

Thursday, September 17, 2026   2:30–4:00 p.m.

---

## Slide 2: Workshop Roadmap

### Workshop Roadmap

- **Composing system prompts** Configure model behavior with system prompts.

- **Curating knowledge collections** Organize source documents in knowledge collections.

- **Configuring skills and tools** Extend model capabilities with skills and tools.

[Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/)

---

## Slide 3: Workshop Agenda

### Workshop Agenda

- Sign in to Sandbox

- Define system prompts

- Compare responses from small models

- Revise in-chat system prompts

- Choose teaching or research examples

- Review system prompts and base models

- Clone models and compare responses

- Draft instructions and create models

Check monthly usage at [Model Access](https://tools.ailab.gc.cuny.edu/model-access).

---

## Slide 4: Sign In

### Sign In

[chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/)

Select **Continue with CUNY Login** and sign in with your CUNY account.

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

This challenge tests how models interpret ambiguous pronouns using context and common-sense reasoning. Changing one or two words between paired sentences changes who a pronoun refers to.

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

---

## Slide 14: Add System Prompt

### Add System Prompt

![CUNY AI Lab logo, DeepSeek V4 Flash 0731, car wash question in message box, and short instructions in System Prompt; white annotations identify Controls button and populated System Prompt field.](images/current/chat-controls-populated-annotated-2026-09-17.svg)

Select **Controls** at top right of chat. Paste these instructions into **System Prompt**, then close Controls.

```text
Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer concisely.
```

---

## Slide 15: Regenerate Responses

### Regenerate Responses

![Mistral Large 3 response recommending walking, with original question and message box; white annotation marks response controls for Regenerate.](images/current/regenerate-mistral-context-2026-09-17.svg)

![Enlarged Mistral Large 3 response controls with Regenerate outlined and marked by an arrow.](images/current/regenerate-mistral-detail-2026-09-17.svg)

Select Regenerate beneath each original response, then choose Try Again. Keep your original question, selected models, and other settings unchanged.

---

## Slide 16: Compare Responses

### Compare Responses

- Compare responses before and after adding system prompt instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

---

## Slide 17: Compare Custom Models

### Compare Custom Models

### Try Examples

Choose one example and experiment with it in chat.

**Teaching**

[STEM Adventure Games](https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games)

Start an adventure. Choose an experiment and make two choices.

**Research**

[Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions)

Paste one pair from [sample revisions](examples/research/sample-revisions.html). Ask it to classify one change and quote evidence.

Save your opening request to use again.

### Review Settings

Review **Base Model** and **System Prompt** for your chosen example.

- [STEM Adventure Games settings](examples.html#stem-chat)

- [Compare Wikipedia Edits settings](examples.html#wikipedia-revisions)

Find Purpose, Procedure, Constraints, and Format in its instructions.

Which instruction explains something you noticed in its response?

---

## Slide 18: Clone Models

### Clone Models

![Workspace Models showing shared workshop examples; white annotation identifies Clone in More menu.](images/current/workshop-clone-2026-09-17.svg)

Select Workspace in left sidebar, then Models. Open ⋯ beside your chosen example and select Clone.

- Rename your copy and give it a unique ID.

- Revise one instruction in **System Prompt**; keep **Base Model** and other settings unchanged.

- Scroll to bottom and select **Save & Create**.

- Open your copy in a new chat and test your saved request.

---

## Slide 19: Compare Configurations

### Compare Configurations

![Sandbox comparison with tabs for original Compare Wikipedia Edits and its clone; white annotations identify both model names above original response. Message box remains visible.](images/current/workshop-compare-2026-09-17.svg)

Start a new chat. Select model ID on bottom right of message box, then Compare. Choose your original model and your copy.

Send your saved request to both models. Include source passages if you chose research. Select each model name to review its response.

What changed? Did your revised instruction work?

Save your request and both responses.

---

## Slide 20: Record Comparisons

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

## Slide 21: Draft System Prompts

### Draft System Prompts

Use remaining time to begin drafting instructions for your own teaching or research task.

```text
Purpose
What should your model help you accomplish?
Procedure
What steps should it follow?
Constraints
What limits should it observe?
Format
How should it present responses?
```

---

## Slide 22: Create Models

### Create Models

![Workspace Models filtered to shared workshop examples, with Create button outlined and marked by an arrow.](images/current/workshop-create-2026-09-17.svg)

Select Workspace → Models → Create to configure your own model.

- Name your configuration and give it a unique ID.

- Select **Base Model** and paste your draft into **System Prompt**.

- Scroll to bottom and select **Save & Create**.

- Start a new chat with your model and try one request.

---

## Slide 23: Workshop Resources

### Workshop Resources

- Review [workshop copy](workshop-copy.html) and [system-prompt examples](examples.html).

- Consult [Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/) and [Open WebUI Models](https://docs.openwebui.com/features/workspace/models/).

- Check [monthly usage](https://tools.ailab.gc.cuny.edu/model-access).

Keep your draft and choose source documents for your next workshop.
