# Preserve Live Base Selections

The parent task reopened the live cards and reported Tool Creator on Kimi K2.7 Code (`kimi-k2.7-code`) and Compare Wikipedia Edits on DeepSeek V4 Flash 0731 (`deepseek-v4-flash-0731`). This local synchronization preserves those observed choices. No live setting was changed by this edit.

Earlier Tool Creator tests used Qwen3 Coder Next. Earlier research tests used Gemma 4 26B A4B IT. Their results do not establish behavior of Kimi or DeepSeek on those cards; the parent task is retesting current settings.

The local Gateway capture predates this readback and has no Kimi record. The parent task supplied the currently observed Kimi ID and label. The existing Gateway capture includes the exact DeepSeek ID and label.

`builder-copy.json` contains no base-model fields and remains unchanged. Model descriptions, starters, and prompt contents were not changed in this metadata update.

- [Complete before snapshot](live-base-readback.before.json)
- [Complete after snapshot](live-base-readback.after.json)
- [Direct diff](live-base-readback.diff)

## Before and After

### examples/model-cards.json

#### Before

````text
{
  "models": [
    {
      "id": "stem-adventure-games",
      "name": "STEM Adventure Games",
      "description": "Explore scientific experiments through a text adventure with numbered choices.",
      "base_model": "deepseek-v4-flash-0731",
      "base_label": "DeepSeek V4 Flash 0731",
      "prompt_file": "examples/stem-chat-system-prompt.txt",
      "starters": [
        {
          "title": "Choose adventures",
          "subtitle": "",
          "content": "Show me the adventure menu."
        },
        {
          "title": "Explore light",
          "subtitle": "",
          "content": "Start an adventure about Newton’s experiments with light and colour."
        }
      ],
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "stem-adventure-games-sources",
      "name": "STEM Adventure Games — Sources",
      "description": "Explore scientific experiments through a text adventure with numbered choices.",
      "base_model": "deepseek-v4-flash-0731",
      "base_label": "DeepSeek V4 Flash 0731",
      "prompt_file": "examples/stem-chat-system-prompt.txt",
      "starters": [
        {
          "title": "Choose adventures",
          "subtitle": "",
          "content": "Show me the adventure menu."
        },
        {
          "title": "Explore light",
          "subtitle": "",
          "content": "Start an adventure about Newton’s experiments with light and colour."
        }
      ],
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "stem-adventure-games-advanced",
      "name": "STEM Adventure Games — Advanced",
      "description": "Play Prism Laboratory, then review or change its experimental procedures.",
      "base_model": "deepseek-v4-pro-0813",
      "base_label": "DeepSeek V4 Pro 0813",
      "prompt_file": "examples/stem-system-prompt.txt",
      "starters": [
        {
          "title": "Start playing",
          "subtitle": "",
          "content": "Start Prism Laboratory."
        },
        {
          "title": "Save progress",
          "subtitle": "",
          "content": "How can I save my progress?"
        },
        {
          "title": "Change experiments",
          "subtitle": "",
          "content": "Help me change an experiment and test whether it works."
        }
      ],
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "cail-sandbox-skill-builder",
      "name": "Kale Skill Builder",
      "description": "Create, revise, and test reusable skills for CAIL Sandbox.",
      "prompt_file": "examples/creators/skill-creator-system-prompt.txt",
      "starters": [
        {
          "title": "Create a skill",
          "subtitle": "for a recurring task",
          "content": "Help me create a reusable skill. I will describe my task, required inputs, and expected output."
        },
        {
          "title": "Revise a skill",
          "subtitle": "using observed results",
          "content": "Help me revise an existing skill. I will provide its instructions, a test request, and the output that needs to change."
        }
      ],
      "base_model": "deepseek-v4-flash-0731",
      "base_label": "DeepSeek V4 Flash 0731",
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "cail-sandbox-tool-creator",
      "name": "CAIL Tool Creator",
      "description": "Create, revise, and test Python tools for CAIL Sandbox.",
      "prompt_file": "examples/creators/tool-creator-system-prompt.txt",
      "starters": [
        {
          "title": "Create a tool",
          "subtitle": "for a specific task",
          "content": "Help me create a Python tool for Open WebUI. I will describe its inputs, expected output, and any required data access."
        },
        {
          "title": "Revise a tool",
          "subtitle": "using observed results",
          "content": "Help me revise an existing Python tool for Open WebUI. I will provide its code, a test input, and the result that needs to change."
        }
      ],
      "base_model": "qwen3-coder-next",
      "base_label": "Qwen: Qwen3 Coder Next",
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "compare-wikipedia-revisions",
      "name": "Compare Wikipedia Edits",
      "description": "Compare passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.",
      "base_model": "gemma-4-26b-a4b-it",
      "base_label": "Gemma 4 26B A4B IT",
      "prompt_file": "examples/research/system-prompt.txt",
      "starters": [
        {
          "title": "Start comparing",
          "subtitle": "Choose revision excerpts",
          "content": "Help me compare a revision of Wikipedia’s academic freedom article. What passages and links should I provide?"
        },
        {
          "title": "Classify changes",
          "subtitle": "Use provided excerpts",
          "content": "I will paste before-and-after excerpts with revision IDs and links. Classify one change and quote evidence for your decision."
        },
        {
          "title": "Review classifications",
          "subtitle": "Check quoted evidence",
          "content": "I will paste a classification with its before-and-after excerpts, revision IDs, and links. Check whether the quoted evidence supports it."
        }
      ],
      "logo_file": "images/cail-logo.png"
    }
  ]
}
````

#### After

````text
{
  "models": [
    {
      "id": "stem-adventure-games",
      "name": "STEM Adventure Games",
      "description": "Explore scientific experiments through a text adventure with numbered choices.",
      "base_model": "deepseek-v4-flash-0731",
      "base_label": "DeepSeek V4 Flash 0731",
      "prompt_file": "examples/stem-chat-system-prompt.txt",
      "starters": [
        {
          "title": "Choose adventures",
          "subtitle": "",
          "content": "Show me the adventure menu."
        },
        {
          "title": "Explore light",
          "subtitle": "",
          "content": "Start an adventure about Newton’s experiments with light and colour."
        }
      ],
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "stem-adventure-games-sources",
      "name": "STEM Adventure Games — Sources",
      "description": "Explore scientific experiments through a text adventure with numbered choices.",
      "base_model": "deepseek-v4-flash-0731",
      "base_label": "DeepSeek V4 Flash 0731",
      "prompt_file": "examples/stem-chat-system-prompt.txt",
      "starters": [
        {
          "title": "Choose adventures",
          "subtitle": "",
          "content": "Show me the adventure menu."
        },
        {
          "title": "Explore light",
          "subtitle": "",
          "content": "Start an adventure about Newton’s experiments with light and colour."
        }
      ],
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "stem-adventure-games-advanced",
      "name": "STEM Adventure Games — Advanced",
      "description": "Play Prism Laboratory, then review or change its experimental procedures.",
      "base_model": "deepseek-v4-pro-0813",
      "base_label": "DeepSeek V4 Pro 0813",
      "prompt_file": "examples/stem-system-prompt.txt",
      "starters": [
        {
          "title": "Start playing",
          "subtitle": "",
          "content": "Start Prism Laboratory."
        },
        {
          "title": "Save progress",
          "subtitle": "",
          "content": "How can I save my progress?"
        },
        {
          "title": "Change experiments",
          "subtitle": "",
          "content": "Help me change an experiment and test whether it works."
        }
      ],
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "cail-sandbox-skill-builder",
      "name": "Kale Skill Builder",
      "description": "Create, revise, and test reusable skills for CAIL Sandbox.",
      "prompt_file": "examples/creators/skill-creator-system-prompt.txt",
      "starters": [
        {
          "title": "Create a skill",
          "subtitle": "for a recurring task",
          "content": "Help me create a reusable skill. I will describe my task, required inputs, and expected output."
        },
        {
          "title": "Revise a skill",
          "subtitle": "using observed results",
          "content": "Help me revise an existing skill. I will provide its instructions, a test request, and the output that needs to change."
        }
      ],
      "base_model": "deepseek-v4-flash-0731",
      "base_label": "DeepSeek V4 Flash 0731",
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "cail-sandbox-tool-creator",
      "name": "CAIL Tool Creator",
      "description": "Create, revise, and test Python tools for CAIL Sandbox.",
      "prompt_file": "examples/creators/tool-creator-system-prompt.txt",
      "starters": [
        {
          "title": "Create a tool",
          "subtitle": "for a specific task",
          "content": "Help me create a Python tool for Open WebUI. I will describe its inputs, expected output, and any required data access."
        },
        {
          "title": "Revise a tool",
          "subtitle": "using observed results",
          "content": "Help me revise an existing Python tool for Open WebUI. I will provide its code, a test input, and the result that needs to change."
        }
      ],
      "base_model": "kimi-k2.7-code",
      "base_label": "Kimi K2.7 Code",
      "logo_file": "images/cail-logo.png"
    },
    {
      "id": "compare-wikipedia-revisions",
      "name": "Compare Wikipedia Edits",
      "description": "Compare passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.",
      "base_model": "deepseek-v4-flash-0731",
      "base_label": "DeepSeek V4 Flash 0731",
      "prompt_file": "examples/research/system-prompt.txt",
      "starters": [
        {
          "title": "Start comparing",
          "subtitle": "Choose revision excerpts",
          "content": "Help me compare a revision of Wikipedia’s academic freedom article. What passages and links should I provide?"
        },
        {
          "title": "Classify changes",
          "subtitle": "Use provided excerpts",
          "content": "I will paste before-and-after excerpts with revision IDs and links. Classify one change and quote evidence for your decision."
        },
        {
          "title": "Review classifications",
          "subtitle": "Check quoted evidence",
          "content": "I will paste a classification with its before-and-after excerpts, revision IDs, and links. Check whether the quoted evidence supports it."
        }
      ],
      "logo_file": "images/cail-logo.png"
    }
  ]
}
````

### examples/research/model-card.md

#### Before

````text
# Compare Wikipedia Edits

## Model Description

Compare passages from Wikipedia’s academic freedom article. Classify changes and explain each decision with quoted evidence.

## Model Setup

| Field | Value |
| --- | --- |
| Name | Compare Wikipedia Edits |
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
````

#### After

````text
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
````
