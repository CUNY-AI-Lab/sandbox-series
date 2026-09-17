# Compare Wikipedia Revisions

## Model Description

Compare paired passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.

## Model Setup

| Field | Value |
| --- | --- |
| Name | Compare Wikipedia Revisions |
| Base Model | Gemma 4 26B A4B IT |
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

1. Context
2. Procedure
3. Constraints
4. Format

## Prompt Suggestions

1. Compare these before-and-after excerpts about academic freedom. Classify one change and quote evidence for your decision.
2. Check whether this revision changes a claim’s meaning or only its wording. Explain any uncertainty.
3. Review my classification against these excerpts. Identify any category that needs different evidence.

## Workshop Progression

Workshop 1 uses one provided revision pair to test system prompt instructions. Workshop 2 can add a classification guide and saved examples as a knowledge collection. Workshop 3 can introduce a skill for repeating these steps and a tool for retrieving specified public revisions.
