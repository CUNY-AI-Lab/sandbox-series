Workshop 1 of 3



### Composing system prompts



Compare and configure models for teaching and research



CUNY AI Lab Sandbox



Developed by Zach Muhlbauer

---

### Workshop Roadmap



- **Composing system prompts** Configure model behavior with system prompts.

- **Curating knowledge collections** Upload documents so models can reference them.

- **Configuring skills and tools** Add web search, code execution, and reusable instructions.



[Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/)

---

### Workshop Agenda



- Request individual access and sign in

- Define system prompts

- Compare responses from small models

- Revise in-chat system prompts

- Review Workspace model cards

- Choose teaching or research examples

- Clone model cards and test revisions



Check monthly usage at [Model Access](https://tools.ailab.gc.cuny.edu/model-access).

---

### Request Access



[ailab.gc.cuny.edu/request-access/](https://ailab.gc.cuny.edu/request-access/)



- Choose **My own access** and sign in with **CUNY Login**.

- Complete your details, select **CAIL Sandbox**, and submit your application.

- After approval, open [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/) and select **Continue with CUNY Login**.



[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

### System Prompts



System prompts are setup instructions that describe how a model should behave.



### User Prompts



Questions or tasks you enter in chat.



### Custom Models



You create a custom model by choosing a base model, such as Gemma, and adding instructions and documents for it to use.



[Basic Concepts](https://ailab.gc.cuny.edu/sandbox-docs/basic-concepts/) · [Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

### Select Models



![Sandbox logo, message box, and Gateway model selector; enlarged detail shows current model choices with model ID outlined and marked by an arrow.](images/current/gateway-selector-hidpi-2026-09-16.svg)



Select model ID on bottom right of message box. Choose Gateway from filters, then select Gemma 4 26B A4B IT.

---

### Chat Features



Upload Files (+)



Attach images, PDFs, or documents.



Integrations



Enable tools that perform operations and skills that give reusable instructions.



Message actions



Find actions beneath each response to copy, edit, or regenerate it. Open More (⋯) for additional actions.



[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

---

### Compare Models



![Sandbox logo, message box, and Gateway model selector; enlarged detail shows Compare beside search field outlined and marked by an arrow.](images/current/gateway-selector-compare-hidpi-2026-09-16.svg)



Start a new chat. Select model ID on bottom right of message box. Select Compare beside search field, then choose two Gateway models. If Compare is unavailable, send identical prompts in separate new chats.

---

### Who Was Late?



Compare how two small models interpret this sentence.



```text
The nurse yelled at the doctor because she was late. Who was late?
```



Send this question to both models.

---

### Winograd Schema Challenge



This challenge tests how models interpret ambiguous pronouns using context and common-sense knowledge. Changing one or two words between paired sentences changes who a pronoun refers to.



In our question, either person could be late.



- Which person does each model choose?

- What assumption supports its answer?



[Levesque, Davis, and Morgenstern (2012)](https://www.cs.nyu.edu/faculty/davise/papers/WSKR2012.pdf)

---

### Compare Outputs



Consider this question.



```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```



What do you think this person wants to accomplish?

---

### Compare Outputs



### Gemma’s Response



![Gemma 3 27B response recommending walking, with model name and generation time.](images/showcase/car-wash-gemma-response.png)



### Qwen’s Response



![Qwen3.5 27B response recommending driving, with model name and generation time.](images/showcase/car-wash-qwen-response.png)

---

### Compare Models



Start a new chat, select two models, and send this question.



```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```



Save both responses with your question and selected model IDs before adding system prompt instructions.

---

### Add System Prompt



![Sandbox logo, message box, and open Controls panel; white annotations identify Controls button and System Prompt field.](images/current/chat-controls-instructions-2026-09-16.svg)



Select **Controls** at top right of chat. Paste these instructions into **System Prompt**, then close Controls.



```text
Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer briefly without inventing context.
```

---

### Regenerate Responses



![Mistral Large 3 response recommending walking, with original question and message box; enlarged recommendation and response controls show Regenerate outlined and marked by an arrow.](images/current/regenerate-mistral-gateway-hidpi-2026-09-16.svg)



Select Regenerate beneath each original response, then choose Try Again. Keep your original question, selected models, and other settings unchanged.

---

### Compare Responses



- Compare responses before and after adding system prompt instructions.

- Does each response identify your goal and state its assumptions? Does either response invent information or ask unnecessary questions?

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?

---

### Open Workspace



![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](images/current/workspace-sidebar-2026-09-15-annotated.svg)



Select Workspace in left sidebar.

---

### Review Custom Models



Choose **Models** to find custom model cards. Each combines a base model with setup instructions and any attached resources.



Review **Base Model** and **System Prompt**, then compare its instructions with your tested prompt.



Continue in chat if Workspace is unavailable.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

### Choose Examples



**Teaching**



[STEM Adventure Games](https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games)



Explore scientific experiments through a text adventure with numbered choices.



**Research**



[Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions)



Compare passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.



Choose either model for your own work.

---

### Clone Model Cards



- In Workspace → Models, find your chosen model and open ⋯ → **Clone**.

- Rename your copy and give it a unique ID.

- Adjust **System Prompt** for your intended users or research question.

- Review **Access**, keep Private, remove copied access grants, and select **Save & Create**.



Test your copy in chat, then revise its instructions.



[Model management](https://docs.openwebui.com/features/workspace/models/)

---

### Model Configuration



![New model form in Workspace with empty Model Name, Base Model, and System Prompt fields outlined; advanced settings are outside view.](images/current/model-create-hidpi-2026-09-16.svg)



Use Model Name, Base Model, and System Prompt to review and adjust your copy. This blank form identifies those fields.

---

### Add Prompt Suggestions



Add a description and prompt suggestions for tasks your model should support.



Users select your custom model to use its instructions and resources.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

Examples

### Situating System Prompts

---

### Select STEM Games



![Model Selector filtered to STEM Adventure Games, with CUNY AI Lab logo and message box visible.](images/current/stem-selector-2026-09-14.png)



Select model ID on bottom right of message box. Search for STEM Adventure Games and select it.

---

### STEM Adventure Games



![STEM Adventure Games presents a short scene and numbered choices directly in Sandbox chat.](images/current/stem-chat-play-hidpi-2026-09-16.png)



Type Start an adventure. Choose an experiment, then reply with a number or describe what you want to do.

---

### Inspect System Prompt



![STEM Adventure Games model editor showing Gemma 3 4B IT as Base Model and opening System Prompt instructions for an adventure played directly in chat.](images/current/stem-chat-model-hidpi-2026-09-16.svg)



Open Workspace → Models → STEM Adventure Games. Review Base Model and System Prompt.

---

### Read Game Instructions



```text
Simulate an interactive game-based learning experience through Choose Your Own STEM Adventure games featuring historically significant scientific experiments.

Each stage presents 4 numbered choices based on historically accurate experimental decisions.

After each choice, briefly state what the player observes, what the result suggests, and what question remains open.
```



What should happen after you choose an action?



[Read full system prompt](examples.html#stem-chat)

---

### Adapt Research Prompts



For [Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions), use [sample revisions](examples/research/sample-revisions.md) to test your copy.



- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.



Save your source material, prompt, response, and assessment together.

---

### Draft System Prompts

---

### Define Prompt Components



Choose one component to change.



- **Context** — Experiment, historical setting, and intended users.

- **Procedure** — Steps your model should follow.

- **Constraints** — Boundaries and missing information.

- **Tone and format** — Language, length, and presentation.

---

### Define Context



Describe what your model should help users do.



- Who will use this model?

- Which experiment or research question will they explore?

- What prior knowledge can you assume?



```text
Guide a short text adventure in which players explore how a prism changes a beam of sunlight.
```

---

### Write Procedures



What should happen before and after each choice?



```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer four numbered choices and wait.
4. Describe what players observe after each choice.
```

---

### Set Constraints



Specify how your model should handle missing evidence.



```text
Do not invent historical details when sources are missing.
Distinguish documented events from invented scenes and choices.
If a source is unavailable, explain what cannot be checked.
```



Test a request that asks for a detail absent from your sources.

---

### Set Tone



Describe how your model should address players.



```text
Address the player as “you.”
Use concise language for scenes and choices.
Explain unfamiliar scientific terms when they first appear.
```



Which terms need explanation for your intended users?

---

### Specify Format



Specify how scenes and choices should appear.



```text
Write a short scene followed by four numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```

---

Refine

### Refine Instructions

---

### Extend Instructions



- Specify what happens when a player asks for a hint.

- Explain how to revisit an earlier decision.

- Require source checks when players ask about historical claims.

- Test how your model responds when evidence is missing.

---

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

### Save Prompts



Save changes to your cloned model. Review **Access** and select **Save & Update**. Reuse this model when adding documents in Workshop 2.

---

### Share Custom Models



- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and any attached collections.



[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

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

### Prepare Source Documents



- Save prompt versions and comparison notes

- Request Workspace and Knowledge collection access

- Select public or approved source documents

- Review [system-prompt examples](examples.html)

- Continue to [Curating knowledge collections](knowledge/)
