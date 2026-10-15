# Adventure Kit Source

Open Workspace → Tools and select Adventure Kit. Click inside code editor, then use Select All and Copy. On this Mac, use ⌘A and ⌘C. Copy complete code, including lines outside visible screen. Preserve original before revision.

[Read complete Adventure Kit 2.1.0 source](adventure-kit.py)

This source was exported from the live Adventure Kit on October 15 and is the version used in the revised-tool hosted test. The published Python file contains only tool code; owner IDs and access metadata from the private export are excluded.

Hosted export SHA-256 `e7637bcb621a7149cd3ad2af812ae9b3e6fff2b923d644f91bf1b5bd9e28ac65`

Published Python SHA-256 `3d4af23b1e34334596cc5256a251393654bdfe858aafc0180ecc402b9f23f888`. Five blank lines had trailing spaces removed for repository formatting; executable statements and game logic are unchanged.

The function is render_adventure. It accepts reviewed schema-version-2 JSON text in scenario_json, plus optional theme and text_speed. The code has no default story, genre, or completion threshold. Setting, goals, choices, consequences, and endings come from the approved input. Empty or invalid input requests correction before play.

Active custom model system prompt defines adventure setting, goals, and rules. Both components must follow it. Ask when required instructions are absent or contradictory.

The historical examples/tools/stem_adventure.py file belongs to the earlier generated demonstration. Use the source linked on this page for the October 15 Adventure Kit exercise.

[Input contract](scenario-contract.html) · [Participant exercises](../../skills/exercises.html)
