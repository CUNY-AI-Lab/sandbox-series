import json

class Tools:
    def validate_play_record(self, json_input: str) -> dict:
        """
        Validates a JSON play-record for structural integrity, type correctness, and alignment.

        :param json_input: A JSON string containing 'commands' (list of strings)
                           and 'events' (list of objects with 'command' and 'valid' keys).
        :return: A dictionary containing 'total_commands' and 'failed_commands',
                 or a dictionary with an 'error' key describing the violation.
        """
        # 1. Input Type Validation
        if not isinstance(json_input, str):
            return {"error": "Input must be a string."}

        # 2. Input Size Constraint
        if len(json_input) > 50000:
            return {"error": "Input exceeds 50,000 character limit."}

        # 3. JSON Parsing
        try:
            data = json.loads(json_input)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format."}

        # 4. Structure Validation
        if not isinstance(data, dict):
            return {"error": "Root must be a JSON object."}

        commands = data.get("commands")
        events = data.get("events")

        if not isinstance(commands, list) or not isinstance(events, list):
            return {"error": "Missing or invalid 'commands' or 'events' arrays."}

        # 5. Command Count Constraint
        command_count = len(commands)
        if command_count > 300:
            return {"error": "Command count exceeds 300 limit."}

        # 6. Count Mismatch Check
        event_count = len(events)
        if command_count != event_count:
            return {"error": f"Mismatch: {command_count} commands vs {event_count} events."}

        # 7. Value and Integrity Validation
        failed_commands = []
        for i in range(command_count):
            cmd_val = commands[i]
            event_val = events[i]

            # Verify command type
            if not isinstance(cmd_val, str):
                return {"error": f"Command at index {i} must be a string."}

            # Verify event structure
            if not isinstance(event_val, dict) or "command" not in event_val or "valid" not in event_val:
                return {"error": f"Event at index {i} is missing required 'command' or 'valid' fields."}

            # Verify event command type
            event_cmd_val = event_val["command"]
            if not isinstance(event_cmd_val, str):
                return {"error": f"Event command at index {i} must be a string."}

            # Verify value matching (Command name must match Event command name)
            if event_cmd_val != cmd_val:
                return {"error": f"Mismatch: command name at index {i} ('{cmd_val}') does not match event record ('{event_cmd_val}')."}

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
