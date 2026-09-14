# Copy Revisions

[Previous complete copy](https://github.com/CUNY-AI-Lab/sandbox-series/blob/552f10c0e8e40bd20073cdbea8ea804622bf3c3e/SLIDES.md) · [Revised complete copy](../SLIDES.md) · [Direct diff](plain-language.diff)

Applied participant instructions without definite articles. Kept exact demonstration questions and quoted sample prompts, except two skill-template placeholders that now specify when to wait for student responses. Replaced compressed labels with descriptions of actions. Workshop 1 now edits system instructions and regenerates responses to an unchanged prompt. Removed showcase captions and both paragraphs requested for deletion.

Terminology follows [Sandbox custom models](https://ailab.gc.cuny.edu/sandbox-docs/models/), [knowledge collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/), [skills and tools](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/), and [Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/).

Checks passed for all 118 slide titles, participant prose without definite articles, preserved source passages, transcript synchronization, local links, and image hashes. Browser checks covered all 118 slides at 1280×720 and 390×844, with no clipped headings, missing images, horizontal overflow, or screenshot overlap with navigation.

Replaced Compare screenshot with a new Firefox capture in dark mode. Dismissed tooltip before capture. Retained CUNY AI Lab logo, message box, and open model selector; added a white Compare label, arrow, and circle outside its control. Verified Compare changes from off to on, then restored it. Screenshot contains authentic interface pixels, with no reconstructed controls.



## index.html — Slide 3

### Before

### Workshop Agenda



- Request individual access and sign in

- Compare responses from small models

- Compare car-wash responses

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse



Before attending, request individual access and sign into the Sandbox.

### After

### Workshop Agenda



- Request individual access and sign in

- Compare responses from small models

- Compare outputs

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse



Before attending, request individual access and sign into Sandbox.

## index.html — Slide 4

### Before

### Request Access



[ailab.gc.cuny.edu/request-access/](https://ailab.gc.cuny.edu/request-access/)



- Choose **My own access** and sign in with **CUNY Login**.

- Complete your details, select **CAIL Sandbox**, and submit the application.

- After approval, open [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/) and select **Continue with CUNY Login**.



[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

### After

### Request Access



[ailab.gc.cuny.edu/request-access/](https://ailab.gc.cuny.edu/request-access/)



- Choose **My own access** and sign in with **CUNY Login**.

- Complete your details, select **CAIL Sandbox**, and submit your application.

- After approval, open [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/) and select **Continue with CUNY Login**.



[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

## index.html — Slide 5

### Before

### Select Models



![Current Sandbox new chat with the model selector inside the message box](images/current/chat-page.png)



Select the model name on the right inside the message box.





Select the model name **on the right inside the message box**.



Type a request, send it, then ask a follow-up. Open **New Chat** when you want to begin with fresh conversation history.



[Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/)

### After

### Select Models



![Sandbox chat with model ID at bottom right of message box](images/current/chat-page.png)



Select model ID on bottom right of message box.





Select model ID on bottom right of message box.



Type a request, send it, then ask a follow-up. Open **New Chat** when you want to begin with fresh conversation history.



[Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/)

## index.html — Slide 6

### Before

### Chat Controls



Upload Files (+)



Attach images, PDFs, or documents.



Integrations



Choose tools and skills for this chat.



Message actions



Copy, edit, or regenerate a response. Open the three-dot menu for additional actions.



[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

### After

### Chat Controls



Upload Files (+)



Attach images, PDFs, or documents.



Integrations



Choose tools and skills for this chat.



Message actions



Copy, edit, or regenerate a response. Open More (⋯) for additional actions.



[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

## index.html — Slide 7

### Before

### Compare Models



![Current model selector with search and the Compare toggle](images/current/model-selector.png)



Open the model selector, turn on Compare, and select two models.





Open the model selector. Turn on **Compare**, then choose two available base models.



If Compare is unavailable, use two fresh chats with the same task and settings.



Switching models midway carries the conversation history forward. Use fresh chats for a clearer initial comparison.

### After

### Compare Models



![Sandbox logo, message box, and model selector with Compare button marked by an arrow](images/current/model-selector-compare-2026-09-14.svg)



Select Compare beside search field, then choose two models.





Open model selector. Select **Compare** beside search field, then choose two models.



If Compare is unavailable, send identical prompts in separate new chats.



Start a new chat before comparing models.

## index.html — Slide 8

### Before

### Who Was Late?



Compare how two small models interpret this sentence.



```text
The nurse yelled at the doctor because she was late. Who was late?
```



Use the same prompt and chat history for both models. Note which models you selected.

### After

### Who Was Late?



Compare how two small models interpret this sentence.



```text
The nurse yelled at the doctor because she was late. Who was late?
```



Send this question to both models.

## index.html — Slide 9

### Before

### Examine Assumptions



“She” could refer to either person. Readers may prefer one interpretation, but the sentence does not establish a unique answer.



- Does each model acknowledge the ambiguity?

- What assumption supports its answer?

- Does the explanation add information absent from the sentence?



Compare the evidence in the answers. A confident explanation can still rest on an unsupported assumption.

### After

### Examine Assumptions



“She” could refer to either person. This sentence does not establish who was late.



- Does each model acknowledge ambiguity?

- What assumption supports its answer?

- Does either explanation add information absent from this sentence?

## index.html — Slide 10

### Before

### Compare Recommendations



Use the same two-model comparison for this question.



```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```



Before reading the responses, write down what you think the user wants to accomplish.

### After

### Compare Outputs



Ask both models this question.



```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```



What do you think this person wants to accomplish?

## index.html — Slide 11

### Before

### Read Gemma’s Response



![Archived car-wash prompt and Gemma response saying to walk](images/showcase/car-wash-gemma.png)



GCDI showcase, May 2026. Gemma recommends walking.





The response shown recommends walking. Read its recommendation against the purpose of the trip.

### After

### Gemma’s Response



![Gemma recommends walking to a car wash](images/showcase/car-wash-gemma.png)

## index.html — Slide 12

### Before

### Read Qwen’s Response



![Archived car-wash prompt and Qwen response saying to take the car](images/showcase/car-wash-qwen.png)



GCDI showcase, May 2026. Qwen recommends taking the car.





Compare this recommendation with Gemma’s. What does each response assume about the trip?

### After

### Qwen’s Response



![Qwen recommends driving to a car wash](images/showcase/car-wash-qwen.png)

## index.html — Slide 13

### Before

### Try Model Comparison



- In a fresh chat, send the car-wash prompt to two available models. Save both responses.

- Compare their reading of the goal, their assumptions, and the reasons they give.

- Add a follow-up stating your purpose, such as washing the car or asking about prices. Does the recommendation change appropriately?



If the purpose is to wash the car, the car must get there. The original wording leaves the purpose unstated.

### After

### Compare Models



- Send your original question to two models. Save both responses.

- Add system instructions in Chat Controls.

- Regenerate responses to your original prompt. Compare outputs before and after adding instructions.

## index.html — Slide 14

### Before

### Evaluate Responses



Compare how each model interprets the question and explains its recommendation.



- Which assumptions does each response make?

- Does either response invent information?

- How does each model respond when you clarify your purpose?



Save the responses with the prompt and model names so you can repeat the comparison.

### After

### Evaluate Responses



Compare how each model interprets your question and explains its recommendation.



- Which assumptions does each response make?

- Does either response invent information?

- How do outputs change after you edit system instructions?



Save both responses with your prompt and selected model IDs.

## index.html — Slide 15

### Before

### System Prompts



A system prompt defines how a model should behave throughout a conversation.



### User Prompts



Questions or tasks you enter in chat.



### System Prompts



Instructions for the model’s role, tone, boundaries, and response style.



Test whether the selected model follows your instructions.



[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/)



[Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

### After

### System Prompts



A system prompt defines how a model should behave throughout a conversation.



### User Prompts



Questions or tasks you enter in chat.



### System Prompts



Instructions defining model behavior, tone, boundaries, and response style.



Test whether your selected model follows these instructions.



[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/)



[Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

## index.html — Slide 16

### Before

### Open Chat Controls



![Current chat Controls panel with its System Prompt field](images/current/chat-controls.png)



Enter instructions in the System Prompt field under Chat Controls.





- Open a fresh chat with one of the models you compared.

- Select **Controls** at the top right.

- Enter the sample in **System Prompt** before sending the task.



Use the conversation’s Controls for this exercise. Personal defaults under Settings have a wider scope.

### After

### Open Chat Controls



![Current chat Controls panel with its System Prompt field](images/current/chat-controls.png)



Enter instructions in System Prompt under Chat Controls.





- Open your chat.

- Select **Controls** at top right.

- Enter sample instructions in **System Prompt**, then regenerate responses to your original prompt.



Use Chat Controls for this exercise. Defaults in Settings apply across chats.

## index.html — Slide 17

### Before

### Test System Prompts



Keep one base model fixed. Add these instructions through the in-chat System Prompt field, then repeat the car-wash prompt in a fresh chat.



```text
Help the user examine a question before settling on an answer.

Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question.

Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.
```

### After

### Test System Prompts



Add these instructions in System Prompt under Chat Controls. Regenerate responses to your original prompt.



```text
Help the user examine a question before settling on an answer.

Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question.

Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.
```

## index.html — Slide 18

### Before

### Compare Responses



- Compare the saved baseline with the response produced using the system prompt.

- Check whether it identifies the goal, states assumptions, and gives a useful answer without unnecessary questioning.

- Try the nurse question again. Does the instruction help with ambiguity in a different form?



Keep the model, optional features, and other defaults consistent. Record any differences you cannot control.

### After

### Compare Responses



- Compare responses before and after adding system instructions.

- Check whether each response identifies your goal, states assumptions, and answers without unnecessary questions.

- Repeat our opening question about who was late. Do these instructions help identify ambiguity?



Keep base models and other settings unchanged. Record any differences you cannot control.

## index.html — Slide 19

### Before

### Open Workspace



Open **Workspace → Models**.



Open the sample model and review its **Base Model** and **System Prompt**. Compare those instructions with the prompt you tested in chat.



Continue in chat if Workspace is unavailable.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### After

### Open Workspace



Open **Workspace → Models**.



Open a sample model and review its **Base Model** and **System Prompt**. Compare those instructions with your tested prompt.



Continue in chat if Workspace is unavailable.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

## index.html — Slide 20

### Before

### Workspace Tabs



![Current Workspace header with Models, Knowledge, Prompts, Skills, Tools, and Create](images/current/workspace-header.png)



Select a Workspace tab, then choose Create.





### Custom Models



Open a model to view its base model and system prompt. Select **Create** to configure your own.



### Knowledge and Tools



Knowledge adds sources. Skills and Tools extend the methods and capabilities available to the model.

### After

### Workspace Tabs



![Current Workspace header with Models, Knowledge, Prompts, Skills, Tools, and Create](images/current/workspace-header.png)



Select a Workspace tab, then choose Create.





### Custom Models



Open a model to view its base model and system prompt. Select **Create** to configure your own.



### Knowledge and Tools



Attach documents under Knowledge. Add reusable instructions under Skills and operations such as web search under Tools.

## index.html — Slide 21

### Before

### Model Configuration



![Current model creation form showing Name, Base Model, and System Prompt](images/current/model-editor.png)



Choose a name and base model, then enter a system prompt.





- **Name** — Use a name that students or colleagues will recognize.

- **Base Model** — Choose a model you have tested.

- **System Prompt** — Add the instructions you tested in chat.



A custom model combines these choices. Creating it does not train a new base model.



[The model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### After

### Model Configuration



![Current model creation form showing Name, Base Model, and System Prompt](images/current/model-editor.png)



Choose a name and base model, then enter a system prompt.





- **Name** — Use a name that students or colleagues will recognize.

- **Base Model** — Choose a model you have tested.

- **System Prompt** — Add instructions you tested in chat.



A custom model combines these choices. Creating it does not train a new base model.



[Model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

## index.html — Slide 22

### Before

### Create Custom Models



Custom models combine a base model with instructions, documents, and tools.



- Enter a name and description that students or colleagues will recognize.

- Select a base model and add your tested system prompt.

- Add prompt suggestions for tasks the model should support.



Students select the custom model to use the instructions and resources you configured.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### After

### Create Custom Models



Custom models combine a base model with instructions, documents, and tools.



- Enter a name and description that students or colleagues will recognize.

- Select a base model and add your tested system prompt.

- Add prompt suggestions for tasks your model should support.



Students select your custom model to use its instructions and resources.



[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

## index.html — Slide 25

### Before

Composition & Writing

 

### Vague Prompts

 

**Weak**

```text
Help students write better.
```

 

### Identify Problems

 

- No role assignment to contextualize the model for specific workflows or domain-knowledge
 
- No boundaries or pedagogical guidance to constrain the model from doing work for students
 
- No success criteria for the model to optimize toward

### After

Composition & Writing

 

### Vague Prompts

 

**Weak**

```text
Help students write better.
```

 

### Identify Problems

 

- No specified role or disciplinary context
 
- No limits on writing for students
 
- No criteria for assessing responses

## index.html — Slide 27

### Before

Composition & Writing

 

### Guide Revision

 

**Strong**

```text
You are a writing scaffold for an English 101 composition course at a public urban university. Students are drafting a position paper on rhetoric in popular media and must revise their first draft in preparation for their final submission.

The core problem: students treat revision as proofreading, fixing grammar and word choice, rather than rethinking argument, structure, and evidence. They lack a process for examining whether their ideas are clear, well-organized, and sufficiently supported. This tool scaffolds the move from surface-level fixes to substantive revision.

Procedure:
1. Request the assignment prompt and student draft before responding.
2. Identify the highest-priority concerns (thesis clarity, structure, evidence) before surface-level issues.
3. For each concern, ask the student a question rather than providing a fix.

Constraints:
- Never generate text that could substitute for the student’s own writing. Focus on higher-order concerns like argument, structure, and evidence.
- If asked to “just fix it,” redirect toward a specific revision step.
- Do not grade or evaluate.
- Tone: Warm and direct. Use “I notice...” and “What if you tried...”
```



Scroll within the prompt to read more.

### After

Composition & Writing

 

### Guide Revision

 

**Strong**

```text
You are a writing scaffold for an English 101 composition course at a public urban university. Students are drafting a position paper on rhetoric in popular media and must revise their first draft in preparation for their final submission.

The core problem: students treat revision as proofreading, fixing grammar and word choice, rather than rethinking argument, structure, and evidence. They lack a process for examining whether their ideas are clear, well-organized, and sufficiently supported. This tool scaffolds the move from surface-level fixes to substantive revision.

Procedure:
1. Request the assignment prompt and student draft before responding.
2. Identify the highest-priority concerns (thesis clarity, structure, evidence) before surface-level issues.
3. For each concern, ask the student a question rather than providing a fix.

Constraints:
- Never generate text that could substitute for the student’s own writing. Focus on higher-order concerns like argument, structure, and evidence.
- If asked to “just fix it,” redirect toward a specific revision step.
- Do not grade or evaluate.
- Tone: Warm and direct. Use “I notice...” and “What if you tried...”
```



Scroll within this prompt to read more.

## index.html — Slide 31

### Before

History

 

### Analyze Primary Sources

 

**Strong**

```text
You are a source-analysis tool for an undergraduate U.S. history survey covering the period from Reconstruction through the Civil Rights Movement. Students must analyze primary source documents from the period and use them as the basis for a historical report.

The core problem: students extract facts from sources rather than analyzing them as constructed arguments shaped by author, audience, and context.

Procedure (based on Wineburg’s historical thinking heuristics):
1. Ask the student to identify the source (title, date, creator, document type) before proceeding.
2. Guide them through the four moves below, one at a time. Never jump ahead.
3. After each move, ask why that detail matters and prompt them to ground their response in specific passages.
4. After all four moves, ask the student to synthesize: what does the full picture reveal about this historical moment?

Four Moves:
- Sourcing — Before reading: who created this, when, and why? What can we infer about reliability and perspective?
- Contextualization — What was happening at the time and place this was produced? How does that shape its meaning?
- Close Reading — What does the text actually say — and what does it leave out, downplay, or assume?
- Corroboration — How does this source compare to others from the period? Where do accounts agree or conflict?

Constraints:
- Never offer guidance before the student has attempted an answer.
- Encourage grounding interpretations in specific passages as analysis develops.
- If unsure about a historical fact, say so. Never invent dates, names, or events.
- Never provide a complete analysis. Ask the next question a historian would ask.
- Tone: Patient and curious.
```



Scroll within the prompt to read more.

### After

History

 

### Analyze Primary Sources

 

**Strong**

```text
You are a source-analysis tool for an undergraduate U.S. history survey covering the period from Reconstruction through the Civil Rights Movement. Students must analyze primary source documents from the period and use them as the basis for a historical report.

The core problem: students extract facts from sources rather than analyzing them as constructed arguments shaped by author, audience, and context.

Procedure (based on Wineburg’s historical thinking heuristics):
1. Ask the student to identify the source (title, date, creator, document type) before proceeding.
2. Guide them through the four moves below, one at a time. Never jump ahead.
3. After each move, ask why that detail matters and prompt them to ground their response in specific passages.
4. After all four moves, ask the student to synthesize: what does the full picture reveal about this historical moment?

Four Moves:
- Sourcing — Before reading: who created this, when, and why? What can we infer about reliability and perspective?
- Contextualization — What was happening at the time and place this was produced? How does that shape its meaning?
- Close Reading — What does the text actually say — and what does it leave out, downplay, or assume?
- Corroboration — How does this source compare to others from the period? Where do accounts agree or conflict?

Constraints:
- Never offer guidance before the student has attempted an answer.
- Encourage grounding interpretations in specific passages as analysis develops.
- If unsure about a historical fact, say so. Never invent dates, names, or events.
- Never provide a complete analysis. Ask the next question a historian would ask.
- Tone: Patient and curious.
```



Scroll within this prompt to read more.

## index.html — Slide 34

### Before

Literature & Cultural Studies

 

### Add Specifics

 

**Getting There**

```text
You are a close-reading scaffold. Help students analyze literary texts by focusing on themes, symbolism, and narrative techniques. Don't just summarize the plot. Ask students to point to specific passages.
```

 

### Compare Improvements

 

- Names specific analytical categories
 
- Addresses the plot-summary problem
 
- Requires textual evidence



### Add Detail

 

- No procedural steps for scaffolding analysis
 
- No critical or theoretical framework
 
- No attention to cultural context

### After

Literature & Cultural Studies

 

### Add Specifics

 

**Getting There**

```text
You are a close-reading scaffold. Help students analyze literary texts by focusing on themes, symbolism, and narrative techniques. Don't just summarize the plot. Ask students to point to specific passages.
```

 

### Compare Improvements

 

- Names specific analytical categories
 
- Discourages plot summary
 
- Requires textual evidence



### Add Detail

 

- No procedural steps for scaffolding analysis
 
- No critical or theoretical framework
 
- No attention to cultural context

## index.html — Slide 35

### Before

Literature & Cultural Studies

 

### Analyze Literary Texts

 

**Strong**

```text
You are a close-reading tool designed for an introductory English course that focuses on cultural studies and literary analysis. Students recently practiced close reading and must now select a brief literary artifact to analyze using techniques associated with New Criticism.

The core problem: students default to summarizing content or importing biographical and historical context rather than attending closely to how the text works: how language, form, imagery, and internal tension generate meaning within the artifact itself.

Procedure:
1. Ask what the student notices about the language in their chosen passage.
2. Prompt them to examine specific textual features (word choice, imagery, syntax, point of view) and how they create meaning.
3. Ask how the passage connects to the work’s larger themes.
4. Guide them toward an interpretive claim grounded in textual evidence.

Framework:
- Treat the text as a self-contained object. Bracket authorial intent and historical context; attend to what the language itself does.
- Look for tension, irony, paradox, and ambiguity as sites of meaning, not problems to resolve. Ask how formal elements (diction, imagery, syntax, tone) work together as a meaningful cultural artifact.
- Once a close reading is underway, invite students to reflect on the method itself: what does focusing on the text alone illuminate, and what does it leave out?

Constraints:
- Facilitate multiple interpretations grounded in textual evidence. Do not prescribe a correct reading.
- If a student reaches for biographical or historical context, redirect them back to the text: “What in the language itself supports that reading?”

Tone: Encouraging and accessible. Affirm observations, then push deeper.
```



Scroll within the prompt to read more.

### After

Literature & Cultural Studies

 

### Analyze Literary Texts

 

**Strong**

```text
You are a close-reading tool designed for an introductory English course that focuses on cultural studies and literary analysis. Students recently practiced close reading and must now select a brief literary artifact to analyze using techniques associated with New Criticism.

The core problem: students default to summarizing content or importing biographical and historical context rather than attending closely to how the text works: how language, form, imagery, and internal tension generate meaning within the artifact itself.

Procedure:
1. Ask what the student notices about the language in their chosen passage.
2. Prompt them to examine specific textual features (word choice, imagery, syntax, point of view) and how they create meaning.
3. Ask how the passage connects to the work’s larger themes.
4. Guide them toward an interpretive claim grounded in textual evidence.

Framework:
- Treat the text as a self-contained object. Bracket authorial intent and historical context; attend to what the language itself does.
- Look for tension, irony, paradox, and ambiguity as sites of meaning, not problems to resolve. Ask how formal elements (diction, imagery, syntax, tone) work together as a meaningful cultural artifact.
- Once a close reading is underway, invite students to reflect on the method itself: what does focusing on the text alone illuminate, and what does it leave out?

Constraints:
- Facilitate multiple interpretations grounded in textual evidence. Do not prescribe a correct reading.
- If a student reaches for biographical or historical context, redirect them back to the text: “What in the language itself supports that reading?”

Tone: Encouraging and accessible. Affirm observations, then push deeper.
```



Scroll within this prompt to read more.

## index.html — Slide 36

### Before

### Adapt Research Prompts



Choose a research task, such as comparing article abstracts, checking how you coded a passage, or documenting a method.



- State the research question and material the model may use.

- Specify the procedure and what counts as evidence.

- Ask the model to explain uncertainty and consider other interpretations.



Save your source material, prompt, response, and assessment together.

### After

### Adapt Research Prompts



Choose a research task, such as comparing article abstracts, checking how you coded a passage, or documenting a method.



- State your research question and identify permitted source material.

- Specify steps and what counts as evidence.

- Ask your model to explain uncertainty and consider other interpretations.



Save your source material, prompt, response, and assessment together.

## index.html — Slide 38

### Before

Structure  

### Define Prompt Components

 

Draft a system prompt using these components.

 

- **Context & Problem** — What course, what students, what learning challenge?
 
- **Procedure** — What steps should the tool follow?
 
- **Constraints** — What should it refuse to do, and how should it redirect?
 
- **Tone** — What register and affect should it use with your students?
 
- **Output Format** — How should it structure its responses?

### After

Structure  

### Define Prompt Components

 

Draft a system prompt using these components.

 

- **Context & Problem** — What course, what students, what learning challenge?
 
- **Procedure** — What steps should your model follow?
 
- **Constraints** — What should it refuse to do, and how should it redirect?
 
- **Tone** — What register and affect should it use with your students?
 
- **Output Format** — How should it structure its responses?

## index.html — Slide 39

### Before

Component 1  

### Define Context

 

Name the tool, the course, the students, and the specific learning challenge.

 

- What kind of tool is this?
 
- Who are your students?
 
- What learning challenge does it address?

 

```text
You are a [tool type] for [course name].
Students are [relevant context].

The core problem: [specific learning challenge].
```

 

**Your turn** Copy this template and fill in the placeholders. Name what the tool does, who the students are, and what learning challenge it addresses.

### After

Component 1  

### Define Context

 

Describe your course, students, and learning challenge.

 

- What kind of tool is this?
 
- Who are your students?
 
- What learning challenge does it address?

 

```text
You are a [tool type] for [course name].
Students are [relevant context].

The core problem: [specific learning challenge].
```

 

**Your turn** Copy this template. Describe what your model should help students do.

## index.html — Slide 40

### Before

Component 2  

### Write Procedures

 

Tell the tool what to do, step by step. Numbered steps give the model a clear sequence rather than a loose set of suggestions.

 

- What should the tool request before responding?
 
- What should it prioritize?
 
- How should it respond to each student input?

 

```text
Procedure:
1. Ask the student for [specific input] before responding.
2. Identify [priority concern] before addressing [secondary concerns].
3. For each issue, [specific action, e.g. ask a question rather than fix it].
```

 

**Your turn** Copy this template and fill in the placeholders. Think about the sequence that matters for your discipline.

### After

Component 2  

### Write Procedures

 

Write numbered steps for your model to follow.

 

- What should your model request before responding?
 
- What should it prioritize?
 
- How should it respond to each student input?

 

```text
Procedure:
1. Ask the student for [specific input] before responding.
2. Identify [priority concern] before addressing [secondary concerns].
3. For each issue, [specific action, e.g. ask a question rather than fix it].
```

 

**Your turn** Copy this template and describe steps you use in your discipline.

## index.html — Slide 41

### Before

Component 3  

### Set Constraints

 

Define what the tool should not do and how it redirects when students push against those limits.

 

- What will students ask it to do *for* them?
 
- How should it redirect instead?
 
- What uncertainty should it name explicitly?

 

```text
Constraints:
- Never [specific output to avoid].
- If asked to [common student request], redirect by [specific alternative].
- If uncertain about [domain content], say so explicitly.
```

 

**Your turn** Copy this template and fill in the placeholders. Keep the tool from doing work students should do themselves.

### After

Component 3  

### Set Constraints

 

Define tasks your model should decline and alternatives it should suggest.

 

- What will students ask it to do *for* them?
 
- How should it redirect instead?
 
- What uncertainty should it name explicitly?

 

```text
Constraints:
- Never [specific output to avoid].
- If asked to [common student request], redirect by [specific alternative].
- If uncertain about [domain content], say so explicitly.
```

 

**Your turn** Copy this template and specify work students should do themselves.

## index.html — Slide 42

### Before

Component 4  

### Set Tone

 

Describe how the model should address your students.

 

- What register fits your students?
 
- Should it feel warm, direct, encouraging?
 
- Are there phrases that model the right affect?

 

```text
Tone: [Adjective and adjective]. Use phrases like "[example phrase]" and "[example phrase]."
```

 

**Your turn** Copy this template and fill in the placeholders. What language makes your students feel supported rather than evaluated?

### After

Component 4  

### Set Tone

 

Describe how your model should address students.

 

- What register fits your students?
 
- Should it feel warm, direct, encouraging?
 
- Which phrases demonstrate your intended tone?

 

```text
Tone: [Adjective and adjective]. Use phrases like "[example phrase]" and "[example phrase]."
```

 

**Your turn** Copy this template. What language helps your students feel supported?

## index.html — Slide 43

### Before

Component 5  

### Specify Format

 

Specify a response format if your task requires consistent structure.

 

- Should each response end with a question?
 
- Should it follow a fixed structure?
 
- What length is appropriate?

 

```text
Format each response as:
Observation: [what you notice]
Focus: [one thing to work on]
Next step: [a specific, actionable suggestion]
Question: [something for the student to consider]
```

 

**Your turn** Copy this template and fill in the placeholders. Not every prompt needs an output format section.

### After

Component 5  

### Specify Format

 

Specify a response format if your task requires consistent structure.

 

- Should each response end with a question?
 
- Should it follow a fixed structure?
 
- What length is appropriate?

 

```text
Format each response as:
Observation: [what you notice]
Focus: [one thing to work on]
Next step: [a specific, actionable suggestion]
Question: [something for the student to consider]
```

 

**Your turn** Copy this template if your task requires a consistent response format.

## index.html — Slide 45

### Before

### Extend Instructions

 

### Set Conditions

 

“If the student submits a draft, focus on structure before style. If they ask a yes/no question, reframe it as an open one. If they ask you to just give them the answer, ask what they’ve tried first.”

 

### Request Concise Responses

 

“Respond to one thing at a time. Do not front-load your full analysis. Ask one question, wait for the student’s response, then proceed.”

 

### Acknowledge Uncertainty

 

“If you are not certain about a factual claim, explicitly state your uncertainty. Never fabricate citations or attribute quotes.”

 

### Support Multiple Languages

 

“If a student writes in a language other than English, respond in that language. Offer to discuss concepts in both languages.” Test language support with the base model and languages your students will use.

### After

### Extend Instructions

 

### Set Conditions

 

“If the student submits a draft, focus on structure before style. If they ask a yes/no question, reframe it as an open one. If they ask you to just give them the answer, ask what they’ve tried first.”

 

### Request Concise Responses

 

“Respond to one thing at a time. Do not front-load your full analysis. Ask one question, wait for the student’s response, then proceed.”

 

### Acknowledge Uncertainty

 

“If you are not certain about a factual claim, explicitly state your uncertainty. Never fabricate citations or attribute quotes.”

 

### Support Multiple Languages

 

“If a student writes in a language other than English, respond in that language. Offer to discuss concepts in both languages.”  Test language support with your base model and languages students will use.

## index.html — Slide 46

### Before

Watch Out  

### Review Common Problems

 

### Prioritize Instructions

 

Keep instructions clear and check for conflicts. If the prompt grows, prioritize its essential procedures and test whether the model follows them.

 

### Resolve Contradictions

 

“Always give detailed feedback” + “Keep responses under 50 words” = confused AI. Read your prompt for conflicts.

 

### Consider Student Questions

 

Your prompt shapes the student’s experience. Test it by asking the kinds of questions your students actually ask.

 

### Retest Revised Prompts

 

Save the prompt version with the responses it produced. Revise when a test reveals a problem, then repeat that test.

### After

Watch Out  

### Review Common Problems

 

### Prioritize Instructions

 

Check instructions for conflicts. Prioritize essential steps and test whether your model follows them.

 

### Resolve Contradictions

 

“Always give detailed feedback” + “Keep responses under 50 words” = confused AI. Read your prompt for conflicts.

 

### Consider Student Questions

 

Test your prompt with questions students ask in your course.

 

### Retest Revised Prompts

 

Save each prompt version with its responses. Revise when a test reveals a problem, then repeat that test.

## index.html — Slide 47

### Before

### Save Prompts



- Save your prompt text with the model name and responses it produced.

- Test a normal request, an incomplete request, and a request that crosses a boundary.

- Revise one instruction and repeat the test in a fresh chat.



Save your tested prompt in a private custom model. Choose the base model, review **Access**, and select **Save & Create**. Reuse this model when adding documents in Workshop 2.

### After

### Save Prompts



- Save your prompt text, model ID, and responses.

- Test a normal request, an incomplete request, and a request that crosses a boundary.

- Revise one instruction and repeat your test in a new chat.



Save your tested prompt in a private custom model. Choose a base model, review **Access**, and select **Save & Create**. Reuse this model when adding documents in Workshop 2.

## index.html — Slide 48

### Before

### Share Custom Models



- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use the model and **Write** access to people who will edit it.

- Check that the people you share with can use the base model and any attached collections, skills, or tools.



[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

### After

### Share Custom Models



- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use your model and **Write** access to people who will edit it.

- Confirm everyone you share with can access your base model and attached collections, skills, and tools.



[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

## index.html — Slide 49

### Before

### Record Comparisons



Record your prompt and model settings alongside the responses you compared.



| Item | Record |
| --- | --- |
| Configuration | Card name, base model, system prompt version, date. |
| Test | User request, enabled features, saved response. |
| Judgment | Criterion, passage from the response, reason for revising or retaining the prompt. |



Use materials you are permitted to upload and share. Sandbox chats may be stored and accessible to administrators or people you share them with.



[Privacy and chat history](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

### After

### Record Comparisons



Save your prompt, model settings, and responses.



| Item | Record |
| --- | --- |
| Configuration | Custom model name, base model, system prompt, settings, and date. |
| Test | User request, enabled features, saved response. |
| Judgment | What you checked, evidence from each response, and any change you plan to test. |



Use materials you are permitted to upload and share. Sandbox chats may be stored and accessible to administrators or people you share them with.



[Privacy and chat history](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

## knowledge/index.html — Slide 2

### Before

### Workshop Agenda



- Confirm Workspace and Knowledge access

- Select source documents

- Create knowledge collections

- Attach collections to model cards

- Check source citations

- Choose procedures for skills



Before attending, confirm individual access, Sandbox sign-in, Workspace access, and Knowledge collection access.

### After

### Workshop Agenda



- Confirm Workspace and Knowledge access

- Select source documents

- Create knowledge collections

- Attach collections to custom models

- Check source citations

- Choose procedures for skills



Before attending, confirm individual access, Sandbox sign-in, Workspace access, and Knowledge collection access.

## knowledge/index.html — Slide 3

### Before

### Review Custom Models



Open the custom model you used in Workshop 1. Attach documents and test whether the model can find and cite relevant passages.



Bring course materials, research papers, or other documents you know well enough to check.



Use [system-prompt examples](../examples.html) if you need a prompt to begin.

### After

### Review Custom Models



Open your custom model from Workshop 1. Attach documents and test whether it can find and cite relevant passages.



Bring course materials, research papers, or other documents you know well enough to check.



Use [system-prompt examples](../examples.html) if you need a prompt to begin.

## knowledge/index.html — Slide 4

### Before

### Open Workspace



![Current Workspace tabs and shared Create button](../images/current/workspace-header.png)



Open Workspace and select Knowledge to create a collection.





Sign in after your Lab access is approved. Open **Workspace → Models** and find your card.



To create a new custom model, choose a base model and add a prompt from [System Prompt Examples](../examples.html).



Request Workspace access from the CUNY AI Lab if the tab is unavailable.



[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

### After

### Open Workspace



![Current Workspace tabs and shared Create button](../images/current/workspace-header.png)



Open Workspace and select Knowledge to create a collection.





Sign in after your Lab access is approved. Open **Workspace → Models** and find your custom model.



To create a new custom model, choose a base model and add a prompt from [System Prompt Examples](../examples.html).



Request Workspace access from CUNY AI Lab if Workspace is unavailable.



[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

## knowledge/index.html — Slide 5

### Before

### Review Model Settings



![Current model editor showing base model, system prompt, and Knowledge](../images/current/model-editor.png)



Review Base Model and System Prompt before attaching documents.





Review **Base Model (From)** and **System Prompt**. Start a fresh chat using the card selected inside the message box.



Ask a question that depends on your source material. Save the response before attaching the collection.



[Model configuration](https://ailab.gc.cuny.edu/sandbox-docs/models/)

### After

### Review Model Settings



![Current model editor showing base model, system prompt, and Knowledge](../images/current/model-editor.png)



Review Base Model and System Prompt before attaching documents.





Review **Base Model (From)** and **System Prompt**. Start a new chat. Select your custom model inside message box.



Ask a question about your source material. Save this response before attaching documents.



[Model configuration](https://ailab.gc.cuny.edu/sandbox-docs/models/)

## knowledge/index.html — Slide 7

### Before

### Create Knowledge Collections



![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../images/current/knowledge-create.png)



Enter a collection name and description, set access, and select Create Knowledge.





- Open **Workspace → Knowledge → Create**.

- Name the collection and describe its contents and purpose.

- Keep it **Private** while building, then choose **Create Knowledge**.



[Create and manage collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

### After

### Create Knowledge Collections



![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../images/current/knowledge-create.png)



Enter a collection name and description, set access, and select Create Knowledge.





- Open **Workspace → Knowledge → Create**.

- Name your collection and describe its contents and purpose.

- Keep it **Private** while building, then choose **Create Knowledge**.



[Create and manage collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

## knowledge/index.html — Slide 8

### Before

### Check Citations



Ask a question with a verifiable answer in one of your documents.



### Course Example



What does the assignment require as evidence for the midterm essay?



### Research example



How does this methods section define the study population?



Check the answer against the original passage. A plausible summary alone does not show that retrieval worked.

### After

### Check Citations



Ask a question with a verifiable answer in one of your documents.



### Course Example



What evidence does this assignment require for our midterm essay?



### Research example



How does this methods section define who was studied?



Check each answer against its source passage.

## knowledge/index.html — Slide 10

### Before

### Retrieve Source Passages



- Uploaded documents are divided into passages and indexed for search.

- Retrieval finds passages relevant to a question.

- The model uses those passages to generate a response.



Check that retrieved passages address your question and support the response.



[Open WebUI retrieval](https://docs.openwebui.com/features/workspace/knowledge/)

### After

### Retrieve Source Passages



- Uploaded documents are divided into passages and indexed for search.

- Retrieval finds passages relevant to a question.

- Your model uses retrieved passages to generate a response.



Check whether retrieved passages address your question and support claims in each response.



[Open WebUI retrieval](https://docs.openwebui.com/features/workspace/knowledge/)

## knowledge/index.html — Slide 12

### Before

Composition & Writing

 

### Incomplete Collections

 

**Weak**

```text
Collection contents:
• syllabus.pdf (14 pages, full course syllabus)
```

 

### Identify Problems

 

- The syllabus may not contain the evidence needed for a revision question. Check which passages are retrieved.
 
- No assignment context for the revision task
 
- No readings or reference materials for the model to draw on

### After

Composition & Writing

 

### Incomplete Collections

 

**Weak**

```text
Collection contents:
• syllabus.pdf (14 pages, full course syllabus)
```

 

### Identify Problems

 

- A syllabus may not explain how to revise an essay. Check which passages are retrieved.
 
- No assignment instructions for revision
 
- No readings or reference materials to consult

## knowledge/index.html — Slide 13

### Before

Composition & Writing

 

### Add Specifics

 

**Getting There**

```text
Collection contents:
• syllabus.pdf
• essay-1-prompt.pdf
• mla-style-guide.pdf
```

 

### Compare Improvements

 

- Separate documents let the model find what it needs
 
- Assignment prompt gives the model context for the revision task
 
- Style guide helps with formatting questions

 

### Add Detail

 

- No course readings for the model to reference during analysis
 
- No common feedback patterns to guide revision
 
- No instructor notes on what substantive revision looks like in this course

### After

Composition & Writing

 

### Add Specifics

 

**Getting There**

```text
Collection contents:
• syllabus.pdf
• essay-1-prompt.pdf
• mla-style-guide.pdf
```

 

### Compare Improvements

 

- Separate documents distinguish individual sources
 
- Assignment instructions describe what revision requires
 
- Style guide helps with formatting questions

 

### Add Detail

 

- No course readings to reference during analysis
 
- No common feedback patterns to guide revision
 
- No instructor notes on what substantive revision looks like in this course

## knowledge/index.html — Slide 16

### Before

History

 

### Incomplete Collections

 

**Weak**

```text
Collection contents:
• textbook-chapter-12.pdf (42 pages)
```

 

### Identify Problems

 

- A general textbook chapter may not answer a question about a particular primary source.
 
- No primary sources for the model to help students analyze
 
- No framework like SOAPS for the model to scaffold source analysis

### After

History

 

### Incomplete Collections

 

**Weak**

```text
Collection contents:
• textbook-chapter-12.pdf (42 pages)
```

 

### Identify Problems

 

- A general textbook chapter may not answer a question about a particular primary source.
 
- No primary sources for students to analyze
 
- No framework like SOAPS to guide source analysis

## knowledge/index.html — Slide 17

### Before

History

 

### Add Specifics

 

**Getting There**

```text
Collection contents:
• syllabus.pdf
• source-analysis-assignment.pdf
• primary-source-1.pdf (Freedmen's Bureau report, 1866)
• primary-source-2.pdf (Congressional testimony, 1871)
```

 

### Compare Improvements

 

- Includes actual primary sources students are working with
 
- Assignment prompt gives the model task-specific context
 
- Documents are separate and focused

 

### Add Detail

 

- No contextual background for the model to draw on when students ask about the period
 
- No SOAPS framework or equivalent to guide source analysis
 
- No source metadata (author, date, document type) to support sourcing questions

### After

History

 

### Add Specifics

 

**Getting There**

```text
Collection contents:
• syllabus.pdf
• source-analysis-assignment.pdf
• primary-source-1.pdf (Freedmen's Bureau report, 1866)
• primary-source-2.pdf (Congressional testimony, 1871)
```

 

### Compare Improvements

 

- Includes actual primary sources students are working with
 
- Assignment instructions explain what students should do
 
- Documents are separate and focused

 

### Add Detail

 

- No historical context for questions about this period
 
- No SOAPS framework or equivalent to guide source analysis
 
- No source metadata (author, date, document type) to support sourcing questions

## knowledge/index.html — Slide 20

### Before

Literature & Cultural Studies

 

### Incomplete Collections

 

**Weak**

```text
Collection contents:
• course-reader.pdf (180 pages, all readings for the semester)
```

 

### Identify Problems

 

- An omnibus reader can make it harder to identify the relevant text. Check whether retrieval selects the intended source.
 
- No assignment context or close-reading framework
 
- No separation between literary texts and critical essays

### After

Literature & Cultural Studies

 

### Incomplete Collections

 

**Weak**

```text
Collection contents:
• course-reader.pdf (180 pages, all readings for the semester)
```

 

### Identify Problems

 

- An omnibus reader can make individual texts harder to identify. Check whether retrieval selects relevant passages.
 
- No assignment context or close-reading framework
 
- No separation between literary texts and critical essays

## knowledge/index.html — Slide 21

### Before

Literature & Cultural Studies

 

### Add Specifics

 

**Getting There**

```text
Collection contents:
• syllabus.pdf
• close-reading-assignment.pdf
• sonny-blues-baldwin.pdf
• new-criticism-overview.pdf
```

 

### Compare Improvements

 

- Individual literary text rather than an omnibus reader
 
- Assignment prompt provides task-specific context
 
- Critical framework document gives the model methodological grounding

 

### Add Detail

 

- No annotated examples showing how to move from observation to interpretation
 
- No key terms for the current unit (e.g., tension, irony, ambiguity)
 
- No instructor notes on what close reading looks like in this course

### After

Literature & Cultural Studies

 

### Add Specifics

 

**Getting There**

```text
Collection contents:
• syllabus.pdf
• close-reading-assignment.pdf
• sonny-blues-baldwin.pdf
• new-criticism-overview.pdf
```

 

### Compare Improvements

 

- Individual literary text rather than an omnibus reader
 
- Assignment prompt provides task-specific context
 
- A document explains how to use a critical framework

 

### Add Detail

 

- No annotated examples showing how to move from observation to interpretation
 
- No key terms for this unit (e.g., tension, irony, ambiguity)
 
- No instructor notes on what close reading looks like in this course

## knowledge/index.html — Slide 23

### Before

### Compare Research Methods



Build a collection from research papers or methods you want to compare.



- Identify a question that requires consulting those sources.

- Ask the model to compare specific claims or methods.

- Check its citations against the uploaded documents.



[Knowledge collections for research](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

### After

### Compare Research Methods



Build a collection from research papers or methods you want to compare.



- Identify a question that requires consulting those sources.

- Ask your model to compare specific claims or methods.

- Check its citations against your uploaded documents.



[Knowledge collections for research](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

## knowledge/index.html — Slide 24

### Before

### Organize Documents



Begin with a small collection so you can test how the model uses your materials.



- Name files so students or colleagues can identify them.

- Use headings to distinguish sections.

- Check whether the model retrieves the passages you need before adding more documents.

### After

### Organize Documents



Begin with a few documents and test how your model uses them.



- Name files so students or colleagues can identify them.

- Use headings to distinguish sections.

- Check whether your model retrieves relevant passages before adding more documents.

## knowledge/index.html — Slide 25

### Before

### Check Retrieval Problems



| Observation | Next check |
| --- | --- |
| No relevant source appears | Check processing, attachment, access, and the retrieval query. |
| The source is present but misread | Compare the answer with the full passage and revise instructions. |
| The answer invents a citation | Open the source and verify the quotation and location. |



Save the failed response before making one change.

### After

### Check Retrieval Problems



| Observation | Next check |
| --- | --- |
| No relevant source appears | Check whether files finished processing, are attached, and are accessible. Review your search query. |
| A source is present but misread | Read cited passages in full and revise instructions. |
| A response invents a citation | Open cited documents and verify quotations and page numbers. |



Save unsuccessful responses before revising anything.

## knowledge/index.html — Slide 26

### Before

### Build Knowledge Collections

 

Choose documents that explain your course or research project, define the task, and provide source material.

### After

### Build Knowledge Collections

 

Choose documents that explain your course or research project and describe what you want to examine.

## knowledge/index.html — Slide 28

### Before

Type 1  

### Describe Course Context

 

These documents describe course goals, structure, and methods students are expected to use.

 

- What are the course’s learning objectives?
 
- What analytical framework or methodology is central to the course?
 
- What course-level context would help the model support those goals?

 

```text
Recommended uploads:

1. syllabus.pdf
   - Course schedule, objectives, and policies

2. [framework-name].txt
   - The analytical method students use
   - Write it out in plain language with definitions
```

 

**Consider** Is there a framework or methodology central to your course? If so, a short document (1-2 pages) explaining it in the terms you use with students could be a strong addition.

### After

Type 1  

### Describe Course Context

 

These documents describe course goals, structure, and methods students are expected to use.

 

- What are your course’s learning objectives?
 
- Which methods do students use in your course?
 
- Which course details would help your model support those goals?

 

```text
Recommended uploads:

1. syllabus.pdf
   - Course schedule, objectives, and policies

2. [framework-name].txt
   - The analytical method students use
   - Write it out in plain language with definitions
```

 

**Consider** Add a short document (1–2 pages) explaining a method you teach, using language familiar to your students.

## knowledge/index.html — Slide 29

### Before

Type 2  

### Describe Assignments

 

These documents define the current task and help the model align its responses with your specific learning objectives.

 

- What does the assignment ask students to do?
 
- What does strong work on this assignment look like?
 
- What patterns come up most often in your feedback?

 

```text
Recommended uploads:

1. [assignment]-prompt.pdf
   - The assignment instructions

2. common-feedback.txt
   - 5-10 patterns you see every semester

3. strong-examples.txt (optional)
   - Excerpts showing what strong work looks like
```

 

**Consider** Which assignment stands to benefit? Try curating assignment instructions alongside a shortlist of common feedback patterns for starters.

### After

Type 2  

### Describe Assignments

 

Assignment instructions describe what students should do and what successful work requires.

 

- What does your assignment ask students to do?
 
- What does strong work on this assignment look like?
 
- What patterns come up most often in your feedback?

 

```text
Recommended uploads:

1. [assignment]-prompt.pdf
   - The assignment instructions

2. common-feedback.txt
   - 5-10 patterns you see every semester

3. strong-examples.txt (optional)
   - Excerpts showing what strong work looks like
```

 

**Consider** Which assignment stands to benefit? Try curating assignment instructions alongside a shortlist of common feedback patterns for starters.

## knowledge/index.html — Slide 30

### Before

Type 3  

### Identify Sources

 

Upload the readings and reference materials students are working with in the current unit. This grounds the model in the actual texts.

 

- What texts are students reading for this assignment?
 
- Are there reference documents (timelines, glossaries, citation guides)?
 
- Can you add brief metadata or context for each source?

 

```text
Recommended uploads:

1. [reading-title].pdf
   - Individual files per text (not one big reader)
   - Add a header with: title, author, date, source

2. context-notes.txt (optional)
   - 2-3 sentences of context per source

3. [reference-guide].pdf
   - Citation style guide, glossary, or timeline
```

 

**Consider** Which readings or sources are students working with right now? Separate files can make sources easier to identify. Test retrieval with your actual questions.

### After

Type 3  

### Identify Sources

 

Upload readings and reference materials students use in your current unit.

 

- What texts are students reading for this assignment?
 
- Are there reference documents (timelines, glossaries, citation guides)?
 
- Can you add brief metadata or context for each source?

 

```text
Recommended uploads:

1. [reading-title].pdf
   - Individual files per text (not one big reader)
   - Add a header with: title, author, date, source

2. context-notes.txt (optional)
   - 2-3 sentences of context per source

3. [reference-guide].pdf
   - Citation style guide, glossary, or timeline
```

 

**Consider** Which readings or sources are students working with right now? Separate files can make sources easier to identify. Test retrieval with your actual questions.

## knowledge/index.html — Slide 31

### Before

### Select Research Materials



Describe your research project and the sources you want the model to use.



Research context



Describe your question, scope, and method.



Instructions



Include a codebook, protocol, or criteria for comparing sources.



Sources



Identify the documents and passages you want to examine.

### After

### Select Research Materials



Describe your research project and identify sources your model should use.



Research context



Describe your question, scope, and method.



Instructions



Include a codebook, protocol, or criteria for comparing sources.



Sources



Identify documents and passages you want to examine.

## knowledge/index.html — Slide 32

### Before

### Attach Knowledge Collections



- Open your collection and upload the first few documents. Wait for processing to finish.

- Check the extracted text against each source.

- Return to **Workspace → Models**, open your card, and select the collection under **Knowledge**.

- Choose **Save & Update**, then start a fresh chat with that card.



[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

### After

### Attach Knowledge Collections



- Open your collection and upload a few documents. Wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your custom model, and select your collection under **Knowledge**.

- Choose **Save & Update**, then start a new chat with your custom model.



[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

## knowledge/index.html — Slide 33

### Before

### Test Retrieval



- Ask a question answered by one source. Verify the answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask a question the collection cannot answer. Check whether the response states that limit.



Repeat the baseline question with the model and prompt unchanged. Record the collection version and passages retrieved with your judgment.

### After

### Test Retrieval



- Ask a question answered by one source. Verify each answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask about something absent from your documents. Check whether your model acknowledges missing information.



Repeat your first question without changing models or system prompts. Record which documents you used, which passages were retrieved, and whether those passages support your model’s response.

## knowledge/index.html — Slide 34

### Before

### Share Knowledge Collections



Share the knowledge collection with the people who will use the custom model.



- Use **Add Access** to grant users or groups **Read** access.

- Check access with someone you shared the model and collection with.

- Choose **Public** only for documents intended for all signed-in Sandbox users.



[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

### After

### Share Knowledge Collections



Share your collection with people who will use your custom model.



- Use **Add Access** to grant users or groups **Read** access.

- Ask someone you shared with to check access to your model and collection.

- Choose **Public** only for documents intended for all signed-in Sandbox users.



[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

## skills/index.html — Slide 3

### Before

### Review Previous Work



Open your custom model and review its system prompt. Choose a procedure you use in teaching or research.



Write instructions for the procedure, attach the skill to your model, and test it.



Bring a knowledge collection if the procedure needs to search your documents.

### After

### Review Previous Work



Open your custom model and review its system prompt. Choose a procedure you use in teaching or research.



Write steps for your procedure, save them as a skill, attach it to your model, and test it.



Bring a knowledge collection if your procedure requires searching documents.

## skills/index.html — Slide 4

### Before

### Choose Procedures



- For teaching, guide a student through a source one question at a time.

- For research, compare a claim with its source or apply a codebook to an excerpt.

- Define what a successful response would show before writing the skill.



The procedure should be specific enough that another person can inspect whether it was followed.

### After

### Choose Procedures



- For teaching, guide a student through a source one question at a time.

- For research, compare a claim with its source or apply a codebook to an excerpt.

- Define what a successful response would show before writing instructions.



Write steps another person can follow and check.

## skills/index.html — Slide 5

### Before

### Define Skills



Skills contain reusable Markdown instructions for tasks or procedures.



The model receives a skill’s name and description and can load its full instructions when needed.



Describe when the skill should be used and what steps it should follow.



[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)



[Open WebUI Skills](https://docs.openwebui.com/features/workspace/skills/)

### After

### Define Skills



Skills contain reusable Markdown instructions for tasks or procedures.



Models receive a skill’s name and description and can load its full instructions when needed.



Describe when to use your skill and which steps to follow.



[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)



[Open WebUI Skills](https://docs.openwebui.com/features/workspace/skills/)

## skills/index.html — Slide 6

### Before

### Create Skills



![Current Skill editor showing name, ID, description, Access, and instructions](../images/current/skill-editor.png)



Enter a name, description, and instructions, then select Save & Create.





- Open **Workspace → Skills → Create**.

- Enter a name, identifier, and description that explain when to use it.

- Write the instructions, review **Access**, and choose **Save & Create**.



[Create and attach a skill](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

### After

### Create Skills



![Current Skill editor showing name, ID, description, Access, and instructions](../images/current/skill-editor.png)



Enter a name, description, and instructions, then select Save & Create.





- Open **Workspace → Skills → Create**.

- Enter a name, identifier, and description that explain when to use it.

- Write instructions, review **Access**, and choose **Save & Create**.



[Create and attach a skill](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

## skills/index.html — Slide 7

### Before

### Attach Skills



- Open **Workspace → Models** and edit your model.

- Select the skill under **Skills**.

- Set **Function Calling** to **Native** under **Advanced Parameters**.

- Select **Save & Update** and test a request that uses the skill.



Use a model that supports tool calling.



[Attach skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

### After

### Attach Skills



- Open **Workspace → Models** and edit your model.

- Select your skill under **Skills**.

- Set **Function Calling** to **Native** under **Advanced Parameters**.

- Select **Save & Update** and test a request that uses your skill.



Use a model that supports tool calling.



[Attach skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

## skills/index.html — Slide 8

### Before

### Compare Responses



Try the same request before and after attaching the skill. Keep the base model, sources, and system prompt fixed.



- Did the model use the intended procedure?

- Did it stop at the planned point for a response?

- Did it preserve evidence and uncertainty?

### After

### Compare Responses



Repeat a request before and after attaching your skill. Keep base model, sources, and system prompt unchanged.



- Did your model follow your instructions?

- Did it pause where you specified?

- Did it preserve evidence and uncertainty?

## skills/index.html — Slide 9

### Before

### Enable Tools



![Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter](../images/current/integrations.png)



Open Integrations beside the plus button to enable tools for this chat.





A tool runs an operation, such as a search, a calculation, or a query of a source collection.



Open **Integrations** beside the plus button for available chat capabilities. Attach reusable tools under **Tools** in the model editor.



Availability depends on account permissions, configuration, and model support.



[Enable tools in chat or on a model](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

### After

### Enable Tools



![Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter](../images/current/integrations.png)



Open Integrations beside + to enable tools for this chat.





A tool runs an operation, such as a search, a calculation, or a search within a knowledge collection.



Open **Integrations** beside + to choose tools for this chat. Attach reusable tools under **Tools** in your model editor.



Availability depends on account permissions, configuration, and model support.



[Enable tools in chat or on a model](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

## skills/index.html — Slide 10

### Before

### Tools & Skills



Skills



Instructions the model can load for a task or procedure.



Tools



Operations the model can call, such as web search, code execution, or database queries.



Test a request that needs the skill or tool. Check what the model used and whether its response is correct.



[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

### After

### Tools & Skills



Skills



Reusable instructions for tasks or procedures.



Tools



Operations such as web search, code execution, or database queries.



Test a request that needs your skill or tool. Check what your model used and whether its response is correct.



[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

## skills/index.html — Slide 12

### Before

Composition & Writing

 

### Original Instructions

 

**Starting Point**

```text
When a student is developing a research topic, walk them through four stages — conjecture, definition, quality, and policy — to help them narrow their question. Ask one stasis at a time.
```

 

- Model walks through all four stages in a single response instead of pausing at each
 
- No procedure for connecting the student’s working topic to each stasis question
 
- Treats stasis as a checklist rather than a deliberative process
 
- No mechanism to let the student reformulate before moving on
 
- Does not help the student identify which stasis their argument addresses

### After

Composition & Writing

 

### Original Instructions

 

**Starting Point**

```text
When a student is developing a research topic, walk them through four stages — conjecture, definition, quality, and policy — to help them narrow their question. Ask one stasis at a time.
```

 

- Model walks through all four stages in a single response instead of pausing at each
 
- No steps connecting a student’s topic to each stasis question
 
- Treats stasis as a checklist rather than a deliberative process
 
- No pause for students to revise their question
 
- Does not help students identify which stasis their argument addresses

## skills/index.html — Slide 14

### Before

Example 2  

### Examine Documents

 

History — The Sourcing Heuristic

### After

Example 2  

### Examine Documents

 

History — Source Analysis

## skills/index.html — Slide 15

### Before

History

 

### Original Instructions

 

**Starting Point**

```text
When a student asks about a primary source, retrieve it from the knowledge collection and walk them through its rhetorical situation using SOAPS. Ask questions one element at a time rather than summarizing.
```

 

- Model paraphrases the source instead of quoting from the uploaded document
 
- No procedure for retrieving and presenting specific passages as evidence
 
- Rushes through all SOAPS dimensions in a single response
 
- Student receives a finished reading rather than a structured inquiry
 
- No requirement to ground each analytical move in the source’s own language

### After

History

 

### Original Instructions

 

**Starting Point**

```text
When a student asks about a primary source, retrieve it from the knowledge collection and walk them through its rhetorical situation using SOAPS. Ask questions one element at a time rather than summarizing.
```

 

- Paraphrases source material without quoting uploaded documents
 
- No procedure for retrieving and presenting specific passages as evidence
 
- Rushes through all SOAPS dimensions in a single response
 
- Student receives a finished reading rather than a structured inquiry
 
- No requirement to support interpretations with quotations

## skills/index.html — Slide 18

### Before

Literature & Cultural Studies

 

### Original Instructions

 

**Starting Point**

```text
When a student shares a film still or visual artifact, guide them from describing formal elements — composition, lighting, framing — toward interpreting how those choices construct meaning in context.
```

 

- Model describes the image for the student instead of directing their attention
 
- No scaffolding from observation to formal analysis to interpretive claim
 
- Treats all visual elements at once rather than isolating one per turn
 
- No mechanism to keep the student doing the looking and the arguing
 
- Skips the gap between “what’s in the frame” and “what argument it makes”

### After

Literature & Cultural Studies

 

### Original Instructions

 

**Starting Point**

```text
When a student shares a film still or visual artifact, guide them from describing formal elements — composition, lighting, framing — toward interpreting how those choices construct meaning in context.
```

 

- Describes images without asking students what they notice
 
- No scaffolding from observation to formal analysis to interpretive claim
 
- Treats all visual elements at once rather than isolating one per turn
 
- No questions prompting students to observe and interpret
 
- Does not connect visual details with interpretive claims

## skills/index.html — Slide 21

### Before

Structure  

### Structure Skills

 

Use three parts to draft this skill.

 

- **Trigger** — When should this skill activate?
 
- **Procedure** — What steps does the model follow, in order?
 
- **Format** — What should the output look like?

### After

Structure  

### Structure Skills

 

Use three parts to draft this skill.

 

- **Trigger** — When should this skill activate?
 
- **Procedure** — Which steps should your model follow?
 
- **Format** — How should responses appear?

## skills/index.html — Slide 22

### Before

Component 1  

### Define Triggers

 

Define when this skill should activate. Test the trigger with a matching request and an unrelated request.

 

- What student action starts this workflow?
 
- Does it activate when they share a draft? Ask about a source? Upload an image?
 
- Should it run automatically, or only when the student asks?

 

```text
Skill: [Skill Name]
When a student [specific action or input], follow this procedure:
```

 

**Your turn** What pedagogical move are you trying to teach the model? Name the student action that should trigger it.

### After

Component 1  

### Define Triggers

 

Describe when to use your skill. Test a relevant request and an unrelated request.

 

- What student action starts this workflow?
 
- Does it activate when they share a draft? Ask about a source? Upload an image?
 
- Should it run automatically, or only when students ask?

 

```text
Skill: [Skill Name]
When a student [specific action or input], follow this procedure:
```

 

**Your turn** Name a student action your skill should respond to.

## skills/index.html — Slide 23

### Before

Component 2  

### Write Procedures

 

The core of every skill. Numbered steps that tell the model what to do, in what order, and when to wait.

 

- What should happen first? What comes next?
 
- Where should the model wait for the student before continuing?
 
- Should it quote, cite, or reference specific materials?

 

```text
Procedure:
1. [First step — what does the model do or ask?]
2. [After the student responds, what comes next?]
3. [Continue the sequence — include wait points]
4. [Final step — synthesis, next action, or handoff]
```

 

**Your turn** Write 3–5 numbered steps. Use the sequence you follow when performing this task yourself.

### After

Component 2  

### Write Procedures

 

Write numbered steps specifying what your model should do and when it should pause.

 

- What should happen first? What comes next?
 
- When should your model wait for a student response?
 
- Should it quote, cite, or reference specific materials?

 

```text
Procedure:
1. [First step — what does the model do or ask?]
2. [After the student responds, what comes next?]
3. [Continue these steps — specify when to wait for a student response]
4. [Final step — synthesis, next action, or handoff]
```

 

**Your turn** Write 3–5 numbered steps in an order you would follow yourself.

## skills/index.html — Slide 24

### Before

Component 3  

### Specify Format

 

Specify what the output should look like. Without a format, the model structures responses however it wants.

 

- Should the model quote the student’s text?
 
- Should each response end with a question?
 
- How long should a response be?

 

```text
Format:
> [quoted excerpt from student work or source document]

[1-2 sentences: what you observe]
[One question for the student]
```

 

**Your turn** Write a short format template. What should each response from the model actually look like?

### After

Component 3  

### Specify Format

 

Specify how responses should be organized.

 

- Should responses quote student writing?
 
- Should each response end with a question?
 
- How long should a response be?

 

```text
Format:
> [quoted excerpt from student work or source document]

[1-2 sentences: what you observe]
[One question for the student]
```

 

**Your turn** Write a template showing how each response should be organized.

## skills/index.html — Slide 26

### Before

Exercise  

### Choose Procedures

 

Which is closest to the skill you want to build?

 

### Establish Stasis

 

Narrow a research topic one question at a time

 

### Examine Documents

 

Quote, then ask who, when, for whom

 

### Analyze Images

 

Describe → analyze → interpret

 

### Choose Alternatives

 

A repeatable teaching or research procedure

### After

Exercise  

### Choose Procedures

 

Which procedure would you like to use?

 

### Establish Stasis

 

Narrow a research topic one question at a time

 

### Examine Documents

 

Quote, then ask who, when, for whom

 

### Analyze Images

 

Describe → analyze → interpret

 

### Choose Another Procedure

 

Use a procedure from your teaching or research.

## skills/index.html — Slide 27

### Before

Draft It  

### Write Instructions

 

Use the three-part structure to write a skill for the move you chose.

 

### Define Triggers

 

What student action starts this?

 

### Write Procedures

 

3–5 numbered steps with wait points.

 

### Specify Format

 

What does each response look like?

 

```text
Skill: [Name]
When a student [trigger action], follow this procedure:

Procedure:
1. [First step]
2. [Second step — include wait points]
3. [Third step]

Format:
> [quoted text from student or source]

[Observation in 1-2 sentences]
[One question]
```

### After

Draft It  

### Write Instructions

 

Describe when to use your skill, which steps to follow, and how responses should appear.

 

### Define Triggers

 

What student action starts this?

 

### Write Procedures

 

Write 3–5 steps and specify when to pause.

 

### Specify Format

 

What does each response look like?

 

```text
Skill: [Name]
When a student [trigger action], follow this procedure:

Procedure:
1. [First step]
2. [Second step — specify when to wait for a student response]
3. [Third step]

Format:
> [quoted text from student or source]

[Observation in 1-2 sentences]
[One question]
```

## skills/index.html — Slide 28

### Before

### Check Source Claims



Use this draft to check an interpretation against a source passage.



```text
When the user asks whether a passage supports a claim, ask for both if either is missing.

1. Quote the relevant passage and identify its source. Do not invent missing metadata.
2. State what the passage directly supports.
3. Identify an inference or competing reading that needs further evidence.
4. Ask one question that would help resolve the difference, then wait.

Keep the quotation separate from your interpretation. If the source is unavailable, explain what cannot be checked.
```



Test it with supported, overstated, and unsupported claims from public or approved material.

### After

### Check Interpretations



Use this draft to check an interpretation against a source passage.



```text
When the user asks whether a passage supports a claim, ask for both if either is missing.

1. Quote the relevant passage and identify its source. Do not invent missing metadata.
2. State what the passage directly supports.
3. Identify an inference or competing reading that needs further evidence.
4. Ask one question that would help resolve the difference, then wait.

Keep the quotation separate from your interpretation. If the source is unavailable, explain what cannot be checked.
```



Test it with supported, overstated, and unsupported claims from public or approved material.

## skills/index.html — Slide 29

### Before

### Test Skills



Create the skill, attach it to your model, confirm native function calling, and save the card. Open a fresh chat with the card.



- Send a request that should trigger the skill.

- Reply once and check whether the procedure continues appropriately.

- Send an unrelated request and check whether the skill is applied unnecessarily.



Record the result before revising the trigger or a procedural step.

### After

### Test Skills



Create your skill, attach it to your custom model, and confirm native function calling. Save your model and start a new chat.



- Send a request that should use your skill.

- Reply once and check whether your model follows your next step.

- Send an unrelated request and check whether your skill is used unnecessarily.



Save results before revising your skill’s description or instructions.

## skills/index.html — Slide 30

### Before

### Inspect Tool Results



With an available search tool, ask for the title and link of a source relevant to a narrow question. Open the returned page and verify the claim.



With an available code tool, use a small calculation whose answer you can check independently.



Look for the actual call and returned result. The sentence “I searched” or “I calculated” does not establish that a tool ran.

### After

### Inspect Tool Results



Use a search tool to find a source relevant to your question. Open its link and check whether it supports your model’s claim.



With an available code tool, use a small calculation whose answer you can check independently.



Inspect tool calls and results. Check whether a tool ran when your model says it searched or calculated.

## skills/index.html — Slide 31

### Before

### Check Calculations



Run this calculation with Code Interpreter.



```text
Use Code Interpreter to calculate the median of [3, 8, 8, 12, 19]. Show the calculation and report whether the tool ran.
```



The expected median is **8**. Check the execution result and the final answer. If the tool is unavailable or fails, the response should report that.

### After

### Check Calculations



Run this calculation with Code Interpreter.



```text
Use Code Interpreter to calculate the median of [3, 8, 8, 12, 19]. Show the calculation and report whether the tool ran.
```



Expected median is **8**. Check calculation output and final answer. If execution fails, your model should report that.

## skills/index.html — Slide 32

### Before

### Record Test Results



| Record | Include |
| --- | --- |
| Configuration | Model, prompt, collection version, skill text, enabled tools. |
| Action | Input, skill loading, tool call, result, final response. |
| Judgment | Expected behavior, observed behavior, evidence, next revision. |



Before sharing, check that the people you share with can use the model and its collections, skills, and tools. Repeat relevant tests after a model or tool update.

### After

### Record Test Results



| Record | Include |
| --- | --- |
| Configuration | Model ID, system prompt, documents, skill instructions, and enabled tools. |
| Action | Request, instructions used, tool calls and results, and final response. |
| Judgment | What you expected, what happened, and any change you plan to test. |



Before sharing, confirm others can access your model, collections, skills, and tools. Repeat relevant tests after updates.

## examples.html

### Before

System-prompt examples | CUNY AI Lab

### System Prompt Examples



Choose a prompt and adapt its purpose, procedure, and constraints to your teaching or research task. Test the prompt with your selected base model.



Replace bracketed text with details about your task.

[Compose System Prompts](./) · [Curate Knowledge Collections](knowledge/) · [Skills & Tools](skills/)

### Examine Assumptions

Help the user examine a question before settling on an answer. Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question. Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.



### Guide Revision

You are a writing scaffold for an English 101 composition course. Help students examine the link between a claim and its evidence. Procedure: 1. Ask for the assignment and a short draft before giving feedback. 2. Identify one concern about the claim or evidence. 3. Ask one question, then wait for the student to respond. Constraints: - Do not write or rewrite the student's sentences. - If asked to "just fix it," offer a specific revision step. - Do not invent sources or grade the work. - Tone: Warm and direct.



### Vague Prompts



Weak

Help students write better.



### Add Specifics



Getting There

You are a writing scaffold for a college composition course. Help students develop their essays by breaking revision into structured steps. Ask them to identify their thesis before giving feedback. Don't write essays for them.



### Guide Revision



Strong

You are a writing scaffold for an English 101 composition course at a public urban university. Students are drafting a position paper on rhetoric in popular media and must revise their first draft in preparation for their final submission. The core problem: students treat revision as proofreading, fixing grammar and word choice, rather than rethinking argument, structure, and evidence. They lack a process for examining whether their ideas are clear, well-organized, and sufficiently supported. This tool scaffolds the move from surface-level fixes to substantive revision. Procedure: 1. Request the assignment prompt and student draft before responding. 2. Identify the highest-priority concerns (thesis clarity, structure, evidence) before surface-level issues. 3. For each concern, ask the student a question rather than providing a fix. Constraints: - Never generate text that could substitute for the student’s own writing. Focus on higher-order concerns like argument, structure, and evidence. - If asked to “just fix it,” redirect toward a specific revision step. - Do not grade or evaluate. - Tone: Warm and direct. Use “I notice...” and “What if you tried...”



### Vague Prompts



Weak

Analyze historical documents.



### Add Specifics



Getting There

You are a history source-analysis tool. Help students analyze primary sources from American history. Ask them to consider the author, audience, and context of each document. Don't just summarize the document for them.



### Analyze Primary Sources



Strong

You are a source-analysis tool for an undergraduate U.S. history survey covering the period from Reconstruction through the Civil Rights Movement. Students must analyze primary source documents from the period and use them as the basis for a historical report. The core problem: students extract facts from sources rather than analyzing them as constructed arguments shaped by author, audience, and context. Procedure (based on Wineburg’s historical thinking heuristics): 1. Ask the student to identify the source (title, date, creator, document type) before proceeding. 2. Guide them through the four moves below, one at a time. Never jump ahead. 3. After each move, ask why that detail matters and prompt them to ground their response in specific passages. 4. After all four moves, ask the student to synthesize: what does the full picture reveal about this historical moment? Four Moves: - Sourcing — Before reading: who created this, when, and why? What can we infer about reliability and perspective? - Contextualization — What was happening at the time and place this was produced? How does that shape its meaning? - Close Reading — What does the text actually say — and what does it leave out, downplay, or assume? - Corroboration — How does this source compare to others from the period? Where do accounts agree or conflict? Constraints: - Never offer guidance before the student has attempted an answer. - Encourage grounding interpretations in specific passages as analysis develops. - If unsure about a historical fact, say so. Never invent dates, names, or events. - Never provide a complete analysis. Ask the next question a historian would ask. - Tone: Patient and curious.



### Vague Prompts



Weak

Help with literary analysis.



### Add Specifics



Getting There

You are a close-reading scaffold. Help students analyze literary texts by focusing on themes, symbolism, and narrative techniques. Don't just summarize the plot. Ask students to point to specific passages.



### Analyze Literary Texts



Strong

You are a close-reading tool designed for an introductory English course that focuses on cultural studies and literary analysis. Students recently practiced close reading and must now select a brief literary artifact to analyze using techniques associated with New Criticism. The core problem: students default to summarizing content or importing biographical and historical context rather than attending closely to how the text works: how language, form, imagery, and internal tension generate meaning within the artifact itself. Procedure: 1. Ask what the student notices about the language in their chosen passage. 2. Prompt them to examine specific textual features (word choice, imagery, syntax, point of view) and how they create meaning. 3. Ask how the passage connects to the work’s larger themes. 4. Guide them toward an interpretive claim grounded in textual evidence. Framework: - Treat the text as a self-contained object. Bracket authorial intent and historical context; attend to what the language itself does. - Look for tension, irony, paradox, and ambiguity as sites of meaning, not problems to resolve. Ask how formal elements (diction, imagery, syntax, tone) work together as a meaningful cultural artifact. - Once a close reading is underway, invite students to reflect on the method itself: what does focusing on the text alone illuminate, and what does it leave out? Constraints: - Facilitate multiple interpretations grounded in textual evidence. Do not prescribe a correct reading. - If a student reaches for biographical or historical context, redirect them back to the text: “What in the language itself supports that reading?” Tone: Encouraging and accessible. Affirm observations, then push deeper.



### Define Context

You are a [tool type] for [course name]. Students are [relevant context]. The core problem: [specific learning challenge].



### Write Procedures

Procedure: 1. Ask the student for [specific input] before responding. 2. Identify [priority concern] before addressing [secondary concerns]. 3. For each issue, [specific action, e.g. ask a question rather than fix it].



### Set Constraints

Constraints: - Never [specific output to avoid]. - If asked to [common student request], redirect by [specific alternative]. - If uncertain about [domain content], say so explicitly.



### Set Tone

Tone: [Adjective and adjective]. Use phrases like "[example phrase]" and "[example phrase]."



### Specify Format

Format each response as: Observation: [what you notice] Focus: [one thing to work on] Next step: [a specific, actionable suggestion] Question: [something for the student to consider]

### After

System-prompt examples | CUNY AI Lab

### System Prompt Examples



Choose a prompt and adapt its purpose, procedure, and constraints to your teaching or research task. Test your prompt with a selected base model.



Replace bracketed text with details about your task.

[Compose System Prompts](./) · [Curate Knowledge Collections](knowledge/) · [Skills & Tools](skills/)

### Examine Assumptions

Help the user examine a question before settling on an answer. Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question. Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.



### Guide Revision

You are a writing scaffold for an English 101 composition course. Help students examine the link between a claim and its evidence. Procedure: 1. Ask for the assignment and a short draft before giving feedback. 2. Identify one concern about the claim or evidence. 3. Ask one question, then wait for the student to respond. Constraints: - Do not write or rewrite the student's sentences. - If asked to "just fix it," offer a specific revision step. - Do not invent sources or grade the work. - Tone: Warm and direct.



### Vague Prompts



Weak

Help students write better.



### Add Specifics



Getting There

You are a writing scaffold for a college composition course. Help students develop their essays by breaking revision into structured steps. Ask them to identify their thesis before giving feedback. Don't write essays for them.



### Guide Revision



Strong

You are a writing scaffold for an English 101 composition course at a public urban university. Students are drafting a position paper on rhetoric in popular media and must revise their first draft in preparation for their final submission. The core problem: students treat revision as proofreading, fixing grammar and word choice, rather than rethinking argument, structure, and evidence. They lack a process for examining whether their ideas are clear, well-organized, and sufficiently supported. This tool scaffolds the move from surface-level fixes to substantive revision. Procedure: 1. Request the assignment prompt and student draft before responding. 2. Identify the highest-priority concerns (thesis clarity, structure, evidence) before surface-level issues. 3. For each concern, ask the student a question rather than providing a fix. Constraints: - Never generate text that could substitute for the student’s own writing. Focus on higher-order concerns like argument, structure, and evidence. - If asked to “just fix it,” redirect toward a specific revision step. - Do not grade or evaluate. - Tone: Warm and direct. Use “I notice...” and “What if you tried...”



### Vague Prompts



Weak

Analyze historical documents.



### Add Specifics



Getting There

You are a history source-analysis tool. Help students analyze primary sources from American history. Ask them to consider the author, audience, and context of each document. Don't just summarize the document for them.



### Analyze Primary Sources



Strong

You are a source-analysis tool for an undergraduate U.S. history survey covering the period from Reconstruction through the Civil Rights Movement. Students must analyze primary source documents from the period and use them as the basis for a historical report. The core problem: students extract facts from sources rather than analyzing them as constructed arguments shaped by author, audience, and context. Procedure (based on Wineburg’s historical thinking heuristics): 1. Ask the student to identify the source (title, date, creator, document type) before proceeding. 2. Guide them through the four moves below, one at a time. Never jump ahead. 3. After each move, ask why that detail matters and prompt them to ground their response in specific passages. 4. After all four moves, ask the student to synthesize: what does the full picture reveal about this historical moment? Four Moves: - Sourcing — Before reading: who created this, when, and why? What can we infer about reliability and perspective? - Contextualization — What was happening at the time and place this was produced? How does that shape its meaning? - Close Reading — What does the text actually say — and what does it leave out, downplay, or assume? - Corroboration — How does this source compare to others from the period? Where do accounts agree or conflict? Constraints: - Never offer guidance before the student has attempted an answer. - Encourage grounding interpretations in specific passages as analysis develops. - If unsure about a historical fact, say so. Never invent dates, names, or events. - Never provide a complete analysis. Ask the next question a historian would ask. - Tone: Patient and curious.



### Vague Prompts



Weak

Help with literary analysis.



### Add Specifics



Getting There

You are a close-reading scaffold. Help students analyze literary texts by focusing on themes, symbolism, and narrative techniques. Don't just summarize the plot. Ask students to point to specific passages.



### Analyze Literary Texts



Strong

You are a close-reading tool designed for an introductory English course that focuses on cultural studies and literary analysis. Students recently practiced close reading and must now select a brief literary artifact to analyze using techniques associated with New Criticism. The core problem: students default to summarizing content or importing biographical and historical context rather than attending closely to how the text works: how language, form, imagery, and internal tension generate meaning within the artifact itself. Procedure: 1. Ask what the student notices about the language in their chosen passage. 2. Prompt them to examine specific textual features (word choice, imagery, syntax, point of view) and how they create meaning. 3. Ask how the passage connects to the work’s larger themes. 4. Guide them toward an interpretive claim grounded in textual evidence. Framework: - Treat the text as a self-contained object. Bracket authorial intent and historical context; attend to what the language itself does. - Look for tension, irony, paradox, and ambiguity as sites of meaning, not problems to resolve. Ask how formal elements (diction, imagery, syntax, tone) work together as a meaningful cultural artifact. - Once a close reading is underway, invite students to reflect on the method itself: what does focusing on the text alone illuminate, and what does it leave out? Constraints: - Facilitate multiple interpretations grounded in textual evidence. Do not prescribe a correct reading. - If a student reaches for biographical or historical context, redirect them back to the text: “What in the language itself supports that reading?” Tone: Encouraging and accessible. Affirm observations, then push deeper.



### Define Context

You are a [tool type] for [course name]. Students are [relevant context]. The core problem: [specific learning challenge].



### Write Procedures

Procedure: 1. Ask the student for [specific input] before responding. 2. Identify [priority concern] before addressing [secondary concerns]. 3. For each issue, [specific action, e.g. ask a question rather than fix it].



### Set Constraints

Constraints: - Never [specific output to avoid]. - If asked to [common student request], redirect by [specific alternative]. - If uncertain about [domain content], say so explicitly.



### Set Tone

Tone: [Adjective and adjective]. Use phrases like "[example phrase]" and "[example phrase]."



### Specify Format

Format each response as: Observation: [what you notice] Focus: [one thing to work on] Next step: [a specific, actionable suggestion] Question: [something for the student to consider]

## WORKSHOP.md

### Before

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

Workshop 1 requires only individual access and sign-in. The facilitator enables the arranged Workspace access during the midpoint exercise. Participants refresh, inspect the sample card, and can save their tested prompt as a private configuration. If access is delayed, participants follow the demonstration and continue testing in chat. Before Workshop 2, arrange Workspace and Knowledge access with the Lab. Before Workshop 3, arrange Skills and Tools access, including authoring permissions for participants who will create or edit resources. Confirm which base models and capabilities are available to the group.

Prepare **Examine Assumptions** as a demonstration card using [this sample prompt](examples/assumption-check.txt) and a tested base model. Keep a plain-text copy available if the demonstration account cannot open it.

Choose two available small models for the opening demonstration. Record their exact identifiers and settings rather than treating screenshot labels as a current inventory. Check personal defaults, folder instructions, memory, and optional features that may introduce additional context. Keep these consistent during comparisons and document differences you cannot control.

Use documents you are permitted to upload and share for collection and skill exercises. Verify sharing through an ordinary participant account, including access to the card, base model, and attached resources. Course enrollment has a separate invitation route in the documentation; it is not a prerequisite for Workshop 1.

## Compose System Prompts

Participants compare model responses, examine assumptions, and test instructions before seeing how a Workspace card can preserve a configuration for reuse. The facilitator models the comparison process on the nurse question, then introduces the car-wash task. Participants take over that task, save a baseline, and compare it with a response shaped by an in-chat system prompt.

### Workshop Agenda

- Request individual access and sign in
- Compare responses from small models
- Compare car-wash responses
- Revise in-chat system prompts
- Explore Workspace models
- Save prompts for reuse

### Lesson Plan

| Minutes | Facilitation and participant activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Introduce the series and agenda. Confirm sign-in. Locate the model selector inside the message box, More, Integrations, message actions, and Controls. | Account readiness and selected model names |
| 10–18 | Demonstrate two small models answering the nurse question. Ask participants to read both responses and identify assumptions. | Exact inputs, model identifiers, responses |
| 18–25 | Demonstrate the car-wash prompt. Show the two cropped GCDI showcase excerpts after the initial live comparison. Discuss recommendations in relation to the purpose of the trip. | Assumptions and evidence supporting each judgment |
| 25–35 | Hand off the car-wash exercise. Participants compare two models in fresh chats and save responses before adding a follow-up that states their purpose. | Baseline and follow-up responses |
| 35–45 | Keep one model fixed. Add the sample through Controls → System Prompt in a fresh chat, repeat the car-wash task, then revisit the nurse question. | Before-and-after comparison using the same criteria |
| 45–55 | Enable the arranged Workspace access. Participants refresh and inspect the prepared sample card with the facilitator. Read Base Model and System Prompt together, then connect those settings to the in-chat exercise. | Prompt text and model choice to carry forward |
| 55–75 | Discuss one disciplinary progression from the examples page. Participants adapt context, procedure, constraints, tone, and format for one teaching or research task. Keep other examples as reference material. | Draft prompt and private card when Workspace access is confirmed |
| 75–85 | Test a normal request, an incomplete request, and a request that conflicts with the intended procedure. Revise one instruction and repeat. | Failure, revision, and retest |
| 85–90 | Share one supported observation. Save prompt versions and comparison notes. Review access needed for Workshop 2. | Next question and access request |

### Compare Small Models

> The nurse yelled at the doctor because she was late. Who was late?

Send exactly this question to two small models with matching context. Ask which interpretation each response chooses and whether it acknowledges ambiguity. Either person can be the referent of “she”; the sentence does not establish a unique answer. A plausible interpretation is different from information established by the wording. Avoid turning this single item into a claim about model-wide bias or ability.

### Compare Car-Wash Responses

> The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.

This wording comes from the [GCDI showcase source](https://docs.google.com/presentation/d/1dwRGEe7WniZOEeMcgQ8_qygHsKFu_ZnG/edit). The original recommendation excerpts remain as archival examples with the obsolete top selector cropped out. Their Qwen labels are inconsistent, so use them to discuss responses rather than establish exact model identities or benchmark rankings. Recorded timings describe those captures only.

Ask participants to write down their interpretation of the trip’s purpose before reading the responses. If the purpose is washing the car, the car needs to get there. The wording leaves that purpose unstated. Participants then add a follow-up such as “I want to wash my car” or “I only want to ask about prices” and inspect whether the recommendation changes appropriately.

| Criterion | Model A evidence | Model B evidence |
| --- | --- | --- |
| Identify stated goal or acknowledge missing purpose | | |
| Distinguish stated facts from assumptions | | |
| Give reasons that support recommendation | | |
| Respond appropriately to clarification | | |

For the in-chat system-prompt exercise, use [Examine Assumptions](examples/assumption-check.txt). It asks the model to examine facts and assumptions without prescribing either demonstration answer. Check whether the added instructions help, cause unnecessary questions, or fail on the second task. Retain the baseline before changing anything.

## Curate Knowledge Collections

Participants upload documents to a knowledge collection and attach it to a custom model. They ask questions about those materials and check whether the model retrieves relevant passages and cites them accurately. Course examples use assignments and readings; research examples compare claims and methods across source documents.

### Workshop Agenda

- Confirm Workspace and Knowledge access
- Select source documents
- Create knowledge collections
- Attach collections to model cards
- Check source citations
- Choose procedures for skills

### Lesson Plan

| Minutes | Facilitation and participant activity | Evidence to retain |
| --- | --- | --- |
| 0–10 | Confirm individual sign-in, Workspace, Knowledge access, and the card or prompt carried from Workshop 1. Save a response before adding sources. | Baseline configuration and response |
| 10–20 | Explain extraction, passages, retrieval, and response context. Demonstrate the current Knowledge creation form. | Source-dependent question and expected passage |
| 20–35 | Discuss one collection progression. Compare what each source contributes to the task. Offer the research collection as an alternative context. | Proposed source list with reasons |
| 35–55 | Create a private collection. Upload a few documents, wait for processing, and inspect extracted text. | Document versions and extraction problems |
| 55–65 | Attach the collection under Knowledge in the model editor and use Save & Update. Keep the model and system prompt fixed. | Collection and card configuration |
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
| 0–10 | Confirm sign-in, Skills and Tools access, authoring permissions, and a usable card. Confirm Knowledge access only when the chosen task requires a collection. | Available dependencies and baseline |
| 10–25 | Explain skills and tools. Demonstrate the Skill editor, model attachment, native function calling, and chat Integrations. | Trigger and capability requirements |
| 25–40 | Discuss one retained disciplinary procedure. Use the research claim-checking example when relevant. | Procedure and success criteria |
| 40–60 | Draft trigger, procedure, and format. Create the skill, attach it, set Function Calling → Native, and save the model. | Skill version and model settings |
| 60–72 | Test a matching request, a follow-up, and an unrelated request. Inspect skill loading and whether the model pauses or continues as instructed. | Procedure-following evidence and failures |
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


### After

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

Participants compare responses and test system instructions before saving a custom model for reuse. Begin with two small models interpreting a sentence about a nurse and doctor. Then ask whether to walk or drive to a car wash. Participants edit system instructions in Chat Controls and regenerate responses to their original prompt.

### Workshop Agenda

- Request individual access and sign in
- Compare responses from small models
- Compare outputs
- Revise in-chat system prompts
- Explore Workspace models
- Save prompts for reuse

### Lesson Plan

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

### Compare Small Models

> The nurse yelled at the doctor because she was late. Who was late?

Send exactly this question to two small models with matching context. Ask which interpretation each response chooses and whether it acknowledges ambiguity. Either person can be the referent of “she”; the sentence does not establish a unique answer. A plausible interpretation is different from information established by the wording. Avoid turning this single item into a claim about model-wide bias or ability.

### Compare Outputs

> The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.

Screenshot provenance and inconsistent Qwen labels are documented in [source history](review/showcase-sources.json). Discuss these responses without treating screenshot labels or timings as reliable model identifiers or comparative measurements.

Ask “What do you think this person wants to accomplish?” Participants save both original responses, add system instructions in Chat Controls, and regenerate responses to their unchanged prompt. Compare assumptions, explanations, and any change in recommendations.

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


## README.md

### Before

# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Compose System Prompts begins the series. Use **Outline** to move to Curate Knowledge Collections and Skills & Tools. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](SLIDES.md)
- [Presenter lesson plans and access requirements](WORKSHOP.md)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Copy review and source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

The first session demonstrates two small models on the nurse question before the car-wash demonstration and handoff. Participants compare responses, check citations, and test tools in teaching and research tasks. Long disciplinary examples remain available as reference material; the lesson plans identify a shorter path for live sessions.

## Development

Static HTML, CSS, and JavaScript. No build step or runtime dependencies.

```sh
python3 -m http.server 8766
python3 scripts/check_series.py
```

After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, the slider, or **Outline** to navigate. On mobile, the slider occupies a full row above the navigation buttons. Text selection does not advance slides. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Outline** links to each workshop, prompt examples, and the complete transcript, including screenshot instructions. Presenter lesson plans remain available through this README.

## Sources

Developed from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools), originally developed by Stefano Morello and Zach Muhlbauer. Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. GCDI comparison excerpts are labeled as archival and cropped to remove the obsolete top selector. See the review folder for provenance and the source-label limitation.


### After

# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Compose System Prompts begins the series. Use **Outline** to move to Curate Knowledge Collections and Skills & Tools. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](SLIDES.md)
- [Presenter lesson plans and access requirements](WORKSHOP.md)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Copy review and source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

Participants first compare how two small models interpret a sentence about a nurse and doctor. They then ask whether to walk or drive to a car wash, edit system instructions, and regenerate responses to their original prompt. Participants compare responses, check citations, and test tools in teaching and research tasks. Long disciplinary examples remain available as reference material; the lesson plans identify a shorter path for live sessions.

## Development

Static HTML, CSS, and JavaScript. No build step or runtime dependencies.

```sh
python3 -m http.server 8766
python3 scripts/check_series.py
```

After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, the slider, or **Outline** to navigate. On mobile, the slider occupies a full row above the navigation buttons. Text selection does not advance slides. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Outline** links to each workshop, prompt examples, and the complete transcript, including screenshot instructions. Presenter lesson plans remain available through this README.

## Sources

Developed from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools), originally developed by Stefano Morello and Zach Muhlbauer. Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. Reused comparison screenshots exclude obsolete controls. Capture provenance and source limitations remain in review files.


