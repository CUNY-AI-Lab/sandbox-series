# Exercise and Workspace revision

Revised 15 September 2026 from `67e5dfd`. Removed a repeated exercise slide, so later slides move back by one. Composing system prompts now has 43 slides; the series has 102.

## What changed

Slides 15–17 now cover copying instructions, pasting them into in-chat System Prompt, and regenerating original responses. Each action appears once. Both annotated control screenshots remain.

Workspace navigation now uses a fresh Firefox screenshot of the left sidebar, with an arrow and outline around Workspace. This replaces the incorrect upper-tab image in both affected workshops. The sidebar image precedes custom-model review in Workshop 1.

[Complete current copy](../SLIDES.md) · [Direct diff](streamline-copy.diff)

## Validation

All 21 copy tests and 31 shared-engine interaction checks pass. Updated tests guard the consecutive three-step sequence, removal of repeated instructions, correct sidebar image, and navigation before model review. Existing screenshot hashes, source preservation, title rules, prompt equality, and 90-minute plans pass. Root slides 15–21 and Knowledge slides 4–5 were checked at 1280 × 720 and 390 × 844; every image loaded and no content overflowed. [Browser measurements](streamline-browser.json) record the checks.

No-ai-slop review checked repetition, clear referents, and necessary transitions. Prompt wording and UI labels remain exact. Short instructions follow the requested slide format.

## Before and after

### Add System Prompt

Source — `index.html`

**Before**

### Add System Prompt

Paste this into in-chat **System Prompt** under **Controls** at top right.

```text
Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer briefly without inventing context.
```

**After**

### Add System Prompt

Copy these instructions for in-chat **System Prompt**.

```text
Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer briefly without inventing context.
```

### Open Chat Controls

Source — `index.html`

**Before**

### Open Chat Controls

![Sandbox logo, message box, and open Controls panel with System Prompt field marked by an arrow](../images/current/chat-controls-2026-09-14-annotated.svg)

Open Controls → System Prompt. Add sample instructions, close Controls, then choose Regenerate → Try Again beneath each original response.

- Open your chat.

- Select **Controls** at top right.

- Add sample instructions in **System Prompt**. Close Controls, then select **Regenerate** beneath each original response, then choose **Try Again**.

Leave your original question unchanged. Use Chat Controls for this exercise; defaults in Settings apply across chats.

**After**

### Open Chat Controls

![Sandbox logo, message box, and open Controls panel with System Prompt field marked by an arrow](../images/current/chat-controls-2026-09-14-annotated.svg)

Select Controls at top right. Paste copied instructions into System Prompt, then close Controls.

### Test System Prompts

Source — `index.html`

**Before**

### Test System Prompts

- Copy sample instructions from [Add System Prompt](../index.html#15).

- Open **Controls** at top right of your chat. Add instructions in **System Prompt**.

- Close Controls. Select **Regenerate** beneath each original response, then choose **Try Again**.

Leave your original question, selected models, and other settings unchanged.

**After**

Removed. Copy, paste, and regeneration each appear once on slides 15–17.

### Regenerate Responses

Source — `index.html`

**Before**

### Regenerate Responses

![Original question, Gemma response, and message box with Regenerate button marked by an arrow](../images/current/regenerate-gemma-2026-09-14-annotated.svg)

After adding system prompt instructions, select Regenerate beneath each original response, then choose Try Again.

**After**

### Regenerate Responses

![Original question, Gemma response, and message box with Regenerate button marked by an arrow](../images/current/regenerate-gemma-2026-09-14-annotated.svg)

Select Regenerate beneath each original response, then choose Try Again. Keep your original question, selected models, and other settings unchanged.

### Compare Responses

Source — `index.html`

**Before**

### Compare Responses

- Compare responses before and after adding system prompt instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

Keep base models and other settings unchanged. Record any differences you cannot control.

**After**

### Compare Responses

- Compare responses before and after adding system prompt instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

### Open Workspace

Source — `index.html`

**Before**

### Open Workspace

Open **Workspace → Models**.

Open a custom model shared with you and review its **Base Model** and **System Prompt**. Compare those instructions with your tested prompt.

Continue in chat if Workspace is unavailable.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

**After**

### Review Custom Models

Choose **Models** and open a custom model shared with you.

Review **Base Model** and **System Prompt**, then compare its instructions with your tested prompt.

Continue in chat if Workspace is unavailable.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### Workspace Tabs

Source — `index.html`

**Before**

### Workspace Tabs

![Current Workspace header with Models, Knowledge, Prompts, Skills, Tools, and Create](../images/current/workspace-header.png)

Select a Workspace tab, then choose Create.

### Custom Models

Open a model to view its base model and system prompt. Select **Create** to configure your own.

### Knowledge and Tools

Attach documents under Knowledge. Add reusable instructions under Skills and operations such as web search under Tools.

**After**

### Open Workspace

![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](../images/current/workspace-sidebar-2026-09-15-annotated.svg)

Select Workspace in left sidebar.

### Model Configuration

Source — `index.html`

**Before**

### Model Configuration

![Current model creation form showing Name, Base Model, and System Prompt](../images/current/model-editor.png)

Choose a name and base model, then enter a system prompt.

- **Name** — Use a name that students or colleagues will recognize.

- **Base Model** — Choose a model you have tested.

- **System Prompt** — Add instructions you tested in chat.

A custom model combines these choices. Creating it does not train a new base model.

[Model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

**After**

### Model Configuration

![Current model creation form showing Name, Base Model, and System Prompt](../images/current/model-editor.png)

Select Create in Models. Choose a name and base model, then enter your system prompt.

- **Name** — Use a name that students or colleagues will recognize.

- **Base Model** — Choose a model you have tested.

- **System Prompt** — Add instructions you tested in chat.

A custom model combines these choices. Creating it does not train a new base model.

[Model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### Review Custom Models

Source — `knowledge/index.html`

**Before**

### Review Custom Models

Open your custom model from Workshop 1. Choose a question about documents you want it to use.

Bring course materials, research papers, or other documents you know well enough to check.

Use [system-prompt examples](../examples.html) if you need a prompt to begin.

**After**

### Review Custom Models

Choose a question about documents you want your custom model to use.

Bring course materials, research papers, or other documents you know well enough to check.

Use [system-prompt examples](../examples.html) if you need a prompt to begin.

### Open Workspace

Source — `knowledge/index.html`

**Before**

### Open Workspace

![Current Workspace tabs and shared Create button](../images/current/workspace-header.png)

Open Workspace → Models and find your custom model before adding documents.

Sign in after your Lab access is approved. Open **Workspace → Models** and find your custom model.

To create a new custom model, choose a base model and add a prompt from [System Prompt Examples](../examples.html).

Request Workspace access from CUNY AI Lab if Workspace is unavailable.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

**After**

### Open Workspace

![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](../images/current/workspace-sidebar-2026-09-15-annotated.svg)

Select Workspace in left sidebar. Choose Models and open your custom model.
