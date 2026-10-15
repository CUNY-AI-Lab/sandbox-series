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

Add the [orchestration clause](exercises.html#add-skill-instructions) to your model’s system prompt. It calls Extend Adventure Games to coordinate Adventure Kit. Select both in the same model card and Save & Update before testing. Adventure Kit 2.1.0 exposes `render_adventure` with reviewed schema-version-2 JSON text in `scenario_json`; that function and argument were verified in the earlier hosted Clone invocation. The new orchestration sequence remains a separate live check.

Read the actual result. `needs_context` and `invalid_input` require correction before play. `render_requested` requests a player display; inspect the rendered player before calling it successful. The model needs the player’s copied Play record to discuss button choices, progress, or completion

## Model Bound Tool Enabler

Filters run before tool execution and can change a request. The existing CAIL Model Bound Tool Enabler filter restores tool IDs already attached to a model when chat composer state omits them. It does not make a model call a function or invent a missing tool binding

Enable **Model Bound Tool Enabler** on your model card before adding Adventure Kit. It restores attached tools when a chat omits them. Keep the card open, check the knowledge collection, tool, skill, and filter, add the orchestration prompt, then Save & Update before testing. This exercise uses the existing filter on your model card.

The filter cannot fix unsupported function calling, malformed arguments, execution errors or a failed display. If the tool is absent from your model's attachments, attach it first. If it is present in the request schema but never called, inspect model support and call mode

## Evidence Status

The October 15 test used the user-authorized STEM Adventure Games (Clone), based on DeepSeek V4 Flash 0731. Adventure Kit 2.1.0 was actually called and rendered an interactive player. Prerequisite, completion, Undo, Stop, and Copy Play Record checks passed. The existing Model Bound Tool Enabler was selected. Its necessity remains unverified because no with/without hosted comparison was run. Local checks of ID merging do not establish necessity

Generic tool and skill content contain no built-in adventure. Design your scene from your active model's system prompt. Resolve missing or contradictory goals before execution and copy actual Play record before discussing an executable run in chat

[Slides](index.html) · [Participant exercises](exercises.html) · [Facilitator notes](facilitator.html)
