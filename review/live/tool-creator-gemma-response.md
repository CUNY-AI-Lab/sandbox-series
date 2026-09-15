**Tool Name:** Play-Record Validator
**Tool ID:** play_record_validator
**Tool Description:** Validates a JSON-encoded play-record containing a sequence of commands and their corresponding execution outcomes. Ensures sequence integrity, command limits, and data structure validity.

### Python Code

```python
import json

class Tools:
    def validate_play_record(self, json_input: str) -> dict:
        """
        Validates a JSON play-record for structural integrity and command-event alignment.

        :param json_input: A JSON string containing 'commands' (list of strings)
                           and 'events' (list of objects with 'command' and 'valid' keys).
        :return: A dictionary containing 'total_commands' and 'failed_commands',
                 or a dictionary with an 'error' key describing the violation.
        """
        # 1. Input Size Constraint
        if len(json_input) > 50000:
            return {"error": "Input exceeds 50,000 character limit."}

        # 2. JSON Parsing
        try:
            data = json.loads(json_input)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format."}

        # 3. Structure Validation
        if not isinstance(data, dict):
            return {"error": "Root must be a JSON object."}

        commands = data.get("commands")
        events = data.get("events")

        if not isinstance(commands, list) or not isinstance(events, list):
            return {"error": "Missing or invalid 'commands' or 'events' arrays."}

        # 4. Command Count Constraint
        command_count = len(commands)
        if command_count > 300:
            return {"error": "Command count exceeds 300 limit."}

        # 5. Count Mismatch Check
        event_count = len(events)
        if command_count != event_count:
            return {"error": f"Mismatch: {command_count} commands vs {event_count} events."}

        # 6. Value and Integrity Validation
        failed_commands = []
        for i in range(command_count):
            cmd_val = commands[i]
            event_val = events[i]

            # Verify event structure
            if not isinstance(event_val, dict) or "command" not in event_val or "valid" not in event_val:
                return {"error": f"Event at index {i} is missing required 'command' or 'valid' fields."}

            # Verify value matching (Command name must match Event command name at same index)
            if event_val["command"] != cmd_val:
                return {"error": f"Mismatch: command name at index {i} ('{cmd_val}') does not match event record ('{event_val['command']}')."}

            # Verify 'valid' is boolean
            if not isinstance(event_val["valid"], bool):
                return {"error": f"Event at index {i} 'valid' field must be a boolean."}

            # Collect failures
            if event_val["valid"] is False:
                failed_commands.append(cmd_val)

        return {
            "total_commands": command_count,
            "failed_commands": failed_commands
        }
```

### Installation Steps

1.  Open your **Workspace**.
2.  Navigate to **Tools** and select **Create**.
3.  Enter the following details:
    *   **Name:** Play-Record Validator
    *   **ID:** `play_record_validator`
    *   **Description:** Validates JSON play-records for command/event alignment and limits.
4.  Paste the **Python Code** provided above into the code editor.
5.  Click **Save & Create**.
6.  To use the tool, go to **Integrations** > **Tools** in a chat session or attach it to a model in the **Workspace** and click **Save & Update**.

### Tests
*Note: The following tests are provided for verification purposes and have not been run.*

#### Test 1: Ordinary Input (Success/Partial Failure)
*   **Input:**
    ```json
    {
      "commands": ["move_up", "jump", "move_down"],
      "events": [
        {"command": "move_up", "valid": true},
        {"command": "jump", "valid": false},
        {"command": "move_down", "valid": true}
      ]
    }
    ```
*   **Expected Result:** `{"total_commands": 3, "failed_commands": ["jump"]}`
*   **Observed Result:** [PENDING]

#### Test 2: Malformed Input (Syntax Error)
*   **Input:** `{"commands": ["attack"], "events": [{"command": "attack", "valid": true}` (Missing closing braces)
*   **Expected Result:** `{"error": "Invalid JSON format."}`
*   **Observed Result:** [PENDING]

#### Test 3: Mismatched Values/Counts (Logic Error)
*   **Input:**
    ```json
    {
      "commands": ["run", "slide"],
      "events": [
        {"command": "run", "valid": true},
        {"command": "jump", "valid": true}
      ]
    }
    ```
*   **Expected Result:** `{"error": "Mismatch: command name at index 1 ('slide') does not match event record ('jump')."}`
*   **Observed Result:** [PENDING]
