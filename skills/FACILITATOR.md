# Facilitator Notes

Tools and Skills · Thursday, October 15, 2026 · 2:30–4:00 p.m. Eastern

New Media Lab · Room 7388.01 · CUNY Graduate Center

## Review status

This 25-slide revision includes the user-selected Adventure Outcomes skill, both system-prompt clauses, the user-provided selection screenshots with numbered annotations, and actual hosted evidence immediately after each test. The user authorized their existing STEM Adventure Games (Clone) for the demonstration. Advanced is excluded. The original standard model was not resolved after all 67 catalog entries across three pages and its editor route were inspected.

## Session plan

| Time Eastern | Activity | Slides |
| --- | --- | --- |
| 2:30–2:40 | Continue or clone; define skills and browse examples | 1–6 |
| 2:40–2:50 | Select Adventure Outcomes, add its prompt clause, and test | 7–10 |
| 2:50–3:10 | Define tools, browse examples, bind Adventure Kit, prepare, and test | 11–21 |
| 3:10–3:20 | Choose revision or creation; copy complete content | 22 |
| 3:20–3:40 | Work with CAIL Workspace Support | 23 |
| 3:40–4:00 | Add a new version, retest, and reflect | 24–25 |

Browse the 11 contributed skills and 14 tools briefly within the existing introduction blocks. Their dated catalog captures are examples of host visibility, not a promise of participant access.

## Skill and discovery

Select the saved Adventure Outcomes resource through Workspace → Models → Edit → Skills → Select Skill. Preserve its exact instructions. This initial exercise does not require transcription into a blank editor; creation or revision comes later.

The October 15 Clone test explicitly requested native `view_skill({"id":"adventure_outcomes"})`. It returned the saved instructions. The answer rejected a false completion claim about a confounded experiment, asked which numbered choice an ambiguous request meant, and acknowledged Stop in exactly one sentence. This is evidence of explicit native loading and observed use, not a benchmark of autonomous discovery. A direct `$` mention injects skill content and may not call view_skill.

The deployed OpenWebUI 0.11.4 discovery path could expose other active, readable skills even when only one was selected on the model. Earlier unrelated skill calls included obsolete adventure instructions. The tested prompt clause names the exact skill and excludes other catalog instructions for this adventure. The 0.12.2 tool-search compatibility update does not itself establish a skill allowlist. Recheck deployed behavior after any upgrade; do not attribute these successful tests to an unverified version change.

## Tool and actual player

Adventure Kit 2.1.0 was exported from the live editor and tested in STEM Adventure Games (Clone), based on DeepSeek V4 Flash 0731. The actual call was `render_adventure` with supplied schema-version-2 JSON text, theme `cuny-blue`, and text_speed `0`. The result reported `render_requested`, one node, four choices, two endings, and three state keys. The embedded interactive player visibly appeared in the chat.

The supplied Seedling Comparison fixture is a fictional classroom simulation. It is separate from the reusable code. This controlled-input test does not establish automatic historical source-to-scenario conversion. The exported tool contains no built-in scenario, genre, or fixed completion threshold.

Hosted actions passed: a prerequisite blocked an early choice; the valid sequence reached the supplied completion rule; Undo returned to active play; Stop halted without completion; Copy Play Record displayed its success message. Initial capture displayed Bauhaus despite a cuny-blue request; a reload displayed CUNY Blue, so the mismatch did not reproduce. Keep this observation in the evidence record rather than claiming an established theme defect.

The existing Model Bound Tool Enabler was selected during the successful tests. It restores model-attached tool IDs when chat state omits them. A with/without comparison was not run, so necessity is not established. Explain its conditional purpose before Adventure Kit and do not enable it globally.

## Participant access

At inspection, both Adventure Kit and Adventure Outcomes displayed Private with no access grants. Host visibility does not prove that participants can select them. No permissions were expanded. Confirm the intended existing participant group's read access, then verify with an authorized participant context before class. Do not expose student identifiers in screenshots or review records.

## Support and new versions

Participants may revise either tool or skill, or create their own. Copy complete original content, active system prompt, required source passages, and the observed problem into CAIL Workspace Support. Ask for complete content, an explanation, and one test. Support does not inherit previous chats or collections automatically.

Preserve the original. Give a revised copy its own Name and ID, review all content, select it, update its prompt clause, and retest identical input with the same model and settings. For a new item, compare expected and observed behavior and try a boundary case. Keep unrun checks explicit.

[Participant exercises](exercises.html) · [Hosted evidence](hosted-evidence.html)

## Access follow-up

After the private-access inspection, the owner reported granting participant read access to both Adventure Kit and Adventure Outcomes. The post-change participant visibility check remains unverified because browser control was stopped. No access change was made by this task.

## Support rehearsal

CAIL Workspace Support returned a complete separate “Adventure Outcomes — Labeled Trial” proposal, an explanation, and an explicitly unrun test. The proposal adds an outcome label while preserving clarification and immediate-stop exceptions. The original Adventure Outcomes remains the selected workshop skill. Creating the separate trial and running its live retest were not completed before browser control stopped. No successful retest of that proposal is claimed.
