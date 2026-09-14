# Curate Knowledge Collections

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

- Attach collections to custom models

- Check source citations

- Choose procedures for skills

Before attending, confirm individual access, Sandbox sign-in, Workspace access, and Knowledge collection access.

---

## Curate Knowledge Collections — 3

### Review Custom Models

Open your custom model from Workshop 1. Attach documents and test whether it can find and cite relevant passages.

Bring course materials, research papers, or other documents you know well enough to check.

Use [system-prompt examples](../examples.html) if you need a prompt to begin.

---

## Curate Knowledge Collections — 4

### Open Workspace

![Current Workspace tabs and shared Create button](../images/current/workspace-header.png)

Open Workspace and select Knowledge to create a collection.

Sign in after your Lab access is approved. Open **Workspace → Models** and find your custom model.

To create a new custom model, choose a base model and add a prompt from [System Prompt Examples](../examples.html).

Request Workspace access from CUNY AI Lab if Workspace is unavailable.

[Access and sign-in](https://ailab.gc.cuny.edu/sandbox-docs/getting-started/)

---

## Curate Knowledge Collections — 5

### Review Model Settings

![Current model editor showing base model, system prompt, and Knowledge](../images/current/model-editor.png)

Review Base Model and System Prompt before attaching documents.

Review **Base Model (From)** and **System Prompt**. Start a new chat. Select your custom model inside message box.

Ask a question about your source material. Save this response before attaching documents.

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

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../images/current/knowledge-create.png)

Enter a collection name and description, set access, and select Create Knowledge.

- Open **Workspace → Knowledge → Create**.

- Name your collection and describe its contents and purpose.

- Keep it **Private** while building, then choose **Create Knowledge**.

[Create and manage collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curate Knowledge Collections — 8

### Check Citations

Ask a question with a verifiable answer in one of your documents.

### Course Example

What evidence does this assignment require for our midterm essay?

### Research example

How does this methods section define who was studied?

Check each answer against its source passage.

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

- Your model uses retrieved passages to generate a response.

Check whether retrieved passages address your question and support claims in each response.

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

- A syllabus may not explain how to revise an essay. Check which passages are retrieved.

- No assignment instructions for revision

- No readings or reference materials to consult

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

- Separate documents distinguish individual sources

- Assignment instructions describe what revision requires

- Style guide helps with formatting questions

### Add Detail

- No course readings to reference during analysis

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

- No primary sources for students to analyze

- No framework like SOAPS to guide source analysis

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

- Assignment instructions explain what students should do

- Documents are separate and focused

### Add Detail

- No historical context for questions about this period

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

- An omnibus reader can make individual texts harder to identify. Check whether retrieval selects relevant passages.

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

- A document explains how to use a critical framework

### Add Detail

- No annotated examples showing how to move from observation to interpretation

- No key terms for this unit (e.g., tension, irony, ambiguity)

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

- Ask your model to compare specific claims or methods.

- Check its citations against your uploaded documents.

[Knowledge collections for research](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curate Knowledge Collections — 24

### Organize Documents

Begin with a few documents and test how your model uses them.

- Name files so students or colleagues can identify them.

- Use headings to distinguish sections.

- Check whether your model retrieves relevant passages before adding more documents.

---

## Curate Knowledge Collections — 25

### Check Retrieval Problems

| Observation | Next check |
| --- | --- |
| No relevant source appears | Check whether files finished processing, are attached, and are accessible. Review your search query. |
| A source is present but misread | Read cited passages in full and revise instructions. |
| A response invents a citation | Open cited documents and verify quotations and page numbers. |

Save unsuccessful responses before revising anything.

---

## Curate Knowledge Collections — 26

### Build Knowledge Collections

Choose documents that explain your course or research project and describe what you want to examine.

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

---

## Curate Knowledge Collections — 29

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

---

## Curate Knowledge Collections — 30

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

---

## Curate Knowledge Collections — 31

### Select Research Materials

Describe your research project and identify sources your model should use.

Research context

Describe your question, scope, and method.

Instructions

Include a codebook, protocol, or criteria for comparing sources.

Sources

Identify documents and passages you want to examine.

---

## Curate Knowledge Collections — 32

### Attach Knowledge Collections

- Open your collection and upload a few documents. Wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your custom model, and select your collection under **Knowledge**.

- Choose **Save & Update**, then start a new chat with your custom model.

[Upload and attach source material](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curate Knowledge Collections — 33

### Test Retrieval

- Ask a question answered by one source. Verify each answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask about something absent from your documents. Check whether your model acknowledges missing information.

Repeat your first question without changing models or system prompts. Record which documents you used, which passages were retrieved, and whether those passages support your model’s response.

---

## Curate Knowledge Collections — 34

### Share Knowledge Collections

Share your collection with people who will use your custom model.

- Use **Add Access** to grant users or groups **Read** access.

- Ask someone you shared with to check access to your model and collection.

- Choose **Public** only for documents intended for all signed-in Sandbox users.

[Roles & Permissions](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Curate Knowledge Collections — 35

### Prepare Skill Instructions

- Save source lists and retrieval tests

- Request Skills and Tools access

- Choose recurring teaching or research procedures

- Review [system-prompt examples](../examples.html)

- Continue to [Skills & Tools](../skills/)
