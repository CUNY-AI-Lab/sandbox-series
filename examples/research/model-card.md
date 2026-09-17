# Compare Wikipedia Edits

## Model Description

Compare passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.

## Model Setup

| Field | Value |
| --- | --- |
| Name | Compare Wikipedia Edits |
| Base Model | DeepSeek V4 Flash 0731 |
| Connection | Gateway |
| Access | Private |
| Sandbox Model | [Open private model](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions) |
| Capabilities | File Upload, File Context, Citations, Status Updates |
| Other Capabilities | Disabled, including Web Search, Memory, and Builtin Tools |
| Default Features | None |
| System Prompt | [system-prompt.txt](system-prompt.txt) |
| Knowledge | None for Workshop 1 |
| Skills | None for Workshop 1 |
| Tools | None for Workshop 1 |

Paste or attach [sample revisions](sample-revisions.md) with revision IDs and source links in chat.

## Prompt Sections

1. Purpose
2. Procedure
3. Constraints
4. Format

## Prompt Suggestions

### Start comparing

Choose revision excerpts

````text
Help me compare a revision of Wikipedia’s academic freedom article. What passages and links should I provide?
````

### Classify changes

Use provided excerpts

````text
I will paste before-and-after excerpts with revision IDs and links. Classify one change and quote evidence for your decision.
````

### Review classifications

Check quoted evidence

````text
I will paste a classification with its before-and-after excerpts, revision IDs, and links. Check whether the quoted evidence supports it.
````

## Workshop Progression

Workshop 1 uses one provided revision pair to test system prompt instructions. Workshop 2 can add a classification guide and saved examples as a knowledge collection. Workshop 3 can introduce a skill for repeating these steps and a tool for retrieving specified public revisions.
