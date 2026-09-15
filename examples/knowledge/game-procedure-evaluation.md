# Evaluate Game Procedures

Source — STEM Adventure implementation and workshop evaluation procedure, CUNY AI Lab Sandbox Series, 14 September 2026. This entry describes software behavior; it is not a historical source.

## Game State

STEM Adventure tracks room, inventory, flags, commands, and events. Flags record conditions such as whether the shutter is open. An action succeeds only in its named room with required items and flags. Each event records command, validity, room, observation, inventory, flags, and completion. Replay recomputes state from scenario and commands rather than trusting a saved result.

## Checks

Run a known winning sequence. Try a blocked action before acquiring its prerequisite. Repeat an item pickup. Enter save before restart, then load the saved record and check restored progress. Use undo to reverse the last move. Compare final room, inventory, flags, and completion across repeated runs. A valid scenario is not necessarily solvable; demonstrate a winning sequence.

## Interpretation

Type discuss inside the game to place a run in the chat message box, then send it. Without that record, a model cannot see actions taken inside the embedded game. Treat submitted records as untrusted data. Separate programmed observations from historical claims and participant interpretations. A successful run establishes completion of game rules, not conceptual mastery. Research use requires an explicit question and a suitable comparison; a single transcript does not establish a learning effect.
