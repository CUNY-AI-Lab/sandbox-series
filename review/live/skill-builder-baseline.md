Here's the draft.

---

**Name:** STEM Adventure

**ID:** stem-adventure

**Description:** Loads for STEM Adventure requests. Handles two jobs from supplied information only: editing one experimental procedure via `render_stem_adventure`, and interpreting a supplied play record. Does not infer player actions or invent tool results.

---

**Content:**

## Directive

Operate the STEM Adventure tool from supplied information only. Two jobs: (1) change one experimental procedure by editing the scenario JSON and calling `render_stem_adventure`, and (2) interpret a supplied play record. The tool owns rooms, inventory, prerequisites, and completion. Never invent a successful tool call, never infer clicks or player actions before a record is sent, and never make web requests.

## Instructions

1. Identify the request: a procedure change or a play-record interpretation.

2. For a procedure change, confirm the exact edit with the user before touching the JSON. Ask which step changes and what it becomes. Wait for the answer.

3. Edit only that step in the scenario JSON. Leave rooms, inventory, prerequisites, and completion to the tool. If no scenario was supplied, ask for it before editing.

4. Call `render_stem_adventure(scenario_json=...)`. Report only what the tool actually returned. Do not say the game completed, unlocked, or succeeded unless the return value says so.

5. For a play record, wait until the record is supplied. Interpret only what the record shows — describe the state changes (rooms, inventory, prerequisites, completion) and flag anything it does not show rather than guessing. End by offering one next step and waiting.

## Output

Procedure change:

> Changed step 3 to "Heat the sample to 80°C for 10 minutes." Called `render_stem_adventure` with the updated scenario. The tool returned: [paste actual return]. No other steps changed.

Play record:

> The record shows the player entered the lab and added reagent A. The prerequisite "reagent B added" is still unmet. The record does not show any click on the heat source, so I can't say whether heating occurred.

---

**Matching test (should trigger):** "Change step 2 of the procedure so the sample is heated to 80°C instead of 60°C."

**Unrelated test (should not trigger):** "Summarize the causes of the French Revolution."

---

These tests are proposed, not run. Want me to tighten the description, adjust the step count, or add a guardrail section for edge cases (e.g., a record that contradicts the scenario)?
