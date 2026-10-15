# Facilitator Notes

Tools and Skills · October 15, 2026 · 2:30–4:00 p.m. Eastern

## Current flow

The user confirmed the saved orchestration skill's menu label is Extend Adventure Games. Opening setup selects that skill, explains tools and examples while the model card remains open, enables Model Bound Tool Enabler, selects Adventure Kit, checks all four attachments, adds one minimal system-prompt clause, and saves the model card once both attachments are selected. Only then do participants open a fresh chat to test orchestration and play. No tester skill belongs in the opening.

Adventure Outcomes and Conclude Adventures are later optional experiments. CAIL Workspace Support follows those experiments; participants can revise either component or create their own. The exact user-provided Adventure Outcomes instructions are preserved as a later reference, not an opening default.

| Time Eastern | Activity | Slides |
| --- | --- | --- |
| 2:30–2:40 | Continue or clone; define skills and browse examples | 1–6 |
| 2:40–2:50 | Select Extend Adventure Games | 7 |
| 2:50–3:00 | Explain tools; enable filter; select Adventure Kit; check the model card; add prompt clause and save | 8–16 |
| 3:00–3:15 | Run the adventure, inspect calls, and play | 17–18 |
| 3:15–3:25 | Experiment with other available skills | 19 |
| 3:25–3:30 | Choose a revision or creation task | 20 |
| 3:30–3:45 | Work with CAIL Workspace Support | 21–22 |
| 3:45–4:00 | Add a new version, retest, and reflect | 23–24 |

## Evidence limits

The newly requested Extend Adventure Games orchestration sequence has not been live-tested by this task. The owner confirmed its current saved name; its current ID, full instructions, and participant visibility have not been read back. Browser control stopped on a prohibited current URL, and it was not retried or bypassed. Do not label earlier Adventure Outcomes or direct Adventure Kit tests as proof of this new orchestration sequence.

The main deck now shows the user-provided live run with view_skill, show_scene, and the ADVENTURES panel. Collapsed call details do not identify the exact skill ID or prove the new minimal prompt was saved. The earlier Adventure Outcomes loading screenshot is kept in the evidence record, outside the opening deck. The original standard model was not resolved across all 67 catalog entries; the user authorized STEM Adventure Games (Clone), DeepSeek V4 Flash 0731, for the successful rehearsals. Advanced was not used for screenshots.

## Skill and discovery

The earlier rehearsal selected saved Adventure Outcomes. Its exact instructions remain available for later optional experimentation.

The October 15 Clone test explicitly requested native `view_skill({"id":"adventure_outcomes"})`. It returned the saved instructions. The answer rejected a false completion claim about a confounded experiment, asked which numbered choice an ambiguous request meant, and acknowledged Stop in exactly one sentence. This is evidence of explicit native loading and observed use, not a benchmark of autonomous discovery. A direct `$` mention injects skill content and may not call view_skill.

The deployed OpenWebUI 0.11.4 discovery path could expose other active, readable skills even when only one was selected on the model. Earlier unrelated skill calls included obsolete adventure instructions. The tested prompt clause names the exact skill and excludes other catalog instructions for this adventure. The 0.12.2 tool-search compatibility update does not itself establish a skill allowlist. Recheck deployed behavior after any upgrade; do not attribute these successful tests to an unverified version change.

## Tool and actual player

Adventure Kit 2.1.0 was exported from the live editor and tested in STEM Adventure Games (Clone), based on DeepSeek V4 Flash 0731. The actual call was `render_adventure` with supplied schema-version-2 JSON text, theme `cuny-blue`, and text_speed `0`. The result reported `render_requested`, one node, four choices, two endings, and three state keys. The embedded interactive player visibly appeared in the chat.

The supplied Seedling Comparison fixture is a fictional classroom simulation. It is separate from the reusable code. This controlled-input test does not establish automatic historical source-to-scenario conversion. The exported tool contains no built-in scenario, genre, or fixed completion threshold.

Hosted actions passed: a prerequisite blocked an early choice; the valid sequence reached the supplied completion rule; Undo returned to active play; Stop halted without completion; Copy Play Record displayed its success message. Initial capture displayed Bauhaus despite a cuny-blue request; a reload displayed CUNY Blue, so the mismatch did not reproduce. Keep this observation in the evidence record rather than claiming an established theme defect.

The existing Model Bound Tool Enabler was selected during the successful tests. It restores model-attached tool IDs when chat state omits them. A with/without comparison was not run, so necessity is not established. Explain its conditional purpose before Adventure Kit and do not enable it globally.


## Access and Support

Adventure Kit and Adventure Outcomes showed Private/no grants at inspection. The owner then reported granting participant read access to both; post-change visibility remains unverified. Extend Adventure Games is now the opening skill, so verify participant visibility of that saved resource too without expanding permissions or exposing student identifiers.

Earlier CAIL Workspace Support returned a separate labeled Adventure Outcomes proposal with an explicitly unrun test. It was not installed or retested. That proposal is not an opening skill or proof of the new orchestration workflow. The current Support activity is general: revise or create a skill or tool, preserve the original, and test the actual saved result.

[Participant exercises](exercises.html) · [Hosted evidence](hosted-evidence.html)
