# Curating knowledge collections

## 1. Curating knowledge collections

[![CUNY AI Lab](../images/cail-wordmark-white.png)](https://ailab.gc.cuny.edu/)



Led by  Zach Muhlbauer  and  Meha Gupta

New Media Lab · Room 7388.01
CUNY Graduate Center

Thursday, October 1, 2026   2:30–4:00 p.m.

[https://cuny-ai-lab.github.io/sandbox-series/knowledge](https://cuny-ai-lab.github.io/sandbox-series/knowledge)

---

## 2. Workshop Roadmap

- **[Composing System Prompts](../basics/)**  Configure model behavior with system prompts. Thursday, September 17

- **Curating Knowledge Collections**  Organize source documents in knowledge collections. Thursday, October 1

- **Configuring Skills and Tools**  Extend model capabilities with skills and tools. Thursday, October 15

[https://ailab.gc.cuny.edu/sandbox-docs/](https://ailab.gc.cuny.edu/sandbox-docs/)

---

## 3. Workshop Agenda

- Explore and clone · 15 minutes

- Select new sources · 25 minutes

- Create and populate collections · 20 minutes

- Revise system prompts · 10 minutes

- Test and revise · 20 minutes

Requires individual access, Sandbox sign-in.

Open Sandbox <https://chat.ailab.gc.cuny.edu/>

---

## 4. Retrieval-Augmented Generation

A Knowledge collection contains documents a custom model can search.

**Retrieval-augmented generation (RAG)** combines information retrieval with text generation. It retrieves relevant source passages and adds them to a model’s context alongside your request and system prompt instructions.

**Search documents → Retrieve passages → Generate response**

 Open WebUI Knowledge <https://docs.openwebui.com/features/workspace/knowledge/>

---

## 5. RAG Under the Hood

### Processing documents

- **Parse**  Extract usable text from files

- **Chunk**  Divide text into smaller passages

- **Embed**  Represent passages numerically so they can be searched by similarity

### Responding to requests

- **Retrieve**  Search for passages relevant to a request

- **Add context**  Append passages to prompt instructions

- **Generate**  Produce a response using that context

---

## 6. Explore STEM Adventures

**STEM Adventure Games** uses source documents to guide a text adventure with numbered choices.

Clone this example, then adapt its sources and instructions for a topic and audience you choose.

<https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games>

---

## 7. Clone Custom Model

Select **Workspace** in left sidebar, then **Models**. Search for **STEM Adventure Games**. Open **⋯** beside it and select **Clone**.

![Workspace Models filtered to STEM Adventure Games, with white annotations identifying Workspace in left sidebar and Clone for original model.](../images/knowledge-stem-2026-09-28/clone-model.svg)

---

## 8. Name Your Copy

Give your copy a unique name and model ID. Base model, system prompt, and settings carry over when you clone.

Scroll to bottom and select **Save & Create**.

![STEM Adventure Games clone form with white annotations identifying its name, model ID, and base model.](../images/knowledge-stem-2026-09-28/review-clone.svg?v=20260928-review)

---

## 9. Try Custom Model

Open **New Chat**. Select model ID on bottom right of message box. Choose **STEM Adventure Games**.

Ask for four adventure options, choose one, and try its numbered choices. Ask for another menu to see new options.

![New chat with original STEM Adventure Games selected. Model selector at bottom right of message box is outlined.](../images/knowledge-collection-2026-10-01/select-original.svg?v=20261001-original)

Select **Workspace** in left sidebar, then **Knowledge**. Open **Sandbox Workshop Collection**.

![Workspace in left sidebar, Knowledge tab, and Sandbox Workshop Collection outlined in Firefox.](../images/knowledge-collection-2026-10-01/navigation.svg)

---

## 10. Example Sources

At **Sandbox Workshop Collection** root, **instructions.txt** describes how sources guide play. Open **Wikipedia** to see source files.

![Sandbox Workshop Collection root with Wikipedia folder and instructions.txt outlined and labeled Source files and Source directions.](../images/knowledge-collection-2026-10-01/root.svg)

**Wikipedia** contains three article files. Open each to review its text and source link.

For your adapted version, start with one article. Add more as needed.

![Wikipedia directory inside Sandbox Workshop Collection with Women-in-science.txt, Scientific-method.txt, and List-of-experiments.txt outlined together.](../images/knowledge-collection-2026-10-01/wikipedia.svg)

---

## 11. Choose Purpose

What should players learn or explore?

Choose a topic and audience for your adaptation of **STEM Adventure Games**. Identify a question players could investigate through their choices.

---

## 12. Find Sources

Start with one Wikipedia article about your chosen topic. Add more only as needed.

Choose substantial passages that give players something to investigate through their choices.

---

## 13. Create Your Collection

Select **Workspace → Knowledge → Create**. Name your collection and describe what your sources cover.

Keep access **Private** and select **Create Knowledge**.

![Create a knowledge base form with STEM Workshop Sources entered and white outlines identifying name, description, and Create Knowledge.](../images/knowledge-stem-2026-09-28/create-custom-collection.svg)

---

## 14. Add Source Text

Select **Add Content → New directory**. Name it **Wikipedia**, select **Create**, then open **Wikipedia**.

![New directory and Wikipedia directory outlined in Sandbox.](../images/knowledge-directories-2026-09-29/directory-workflow.svg)

Select **Add Content → Add text content**. Use article title as filename.

Copy and paste several paragraphs or complete sections from your chosen Wikipedia article, including its link.

![List of experiments editor filled with Wikipedia experiment entries, with source link outlined.](../images/knowledge-directories-2026-09-29/paste-excerpt.svg)

Select **Save**. One Wikipedia article is enough to begin. Keep any additional articles in separate files with their links.

Wait for processing, then open each file to check text.

![Bottom of populated List of experiments editor with Save outlined.](../images/knowledge-directories-2026-09-29/save-excerpt.svg)

---

## 15. Add Source Guidance

Before testing, add two short sources alongside your Wikipedia material.

- **Secondary source** — An explanation or analysis that helps interpret your topic.

- **Heuristic source** — Questions or rules of thumb that guide player decisions.

Return to collection root. Use **Add Content → Add text content** to save relevant passages and source links in separate, clearly named files.

---

## 16. Add Instructions

Select collection name above directory contents to return to its root. Select **Add Content → Add text content**.

Enter **instructions** as title; Sandbox adds **.txt**. Use your page titles and filenames to explain which material grounds scenes, which helps interpret them, and which guides player choices. Select **Save**.

![Add text content editor titled instructions, with directions for using three STEM Wikipedia sources. Title outlined; Sandbox adds .txt when saved.](../images/knowledge-directories-2026-09-29/create-instructions.svg)

In **Workspace → Models**, open **⋯ → Edit** beside your saved copy.

Under **Knowledge**, replace **STEM Wikipedia Experiments** with your own collection. Scroll up to **System Prompt**.

![Model editor with Select Knowledge and STEM Workshop Sources in its collection picker annotated.](../images/knowledge-stem-2026-09-28/attach-knowledge.svg?v=20260928-review2)

In cloned **System Prompt**, revise **Purpose** and **Audience** for your topic. Under **Procedure**, replace source and retrieval directions above numbered steps.

Offer four adventure options immediately. After a player chooses, retrieve instructions.txt from attached Knowledge collection and use its directions to find relevant source passages. Use article passages for details, secondary sources for interpretation, and heuristic sources for questions or decision rules during play.

Remove instructions that refer to sources you replaced. Keep numbered game steps, **Constraints**, and **Format**. Select **Save & Update**.

---

## 17. Test Custom Model

- Select **New Chat** in left sidebar.

- Select model ID on bottom right of message box. Choose your saved copy.

- Ask for four adventure options about your topic. Choose one to begin.

---

## 18. Check Citations

In same chat, ask “Which passage supports this scene? Quote it and cite your source.”

Select a citation beside a response. Does its source passage support that response?

![STEM Adventure Games chat with citation beside a response outlined and labeled. Message box remains visible.](../images/knowledge-stem-2026-09-28/check-citations.svg?v=20260928-chat)

---

## 19. Compare Responses

Keep your test chat open. Open **STEM Adventure Games** in another tab and send same opening request.

<https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games>

- How do responses differ?

- Does your copy use new sources as instructed?

---

## 20. Revise and Retest

Choose one problem you observed. Revise source guidance or system prompt instructions. Add another Wikipedia article only if needed.

For source changes, update copied excerpts and **instructions.txt**. Wait for processing. For prompt changes, select **Save & Update**.

Open **New Chat**, select your saved copy, and repeat your request. Did this change resolve that problem?

---

## 21. Share Custom Model

In your copy’s editor, open **Access** and grant intended users or groups **Read** access. Give those same users **Read** access to its Knowledge collection.

Ask someone to try your copy and check its citations.

 Sandbox Roles & Permissions <https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/>

---

## 22. Parting Questions

How else could you see yourself using knowledge collections in the future?

What are the limitations of this approach?

---

## 23. Workshop Resources

Check responses against sources in your collection. Next workshop introduces tools that retrieve Wikipedia content live.

### Workshop Materials

- Review Composing System Prompts <https://cuny-ai-lab.github.io/sandbox-series/basics/>

- Consult Sandbox Knowledge documentation <https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/>

- Consult Open WebUI Knowledge <https://docs.openwebui.com/features/workspace/knowledge/>

- Check monthly usage <https://tools.ailab.gc.cuny.edu/model-access>

### Example Model

- Open STEM Adventure Games <https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games>
