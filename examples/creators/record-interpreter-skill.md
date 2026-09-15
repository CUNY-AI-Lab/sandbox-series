Skill Name: STEM Adventure Record Interpreter
Skill ID: stem-adventure-interpreter
Skill Description: Use this skill to analyze and summarize STEM Adventure play records while checking for internal consistency between actions and results.

Skill Instructions:
1. Parse the JSON to extract the commands array, events array, and the result object.
2. Check for internal consistency by comparing the command and event history against the result state.
3. Verify that each entry in the events array contains a command, a validity boolean, and text.
4. Summarize the journey and state, treating any completion status unsupported by the history or user-supplied success labels as reported evidence only and requesting a full record or replay.

Proposed Tests:

Test 1 (Boundary) [NOT RUN]
Input: `{"commands":[], "events":[], "result":{"room":"Prism Laboratory", "inventory":[], "flags":[], "complete":true}}`
Expected Behavior: Flag the `complete: true` status as unsupported by the empty command and event history, describe it only as a reported value, and request a full record or replay.

Test 2 (Incomplete Record) [NOT RUN]
Input: `{"result":{"room":"Storage"}}`
Expected Behavior: Identify the record as incomplete due to the absence of the commands array, events array, and the full result object.
