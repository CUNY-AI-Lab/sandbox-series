# Facilitator Notes

Tools and Skills · October 15, 2026 · 2:30–4:00 p.m. Eastern

## Current flow

The supplied screenshots name Adventure Panel Play as the skill and Adventure Panel as the tool. Select both on the same model card, check the pictured Model Bound Tool Enabler filter, add the current prompt clause, and save before opening a fresh test chat. The skill supplies a procedure; the tool displays a scene and sends a selected numbered choice to chat. Setting, goals, rules, and sources come from each participant's system prompt.

Adventure Outcomes and Conclude Adventure Game remain optional experiments after the first run. CAIL Workspace Support follows those experiments; participants can revise either component or create their own.

| Time Eastern | Activity | Slides |
| --- | --- | --- |
| 2:30–2:40 | Continue or clone; define skills and tools; select a base model | 1–5 |
| 2:40–2:50 | Enable the filter and select Adventure Panel Play | 6–7 |
| 2:50–3:00 | Select Adventure Panel; check the model card; add the prompt clause and save | 8–10 |
| 3:00–3:15 | Run the adventure, inspect calls, and play | 11–12 |
| 3:15–3:25 | Experiment with other available skills | 13 |
| 3:25–3:30 | Choose a revision or creation task | 14 |
| 3:30–3:45 | Work with CAIL Workspace Support | 15–16 |
| 3:45–4:00 | Add a new version, retest, and reflect | 17–18 |

## Evidence limits

Slides 7–9 and 13 use the three user-supplied October 15 screenshots. The source images are embedded unchanged, with separate arrow annotations and numbered labels. The screenshots establish visible names and selection states. They do not establish a successful call, saved configuration, or participant access. The skill ID in the revised prompt clause is `extend-adventure-games`, as recorded in the existing Adventure Panel verification and current model-card text.

The results below describe earlier tests at their stated versions. Adventure Kit's declarative state engine and its Undo/Play Record controls are not the same implementation as Adventure Panel's turn-by-turn display. Do not present earlier Kit checks as proof that Panel enforces game state. For Panel, confirm the choice's user message, next scene, rule consistency, and immediate stop. The current slide update runs no new model inference.

The main deck now shows the user-provided live run with view_skill, show_scene, and the ADVENTURES panel. Collapsed call details do not identify the exact skill ID or prove the new minimal prompt was saved. The earlier Adventure Outcomes loading screenshot is kept in the evidence record, outside the opening deck. The original standard model was not resolved across all 67 catalog entries; the user authorized STEM Adventure Games (Clone), DeepSeek V4 Flash 0731, for the successful rehearsals. Advanced was not used for screenshots.

## Skill and discovery

The earlier rehearsal selected saved Adventure Outcomes. Its exact instructions remain available for later optional experimentation.

The October 15 Clone test explicitly requested native `view_skill({"id":"adventure_outcomes"})`. It returned the saved instructions. The answer rejected a false completion claim about a confounded experiment, asked which numbered choice an ambiguous request meant, and acknowledged Stop in exactly one sentence. This is evidence of explicit native loading and observed use, not a benchmark of autonomous discovery. A direct `$` mention injects skill content and may not call view_skill.

The deployed OpenWebUI 0.11.4 discovery path could expose other active, readable skills even when only one was selected on the model. Earlier unrelated skill calls included obsolete adventure instructions. The tested prompt clause names the exact skill and excludes other catalog instructions for this adventure. The 0.12.2 tool-search compatibility update does not itself establish a skill allowlist. Recheck deployed behavior after any upgrade; do not attribute these successful tests to an unverified version change.

## Tool and actual player

Adventure Kit 2.1.0 was exported from the live editor and tested in STEM Adventure Games (Clone), based on DeepSeek V4 Flash 0731. The actual call was `render_adventure` with supplied schema-version-2 JSON text, theme `cuny-blue`, and text_speed `0`. The result reported `render_requested`, one node, four choices, two endings, and three state keys. The embedded interactive player visibly appeared in the chat.

The supplied Seedling Comparison fixture is a fictional classroom simulation. It is separate from the reusable code. This controlled-input test does not establish automatic historical source-to-scenario conversion. The exported tool contains no built-in scenario, genre, or fixed completion threshold.

Hosted actions passed: a prerequisite blocked an early choice; the valid sequence reached the supplied completion rule; Undo returned to active play; Stop halted without completion; Copy Play Record displayed its success message. Initial capture displayed Bauhaus despite a cuny-blue request; a reload displayed CUNY Blue, so the mismatch did not reproduce. Keep this observation in the evidence record rather than claiming an established theme defect.

The existing Model Bound Tool Enabler was selected during the successful tests. It restores model-attached tool IDs when chat state omits them. The current workshop explicitly enables it on the model card before adding Adventure Panel. A with/without comparison was not run, so necessity is not established. The exercise does not change global filter settings.


## Access and Support

Adventure Kit and Adventure Outcomes showed Private/no grants at inspection. The owner then reported granting participant read access to both; post-change visibility remains unverified. Adventure Panel Play is now the opening skill, so verify participant visibility of that saved resource too without expanding permissions or exposing student identifiers.

Earlier CAIL Workspace Support returned a separate labeled Adventure Outcomes proposal with an explicitly unrun test. It was not installed or retested. That proposal is not an opening skill or proof of the new orchestration workflow. The current Support activity is general: revise or create a skill or tool, preserve the original, and test the actual saved result.

[Participant exercises](exercises.html) · [Hosted evidence](hosted-evidence.html)
