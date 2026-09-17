## Example Navigation

[Examine Assumptions](#assumptions) · [STEM Adventure Games](#stem-chat) · [Check Game Sources](#stem-sources) · [Advanced Game Instructions](#stem-system)

## Model Card

# Compare Wikipedia Revisions

Draft for review before live configuration.

## Model Description

Compare paired passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.

## Model Settings

| Field | Value |
| --- | --- |
| Name | Compare Wikipedia Revisions |
| Base Model | Gemma 4 26B A4B IT |
| Connection | Gateway |
| Access | Private |
| System Prompt | [system-prompt.txt](system-prompt.txt) |
| Knowledge | None for Workshop 1 |
| Skills | None for Workshop 1 |
| Tools | None for Workshop 1 |

Confirm base model availability in Gateway before saving. Users paste or attach paired excerpts with revision IDs and source links in chat. This draft contains no invented revisions or source passages.

## Prompt Suggestions

1. Compare these before-and-after excerpts about academic freedom. Classify one change and quote evidence for your decision.
2. Check whether this revision changes a claim’s meaning or only its wording. Explain any uncertainty.
3. Review my classification against these excerpts. Identify any category that needs different evidence.

## Workshop Progression

Workshop 1 uses one provided revision pair to test system prompt instructions. Workshop 2 can add a classification guide and saved examples as a knowledge collection. Workshop 3 can introduce a skill for repeating these steps and a tool for retrieving specified public revisions.
