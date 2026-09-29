# Curating knowledge collections

## 1. Curating knowledge collections

![CUNY AI Lab](../images/cail-wordmark-white.png)





Led by  Zach Muhlbauer  and  Meha Gupta

New Media Lab · Room 7388.01
CUNY Graduate Center

Thursday, October 1, 2026   2:30–4:00 p.m.

---

## 2. Workshop Agenda

- Explore and clone · 15 minutes

- Select new sources · 25 minutes

- Create and populate collections · 20 minutes

- Revise system prompts · 10 minutes

- Test and revise · 20 minutes

Requires individual access, Sandbox sign-in.

Open Sandbox <https://chat.ailab.gc.cuny.edu/>

---

## 3. Retrieval-Augmented Generation

A Knowledge collection contains documents a custom model can search.

**Retrieval-augmented generation (RAG)** combines information retrieval with text generation. It retrieves relevant source passages and adds them to a model’s context alongside your request and system prompt instructions.

**Search documents → Retrieve passages → Generate response**

 Open WebUI Knowledge <https://docs.openwebui.com/features/workspace/knowledge/>

---

## 4. Explore STEM Adventures

**STEM Adventure Games** uses source documents to guide a text adventure with numbered choices.

Clone this example, then adapt its sources and instructions for a topic and audience you choose.

<https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games>

---

## 5. Clone Custom Model

![Workspace Models filtered to STEM Adventure Games, with white annotations identifying Workspace in left sidebar and Clone for original model.](../images/knowledge-stem-2026-09-28/clone-model.svg)

Select **Workspace** in left sidebar, then **Models**. Search for **STEM Adventure Games**. Open **⋯** beside it and select **Clone**.

---

## 6. Name Your Copy

![STEM Adventure Games clone form with white annotations identifying its name, model ID, and base model.](../images/knowledge-stem-2026-09-28/review-clone.svg?v=20260928-review)

Give your copy a unique name and model ID. Base model, system prompt, and settings carry over when you clone.

Scroll to bottom and select **Save & Create**.

---

## 7. Try Custom Model

Open **New Chat**. Select model ID on bottom right of message box. Choose your saved copy.

Select **Start an adventure**, choose an experiment, and try its numbered choices. Ask for another menu to see new options.

---

## 8. Example Sources

![Expanded Sandbox sidebar showing Workspace, Knowledge tab, and STEM Wikipedia Experiments collection, each outlined.](../images/knowledge-stem-2026-09-28/find-knowledge.svg?v=20260928-review2)

Select **Workspace → Knowledge** and open **STEM Wikipedia Experiments** to see how an example collection is organized.

![STEM Wikipedia Experiments containing three original Wikipedia source documents, outlined together.](../images/knowledge-stem-2026-09-28/collection-documents.svg?v=20260928-4)

**List of experiments** guides adventure options; **Scientific method** guides decisions; **Women in science** adds historical context.

Next, choose sources for your adapted version.

---

## 9. Choose Purpose

What should players learn or explore?

Choose a topic and audience for your adaptation of **STEM Adventure Games**. Identify a question players could investigate through their choices.

---

## 10. Find Sources

Locate two or three Wikipedia articles or other documents about your chosen topic.

Read relevant passages. Choose sources that explain what players could investigate and which decisions they could make.

---

## 11. Prepare Documents

Copy relevant source text into documents and save as PDF, Markdown, or plain text. Include a title, source URL, and date saved in each file.

Use descriptive filenames. These saved documents become your collection; links alone do not include article text.

---

## 12. Create Your Collection

![Create a knowledge base form with STEM Workshop Sources entered and white outlines identifying name, description, and Create Knowledge.](../images/knowledge-stem-2026-09-28/create-custom-collection.svg)

Select **Workspace → Knowledge → Create**. Name your collection and describe what your sources cover.

Keep access **Private** and select **Create Knowledge**.

---

## 13. Upload Your Sources

![New STEM Workshop Sources collection showing No content found, with Add Content open and Upload files annotated.](../images/knowledge-stem-2026-09-28/upload-custom-sources.svg?v=20260928-review2)

Your new collection starts empty. Select **Add Content → Upload files** and upload documents you prepared.

Wait for processing, then open each file to check text and source links.

---

## 14. Attach Your Collection

![Model editor with Select Knowledge and STEM Workshop Sources in its collection picker annotated.](../images/knowledge-stem-2026-09-28/attach-knowledge.svg?v=20260928-review2)

In **Workspace → Models**, find your saved copy. Open **⋯ → Edit**.

Under **Knowledge**, remove **STEM Wikipedia Experiments** from your copy and select your own collection. Scroll up to **System Prompt**.

---

## 15. Update Purpose

In **System Prompt**, revise **Purpose** and **Audience** for your chosen topic. Use this as a starting point.

Create a text adventure about [topic] for [audience]. Let players investigate [question] through their decisions.

---

## 16. Update Sources

Under **Procedure → Source documents**, replace original source names with filenames you uploaded. Explain how each document should guide play.

Use [filename] to guide [adventure options, decisions, or background details].

Remove instructions that refer to sources you replaced.

---

## 17. Revise Instructions

Check remaining instructions against your chosen topic.

- **Procedure** · Revise directions that conflict with your topic.

- **Constraints** · Keep documented details distinct from invented scenes.

- **Format** · Retain brief scenes and numbered choices.

Select **Save & Update**.

---

## 18. Test Custom Model

- Select **New Chat** in left sidebar.

- Select model ID on bottom right of message box. Choose your saved copy.

- Ask for four adventure options about your topic. Choose one to begin.

---

## 19. Check Citations

![STEM Adventure Games chat with citation beside a response outlined and labeled. Message box remains visible.](../images/knowledge-stem-2026-09-28/check-citations.svg?v=20260928-chat)

In same chat, ask “Which passage supports this scene? Quote it and cite your source.”

Select a citation beside a response. Does its source passage support that response?

---

## 20. Compare Responses

Keep your test chat open. Open **STEM Adventure Games** in another tab and send same opening request.

<https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games>

- How do responses differ?

- Does your copy use new sources as instructed?

---

## 21. Revise and Retest

Choose one problem you observed and revise its source document or system prompt instruction.

For document changes, replace outdated files in your collection and wait for processing. For prompt changes, select **Save & Update**.

Open **New Chat**, select your saved copy, and repeat your request. Did this change resolve that problem?

---

## 22. Share Custom Model

In your copy’s editor, open **Access** and grant intended users or groups **Read** access. Give those same users **Read** access to its Knowledge collection.

Ask someone to try your copy and check its citations.

 Sandbox Roles & Permissions <https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/>

---

## 23. Workshop Resources

Choose another topic or experiment. Refresh source documents when needed and check responses against versions you saved.

### Workshop Materials

- Review Composing System Prompts <https://cuny-ai-lab.github.io/sandbox-series/basics/>

- Consult Sandbox Knowledge documentation <https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/>

- Consult Open WebUI Knowledge <https://docs.openwebui.com/features/workspace/knowledge/>

- Check monthly usage <https://tools.ailab.gc.cuny.edu/model-access>

### Example Model

- Open STEM Adventure Games <https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games>
