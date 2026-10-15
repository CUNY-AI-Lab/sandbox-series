# Adventure Input

Adventure Kit 2.0.0 · Hosted save and readback recorded October 14

Active custom model system prompt defines setting, goals, and rules. The model translates those instructions into Adventure Kit data. Ask about absent or contradictory context before play. Review that translation with the participant; generic JSON support alone does not prove prompt fidelity

The tool has no built-in adventure. Test fixtures remain separate from reusable code and skill. Blank input requests context rather than substituting a story

## Data Fields

Required fields are schema_version (2), title, introduction, start, state, nodes, and endings. Each node has name, text, and choices. Each choice has a unique id, visible label, and result text. Optional to changes node; when controls validity; effects alter declared state

State values may be numbers, strings, booleans, or lists of strings. Conditions compare declared variables through eq, ne, gt, gte, lt, lte, or includes. all, any, and not combine conditions. Effects use set, add, append, or remove with key and value

Each ending declares id, label, text, status (complete or failed), terminal (true or false), and when. Empty endings permits open-ended play. First matching ending has priority. A nonterminal ending permits continued choices. Undo replays earlier choices and recalculates outcomes; Stop halts immediately without claiming completion

Optional objective displays a participant-defined goal. global_choices applies choices across nodes. sources records supplied id, text, and optional URL when a prompt requires source evidence. The tool does not retrieve or verify sources

## Evidence

Open Play record in the v2 player and copy actual choices, rule results, and state into chat. Narrative skill guidance cannot alter that state. A copied record may become stale after Undo, Restart, or another action

## Current Hosted Version

Dated preparation records confirm stem_adventure v2.0.0 after an authorized save. Exact exports preserve v1.1.0 and v2.0.0, with ID, owner and Private access unchanged. V2 has no built-in adventure or old blank-input fallback. Older rooms/actions/goal_flags content needs explicit conversion to schema version 2. Participant access and full prompt-to-tool acceptance remain unverified

[Copy current source](source.html) · [Participant exercises](../../skills/exercises.html)
