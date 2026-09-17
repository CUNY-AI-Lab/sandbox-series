# Curating knowledge collections

## Curating knowledge collections — 1

### Curating knowledge collections

Upload documents for models to reference in teaching and research

CUNY AI Lab Sandbox

Developed by Zach Muhlbauer

---

## Curating knowledge collections — 2

### Workshop Agenda

- Confirm Workspace and Knowledge access

- Select source documents

- Create knowledge collections

- Attach collections to custom models

- Check source citations

- Choose procedures for skills

Before attending, confirm individual access, Sandbox sign-in, Workspace access, and Knowledge collection access.

---

## Curating knowledge collections — 3

### Knowledge Collections

A knowledge collection contains uploaded documents that a model can search when responding to questions.

Collections support PDFs, Markdown, and plain text. Attach a collection to a custom model under **Knowledge**.

[Knowledge Bases  https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)[Open WebUI Knowledge  https://docs.openwebui.com/features/workspace/knowledge/](https://docs.openwebui.com/features/workspace/knowledge/)

---

## Curating knowledge collections — 4

### Choose Questions

Choose a question your documents can answer.

Bring course materials, research papers, or other documents you know well enough to check.

Use [system-prompt examples](../examples.html) if you need a prompt to begin.

---

## Curating knowledge collections — 5

### Open Workspace

![Sandbox chat with CUNY AI Lab logo and message box visible; arrow marks Workspace in left sidebar](../images/current/workspace-sidebar-2026-09-15-annotated.svg)

Select Workspace in left sidebar. Choose Models and open your custom model.

[Model Registry  https://ailab.gc.cuny.edu/models/](https://ailab.gc.cuny.edu/models/)

---

## Curating knowledge collections — 6

### Review Model Settings

Open your private copy of **STEM Adventure Games** or **Compare Wikipedia Edits**.

Review **Base Model** and **System Prompt**. Keep instructions from Workshop 1. Leave Skills and Tools unselected.

[Review system prompts  https://cuny-ai-lab.github.io/sandbox-series/examples.html](../examples.html)

---

## Curating knowledge collections — 7

### Save Initial Response

Start a new chat. Select model ID on bottom right of message box. Choose your custom model.

Ask your document question and save its response before attaching documents. Record any sources it uses.

---

## Curating knowledge collections — 8

### Retrieve Source Passages

- Uploaded documents are divided into passages and indexed for search.

- Retrieval finds passages relevant to a question.

- Your model can use retrieved passages in its response.

Which passages did your model use, and do they support its claims?

[Open WebUI retrieval  https://docs.openwebui.com/features/workspace/knowledge/](https://docs.openwebui.com/features/workspace/knowledge/)

---

## Curating knowledge collections — 9

### Open STEM Collection

![STEM Wikipedia Experiments listing three Wikipedia imports and four added entries. Entries cover source status, List of experiments, procedural variations, and software checks.](../images/current/stem-knowledge-2026-09-14.png)

Open Workspace → Knowledge. Search for STEM and open STEM Wikipedia Experiments.

---

## Curating knowledge collections — 10

### Review Source Roles

Use sources for different questions.

List of experiments

Choose experiments, scientists, and questions to investigate.

Scientific method

Examine hypotheses, measurement, and revision.

Women in science

Investigate collaboration, recognition, and institutions.

Check whether a scene follows its sources or adds invented details.

---

## Curating knowledge collections — 11

### Inspect Imported Text

Open each file and compare its contents with its source page.

- Confirm article text is present.

- Check headings, missing passages, and extraction errors.

- Record article title, source URL, and revision date.

List of experiments once imported a Wikimedia rate-limit error. Article text was restored on September 17, 2026. Check contents after every import.

---

## Curating knowledge collections — 12

### Review Attached Knowledge

![STEM Adventure Games model editor with STEM Wikipedia Experiments attached under Knowledge; Tools and Skills have no selections. White outlines identify these controls.](../images/current/knowledge-attachments-3x-2026-09-16.svg)

In your STEM copy, select STEM Wikipedia Experiments under Knowledge and choose Save & Update. Skills and Tools are added in Workshop 3.

---

## Curating knowledge collections — 13

### Check Game Sources

In your STEM copy, start an adventure about light and colour. Choose one action, then ask about its historical sources.

```text
Which objects in this scene appear in Newton: Light and Colour? Quote a relevant passage. Which details were invented for this game?
```

Open cited material. Does it support your model’s response?

[Read Newton source summary  https://cuny-ai-lab.github.io/sandbox-series/examples/knowledge/newton-light-colour.html](../examples/knowledge/newton-light-colour.html)[Read Newton’s account  https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006](https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00006)

---

## Curating knowledge collections — 14

### Select Documents

Begin with a few documents you know well enough to check.

- Course materials, such as syllabi, readings, or assignment instructions

- Research papers, methods, or annotated bibliographies

Use Markdown, plain text, or readable PDFs. Name files clearly and use headings to separate sections.

Check scanned or complex PDFs before uploading. Convert them to text if needed.

[Document formats  https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)[Explore source examples  https://cuny-ai-lab.github.io/sandbox-series/knowledge/reference.html](reference.html)

---

## Curating knowledge collections — 15

### Build Knowledge Collections

Choose documents that explain your course or research project and describe what you want to examine.

---

## Curating knowledge collections — 16

### Choose Reference Materials

Choose documents for your teaching or research task.

- Use [Newton: Light and Colour](../examples/knowledge/newton-light-colour.html) for apparatus and observations.

- Use [Newton: Experimental Variants](../examples/knowledge/newton-experimental-variants.html) for changes to experimental procedures.

Read documents before uploading; distinguish summaries from original accounts.

[Download Light and Colour  https://cuny-ai-lab.github.io/sandbox-series/examples/knowledge/newton-light-colour.md](../examples/knowledge/newton-light-colour.md)[Download Experimental Variants  https://cuny-ai-lab.github.io/sandbox-series/examples/knowledge/newton-experimental-variants.md](../examples/knowledge/newton-experimental-variants.md)

---

## Curating knowledge collections — 17

### Create Knowledge Collections

![Current Create a knowledge base form with name, description, Private access, and Create Knowledge](../images/current/knowledge-create-3x-2026-09-16.png)

Open Workspace → Knowledge → Create. Enter a name and description, keep access Private, then select Create Knowledge.

---

## Curating knowledge collections — 18

### Attach Knowledge Collections

- Open Workspace → Knowledge → your collection. Use Add Content to upload documents, then wait for processing to finish.

- Check extracted text against each source.

- Return to **Workspace → Models**, open your chosen custom model, and select your collection under **Knowledge**. Remove collections unrelated to your question.

- Choose **Save & Update**, then start a new chat with your custom model.

[Upload and attach source material  https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/)

---

## Curating knowledge collections — 19

### Test Retrieval

- Ask a question answered by one source. Verify each answer and quotation.

- Ask a question that needs two sources. Check whether both are used accurately.

- Ask about something absent from your documents. Check whether your model acknowledges missing information.

Repeat your saved question after attaching documents. Keep base model and system prompt unchanged. Compare responses and check which source passages were used.

---

## Curating knowledge collections — 20

### Check Retrieval Problems

| Observation | Next check |
| --- | --- |
| No relevant source appears | Check whether files finished processing, are attached, and are accessible. Review your search query. |
| A source is present but misread | Read cited passages in full and revise instructions. |
| A response invents a citation | Open cited documents and verify quotations and page numbers. |

Save unsuccessful responses before revising anything.

---

## Curating knowledge collections — 21

### Share Knowledge Collections

Share your collection with people who will use your custom model.

- Use **Add Access** to grant users or groups **Read** access.

- Ask someone you shared with to check access to your model and collection.

- Choose **Public** only for documents intended for all signed-in Sandbox users.

[Roles & Permissions  https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/](https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/)

---

## Curating knowledge collections — 22

### Prepare Skill Instructions

- Save source lists and retrieval tests

- Request Skills and Tools access

- Choose recurring teaching or research procedures

- Review [system-prompt examples](../examples.html)

- Continue to [Configuring skills and tools](../skills)
