### Skill & Tool Examples

Choose an example to adapt for your teaching or research.

[Return to workshop](./) · [System prompt examples](../examples.html)[Write Instructions](#write-instructions) · [Check Interpretations](#check-interpretations) · [Check Skill Drafts](#check-skill-drafts) · [Check Generated Code](#check-generated-code) · [Test Game Commands](#game-commands)

### Write Instructions

Describe when to use your skill, which steps to follow, and when to pause.

Paste into Instructions under Workspace → Skills → Create.

```text
Use this skill when [specific request or action].

1. [First step]
2. [Next step]
3. [What to check before continuing]
4. [When to wait for user input]

Format responses as [required structure].
```

### Check Interpretations

Use this draft to check an interpretation against a source passage.

Paste into Instructions under Workspace → Skills → Create.

```text
When the user asks whether a passage supports a claim, ask for both if either is missing.

1. Quote the relevant passage and identify its source. Do not invent missing metadata.
2. State what the passage directly supports.
3. Identify an inference or competing reading that needs further evidence.
4. Ask one question that would help resolve the difference, then wait.

Keep the quotation separate from your interpretation. If the source is unavailable, explain what cannot be checked.
```

Test it with supported, overstated, and unsupported claims from public or approved material.

### Check Skill Drafts

This example has no commands or events but reports completion. Can a skill establish that play occurred?

```text
{"commands":[],"events":[],"result":{"complete":true}}
```

An empty history cannot establish completion. Request a full record or replay.

Send this example to Kale Skill Builder with your skill draft. Check whether revised instructions flag missing evidence.

[Read corrected skill draft](../examples/creators/record-interpreter-skill.md) · [Inspect initial response](../review/live/skill-builder-consistency-failure.md)

### Check Generated Code

This recorded test checks a separate draft tool that validates play records. Each command must be text.

```text
{"commands":[42],"events":[{"command":42,"valid":false}]}
```

Expected behavior is to reject numeric commands. Initial creator output accepted them.

Send observed failure back to Tool Creator, then repeat your tests.

[Inspect original draft](../review/live/record-validator-before.py) · [Read corrected tool](../examples/creators/record-validator.py) · [Review executed tests](../review/live/tool-creator-corrected-tests.json)

### Test Game Commands

Enter each command separately inside Prism Laboratory.

```text
go north
take prism
take screen
go south
go east
open shutter
use prism
use screen
test red light
record result
```

Immediately after take prism, repeat take prism and check its response before continuing.

[Download commands](../examples/adventure/winning-commands.json)
