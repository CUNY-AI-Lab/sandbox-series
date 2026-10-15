# Hosted Evidence

October 15, 2026 · STEM Adventure Games (Clone) · DeepSeek V4 Flash 0731

## Adventure Outcomes

The saved resource was explicitly loaded through native `view_skill` with `{"id":"adventure_outcomes"}`. Its returned name and instructions matched the selected skill. This was not a direct `$` mention or an autonomous discovery benchmark.

With a supplied record showing no measured growth and a choice that changed both light and water, the response rejected the player's unsupported success claim and did not declare completion. It asked for a numbered choice when the follow-up was ambiguous. The stop request produced one sentence and no further choices.

![Actual saved-skill call and response](../images/skills-2026-10-15/adventure-outcomes-hosted.svg)

## Adventure Kit 2.1.0

The revised tool was exported and tested in a fresh Clone chat. The actual function was `render_adventure`, with reviewed schema-version-2 JSON text in `scenario_json`, theme `cuny-blue`, and text_speed `0`. The returned result reported `render_requested`, title Seedling Comparison, and sizes of one node, four choices, two endings, and three state keys. The embedded interactive player appeared in the same chat.

![Actual tool call and embedded player](../images/skills-2026-10-15/adventure-kit-hosted.svg)

| Action | Observed result |
| --- | --- |
| Vary light before baseline | Blocked; state unchanged |
| Record baseline, vary light, compare simulated growth | Supplied completion rule matched; status complete |
| Undo | Returned to active; observed false; ending null |
| Stop | Status stopped; no false completion; choices removed |
| Copy Play Record | Play record copied confirmation |

The fictional classroom fixture was supplied to the tool; it is not embedded in the reusable code. This test does not establish automatic conversion of every model prompt or historical source. Initial screenshot displayed Bauhaus despite a cuny-blue argument; CUNY Blue appeared after reload, and the mismatch did not reproduce.

## Limits and access

The existing Model Bound Tool Enabler was selected during testing; a with/without comparison was not run. Both saved resources showed Private with no access grants at inspection. No participant account access or permission expansion is claimed. Screenshots record actual UI; annotations identify observed controls and results.

[Exercises](exercises.html) · [Adventure Outcomes](../examples/adventure-kit/adventure-outcomes.html) · [Tool source](../examples/adventure-kit/source.html)

## Access follow-up

After the private-access inspection, the owner reported granting participant read access to both Adventure Kit and Adventure Outcomes. The post-change participant visibility check remains unverified because browser control was stopped. No access change was made by this task.

## Support rehearsal

CAIL Workspace Support returned a complete separate “Adventure Outcomes — Labeled Trial” proposal, an explanation, and an explicitly unrun test. The proposal adds an outcome label while preserving clarification and immediate-stop exceptions. The original Adventure Outcomes remains the selected workshop skill. Creating the separate trial and running its live retest were not completed before browser control stopped. No successful retest of that proposal is claimed.
