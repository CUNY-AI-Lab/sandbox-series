# Visible workshop instructions

Removed all 13 hidden-note blocks from the three current workshops. Required steps now appear in captions; repeated instructions were cut, and two unique explanations moved to existing visible slides. No screenshots or slide numbers changed.

[Full copy](../../SLIDES.md) · [Direct diff](copy.diff) · [Browser checks](browser.json)

All 102 slides have no hidden participant content. Fifteen affected slides passed desktop and mobile overflow and image checks. Series checks and all 21 copy tests pass; the checks now reject hidden content inside slides.

## Before and after

### index.html · 6

**Before**

### Select Models

![Sandbox chat with model ID at bottom right of message box](../../images/current/chat-page.png)

Select model ID on bottom right of message box.

Type a request, send it, then ask a follow-up. Open **New Chat** when you want to begin with fresh conversation history.

[Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/)

**After**

### Select Models

![Sandbox chat with model ID at bottom right of message box](../../images/current/chat-page.png)

Select model ID on bottom right of message box. Type a request, send it, then ask a follow-up. Open New Chat to start without earlier messages.

### index.html · 8

**Before**

### Compare Models

![Sandbox logo, message box, and model selector with Compare button marked by an arrow](../../images/current/model-selector-compare-2026-09-14.svg)

Start a new chat. Select Compare beside search field, then choose two models.

Select model ID on bottom right of message box.

Select **Compare** beside search field, then choose two small models.

If Compare is unavailable, send identical prompts in separate new chats.

**After**

### Compare Models

![Sandbox logo, message box, and model selector with Compare button marked by an arrow](../../images/current/model-selector-compare-2026-09-14.svg)

Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two small models. If Compare is unavailable, send identical prompts in separate new chats.

### index.html · 21

**Before**

### Model Configuration

![Current model creation form showing Name, Base Model, and System Prompt](../../images/current/model-editor.png)

Select Create in Models. Choose a name and base model, then enter your system prompt.

- **Name** — Use a name that students or colleagues will recognize.

- **Base Model** — Choose a model you have tested.

- **System Prompt** — Add instructions you tested in chat.

A custom model combines these choices. Creating it does not train a new base model.

[Model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

**After**

### Model Configuration

![Current model creation form showing Name, Base Model, and System Prompt](../../images/current/model-editor.png)

Select Create in Models. Enter a recognizable name, choose a tested base model, and add your tested system prompt.

### index.html · 22

**Before**

### Create Custom Models

Custom models combine a base model with instructions, documents, and tools.

- Enter a name and description that students or colleagues will recognize.

- Select a base model and add your tested system prompt.

- Add prompt suggestions for tasks your model should support.

Users select your custom model to use its instructions and resources.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

**After**

### Create Custom Models

Custom models combine a base model with instructions, documents, and tools. Creating a custom model does not train a new base model.

- Enter a name and description that students or colleagues will recognize.

- Select a base model and add your tested system prompt.

- Add prompt suggestions for tasks your model should support.

Users select your custom model to use its instructions and resources.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### index.html · 24

**Before**

### Select STEM Games

![Model Selector filtered to STEM Adventure Games, with CUNY AI Lab logo and message box visible.](../../images/current/stem-selector-2026-09-14.png)

Select model ID on bottom right of message box. Search for STEM Adventure Games and select it.

**After**

### Select STEM Games

![Model Selector filtered to STEM Adventure Games, with CUNY AI Lab logo and message box visible.](../../images/current/stem-selector-2026-09-14.png)

Select model ID on bottom right of message box. Search for STEM Adventure Games and select it.

### index.html · 25

**Before**

### STEM Adventure Games

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](../../images/current/stem-game-2026-09-14.png)

Send Begin Prism Laboratory to open this game. Enter help inside its command box to list available commands.

Enter commands inside Prism Laboratory. Type help to list commands, including save, load, and discuss.

**After**

### STEM Adventure Games

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](../../images/current/stem-game-2026-09-14.png)

Send Begin Prism Laboratory to open this game. Enter help inside its command box to list available commands, including save, load, and discuss.

### index.html · 26

**Before**

### Inspect System Prompt

![STEM Adventure Games model editor showing DeepSeek V4 Pro 0813 under Base Model and opening system prompt instructions.](../../images/current/stem-model-2026-09-14.png)

Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt. Base model shown here was selected on September 14, 2026.

**After**

### Inspect System Prompt

![STEM Adventure Games model editor showing DeepSeek V4 Pro 0813 under Base Model and opening system prompt instructions.](../../images/current/stem-model-2026-09-14.png)

Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt.

### knowledge/index.html · 6

**Before**

### Review Model Settings

![Current model editor showing base model, system prompt, and Knowledge](../../images/current/model-editor.png)

Review Base Model and System Prompt before attaching documents.

Review **Base Model (From)** and **System Prompt**. Start a new chat. Select model ID on bottom right of message box. Choose your custom model.

Ask a question about your source material. Save this response before attaching documents.

[Model configuration](https://ailab.gc.cuny.edu/sandbox-docs/models/)

**After**

### Review Model Settings

![Current model editor showing base model, system prompt, and Knowledge](../../images/current/model-editor.png)

Review Base Model and System Prompt. Start a new chat. Select model ID on bottom right of message box. Choose your custom model and ask a question about your documents. Save its response before attaching documents.

### knowledge/index.html · 9

**Before**

### Open STEM Collection

![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, Newton’s optical experiments, procedural variations, and software checks.](../../images/current/stem-knowledge-2026-09-14.png)

Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments. Inspect each file before using it as evidence.

**After**

### Open STEM Collection

![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, Newton’s optical experiments, procedural variations, and software checks.](../../images/current/stem-knowledge-2026-09-14.png)

Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments.

### knowledge/index.html · 12

**Before**

### Review Attached Knowledge

![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge, STEM Adventure enabled under Tools, and Extend STEM Adventures enabled under Skills.](../../images/current/stem-attachments-2026-09-14.png)

Open Workspace → Models → STEM Adventure Games. Scroll to Knowledge and review its attached collection. For your own model, select a collection and choose Save & Update.

**After**

### Review Attached Knowledge

![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge, STEM Adventure enabled under Tools, and Extend STEM Adventures enabled under Skills.](../../images/current/stem-attachments-2026-09-14.png)

Open Workspace → Models → STEM Adventure Games. Under Knowledge, review STEM Wikipedia Experiments.

### knowledge/index.html · 24

**Before**

### Create Knowledge Collections

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../../images/current/knowledge-create.png)

Enter a collection name and description, set access, and select Create Knowledge.

- Open **Workspace → Knowledge → Create**.

- Name your collection and describe its contents and purpose.

- Keep it **Private** while building, then choose **Create Knowledge**.

[Create and manage collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

**After**

### Create Knowledge Collections

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../../images/current/knowledge-create.png)

Open Workspace → Knowledge → Create. Enter a name and description, keep access Private, then select Create Knowledge.

### skills/index.html · 6

**Before**

### Enable Tools

![Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter](../../images/current/integrations.png)

Open Integrations beside +. Under Tools, confirm STEM Adventure is enabled for this chat.

A tool runs an operation, such as a search, a calculation, or a search within a knowledge collection.

Open **Integrations** beside + to choose tools for this chat. Attach reusable tools under **Tools** in your model editor.

Availability depends on account permissions, configuration, and model support.

[Enable tools in chat or on a model](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

**After**

### Enable Tools

![Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter](../../images/current/integrations.png)

Open Integrations beside +. Under Tools, confirm STEM Adventure is enabled for this chat.

### skills/index.html · 7

**Before**

### Inspect Game Rules

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](../../images/current/stem-game-2026-09-14.png)

Send Begin Prism Laboratory to STEM Adventure Games. Enter help inside its command box.

STEM Adventure applies rules for rooms, inventory, actions, and completion.

- Enter go north to reach Storeroom.

- Enter take prism to add a prism to inventory.

- Enter help to list available actions.

- Try record result before completing required steps.

[Open game](../../examples/adventure/preview.html) · [Read scenario JSON](../../examples/adventure/prism.json)

**After**

### Inspect Game Rules

![Prism Laboratory embedded in Sandbox with Unicode borders, room and move status, game transcript, and one command line.](../../images/current/stem-game-2026-09-14.png)

Send Begin Prism Laboratory to STEM Adventure Games. Enter help inside its command box, then go north and take prism. [Open game](../../examples/adventure/preview.html) · [Read scenario JSON](../../examples/adventure/prism.json)

### skills/index.html · 19

**Before**

### Create Skills

![Extend STEM Adventures in Workspace Skills, showing its name, description, and Markdown instructions for game play, procedural extensions, and submitted records.](../../images/current/stem-skill-2026-09-14.png)

Use this saved example when creating your own skill. Review its name, description, and instructions.

- Open **Workspace → Skills → Create**.

- Enter a name, identifier, and description that explain when to use it.

- Write instructions, review **Access**, and choose **Save & Create**.

[Create and attach a skill](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

**After**

### Create Skills

![Extend STEM Adventures in Workspace Skills, showing its name, description, and Markdown instructions for game play, procedural extensions, and submitted records.](../../images/current/stem-skill-2026-09-14.png)

Open Workspace → Skills → Create. Enter a name, identifier, and description that explain when to use your skill. Write instructions, review Access, and choose Save & Create.

### skills/index.html · 26

**Before**

### Install Tool Code

- Open **Workspace → Tools → Create**.

- Enter Name, ID, and Description.

- Paste [STEM Adventure code](../../examples/tools/stem_adventure.py) and review it.

- Select **Save & Create**.

- Enable your tool through **Integrations → Tools**.

Use a private copy when changing code.

**After**

### Install Tool Code

- Open **Workspace → Tools → Create**.

- Enter Name, ID, and Description.

- Paste [STEM Adventure code](../../examples/tools/stem_adventure.py) and review it.

- Select **Save & Create**.

- Enable your tool through **Integrations → Tools**.

Use a private copy when changing code. Attach reusable tools under Tools in your model editor.
