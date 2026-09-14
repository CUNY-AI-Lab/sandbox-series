# Sandbox Workshops

## Compose System Prompts — 1

Workshop 1 of 3

### Compose System Prompts

Compare and configure models for teaching and research

CUNY AI Lab Sandbox

Developed by Stefano Morello and Zach Muhlbauer

---

## Compose System Prompts — 2

### Workshop Roadmap

- **Compose System Prompts** Configure model behavior with system prompts.

- **Curate Knowledge Collections** Upload documents so models can reference them.

- **Skills & Tools** Add web search, code execution, and reusable instructions.

[Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/)

---

## Compose System Prompts — 3

### Workshop Agenda

- Request individual access and sign in

- Compare responses from small models

- Compare car-wash responses

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse

Before attending, request individual access and sign into the Sandbox.

---

## Compose System Prompts — 4

### Request Access

[ailab.gc.cuny.edu/request-access/](https://ailab.gc.cuny.edu/request-access/)

- Choose **My own access** and sign in with **CUNY Login**.

- Complete your details, select **CAIL Sandbox**, and submit the application.

- After approval, open [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/) and select **Continue with CUNY Login**.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Compose System Prompts — 5

### Select Models

![Current Sandbox new chat with the model selector inside the message box](images/current/chat-page.png)

Select the model name on the right inside the message box.

Select the model name **on the right inside the message box**.

Type a request, send it, then ask a follow-up. Open **New Chat** when you want to begin with fresh conversation history.

[Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/)

---

## Compose System Prompts — 6

### Chat Controls

Upload Files (+)

Attach images, PDFs, or documents.

Integrations

Choose tools and skills for this chat.

Message actions

Copy, edit, or regenerate a response. Open the three-dot menu for additional actions.

[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

---

## Compose System Prompts — 7

### Compare Models

![Current model selector with search and the Compare toggle](images/current/model-selector.png)

Open the model selector, turn on Compare, and select two models.

Open the model selector. Turn on **Compare**, then choose two available base models.

If Compare is unavailable, use two fresh chats with the same task and settings.

Switching models midway carries the conversation history forward. Use fresh chats for a clearer initial comparison.

---

## Compose System Prompts — 8

### Who Was Late?

Compare how two small models interpret this sentence.

```text
The nurse yelled at the doctor because she was late. Who was late?
```

Use the same prompt and chat history for both models. Note which models you selected.

---

## Compose System Prompts — 9

### Examine Assumptions

“She” could refer to either person. Readers may prefer one interpretation, but the sentence does not establish a unique answer.

- Does each model acknowledge the ambiguity?

- What assumption supports its answer?

- Does the explanation add information absent from the sentence?

Compare the evidence in the answers. A confident explanation can still rest on an unsupported assumption.

---

## Compose System Prompts — 10

### Compare Recommendations

Use the same two-model comparison for this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

Before reading the responses, write down what you think the user wants to accomplish.

---

## Compose System Prompts — 11

### Read Gemma’s Response

![Archived car-wash prompt and Gemma response saying to walk](images/showcase/car-wash-gemma.png)

GCDI showcase, May 2026. Gemma recommends walking.

The response shown recommends walking. Read its recommendation against the purpose of the trip.

---

## Compose System Prompts — 12

### Read Qwen’s Response

![Archived car-wash prompt and Qwen response saying to take the car](images/showcase/car-wash-qwen.png)

GCDI showcase, May 2026. Qwen recommends taking the car.

Compare this recommendation with Gemma’s. What does each response assume about the trip?

---

## Compose System Prompts — 13

### Try Model Comparison

- In a fresh chat, send the car-wash prompt to two available models. Save both responses.

- Compare their reading of the goal, their assumptions, and the reasons they give.

- Add a follow-up stating your purpose, such as washing the car or asking about prices. Does the recommendation change appropriately?

If the purpose is to wash the car, the car must get there. The original wording leaves the purpose unstated.

---

## Compose System Prompts — 14

### Evaluate Responses

Compare how each model interprets the question and explains its recommendation.

- Which assumptions does each response make?

- Does either response invent information?

- How does each model respond when you clarify your purpose?

Save the responses with the prompt and model names so you can repeat the comparison.

---

## Compose System Prompts — 15

### System Prompts

A system prompt defines how a model should behave throughout a conversation.

### User Prompts

Questions or tasks you enter in chat.

### System Prompts

Instructions for the model’s role, tone, boundaries, and response style.

Test whether the selected model follows your instructions.

[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/)

[Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

---

## Compose System Prompts — 16

### Open Chat Controls

![Current chat Controls panel with its System Prompt field](images/current/chat-controls.png)

Enter instructions in the System Prompt field under Chat Controls.

- Open a fresh chat with one of the models you compared.

- Select **Controls** at the top right.

- Enter the sample in **System Prompt** before sending the task.

Use the conversation’s Controls for this exercise. Personal defaults under Settings have a wider scope.

---

## Compose System Prompts — 17

### Test System Prompts

Keep one base model fixed. Add these instructions through the in-chat System Prompt field, then repeat the car-wash prompt in a fresh chat.

```text
Help the user examine a question before settling on an answer.

Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question.

Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.
```

---

## Compose System Prompts — 18

### Compare Responses

- Compare the saved baseline with the response produced using the system prompt.

- Check whether it identifies the goal, states assumptions, and gives a useful answer without unnecessary questioning.

- Try the nurse question again. Does the instruction help with ambiguity in a different form?

Keep the model, optional features, and other defaults consistent. Record any differences you cannot control.

---

## Compose System Prompts — 19

### Open Workspace

Open **Workspace → Models**.

Open the sample model and review its **Base Model** and **System Prompt**. Compare those instructions with the prompt you tested in chat.

Continue in chat if Workspace is unavailable.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Compose System Prompts — 20

### Workspace Tabs

![Current Workspace header with Models, Knowledge, Prompts, Skills, Tools, and Create](images/current/workspace-header.png)

Select a Workspace tab, then choose Create.

### Custom Models

Open a model to view its base model and system prompt. Select **Create** to configure your own.

### Knowledge and Tools

Knowledge adds sources. Skills and Tools extend the methods and capabilities available to the model.

---

## Compose System Prompts — 21

### Model Configuration

![Current model creation form showing Name, Base Model, and System Prompt](images/current/model-editor.png)

Choose a name and base model, then enter a system prompt.

- **Name** — Use a name that students or colleagues will recognize.

- **Base Model** — Choose a model you have tested.

- **System Prompt** — Add the instructions you tested in chat.

A custom model combines these choices. Creating it does not train a new base model.

[The model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Compose System Prompts — 22

### Create Custom Models

Custom models combine a base model with instructions, documents, and tools.

- Enter a name and description that students or colleagues will recognize.

- Select a base model and add your tested system prompt.

- Add prompt suggestions for tasks the model should support.

Students select the custom model to use the instructions and resources you configured.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Compose System Prompts — 23

Examples

### Structure System Prompts

---

## Compose System Prompts — 24

Example 1

### Teach Composition

---

## Compose System Prompts — 25

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

---

## Compose System Prompts — 26

Composition & Writing

### Add Specifics

**Getting There**

```text
You are a writing scaffold for a college composition course. Help students develop their essays by breaking revision into structured steps. Ask them to identify their thesis before giving feedback. Don't write essays for them.
```

### Compare Improvements

- Assigns a role and disciplinary context

- Includes a basic pedagogical move

- Sets one boundary

### Add Detail

- No procedural instructions for *how* to give feedback

- No awareness of student population or course level

- No edge-case handling

---

## Compose System Prompts — 27

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

---

## Compose System Prompts — 28

Example 2

### Analyze Primary Sources

---

## Compose System Prompts — 29

History

### Vague Prompts

**Weak**

```text
Analyze historical documents.
```

### Identify Problems

- No methodological framework

- No period or geographic focus

- No guidance on handling hallucinated facts or invented sources

---

## Compose System Prompts — 30

History

### Add Specifics

**Getting There**

```text
You are a history source-analysis tool. Help students analyze primary sources from American history. Ask them to consider the author, audience, and context of each document. Don't just summarize the document for them.
```

### Compare Improvements

- Assigns a role and disciplinary scope

- References a real methodology

- Sets a boundary against summarization

### Add Detail

- No procedural steps for guiding analysis

- No handling of uncertainty or AI limitations

- No attention to historiographical perspective

---

## Compose System Prompts — 31

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

---

## Compose System Prompts — 32

Example 3

### Analyze Literary Texts

---

## Compose System Prompts — 33

Literature & Cultural Studies

### Vague Prompts

**Weak**

```text
Help with literary analysis.
```

### Identify Problems

- Defaults to plot summary

- No theoretical or critical framework

- No requirement for textual evidence

---

## Compose System Prompts — 34

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

---

## Compose System Prompts — 35

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

---

## Compose System Prompts — 36

### Adapt Research Prompts

Choose a research task, such as comparing article abstracts, checking how you coded a passage, or documenting a method.

- State the research question and material the model may use.

- Specify the procedure and what counts as evidence.

- Ask the model to explain uncertainty and consider other interpretations.

Save your source material, prompt, response, and assessment together.

---

## Compose System Prompts — 37

### Draft System Prompts

---

## Compose System Prompts — 38

Structure

### Define Prompt Components

Draft a system prompt using these components.

- **Context & Problem** — What course, what students, what learning challenge?

- **Procedure** — What steps should the tool follow?

- **Constraints** — What should it refuse to do, and how should it redirect?

- **Tone** — What register and affect should it use with your students?

- **Output Format** — How should it structure its responses?

---

## Compose System Prompts — 39

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

---

## Compose System Prompts — 40

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

---

## Compose System Prompts — 41

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

---

## Compose System Prompts — 42

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

---

## Compose System Prompts — 43

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

---

## Compose System Prompts — 44

Refine

### Refine Instructions

---

## Compose System Prompts — 45

### Extend Instructions

### Set Conditions

“If the student submits a draft, focus on structure before style. If they ask a yes/no question, reframe it as an open one. If they ask you to just give them the answer, ask what they’ve tried first.”

### Request Concise Responses

“Respond to one thing at a time. Do not front-load your full analysis. Ask one question, wait for the student’s response, then proceed.”

### Acknowledge Uncertainty

“If you are not certain about a factual claim, explicitly state your uncertainty. Never fabricate citations or attribute quotes.”

### Support Multiple Languages

“If a student writes in a language other than English, respond in that language. Offer to discuss concepts in both languages.” Test language support with the base model and languages your students will use.

---

## Compose System Prompts — 46

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

---

## Compose System Prompts — 47

### Save Prompts

- Save your prompt text with the model name and responses it produced.

- Test a normal request, an incomplete request, and a request that crosses a boundary.

- Revise one instruction and repeat the test in a fresh chat.

Save your tested prompt in a private custom model. Choose the base model, review **Access**, and select **Save & Create**. Reuse this model when adding documents in Workshop 2.

---

## Compose System Prompts — 48

### Share Custom Models

- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use the model and **Write** access to people who will edit it.

- Check that the people you share with can use the base model and any attached collections, skills, or tools.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Compose System Prompts — 49

### Record Comparisons

Record your prompt and model settings alongside the responses you compared.

| Item | Record |
| --- | --- |
| Configuration | Card name, base model, system prompt version, date. |
| Test | User request, enabled features, saved response. |
| Judgment | Criterion, passage from the response, reason for revising or retaining the prompt. |

Use materials you are permitted to upload and share. Sandbox chats may be stored and accessible to administrators or people you share them with.

[Privacy and chat history](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Compose System Prompts — 50

### Prepare Source Documents

- Save prompt versions and comparison notes

- Request Workspace and Knowledge collection access

- Select public or approved source documents

- Review [system-prompt examples](examples.html)

- Continue to [Curate Knowledge Collections](knowledge/)


## Curate Knowledge Collections — 1

### Curate Knowledge Collections

Upload documents for models to reference in teaching and research

CUNY AI Lab Sandbox

Developed by Stefano Morello and Zach Muhlbauer

---

## Curate Knowledge Collections — 2

### Workshop Agenda

- Confirm Workspace and Knowledge access

- Select source documents

- Create knowledge collections

- Attach collections to model cards

- Check source citations

- Choose procedures for skills

Before attending, confirm individual access, Sandbox sign-in, Workspace access, and Knowledge collection access.

---

## Curate Knowledge Collections — 3

### Review Custom Models

Open the custom model you used in Workshop 1. Attach documents and test whether the model can find and cite relevant passages.

Bring course materials, research papers, or other documents you know well enough to check.

Use [system-prompt examples](examples.html) if you need a prompt to begin.

---

## Curate Knowledge Collections — 4

### Open Workspace

![Current Workspace tabs and shared Create button](images/current/workspace-header.png)

Open Workspace and select Knowledge to create a collection.

Sign in after your Lab access is approved. Open **Workspace → Models** and find your card.

To create a new custom model, choose a base model and add a prompt from [System Prompt Examples](examples.html).

Request Workspace access from the CUNY AI Lab if the tab is unavailable.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Curate Knowledge Collections — 5

### Review Model Settings

![Current model editor showing base model, system prompt, and Knowledge](images/current/model-editor.png)

Review Base Model and System Prompt before attaching documents.

Review **Base Model (From)** and **System Prompt**. Start a fresh chat using the card selected inside the message box.

Ask a question that depends on your source material. Save the response before attaching the collection.

[Model configuration](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Curate Knowledge Collections — 6

### Knowledge Collections

A knowledge collection contains uploaded documents that a model can search when responding to questions.

Collections support PDFs, Markdown, and plain text. Attach a collection to a custom model under **Knowledge**.

[Knowledge Bases](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

[Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/)

---

## Curate Knowledge Collections — 7

### Create Knowledge Collections

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](images/current/knowledge-create.png)

Enter a collection name and description, set access, and select Create Knowledge.

- Open **Workspace → Knowledge → Create**.

- Name the collection and describe its contents and purpose.

- Keep it **Private** while building, then choose **Create Knowledge**.

[Create and manage collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curate Knowledge Collections — 8

### Check Citations

Ask a question with a verifiable answer in one of your documents.

### Course Example

What does the assignment require as evidence for the midterm essay?

### Research example

How does this methods section define the study population?

Check the answer against the original passage. A plausible summary alone does not show that retrieval worked.

---

## Curate Knowledge Collections — 9

### Select Documents

Choose documents with clear headings and readable text.

- Course syllabi, readings, or assignment instructions

- Research papers, methods, or annotated bibliographies

- Markdown, plain text, or well-formatted PDFs

Check scans and complex PDFs before uploading. Convert them to text if necessary.

[Document formats](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curate Knowledge Collections — 10

### Retrieve Source Passages

- Uploaded documents are divided into passages and indexed for search.

- Retrieval finds passages relevant to a question.

- The model uses those passages to generate a response.

Check that retrieved passages address your question and support the response.

[Open WebUI retrieval](https://docs.openwebui.com/features/workspace/knowledge/)

---

## Curate Knowledge Collections — 11

Example 1

### Organize Source Documents

---

## Curate Knowledge Collections — 12

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

---

## Curate Knowledge Collections — 13

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

---

## Curate Knowledge Collections — 14

Composition & Writing

### Support Revision

**Strong**

```text
Collection contents:

Course Context
• syllabus.pdf: schedule, learning objectives, policies
• revision-philosophy.txt: instructor notes on what revision means in this course

Assignment Materials (Essay 1: Rhetoric in Popular Media)
• essay-1-prompt.pdf: assignment instructions and requirements
• common-feedback.txt: patterns from past semesters (e.g., thesis too broad, evidence not analyzed)

Reference Materials
• mla-style-guide.pdf: citation and formatting conventions
• strong-intro-examples.txt: examples of effective introductions
• revision-checklist.pdf: the same checklist students use in peer review
```

---

## Curate Knowledge Collections — 15

Example 2

### Analyze Primary Sources

---

## Curate Knowledge Collections — 16

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

---

## Curate Knowledge Collections — 17

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

---

## Curate Knowledge Collections — 18

History

### Compare Primary Sources

**Strong**

```text
Collection contents:

Course Context
• syllabus.pdf: schedule, themes, learning objectives
• soaps-framework.txt: the analytical framework students use, with definitions and examples

Primary Sources (Reconstruction Unit)
• freedmens-bureau-report-1866.pdf: with metadata: author, date, document type, archive
• congressional-testimony-1871.pdf: with metadata
• source-context-notes.txt: brief historical context for each source (2-3 sentences each)

Reference Materials
• period-timeline.txt: key events 1865-1877 for contextualization questions
• common-analysis-errors.txt: patterns from past semesters (e.g., treating sources as neutral facts)
• chicago-citation-guide.pdf: citation format for history papers
```

---

## Curate Knowledge Collections — 19

Example 3

### Analyze Literary Texts

---

## Curate Knowledge Collections — 20

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

---

## Curate Knowledge Collections — 21

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

---

## Curate Knowledge Collections — 22

Literature & Cultural Studies

### Support Textual Analysis

**Strong**

```text
Collection contents:

Course Context
• syllabus.pdf: schedule, texts, learning objectives
• new-criticism-framework.txt: key concepts and terms for this unit (tension, irony, paradox, ambiguity, diction, imagery)

Assignment Materials (Close Reading Essay)
• close-reading-assignment.pdf: instructions and requirements
• annotated-passage-example.txt: model annotation showing how to move from observation to interpretation

Literary Texts (Current Unit)
• sonny-blues-baldwin.pdf: the primary text for this assignment
• passage-selections.txt: key passages the instructor has flagged for class discussion
```

---

## Curate Knowledge Collections — 23

### Compare Research Methods

Build a collection from research papers or methods you want to compare.

- Identify a question that requires consulting those sources.

- Ask the model to compare specific claims or methods.

- Check its citations against the uploaded documents.

[Knowledge collections for research](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curate Knowledge Collections — 24

### Organize Documents

Begin with a small collection so you can test how the model uses your materials.

- Name files so students or colleagues can identify them.

- Use headings to distinguish sections.

- Check whether the model retrieves the passages you need before adding more documents.

---

## Curate Knowledge Collections — 25

### Check Retrieval Problems

| Observation | Next check |
| --- | --- |
| No relevant source appears | Check processing, attachment, access, and the retrieval query. |
| The source is present but misread | Compare the answer with the full passage and revise instructions. |
| The answer invents a citation | Open the source and verify the quotation and location. |

Save the failed response before making one change.

---

## Curate Knowledge Collections — 26

### Build Knowledge Collections

Choose documents that explain your course or research project, define the task, and provide source material.

---

## Curate Knowledge Collections — 27

### Choose Reference Materials

Think about which type of course document you would add first

- **Course Context** Syllabus sections, weekly schedule

- **Assignment Materials** Instructions, feedback examples

- **Source Materials** Excerpted readings, primary sources

---

## Curate Knowledge Collections — 28

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

---

## Curate Knowledge Collections — 29

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

---

## Curate Knowledge Collections — 30

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

---

## Curate Knowledge Collections — 31

### Select Research Materials

Describe your research project and the sources you want the model to use.

Research context

Describe your question, scope, and method.

Instructions

Include a codebook, protocol, or criteria for comparing sources.

Sources

Identify the documents and passages you want to examine.

---

## Curate Knowledge Collections — 32

### Attach Knowledge Collections

- Open your collection and upload the first few documents. Wait for processing to finish.

- Check the extracted text against each source.

- Return to **Workspace → Models**, open your card, and select the collection under **Knowledge**.

- Choose **Save & Update**, then start a fresh chat with that card.

[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curate Knowledge Collections — 33

### Test Retrieval

- Ask a question answered by one source. Verify the answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask a question the collection cannot answer. Check whether the response states that limit.

Repeat the baseline question with the model and prompt unchanged. Record the collection version and passages retrieved with your judgment.

---

## Curate Knowledge Collections — 34

### Share Knowledge Collections

Share the knowledge collection with the people who will use the custom model.

- Use **Add Access** to grant users or groups **Read** access.

- Check access with someone you shared the model and collection with.

- Choose **Public** only for documents intended for all signed-in Sandbox users.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Curate Knowledge Collections — 35

### Prepare Skill Instructions

- Save source lists and retrieval tests

- Request Skills and Tools access

- Choose recurring teaching or research procedures

- Review [system-prompt examples](examples.html)

- Continue to [Skills & Tools](skills)


## Skills & Tools — 1

### Skills & Tools

Add tools and reusable instructions for teaching and research

CUNY AI Lab Sandbox

Developed by Stefano Morello and Zach Muhlbauer

---

## Skills & Tools — 2

### Workshop Agenda

- Confirm Skills and Tools access

- Choose recurring procedures

- Write skill instructions

- Attach skills to models

- Inspect tool calls and results

- Test models with skills and tools

Before attending, confirm individual access, Sandbox sign-in, and Skills and Tools access. Creating or editing resources also requires Workspace access. Knowledge access is needed only when your task uses a collection.

---

## Skills & Tools — 3

### Review Previous Work

Open your custom model and review its system prompt. Choose a procedure you use in teaching or research.

Write instructions for the procedure, attach the skill to your model, and test it.

Bring a knowledge collection if the procedure needs to search your documents.

---

## Skills & Tools — 4

### Choose Procedures

- For teaching, guide a student through a source one question at a time.

- For research, compare a claim with its source or apply a codebook to an excerpt.

- Define what a successful response would show before writing the skill.

The procedure should be specific enough that another person can inspect whether it was followed.

---

## Skills & Tools — 5

### Define Skills

Skills contain reusable Markdown instructions for tasks or procedures.

The model receives a skill’s name and description and can load its full instructions when needed.

Describe when the skill should be used and what steps it should follow.

[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

[Open WebUI Skills](https://docs.openwebui.com/features/workspace/skills/)

---

## Skills & Tools — 6

### Create Skills

![Current Skill editor showing name, ID, description, Access, and instructions](images/current/skill-editor.png)

Enter a name, description, and instructions, then select Save & Create.

- Open **Workspace → Skills → Create**.

- Enter a name, identifier, and description that explain when to use it.

- Write the instructions, review **Access**, and choose **Save & Create**.

[Create and attach a skill](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Skills & Tools — 7

### Attach Skills

- Open **Workspace → Models** and edit your model.

- Select the skill under **Skills**.

- Set **Function Calling** to **Native** under **Advanced Parameters**.

- Select **Save & Update** and test a request that uses the skill.

Use a model that supports tool calling.

[Attach skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Skills & Tools — 8

### Compare Responses

Try the same request before and after attaching the skill. Keep the base model, sources, and system prompt fixed.

- Did the model use the intended procedure?

- Did it stop at the planned point for a response?

- Did it preserve evidence and uncertainty?

---

## Skills & Tools — 9

### Enable Tools

![Current Integrations menu showing Tools, Skills, Web Search, and Code Interpreter](images/current/integrations.png)

Open Integrations beside the plus button to enable tools for this chat.

A tool runs an operation, such as a search, a calculation, or a query of a source collection.

Open **Integrations** beside the plus button for available chat capabilities. Attach reusable tools under **Tools** in the model editor.

Availability depends on account permissions, configuration, and model support.

[Enable tools in chat or on a model](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Skills & Tools — 10

### Tools & Skills

Skills

Instructions the model can load for a task or procedure.

Tools

Operations the model can call, such as web search, code execution, or database queries.

Test a request that needs the skill or tool. Check what the model used and whether its response is correct.

[Tools & Skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/)

---

## Skills & Tools — 11

Example 1

### Establish Stasis

Composition — Stasis Theory

---

## Skills & Tools — 12

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

---

## Skills & Tools — 13

Composition & Writing

### Revised Instructions

**Strong**

```text
Skill: Establishing Stasis for a Research Topic
When a student is developing or narrowing a research topic, follow this procedure:

Procedure:
1. Ask the student to state their topic in one sentence. Do not evaluate or refine it yet.
2. Conjecture: “What has happened or is happening that makes this worth investigating?” Wait for their answer. Use what they say to sharpen the next question.
3. Definition: Point to a key term in their response. “How are you defining [term]? What kind of problem is this — legal, ethical, empirical, cultural?” Wait.
4. Quality: “What’s at stake, and for whom? What makes this serious enough to argue about in an 8-page paper?” If their scope is too broad, ask them to name one specific population or context. Wait.
5. Policy: “What should be done, and by whom?” Help the student see whether their argument is making a factual claim, a definitional claim, a value judgment, or a policy proposal.
6. Ask: “Which of these four questions does your argument most need to answer?” Guide them toward a thesis grounded in that stasis.

Format:
Your topic: [student’s stated topic]

[One stasis question, tied to a specific phrase the student used]
[1–2 sentences explaining why this question matters for their project]
```

---

## Skills & Tools — 14

Example 2

### Examine Documents

History — The Sourcing Heuristic

---

## Skills & Tools — 15

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

---

## Skills & Tools — 16

History

### Revised Instructions

**Strong**

```text
Skill: Sourcing a Primary Document
When a student asks about or encounters a primary source from the course, follow this procedure:

Procedure:
1. Retrieve the document from the knowledge collection. Quote a key passage — do not paraphrase or summarize.
2. Present the passage in a block quote with its metadata (title, date, author) drawn from the uploaded file.
3. Ask: “Who created this document, and what was their position or stake?” Wait for the student’s answer.
4. After they respond, point to a specific phrase in the quoted passage that supports, complicates, or challenges their answer.
5. Ask: “When and where was this written? What was happening at that moment that shaped what the author could say?” Wait.
6. Ask: “Who was the intended audience? How does knowing that change what the document means?” Wait.
7. After all three sourcing moves, ask: “Given what you now know about the author, the moment, and the audience — what can this source tell us, and what can’t it?”

Format:
> [quoted passage from uploaded source]
— [Author], [Title], [Date]

[One sourcing question]
[1–2 sentences connecting the question to a specific phrase in the passage]
```

---

## Skills & Tools — 17

Example 3

### Analyze Images

Literature — Cinematic Mise-en-Scène

---

## Skills & Tools — 18

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

---

## Skills & Tools — 19

Literature & Cultural Studies

### Revised Instructions

**Strong**

```text
Skill: Reading Cinematic Images
When a student uploads a film still, photograph, or visual artifact — or asks about an image from the knowledge collection — follow this procedure:

Procedure:
1. Use an uploaded image only when the selected model can inspect images. If the visual is unavailable, ask the student to upload it or describe it. Do not assume text retrieval from a knowledge collection provides the original image.
2. Ask: “What do you notice first?” Let the student describe before you respond.
3. After their description, direct attention to one formal element they haven’t mentioned — composition, lighting, color, framing, depth of field, or gaze. Ask what it does.
4. Ask how that formal choice shapes the viewer’s experience. Move from what is in the frame to how the image is constructed.
5. Introduce context: ask the student to connect the visual choices to the cultural moment, genre, or argument of the work. If relevant context exists in the knowledge collection, quote it.
6. Guide them toward an interpretive claim: “Based on what you’ve observed, what argument is this image making?”

Framework: Description → Analysis → Interpretation
• Description: What is literally in the frame?
• Analysis: How do formal elements (light, angle, placement) create meaning?
• Interpretation: What claim can the student make, grounded in visual evidence?
```

---

## Skills & Tools — 20

### Write Skills

---

## Skills & Tools — 21

Structure

### Structure Skills

Use three parts to draft this skill.

- **Trigger** — When should this skill activate?

- **Procedure** — What steps does the model follow, in order?

- **Format** — What should the output look like?

---

## Skills & Tools — 22

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

---

## Skills & Tools — 23

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

---

## Skills & Tools — 24

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

---

## Skills & Tools — 25

Hands-On

### Draft Skills

Choose a teaching or research procedure and write steps that another person can inspect.

---

## Skills & Tools — 26

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

---

## Skills & Tools — 27

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

---

## Skills & Tools — 28

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

---

## Skills & Tools — 29

### Test Skills

Create the skill, attach it to your model, confirm native function calling, and save the card. Open a fresh chat with the card.

- Send a request that should trigger the skill.

- Reply once and check whether the procedure continues appropriately.

- Send an unrelated request and check whether the skill is applied unnecessarily.

Record the result before revising the trigger or a procedural step.

---

## Skills & Tools — 30

### Inspect Tool Results

With an available search tool, ask for the title and link of a source relevant to a narrow question. Open the returned page and verify the claim.

With an available code tool, use a small calculation whose answer you can check independently.

Look for the actual call and returned result. The sentence “I searched” or “I calculated” does not establish that a tool ran.

---

## Skills & Tools — 31

### Check Calculations

Run this calculation with Code Interpreter.

```text
Use Code Interpreter to calculate the median of [3, 8, 8, 12, 19]. Show the calculation and report whether the tool ran.
```

The expected median is **8**. Check the execution result and the final answer. If the tool is unavailable or fails, the response should report that.

---

## Skills & Tools — 32

### Record Test Results

| Record | Include |
| --- | --- |
| Configuration | Model, prompt, collection version, skill text, enabled tools. |
| Action | Input, skill loading, tool call, result, final response. |
| Judgment | Expected behavior, observed behavior, evidence, next revision. |

Before sharing, check that the people you share with can use the model and its collections, skills, and tools. Repeat relevant tests after a model or tool update.

---

## Skills & Tools — 33

### Repeat Tests

- Save prompts, sources, skills, and tool settings

- Compare expected and observed behavior

- Revise instructions from recorded failures

- Verify shared access with intended users

- Retest after model or tool updates

[Browse system-prompt examples](examples.html) · [Return to Compose System Prompts](.)
