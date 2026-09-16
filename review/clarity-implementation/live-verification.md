# Firefox verification

Checked September 16, 2026, in an administrator account using Firefox. These observations do not establish non-admin participant access. The user deferred that account check.

## Source-only configuration

Created a private custom model, **STEM Adventure Games — Sources**, with the existing source-checking system prompt and STEM Wikipedia Experiments attached under Knowledge. No skills or custom tools are attached. The shared STEM Adventure Games model was not changed. The private example has no access grants.

Final settings use DeepSeek V4 Pro 0813, Function Calling **Legacy**, and collection mode **Focused Retrieval**. Web Search, Image Generation, Code Interpreter, Terminal, Memory, and Builtin Tools are disabled. File Upload, File Context, and Citations remain enabled.

## Download and upload

Clicked the scenario download link in the local workshop using Firefox. The save dialog supplied `prism-scenario.md`; downloaded bytes match `examples/adventure/prism-scenario.md`. Uploaded that downloaded file to a chat with the source-only model. The chat showed the 1.9 KB attachment and accepted the workshop's source question.

## Source comparison

Used the exact Workshop 2 request:

> Using Newton: Light and Colour, identify apparatus details simplified in the attached Prism Laboratory scenario. Quote a relevant passage and identify this entry as a source summary. If it is unavailable, say so.

The first response, with Function Calling left at Default and built-in tools disabled, used only the uploaded scenario. It correctly said the Newton entry was unavailable. Switching the collection to Entire Document and regenerating did not resolve that failure in this chat.

Set Function Calling explicitly to Legacy, restored Focused Retrieval, saved the private model, reloaded the chat, and regenerated the original question. The response then retrieved three sources and quoted the Newton summary:

> One screen and one collectible prism simplify an apparatus involving two boards and two prisms.

The response identified the entry as a source summary rather than primary historical text. Opened its citation in Firefox and verified that the quoted sentence appears under **Use in Prism Laboratory**. No adventure game or skill was invoked. This verifies one source-checking request in this administrator account, not retrieval reliability across arbitrary documents or participant accounts.

Open WebUI documents that native function calling requires model-called knowledge tools, while disabling native mode restores automatic retrieval. That distinction informed the explicit Legacy setting now shown in Workshop 2. [Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/)

## Screenshot states

- Model creation: empty Name, Base Model, and System Prompt fields.
- Model review: source-checking model with populated base model and prompt; Knowledge temporarily removed for the initial-response illustration. The unsaved change was discarded.
- Knowledge attachment: saved collection present; Skills and Tools empty.
- Clone: actual menu item on STEM Adventure Games.
- Private copy: unsaved clone with Private access and no inherited user/group grants. This clone was not saved.
- Skill creation: empty form, including Instructions and Save & Create.

The saved source-only configuration retains its collection. Live changes are limited to this private example; participant sharing remains for the user to arrange.
