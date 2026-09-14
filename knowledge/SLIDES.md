# Curating Knowledge Collections

Generated from index.html. Screenshot instructions appear in Notes during presentation.

## Curating Knowledge Collections — 1

### Curating Knowledge Collections

Selecting and testing sources for teaching and research

CUNY AI Lab Sandbox

Developed by Stefano Morello and Zach Muhlbauer

---

## Curating Knowledge Collections — 2

### Curate and check evidence

- Confirm Workspace and Knowledge access

- Select source documents

- Create knowledge collections

- Attach collections to model cards

- Check retrieved evidence

- Prepare sources for procedural tasks

Require individual access and Sandbox sign-in from Workshop 1, plus Workspace and Knowledge collection access.

---

## Curating Knowledge Collections — 3

### Continue with your configuration

Bring the card and prompt from Composing System Prompts. Today you will add a small collection of sources and examine what the model retrieves.

A teaching project might use an assignment and readings. A research project might use a method, a codebook, and a few source documents.

Keep your baseline response so you can compare the effect of adding those sources.

---

## Curating Knowledge Collections — 4

### Confirm access and open Workspace

![Current Workspace tabs and shared Create button](../images/current/workspace-header.png)

Select Models to edit the configuration, or Knowledge to create a collection.

#### Supporting notes

Sign in after your Lab access is approved. Open **Workspace → Models** and find your card.

If you are joining here, use the sample prompt from the first workshop and choose a base model you can test.

Workspace authoring access is arranged separately from ordinary chat access.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Curating Knowledge Collections — 5

### Keep the model and prompt fixed

![Current model editor showing base model, system prompt, and Knowledge](../images/current/model-editor.png)

Knowledge attaches in the same editor as the base model and system prompt.

#### Supporting notes

Review **Base Model (From)** and **System Prompt**. Start a fresh chat using the card selected inside the message box.

Ask a question that depends on your source material. Save the response before attaching the collection.

[Model configuration](https://ailab.gc.cuny.edu/sandbox-docs/models/)

---

## Curating Knowledge Collections — 6

### What is a knowledge collection?

A knowledge collection holds documents that the Sandbox can retrieve for a model to use as context.

Your system prompt describes how to work with evidence. The collection makes selected source material available to that process.

Retrieval does not guarantee that the right passage will be found or that the answer will interpret it accurately.

[Knowledge Bases](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating Knowledge Collections — 7

### Create a collection

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../images/current/knowledge-create.png)

Blank form captured in Firefox. No collection was created for this screenshot.

#### Supporting notes

- Open **Workspace → Knowledge → Create**.

- Name the collection and describe its contents and purpose.

- Keep it **Private** while building, then choose **Create Knowledge**.

[Create and manage collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating Knowledge Collections — 8

### What changes when a source is available?

Ask a question with a verifiable answer in one of your documents.

### Teaching example

What does the assignment require as evidence for the midterm essay?

### Research example

How does this methods section define the study population?

Check the answer against the original passage. A plausible summary alone does not show that retrieval worked.

---

## Curating Knowledge Collections — 9

### Choose material you can inspect

Start with a few readable PDFs, Markdown files, or plain-text documents. Use material you are permitted to process and share.

- Include titles, authors, dates, and section headings.

- Check extracted text, especially scans and multi-column PDFs.

- Keep a source copy so quotations and page references can be checked.

Uploading a dataset as text does not perform a reliable numerical analysis. Use a suitable tool and verify its computation when the task requires it.

---

## Curating Knowledge Collections — 10

### How documents reach the model

- The Sandbox extracts text and divides it into passages.

- Retrieval selects passages relevant to a question or search.

- The selected passages become context for a response.

- You check the response against the cited source.

The configuration may use automatic retrieval or a native knowledge tool. Inspect the actual retrieval or tool result rather than assuming every file was read.

[Retrieval and indexing](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating Knowledge Collections — 11

Example 1

### What Makes an Effective Knowledge Collection?

Starting with Composition & Writing

---

## Curating Knowledge Collections — 12

Composition & Writing

### The Bare Minimum

**Weak**

```text
Collection contents:
• syllabus.pdf (14 pages, full course syllabus)
```

### What goes wrong?

- The syllabus may not contain the evidence needed for a revision question. Check which passages are retrieved.

- No assignment context for the revision task

- No readings or reference materials for the model to draw on

---

## Curating Knowledge Collections — 13

Composition & Writing

### Getting Warmer

**Getting There**

```text
Collection contents:
• syllabus.pdf
• essay-1-prompt.pdf
• mla-style-guide.pdf
```

### What improved?

- Separate documents let the model find what it needs

- Assignment prompt gives the model context for the revision task

- Style guide helps with formatting questions

### What's still missing?

- No course readings for the model to reference during analysis

- No common feedback patterns to guide revision

- No instructor notes on what substantive revision looks like in this course

---

## Curating Knowledge Collections — 14

Composition & Writing

### A Collection That Grounds Revision

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

## Curating Knowledge Collections — 15

Example 2

### Primary Source Analysis

---

## Curating Knowledge Collections — 16

History

### The Bare Minimum

**Weak**

```text
Collection contents:
• textbook-chapter-12.pdf (42 pages)
```

### What goes wrong?

- A general textbook chapter may not answer a question about a particular primary source.

- No primary sources for the model to help students analyze

- No framework like SOAPS for the model to scaffold source analysis

---

## Curating Knowledge Collections — 17

History

### Getting Warmer

**Getting There**

```text
Collection contents:
• syllabus.pdf
• source-analysis-assignment.pdf
• primary-source-1.pdf (Freedmen's Bureau report, 1866)
• primary-source-2.pdf (Congressional testimony, 1871)
```

### What improved?

- Includes actual primary sources students are working with

- Assignment prompt gives the model task-specific context

- Documents are separate and focused

### What's still missing?

- No contextual background for the model to draw on when students ask about the period

- No SOAPS framework or equivalent to guide source analysis

- No source metadata (author, date, document type) to support sourcing questions

---

## Curating Knowledge Collections — 18

History

### A Collection for Historical Inquiry

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

## Curating Knowledge Collections — 19

Example 3

### Close Reading & Literary Analysis

---

## Curating Knowledge Collections — 20

Literature & Cultural Studies

### The Bare Minimum

**Weak**

```text
Collection contents:
• course-reader.pdf (180 pages, all readings for the semester)
```

### What goes wrong?

- An omnibus reader can make it harder to identify the relevant text. Check whether retrieval selects the intended source.

- No assignment context or close-reading framework

- No separation between literary texts and critical essays

---

## Curating Knowledge Collections — 21

Literature & Cultural Studies

### Getting Warmer

**Getting There**

```text
Collection contents:
• syllabus.pdf
• close-reading-assignment.pdf
• sonny-blues-baldwin.pdf
• new-criticism-overview.pdf
```

### What improved?

- Individual literary text rather than an omnibus reader

- Assignment prompt provides task-specific context

- Critical framework document gives the model methodological grounding

### What's still missing?

- No annotated examples showing how to move from observation to interpretation

- No key terms for the current unit (e.g., tension, irony, ambiguity)

- No instructor notes on what close reading looks like in this course

---

## Curating Knowledge Collections — 22

Literature & Cultural Studies

### A Collection for Close Reading

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

## Curating Knowledge Collections — 23

### A research collection

For a small qualitative coding exercise, begin with a codebook, a methods note, and a few public or approved excerpts.

- Keep definitions and exclusion criteria with the codebook.

- Identify each excerpt and preserve enough context to interpret it.

- Record competing codes and the evidence for each judgment.

Test whether the model distinguishes source language from its own interpretation. Compare its suggestion with your independent reading.

---

## Curating Knowledge Collections — 24

### Curate around the task

Begin with a small set of sources you know well. Add documents when a test reveals a specific gap.

- Use descriptive names and headings, then inspect retrieval.

- Keep versions visible when a syllabus, protocol, or codebook changes.

- Add notes that explain how the sources relate to the task.

Focused files can make a collection easier to maintain. Their length alone does not establish retrieval quality.

---

## Curating Knowledge Collections — 25

### Diagnose a weak answer

| Observation | Next check |
| --- | --- |
| No relevant source appears | Check processing, attachment, access, and the retrieval query. |
| The source is present but misread | Compare the answer with the full passage and revise instructions. |
| The answer invents a citation | Open the source and verify the quotation and location. |

Save the failed response before making one change.

---

## Curating Knowledge Collections — 26

Part IV

### Building Your
Knowledge Collection

Three types of references to consider, then steps for how to create, curate, and use your first collection.

---

## Curating Knowledge Collections — 27

### Types of Reference Material

Think about which type of course document you would add first

- **Course Context** Syllabus sections, weekly schedule

- **Assignment Materials** Instructions, feedback examples

- **Source Materials** Excerpted readings, primary sources

---

## Curating Knowledge Collections — 28

Type 1

### Course Context

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

## Curating Knowledge Collections — 29

Type 2

### Assignment Materials

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

## Curating Knowledge Collections — 30

Type 3

### Source Materials

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

## Curating Knowledge Collections — 31

### Use the same structure for research

The preceding templates use course materials. For a research task, substitute the following documents.

Project context

Research question, scope, method, and definitions.

Task criteria

Codebook, inclusion criteria, or comparison procedure.

Sources

Public or approved excerpts with stable identifiers and provenance.

---

## Curating Knowledge Collections — 32

### Upload, inspect, and attach

- Open your collection and upload the first few documents. Wait for processing to finish.

- Check the extracted text against each source.

- Return to **Workspace → Models**, open your card, and select the collection under **Knowledge**.

- Choose **Save & Update**, then start a fresh chat with that card.

[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating Knowledge Collections — 33

### Test evidence and absence

- Ask a question answered by one source. Verify the answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask a question the collection cannot answer. Check whether the response states that limit.

Repeat the baseline question with the model and prompt unchanged. Record the collection version and passages retrieved with your judgment.

---

## Curating Knowledge Collections — 34

### Share the collection deliberately

Check access to the card, base model, and collection with an ordinary participant account.

Give the intended group read access when the materials are ready. Public access, where available, means signed-in Sandbox users.

Retrieved passages enter the model request and can appear in responses. Provider retention settings do not make the source confidential from the people who can use or administer the chat.

[Sharing and permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Curating Knowledge Collections — 35

### Prepare for Skills & Tools

- Save source lists and retrieval tests

- Request Skills and Tools access

- Choose recurring teaching or research procedures

- Review [system-prompt examples](../examples.html)

- Continue to [Customizing Skills & Tools](../skills/)
