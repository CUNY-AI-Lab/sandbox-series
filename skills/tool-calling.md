# Check Tool Calling

When a model calls a tool, it sends a function name and arguments. Sandbox executes that function and returns a result. This is tool calling, otherwise known as function calling. A statement that a tool will run is not execution evidence

## Check Your Configuration

Use your private model copy. Record its ID, base model, system prompt, calling mode and attached tools. Confirm Adventure Kit is available and selected. Inspect actual call details after a test and retain errors and returned data

| Stage | Record |
| --- | --- |
| Configuration | Model and base IDs, Native function calling, attached tool ID and available schema |
| Request | Exact prompt and supplied adventure context |
| Call | Emitted function name and complete arguments |
| Execution | Returned status, result or error |
| Display | Actual rendered player and one observed action |
| Response | Model follow-up compared with returned data |

## Add Instructions Before Testing

Every participant adds the [tool-calling clause](exercises.html#add-tool-instructions) to their model’s system prompt, saves it, and preserves the existing adventure instructions. The clause calls `render_adventure` with reviewed schema-version-2 JSON text in `scenario_json` after the player approves the adventure. This function and argument are verified in the October 14 hosted 2.0.0 export. Current model binding and outgoing schema remain live checks

Read the actual result. `needs_context` and `invalid_input` require correction before play. `render_requested` requests a player display; inspect the rendered player before calling it successful. The model needs the player’s copied Play record to discuss button choices, progress, or completion

## Model Bound Tool Enabler

Filters run before tool execution and can change a request. The existing CAIL Model Bound Tool Enabler filter restores tool IDs already attached to a model when chat composer state omits them. It does not make a model call a function or invent a missing tool binding

Use this conditional check before implementing your adventure. If call details show a model-attached tool is missing, inspect the existing filter on your private model card, select it if available, save your copy and repeat the identical test in a fresh chat. Confirm the current filter before use. Do not install a replacement or enable it globally for this exercise

The filter cannot fix unsupported function calling, malformed arguments, execution errors or a failed display. If the tool is absent from your model's attachments, attach it first. If it is present in the request schema but never called, inspect model support and call mode

## Evidence Status

Earlier agent preparation verified Adventure Kit execution in a separate DeepSeek V4 Flash 0731 QA configuration with Native calling and supplied fictional material. Current STEM model invocation and a live enabler comparison remain unverified. Eleven local checks verified the preserved enabler's ID-merging behavior. Those checks used no hosted model

Generic tool and skill content contain no built-in adventure. Design your scene from your active model's system prompt. Resolve missing or contradictory goals before execution and copy actual Play record before discussing an executable run in chat

[Slides](index.html) · [Participant exercises](exercises.html) · [Facilitator notes](facilitator.html)
