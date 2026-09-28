# Curating knowledge collections

## 1. Curating knowledge collections

![CUNY AI Lab](../images/cail-wordmark-white.png)



### Curating knowledge collections



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



**Retrieval-augmented generation (RAG)** combines information retrieval with text generation. Relevant passages are retrieved from external sources and added to a model’s context. Custom models use those passages with your request and system prompt instructions to generate a response.



**Search sources → Retrieve passages → Generate response**

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

![STEM Adventure Games clone form with white annotations identifying its name, model ID, and base model.](../images/knowledge-stem-2026-09-28/review-clone.svg)

Give your copy a unique name and model ID. Base model, system prompt, and settings carry over when you clone.

Scroll to bottom and select **Save & Create**.

---

## 7. Try Custom Model

Select **Start an adventure**. Choose from four experiments and try its numbered choices. Ask for another menu to explore new options.

---

## 8. Example Sources

![Expanded Sandbox sidebar showing Workspace, Knowledge tab, and STEM Wikipedia Experiments collection, each outlined.](../images/knowledge-stem-2026-09-28/find-knowledge.svg?v=20260928-2)

Select **Workspace → Knowledge** and open **STEM Wikipedia Experiments** to see how an example collection is organized.

![STEM Wikipedia Experiments containing three original Wikipedia source documents, outlined together.](../images/knowledge-stem-2026-09-28/collection-documents.svg?v=20260928-4)

This collection supports adventure choices, experimental methods, and historical context. Next, choose sources for your adapted version.

---

## 9. Choose Purpose

What should participants learn or do with your adapted version?

Choose a topic and audience for **STEM Adventure Games**. Decide what players should explore through their choices.

---

## 10. Find Sources

Locate two or three Wikipedia articles or other documents that fit your purpose. Choose material with enough detail to guide scenes and decisions.

Read relevant passages and decide how each source will contribute to your version.

---

## 11. Prepare Documents

Save selected source text as PDF, Markdown, or plain text. Include a title, source URL, and date in each file.

Use descriptive filenames. You will name these documents in your system prompt.

---

## 12. Create Your Collection

![Create a knowledge base form with STEM Workshop Sources entered and white outlines identifying name, description, and Create Knowledge.](../images/knowledge-stem-2026-09-28/create-custom-collection.svg)

Select **Workspace → Knowledge → Create**. Name your collection and describe what your sources cover.

Keep access **Private** and select **Create Knowledge**.

---

## 13. Upload Your Sources

![New STEM Workshop Sources collection showing No content found, with Add Content open and Upload files annotated.](../images/knowledge-stem-2026-09-28/upload-custom-sources.svg)

Your new collection starts empty. Select **Add Content → Upload files** and upload documents you prepared.

Wait for processing, then open each file to check text and source links.

---

## 14. Attach Your Collection

![Model editor with white annotations identifying Select Knowledge and an attached collection.](../images/knowledge-stem-2026-09-28/attach-knowledge.svg)

Open cloned custom model in **Workspace → Models**. Under **Knowledge**, remove any inherited collection attachments, then select your own collection.

Continue to **System Prompt** in this editor.

---

## 15. Update Purpose

In **System Prompt**, revise **Purpose** to describe your topic, audience, and task. Replace bracketed text with your choices.

Create a choice-based adventure about [topic] for [audience]. Let players explore [question or practice] through their decisions.

---

## 16. Name Sources

Under **Procedure**, replace original source names with filenames you uploaded. State how each document should guide responses.

Use [filename] for [specific information or method]. Use [filename] for [additional context or evidence].

Remove instructions that refer to sources you replaced.

---

## 17. Revise Instructions

Review remaining instructions for your adapted purpose.

- **Procedure** · Describe what players should do.

- **Constraints** · State which details need source support.

- **Format** · Specify how responses should appear.

Retain brief scenes and numbered choices.

Select **Save & Update**.

---

## 18. Test Custom Model

![STEM Adventure Games chat showing four experiment choices and an annotated model selector.](../images/knowledge-stem-2026-09-28/test-retrieval.svg)

Start a new chat. Select model ID on bottom right of message box. Choose your copy.

Ask for four adventure options about your chosen topic. Choose one, then ask “Which passage supports this scene? Quote it and cite your source.”

---

## 19. Check Citations

![Wikipedia source passage opened from a STEM Adventure Games citation, with its document name and supporting text annotated.](../images/knowledge-stem-2026-09-28/check-citations.svg)

Select a citation to inspect its source.



- Does quoted text match your document?

- Does it support this custom model’s interpretation?

---

## 20. Compare Responses

Use one request with original model and your copy. Choose one experiment for both. Compare how each uses source documents.



- What changed with your sources and instructions? Check scenes and experimental choices.

- What did this custom model miss or misinterpret?

---

## 21. Revise and Retest

Change one source document or system prompt instruction based on what you observed, then repeat your request in a new chat.

If a custom model misses a source, check that its file finished processing, your collection is attached, and instructions name your new documents.

---

## 22. Share Custom Model

To share your work, grant intended users or groups **Read** access to your copy and its collection.



Ask someone to try your copy and check its citations.

 Sandbox Roles & Permissions <https://ailab.gc.cuny.edu/sandbox-docs/roles-permissions/>

---

## 23. Workshop Resources

Choose another topic or experiment. Refresh source documents when needed and check responses against versions you saved.

### Workshop Materials

- Review Composing system prompts <https://cuny-ai-lab.github.io/sandbox-series/index.html>

- Consult Sandbox Knowledge documentation <https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/>

- Consult Open WebUI Knowledge <https://docs.openwebui.com/features/workspace/knowledge/>

- Check monthly usage <https://tools.ailab.gc.cuny.edu/model-access>

### Example Model

- Open STEM Adventure Games <https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games>
