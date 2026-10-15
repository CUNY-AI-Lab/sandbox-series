# Facilitator Notes

Tools and Skills · Thursday, October 15, 2026 · 2:30–4:00 p.m. Eastern

New Media Lab · Room 7388.01 · CUNY Graduate Center

## Review status

This 24-slide revision includes two short system-prompt clauses: check Extend STEM Adventures for adventure extensions or Play records, and call Adventure Kit after approval. The actual saved-skill-use demonstration and the standard STEM Adventure Games tool-call/game demonstration remain pending. No screenshot of Advanced appears in this revision.

## Session plan

| Time Eastern | Activity | Slides |
| --- | --- | --- |
| 2:30–2:40 | Continue or clone; define skills and browse examples | 1–6 |
| 2:40–2:50 | Select a saved skill, add its prompt clause, and test | 7–9 |
| 2:50–3:10 | Define tools, browse examples, bind Adventure Kit, prepare, and test | 10–19 |
| 3:10–3:20 | Choose revision or creation; copy complete content | 20 |
| 3:20–3:40 | Work with CAIL Workspace Support; draft Extend Adventure Games | 21–22 |
| 3:40–4:00 | Add a new version, retest, and reflect | 23–24 |

Browse the catalog slides briefly within the existing introduction blocks. They add examples without changing the outline’s 90-minute allocation. Preserve the six actions: clone or continue, add Adventure Kit, experiment, copy editable content, revise with Support, and add a new version.

## Skill module

Define a skill as instructions the model loads and follows for a repeatable task. Select Extend STEM Adventures in Workspace → Models → Edit → Skills, if the participant account has access, before adding the short clause to the model's prompt. Creation is an option later in the Support activity.

Existing Extend STEM Adventures uses the obsolete render_stem_adventure and rooms/actions/goal_flags contract. The short prompt clause tells the model to check that skill, but it does not make the skill compatible with Adventure Kit v2. Before attempting an extension, review or revise its saved instructions for the current tool. Check actual saved-resource loading and use, then missing evidence and an immediate request to stop. Model guidance cannot enforce executable game state.

## Tool module

Adventure Kit v2 takes a complete schema_version 2 scenario in scenario_json. Its render_adventure function does not contain a default story, genre, goal, or completion threshold. The active prompt and reviewed participant request supply the scenario and rules. Empty input requests context. The model must call the function, the result must return, and the embedded player must visibly appear before claiming a successful run.

Inspect one choice before and after its prerequisite, Undo, and immediate Stop. Copy the latest Play record into chat before discussing choices. A copied record can become stale after another choice, Undo, or Restart. The game controls executable state; the skill can interpret supplied evidence only.

## Catalog scope

October 15 captures cover 11 contributed skills and 14 tools visible to the host account. One private QA skill and one private QA tool are excluded from the contributed examples. Crops retain actual titles and descriptions without browser tabs, private chats, account details, admin toggles, or valves. Long descriptions retain the interface’s own truncation; the accessible catalog page supplies their full observed text.

Host visibility does not establish participant access. The Shared with you filter included History Of Ideas Abstract Critique even though its Access dialog showed Private and no grants. Adventure Kit is also private to its owner in the inspected configuration. Do not change sharing automatically or promise that every participant sees these entries. Confirm the intended workshop resources from a participant account before class.

## Current hosted evidence

The title search returned eight entries, including Advanced and participant clones, but did not resolve the exact standard STEM Adventure Games configuration. All 68 model entries across three catalog pages have not yet been inspected. The standard model may have been renamed or may appear through another entry; its absence is not established. Advanced was briefly corrected and enabled under explicit hosted-test approval. One diagnostic request retrieved scientific-method sources and proposed a scene. The request expressly required review before calling Adventure Kit, so stopping after the proposed scene was expected. No render_adventure was submitted in that diagnostic; this does not diagnose an invocation failure. Original prompt and inactive flag were restored, with access and integrations preserved. This diagnostic is excluded from demonstration slides.

Earlier October 14 QA verified the tool with a supplied archive fixture on a separate DeepSeek model. That confirms that configuration only; it does not substitute for the requested standard-model demonstration. No live participant test is claimed.

## Support and new versions

Participants choose to revise either the tool or a skill, or create their own. Copy the complete original code/instructions, active system prompt, required source passages, and observed problem into a chat with CAIL Workspace Support. Ask for complete revised content, an explanation, and a test. Support does not inherit the participant’s previous chat or collection automatically.

Slide 22 gives a tool creation option within this same activity: Extend Adventure Games adapts the adventure just played to one lesson outcome. Participants give Support the prompt, lesson passages, weekly concepts, current Adventure Kit scenario, and Play record. The proposed tool preserves game rules, grounds a decision in course theory and a dated source, asks students to critique the evidence, and returns a revised schema-version-2 scenario for review before any Adventure Kit call. If web retrieval is unavailable, participants supply a dated source. Treat the output as a draft until its code, output, and actual game behavior are checked.

The captured catalog does not show a saved tool named Extend Adventure Games. Do not tell participants to select it until they have created and saved it. The short follow-on clause in the handout names that new tool, requires review of its proposal, and then calls Adventure Kit to render the approved scenario.

Preserve the original. In Workspace → Tools or Skills → Create, give the new version its own Name and ID, replace sample content completely, review Access, and Save & Create. Select the new item and repeat the same request under the same model and settings. Report expected and observed behavior and leave unrun checks explicit.
