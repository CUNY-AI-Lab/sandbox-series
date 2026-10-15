# Adventure Input

Adventure Kit 2.1.0 · Exported and hosted-tested October 15

Active custom model system prompt defines setting, goals, and rules. The model translates those instructions into Adventure Kit data. Ask about absent or contradictory context before play. Review that translation with the participant; generic JSON support alone does not prove prompt fidelity

The tool has no built-in adventure. Test fixtures remain separate from reusable code and skill. Blank input requests context rather than substituting a story

## Data Fields

Required fields are schema_version (2), title, introduction, start, nodes, and endings. State is optional and defaults to an empty object; declare variables before using them in conditions or effects. Each node has name, text, and choices. Each choice has a unique id, visible label, and result text. Optional to changes node; when controls validity; effects alter declared state

State values may be numbers, strings, booleans, or lists of strings. Conditions compare declared variables through eq, ne, gt, gte, lt, lte, or includes. all, any, and not combine conditions. Effects use set, add, append, or remove with key and value

Each ending declares id, label, text, status (complete or failed), terminal (true or false), and when. Empty endings permits open-ended play. First matching ending has priority. A nonterminal ending permits continued choices. Undo replays earlier choices and recalculates outcomes; Stop halts immediately without claiming completion

Optional objective displays a participant-defined goal. global_choices applies choices across nodes. sources records supplied id, text, and optional URL when a prompt requires source evidence. The tool does not retrieve or verify sources

## Evidence

Open Play record in the v2 player and copy actual choices, rule results, and state into chat. Narrative skill guidance cannot alter that state. A copied record may become stale after Undo, Restart, or another action

## Current Hosted Version

The live October 15 export identifies version 2.1.0 and tool ID stem_adventure. Its function is render_adventure(scenario_json, theme, text_speed). scenario_json is JSON text. Themes are cuny-blue, linux-terminal, classic-arcade, and bauhaus. Default theme is cuny-blue and default text speed is 75. Server validation checks rule references before requesting a render.

The Clone test rendered the supplied scenario and passed prerequisite, completion, Undo, Stop, and Copy Play Record checks. The test fixture is separate from the reusable code. Participant access remains a separate check.

[Copy current source](source.html) · [Participant exercises](../../skills/exercises.html)
