![CUNY AI Lab](images/logo-horizontal.png)

### Curating Knowledge Collections

A Workshop for the [CUNY AI Lab Sandbox](https://chat.ailab.gc.cuny.edu)

March 23, 2026

Developed by Stefano Morello and Zach Muhlbauer

---

Workshop Series

### Three Weeks, Three Skills

March 16 (Last Week)

### [Composing System Prompts ✓](https://cuny-ai-lab.github.io/system-prompting)

Learned how system prompts help orchestrate and constrain AI models to address course goals

March 23 (This Week)

### Curating Knowledge Collections

Upload syllabi, readings, and relevant sources to ground AI models in course materials

March 30

### Customizing Skills & Tools

Build specialized skills, tools, and workflows tailored to your courses

---

Getting Started

### Sign In and Navigate to Workspace

Before we begin, make sure you can access the CUNY AI Lab Sandbox.

### 1. Go to [chat.ailab.gc.cuny.edu](https://chat.ailab.gc.cuny.edu)

Sign in with your CUNY account. If you don’t have access yet, let us know and we’ll get you set up.

### 2. Open Workspace

Look for **Workspace** in the top left, three rows below **New Chat**. Click it. This is where you’ll build your model card and knowledge collection.

**Next:** Once you’re signed in and can see the Workspace menu, you’re ready to set up your model card on the next slide.

![Open WebUI sidebar showing Workspace menu item](images/slide3-workspace-create.png)

**Workspace → Models**
Navigate to Workspace in the sidebar, then open the Models tab.

![Workspace Models page listing custom models in the Sandbox](images/slide3-model-basics.png)

**Models List**
Click **+ New Model** to create one, or open an existing model card.

---

Before We Start

### Set Up Your Model Card

Knowledge collections attach to a model card in **Workspace → Models**. After you build your collection, complete these steps to bring everything together.

### 1. Name the model card

Give it a descriptive name tied to your course, for example *ENGL 101 Writing Scaffold* or *History 202 Source Analysis Tool*.

### 2. Select a base model

Choose a base model from the Sandbox (e.g., GLM-5, GPT-OSS-120b, or Kimi-k2.5). This is the underlying model your custom configuration will run on.

### 3. Add your system prompt

Find the **System Prompt** field under Model Params and paste the prompt you wrote last week.

### 4. Save your work

Click the **Save** button. Your model card is now ready for a knowledge collection.

![Model card editor showing fields for name, base model, system prompt, and knowledge collection](images/slide3-system-prompt.png)

**Inside the Model Card**
Name your model, select a base model, paste your system prompt, and save. The **Knowledge** section below is where today’s collection will attach.

**Keep this tab open.** You will return to this model card at the end of today’s exercise to attach the knowledge collection you build.

---

Dry Run

### Test Your Model in Chat

Your model is saved. Now test it to make sure it responds as expected before attaching a knowledge collection.

### 1. Click New Chat

Go back to the chat interface. Click **New Chat** in the top left to start a fresh conversation.

### 2. Toggle the model selector

At the top of the chat window, you’ll see the model name. Click the dropdown arrow next to it.

### 3. Select your model

Find your newly created model (e.g., **ENGL 101 Writing Scaffold**) in the dropdown list and select it.

### 4. Send a test message

Type a simple message related to your course. Send it and observe the response.

![Open WebUI chat interface showing the model selector dropdown with a custom model selected, and the message input field](images/slide5.png)

**Test Your Model**
Click **New Chat** (1), select your model from the dropdown (2-3), and type a test message (4).

**Look for:** Does your custom model respond as expected? How has your system prompt shaped its output?

---

Part I

### Knowledge Collections

What they are, where they live, and how they work

---

The Basics

### What Is a Knowledge Collection?

A **knowledge collection** is a set of documents you upload to ground an AI model in your course materials. The model retrieves relevant passages from these documents when responding.

Think of it as a **reference shelf** for your custom AI model: the sources it draws on, the assignments it references, and the disciplinary context that shapes its responses.

*Next we’ll show you where to find knowledge collections in the Sandbox and how to curate and use them with pedagogical intent.*

What you build

Hidden

System Prompt

“You are a writing scaffold…”

+

New

Knowledge Collection

syllabus.pdf, prompt.pdf…

student never sees above

👤  Student   “What does the assignment say about evidence?”

🤖

AI Model

Retrieves passages from uploaded course materials

🤖  Response   “The assignment asks for at least three sources cited with specific page numbers. Let’s look at what you have so far.”

What the student sees

---

Workspace

### Where to Find Knowledge Collections

Knowledge collections and model cards both live in the **Workspace** menu. Here’s how they connect:

### Workspace → Knowledge

Where collections are created, named, and populated with course documents.

### Workspace → Models

Where collections are attached to a model card via the **Knowledge** field, giving the model access to your materials.

**Key distinction:** Your system prompt defines how the model responds. The knowledge collection provides the source material it draws on. Both are configured in the same model card.

![Workspace Knowledge tab showing existing collections and the New Knowledge button](images/slide4-a.png)

**Workspace → Knowledge**
Click **+ New Knowledge** to create a collection.

![Create a knowledge base form with name, description, and privacy settings](images/slide4-b.png)

**Name and Describe**
Give your collection a name, describe its contents, and set access. Click **Create Knowledge** when ready.

![Workspace Models page listing custom models](images/slide4-c.png)

**Workspace → Models**
Open your model card to attach the collection.

![Model card editor with Knowledge section highlighted showing Select Knowledge and Upload Files](images/slide4-d.png)

**Knowledge Field**
Click **Select Knowledge** to attach your collection to the model card.

---

Why Bother?

### Why Knowledge Collections Matter

If you create a custom model that acts as a course assistant, a student might ask: **“What should I focus on for the midterm essay?”**

### Without Knowledge Collection

“For a midterm essay, you should generally focus on your thesis statement, use evidence from your readings, and structure your argument clearly. Make sure to address counterarguments.”

Generic advice. No connection to the assignment or the course readings.

### With Knowledge Collection

“Based on the assignment prompt, your essay should analyze one primary source from the Reconstruction unit using the SOAPS framework we practiced. The prompt emphasizes evidence and sourcing. Which document are you considering?”

Grounded in the actual assignment and course methodology.

---

Building Materials

### What Can You Upload?

Uploaded files ground AI models in context and help shape their responses. These documents are stored on CUNY’s self-hosted servers and made private by default.

### Syllabi

Course schedule, learning objectives, policies, and expectations

### Assignment Prompts

Instructions, requirements, and criteria for each assignment

### Rubrics

Evaluation criteria so the model can reference specific expectations

### Course Readings

Primary sources, articles, chapters, and excerpts students are working with

### Lecture Notes

Key concepts, frameworks, and terminology from your lectures

### Style Guides

Citation formats, disciplinary conventions, writing guidelines

### Sample Work

Exemplars that model the kinds of work you expect

### Data Sets

Spreadsheets, CSV files, or structured data students analyze in labs or projects

### Glossaries

Discipline-specific terminology, definitions, and key concepts for the course

### Problem Sets

Exercises, practice questions, or worked examples with solutions

### Lab Protocols

Step-by-step procedures, safety guidelines, and equipment instructions

### Case Studies

Real-world scenarios, historical cases, or clinical examples used in coursework

---

Under the Hood   Retrieval-Augmented Generation

### How Your Documents Reach the Model

When a student asks a question, the system doesn’t feed the *entire* collection to the model. It searches for the most relevant passages and uses them as the basis for its response.

- **Chunking:** Your files are split into smaller passages when uploaded

- **Matching:** Questions are matched against those chunks

- **Injection:** Closest matches appended to model’s context window

- **Response:** Model generates output grounded in retrieved passages

**Implication:** Short, focused documents with clear headings retrieve better than long, unstructured files. In other words, the way you organize your materials matters.

👤

Student Question

“What does the assignment say about citations?”

🔍

Search Collection

Finds relevant passages from your files

🤖

AI Model + Retrieved Context

System prompt + relevant passages + student message

✅

Grounded Response

Answer references your actual course materials

---

Part II: Example 1

### What Makes an Effective Knowledge Collection?

Starting with Composition & Writing

---

Composition & Writing

### The Bare Minimum

```text
Collection contents:
• syllabus.pdf (14 pages, full course syllabus)
```

### What goes wrong?

- One large document retrieves poorly: retrieved passages are often irrelevant

- No assignment context for the revision task

- No readings or reference materials for the model to draw on

---

Composition & Writing

### Getting Warmer

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

Composition & Writing

### A Collection That Grounds Revision

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

Example 2

### Primary Source Analysis

---

History

### The Bare Minimum

```text
Collection contents:
• textbook-chapter-12.pdf (42 pages)
```

### What goes wrong?

- A full textbook chapter is too long and too general: retrieved passages are often irrelevant

- No primary sources for the model to help students analyze

- No framework like SOAPS for the model to scaffold source analysis

---

History

### Getting Warmer

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

History

### A Collection That Fosters Historical Thinking

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

Example 3

### Close Reading & Literary Analysis

---

Literature & Cultural Studies

### The Bare Minimum

```text
Collection contents:
• course-reader.pdf (180 pages, all readings for the semester)
```

### What goes wrong?

- A 180-page file retrieves unpredictably: the model might pull from the wrong text entirely

- No assignment context or close-reading framework

- No separation between literary texts and critical essays

---

Literature & Cultural Studies

### Getting Warmer

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

Literature & Cultural Studies

### A Collection That Fosters Close Reading

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

Part III

### Curating for
Retrieval Quality

Tips for curating collections, and common pitfalls to avoid

---

### Curation Best Practices

### One Document, One Purpose

Upload separate files; focused documents retrieve better than omnibus ones

### Add Metadata and Headings

Titles, authors, dates, and section headings serve as retrieval anchors

### Supply What’s Not in the Documents

Include meta documents like “common-feedback.txt” that signpost how to use sources in the collection

### Update Per Unit

Swap course materials as the semester progresses; up-to-date collections outperform semester-wide ones

---

Watch Out

### Common Pitfalls

### Dumping Everything In

Uploading every reading dilutes retrieval; start small and add materials as you test

### One Giant PDF

A 200-page course reader retrieves unpredictably; short, well-labeled documents work far better

### Forgetting the System Prompt

Without explicit instructions for drawing on the collection, it is just a pile of documents

### Assuming Full Coverage

Only retrieved passages appear in each response; if something is critical, give it its own file

---

Part IV

### Building Your
Knowledge Collection

Three types of references to consider, then steps for how to create, curate, and use your first collection.

---

### Types of Reference Material

Think about which type of course document you would add first

- **Course Context:** Syllabus sections, weekly schedule

- **Assignment Materials:** Instructions, feedback examples

- **Source Materials:** Excerpted readings, primary sources

---

Type 1

### Course Context

These documents give the model a picture of your course: its goals, structure, and the methods students are expected to use.

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

**Consider:** Is there a framework or methodology central to your course? If so, a short document (1-2 pages) explaining it in the terms you use with students could be a strong addition.

---

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

**Consider:** Which assignment stands to benefit? Try curating assignment instructions alongside a shortlist of common feedback patterns for starters.

---

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

**Consider:** Which readings or sources are students working with right now? Individual files retrieve better than a single combined PDF.

---

Putting It Together

### Create Your Collection

Now create the collection you’ve been thinking about.

### 1. Go to Workspace → Knowledge

Click **+ New Knowledge** to start a new collection.

### 2. Name and describe it

Give it a clear name tied to your course and a short description of what it contains.

### 3. Upload your first file

Start with the document type that caught your eye - be it course context, assignment materials, or source materials.

![Workspace Knowledge tab showing collections and New Knowledge button](images/slide4-a.png)

**Workspace → Knowledge**
Click **+ New Knowledge** to create a collection.

![Create a knowledge base form with name, description, and privacy settings](images/slide4-b.png)

**Name and Describe**
Give your collection a name and set access to private.

---

Final Step

### Attach Your Collection

Connect your collection to the model card you set up earlier.

### 1. Return to your model card

Go to **Workspace → Models** and open the model card you created at the start of today’s session.

### 2. Attach the collection

Find the **Knowledge** field and click **Select Knowledge**. Choose the collection you just created.

### 3. Save and test

Save the model card, open a new chat with your model, and ask a question only answerable from your collection.

![Workspace Models page listing custom models](images/slide4-c.png)

**Workspace → Models**
Open the model card you created earlier.

![Model card editor with Knowledge section highlighted showing Select Knowledge and Upload Files](images/slide4-d.png)

**Attach Your Collection**
Click **Select Knowledge** to connect your collection to the model.

---

Coming Up

### The Road Ahead

March 16

### System Prompts ✓

Configured how the model responds and scaffolds learning

March 23 (Today)

### Knowledge Collections ✓

Grounded the model in your course materials so it can reference real documents

March 30 (Next Week)

### Skills & Tools

Build specialized skills, tools, and workflows tailored to your courses

Each workshop builds on the last. The system prompt you wrote last week now drives a model grounded in the knowledge collection you built today. Next week, you’ll extend it with custom skills and tools.

[ailab.gc.cuny.edu](https://ailab.gc.cuny.edu)
