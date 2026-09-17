# Compare Wikipedia Edits

## Model Description

Choose a Wikipedia article or browse recent edits, then compare revisions with quoted evidence.

## Model Setup

| Field | Value |
| --- | --- |
| Name | Compare Wikipedia Edits |
| Base Model | DeepSeek V4 Flash 0731 |
| Connection | Gateway |
| Access | Private |
| Sandbox Model | [Open private model](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions) |
| Function Calling | Native |
| Capabilities | File Upload, File Context, Citations, Status Updates, Web Search, Builtin Tools |
| Builtin Tools | Web Search only; all other categories disabled |
| Other Capabilities | Disabled, including Memory |
| Default Features | Web Search |
| System Prompt | [system-prompt.txt](system-prompt.txt) |
| Knowledge | None for Workshop 1 |
| Skills | None for Workshop 1 |
| Tools | None for Workshop 1 |

Choose an article by topic, title, or link, or ask for recently edited articles in chat. You can also paste or attach your own revision pair. [Sample revisions](sample-revisions.md) provide an optional worked example.

## Prompt Sections

1. Purpose
2. Procedure
3. Constraints
4. Format

## Prompt Suggestions

### Browse recent edits

Find recently updated articles

````text
Show me three recently edited Wikipedia articles so I can choose one to compare.
````

### Choose an article

Use a topic, title, or link

````text
Help me choose a Wikipedia article by topic, title, or link.
````

### Compare provided excerpts

Use a revision pair

````text
I will paste before-and-after excerpts with revision IDs and links. Classify one change and quote evidence for your decision.
````

## Workshop Progression

Workshop 1 uses one retrieved or pasted revision pair to test system prompt instructions. Reuse the same passages and revision links when comparing the original model and a clone. Workshop 2 can add a classification guide and saved examples as a knowledge collection. Workshop 3 can introduce a skill for repeating these steps and a custom tool for retrieving specified public revisions.
