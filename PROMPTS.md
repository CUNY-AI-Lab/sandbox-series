# Compose System Prompts

CUNY AI Lab Sandbox workshop. Generated from index.html; do not edit this mirror directly.

## Slide 1: Compose System Prompts

Workshop 1 of 3

### Compose System Prompts

Compare and configure models for teaching and research

CUNY AI Lab Sandbox

Developed by Stefano Morello and Zach Muhlbauer

---

## Slide 2: Workshop Roadmap

### Workshop Roadmap

- **Compose System Prompts** Configure model behavior with system prompts.

- **Curate Knowledge Collections** Upload documents so models can reference them.

- **Skills & Tools** Add web search, code execution, and reusable instructions.

[Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/)

---

## Slide 3: Workshop Agenda

### Workshop Agenda

- Request individual access and sign in

- Compare responses from small models

- Compare car-wash responses

- Revise in-chat system prompts

- Explore Workspace models

- Save prompts for reuse

Before attending, request individual access and sign into the Sandbox.

---

## Slide 4: Request Access

### Request Access

[ailab.gc.cuny.edu/request-access/](https://ailab.gc.cuny.edu/request-access/)

- Choose **My own access** and sign in with **CUNY Login**.

- Complete your details, select **CAIL Sandbox**, and submit the application.

- After approval, open [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu/) and select **Continue with CUNY Login**.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Slide 5: Select Models

### Select Models

![Current Sandbox new chat with the model selector inside the message box](images/current/chat-page.png)

Select the model name on the right inside the message box.

#### Supporting notes

Select the model name **on the right inside the message box**.

Type a request, send it, then ask a follow-up. Open **New Chat** when you want to begin with fresh conversation history.

[Quick Tour](https://ailab.gc.cuny.edu/sandbox-docs/quick-tour/)

---

## Slide 6: Chat Controls

### Chat Controls

Upload Files (+)

Attach images, PDFs, or documents.

Integrations

Choose tools and skills for this chat.

Message actions

Copy, edit, or regenerate a response. Open the three-dot menu for additional actions.

[Sandbox Basics](https://ailab.gc.cuny.edu/sandbox-docs/sandbox-basics/)

---

## Slide 7: Compare Models

### Compare Models

![Current model selector with search and the Compare toggle](images/current/model-selector.png)

Open the model selector, turn on Compare, and select two models.

#### Supporting notes

Open the model selector. Turn on **Compare**, then choose two available base models.

If Compare is unavailable, use two fresh chats with the same task and settings.

Switching models midway carries the conversation history forward. Use fresh chats for a clearer initial comparison.

---

## Slide 8: Who Was Late?

### Who Was Late?

The facilitator sends this question to two small models. Read both responses.

```text
The nurse yelled at the doctor because she was late. Who was late?
```

Use the same prompt and chat history for both models. Note which models you selected.

---

## Slide 9: Examine Assumptions

### Examine Assumptions

“She” could refer to either person. Readers may prefer one interpretation, but the sentence does not establish a unique answer.

- Does each model acknowledge the ambiguity?

- What assumption supports its answer?

- Does the explanation add information absent from the sentence?

Compare the evidence in the answers. A confident explanation can still rest on an unsupported assumption.

---

## Slide 10: Compare Recommendations

### Compare Recommendations

Use the same two-model comparison for this question.

```text
The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.
```

Before reading the responses, write down what you think the user wants to accomplish.

---

## Slide 11: Read Gemma’s Response

### Read Gemma’s Response

![Archived car-wash prompt and Gemma response saying to walk](images/showcase/car-wash-gemma.png)

GCDI showcase, May 2026. Gemma recommends walking.

#### Supporting notes

The response shown recommends walking. Read its recommendation against the purpose of the trip.

---

## Slide 12: Read Qwen’s Response

### Read Qwen’s Response

![Archived car-wash prompt and Qwen response saying to take the car](images/showcase/car-wash-qwen.png)

GCDI showcase, May 2026. Qwen recommends taking the car.

#### Supporting notes

This response recommends taking the car. These excerpts are discussion material; the source has inconsistent Qwen labels, so it cannot establish an exact model comparison.

---

## Slide 13: Try Model Comparison

### Try Model Comparison

- In a fresh chat, send the car-wash prompt to two available models. Save both responses.

- Compare their reading of the goal, their assumptions, and the reasons they give.

- Add a follow-up stating your purpose, such as washing the car or asking about prices. Does the recommendation change appropriately?

If the purpose is to wash the car, the car must get there. The original wording leaves the purpose unstated.

---

## Slide 14: Evaluate Responses

### Evaluate Responses

Compare how each model interprets the question and explains its recommendation.

- Which assumptions does each response make?

- Does either response invent information?

- How does each model respond when you clarify your purpose?

Save the responses with the prompt and model names so you can repeat the comparison.

---

## Slide 15: System Prompts

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

## Slide 16: Open Chat Controls

### Open Chat Controls

![Current chat Controls panel with its System Prompt field](images/current/chat-controls.png)

Enter instructions in the System Prompt field under Chat Controls.

#### Supporting notes

- Open a fresh chat with one of the models you compared.

- Select **Controls** at the top right.

- Enter the sample in **System Prompt** before sending the task.

Use the conversation’s Controls for this exercise. Personal defaults under Settings have a wider scope.

---

## Slide 17: Test System Prompts

### Test System Prompts

Keep one base model fixed. Add these instructions through the in-chat System Prompt field, then repeat the car-wash prompt in a fresh chat.

```text
Help the user examine a question before settling on an answer.

Identify the goal and the information stated in the question. Separate those facts from assumptions needed to answer it. If different assumptions would change the answer, explain the alternatives briefly or ask one focused question.

Give a concise answer that states its assumptions. Do not invent missing context. Revise the answer when the user adds relevant information.
```

The instructions address assumptions across tasks. They do not prescribe a car-wash answer.

---

## Slide 18: Compare Responses

### Compare Responses

- Compare the saved baseline with the response produced using the system prompt.

- Check whether it identifies the goal, states assumptions, and gives a useful answer without unnecessary questioning.

- Try the nurse question again. Does the instruction help with ambiguity in a different form?

Keep the model, optional features, and other defaults consistent. Record any differences you cannot control.

---

## Slide 19: Open Workspace

### Open Workspace

Open **Workspace → Models** after the facilitator confirms access.

Open the sample model and review its **Base Model** and **System Prompt**. Compare those instructions with the prompt you tested in chat.

Continue in chat if Workspace is unavailable.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Slide 20: Workspace Tabs

### Workspace Tabs

![Current Workspace header with Models, Knowledge, Prompts, Skills, Tools, and Create](images/current/workspace-header.png)

Select a Workspace tab, then choose Create.

#### Supporting notes

### Custom Models

Watch the facilitator open the prepared sample and locate Create.

### Knowledge and Tools

Knowledge adds sources. Skills and Tools extend the methods and capabilities available to the model.

---

## Slide 21: Model Configuration

### Model Configuration

![Current model creation form showing Name, Base Model, and System Prompt](images/current/model-editor.png)

Choose a name and base model, then enter a system prompt.

#### Supporting notes

- **Name** what students will recognize.

- **Base Model** what generates the responses.

- **System Prompt** how you want it to respond.

A custom model combines these choices. Creating it does not train a new base model.

[The model editor](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Slide 22: Create Custom Models

### Create Custom Models

Custom models combine a base model with instructions, documents, and tools.

- Enter a name and description that students or colleagues will recognize.

- Select a base model and add your tested system prompt.

- Add prompt suggestions for tasks the model should support.

Students select the custom model to use the instructions and resources you configured.

[Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Slide 23: Structure System Prompts

Examples

### Structure System Prompts

---

## Slide 24: Teach Composition

Example 1

### Teach Composition

---

## Slide 25: Vague Prompts

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

## Slide 26: Add Specifics

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

## Slide 27: Guide Revision

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

Scroll to read the full prompt. The complete text is also in the workshop handout.

---

## Slide 28: Analyze Primary Sources

Example 2

### Analyze Primary Sources

---

## Slide 29: Vague Prompts

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

## Slide 30: Add Specifics

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

## Slide 31: Analyze Primary Sources

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

Scroll to read the full prompt. The complete text is also in the workshop handout.

---

## Slide 32: Analyze Literary Texts

Example 3

### Analyze Literary Texts

---

## Slide 33: Vague Prompts

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

## Slide 34: Add Specifics

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

## Slide 35: Analyze Literary Texts

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

Scroll to read the full prompt. The complete text is also in the workshop handout.

---

## Slide 36: Adapt Research Prompts

### Adapt Research Prompts

Choose a bounded task such as comparing article abstracts, checking a coding decision, or documenting a method.

- State the research question and material the model may use.

- Specify the procedure and what counts as evidence.

- Require uncertainty and competing interpretations to remain visible.

Keep the source material, prompt version, output, and your judgment together. The researcher remains responsible for interpretation.

---

## Slide 37: Draft System Prompts

Drafting exercise

### Draft System Prompts

---

## Slide 38: Define Prompt Components

Structure

### Define Prompt Components

Each system prompt is built from modular components. We’ll draft yours one piece at a time.

- **Context & Problem** — What course, what students, what learning challenge?

- **Procedure** — What steps should the tool follow?

- **Constraints** — What should it refuse to do, and how should it redirect?

- **Tone** — What register and affect should it use with your students?

- **Output Format** — How should it structure its responses?

---

## Slide 39: Define Context

Component 1

### Define Context

Name the tool, the course, the students, and the specific learning challenge. Everything else follows from this.

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

## Slide 40: Write Procedures

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

## Slide 41: Set Constraints

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

## Slide 42: Set Tone

Component 4

### Set Tone

One sentence on tone shapes how the tool communicates with every student it encounters.

- What register fits your students?

- Should it feel warm, direct, encouraging?

- Are there phrases that model the right affect?

```text
Tone: [Adjective and adjective]. Use phrases like "[example phrase]" and "[example phrase]."
```

**Your turn** Copy this template and fill in the placeholders. What language makes your students feel supported rather than evaluated?

---

## Slide 43: Specify Format

Component 5

### Specify Format

Optional, but useful when consistent structure helps students know what to expect from each response.

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

## Slide 44: Refine Instructions

Refine

### Refine Instructions

---

## Slide 45: Extend Instructions

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

## Slide 46: Review Common Problems

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

## Slide 47: Save Prompts

### Save Prompts

- Save your prompt text with the model name and responses it produced.

- Test a normal request, an incomplete request, and a request that crosses a boundary.

- Revise one instruction and repeat the test in a fresh chat.

With Workspace access confirmed, save the tested prompt in a private model card. Choose the base model, review Access, and use Save & Create. Bring that configuration to Workshop 2.

---

## Slide 48: Share Custom Models

### Share Custom Models

- Open **Access → Add Access** and select users or a course group.

- Grant **Read** access to people who will use the model and **Write** access to people who will edit it.

- Check that participants can use the base model and any attached collections, skills, or tools.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Slide 49: Record Comparisons

### Record Comparisons

Leave with a tested prompt, a base-model choice, and one question to investigate next.

| Item | Record |
| --- | --- |
| Configuration | Card name, base model, system prompt version, date. |
| Test | User request, enabled features, saved response. |
| Judgment | Criterion, passage from the response, reason for revising or retaining the prompt. |

Use public or approved material. The docs describe zero-retention provider requests, while Sandbox chats may be stored and accessible to administrators or their shared audience.

[Privacy and chat history](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/) · [Facilitator outline and worksheet](WORKSHOP.md)

---

## Slide 50: Prepare Source Documents

### Prepare Source Documents

- Save prompt versions and comparison notes

- Request Workspace and Knowledge collection access

- Select public or approved source documents

- Review [system-prompt examples](examples.html)

- Continue to [Curate Knowledge Collections](knowledge/)
