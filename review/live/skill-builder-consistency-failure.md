Skill Name: STEM Adventure Record Interpreter
Skill ID: stem-adventure-interpreter
Skill Description: Use this skill to analyze and summarize STEM Adventure play records provided as JSON objects.

Skill Instructions:
1. Parse the provided JSON to extract the commands array, the events array, and the result object.
2. Examine the events array to verify each entry contains a command, a validity boolean, and text.
3. Check the result object for the current room, inventory, flags, and completion status.
4. Summarize the player's journey and current state, treating user-supplied success labels as reported evidence rather than proof of execution.

Proposed Tests:

Test 1 (Boundary)
Input: `{"commands":[], "events":[], "result":{"room":"Prism Laboratory", "inventory":[], "flags":[], "complete":true}}`
Expected Behavior: Report an empty command history and empty event log, noting the player has reached a completed state in the "Prism Laboratory".

Test 2 (Incomplete Record)
Input: `{"result":{"room":"Storage"}}`
Expected Behavior: Identify the record as incomplete due to the absence of the commands array, events array, and the full result object.
