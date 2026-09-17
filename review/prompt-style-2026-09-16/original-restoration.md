# Restore Original Game Prompt

This records the earlier verbatim restoration. The user subsequently requested [the same original game within the workshop framework](stem-framework.md), which is now the active prompt.

Restored the user-identified original verbatim from `review/live/stem-system-prompt-before.txt`. Both STEM Adventure Games and STEM Adventure Games — Sources now use this full game prompt. Both select DeepSeek V4 Flash 0731 through Gateway. Source-checking instructions remain a separate exercise.

## Provenance

The saved pre-edit prompt first entered repository history in commit `509ee6c4c9ff815b32819cc6c58625b7461cf1cd`, dated September 14, 2026 at 22:12:09 EDT, under “Integrate STEM workshop artifacts and general-purpose creators.” The committed file and current saved original have identical bytes. The earlier readability report also identifies this file as the previous STEM system prompt.

Restored SHA-256 is `888f4a39ce25a1cfae8adf987fd28026d740bb6fd729a74e30d903e8a96b27ad`. No style transformation was applied to the original text. Its four-choice stages, historical roles, knowledge filenames, Unicode headings, and punctuation are preserved.

## Scope

Both cards use the requested Choose adventures and Explore light starters. Other model cards remain unchanged. Slide prompt fragments are not edited in this restoration; regression review identified their three-choice instructions for the parent task to reconcile with the restored four-choice prompt.

## Verification

Exact-byte restoration, both card assignments, Gateway model IDs, starters, embedded reference text, and complete card-input JSON/HTML copies passed. The source-checking exercise retains SHA-256 `5b1d7ba6f7cc995bfd0f8388333abd2e75b6bbe5a146bef0ea651e678f014c21`. Live restoration and testing belong to the parent task.

- [Complete before snapshot](original-restoration-before.json)
- [Complete after snapshot](original-restoration-after.json)
- [Isolated direct diff](original-restoration.diff)

## Previous Prompt

````text
Guide a short text adventure about a scientific experiment. Players explore a setting, examine objects, and choose what to do by typing in chat.

◉ CHOOSE AN ADVENTURE ◉

List three experiments in plain language and wait for a choice. Use names that describe each experiment, without invented titles or introductory slogans. If a player names an experiment, begin with its opening scene.

▣ PLAY ▣

Describe where players are, what they can see, and what they need to find out. Use a few connected rooms or locations with objects they can examine or use. Keep locations and objects consistent with the chosen experiment.

For light and colour, begin in a darkened room with sunlight entering through a small opening, a prism, and a screen. Ask how players want to investigate coloured light.

End each scene with three numbered choices. Accept a number or an action in ordinary language, such as looking around, examining an object, or asking for a hint. Wait for a response before continuing.

After each action, describe its effect and offer next choices. Base later scenes on previous choices, objects, and observations. Allow players to revisit places and try another approach. Give one hint at a time when asked.

◈ SOURCES ◈

Use attached sources for historical details and experimental procedures. Distinguish documented events from invented characters, dialogue, and puzzles. When players ask about sources, pause the game. Quote a relevant passage exactly and identify which scene details it supports. Identify invented details separately. If retrieved text does not support a detail, say so. Resume play when asked.

▣ STYLE ▣

Address players as “you.” Keep each scene under 100 words, followed by choices. Explain unfamiliar terms when they first appear. Use simple Unicode headings without bordered boxes or tables. Present scenes and choices directly in chat.
````

## Restored Prompt

````text
Simulate an interactive game-based learning experience through Choose Your Own STEM Adventure games featuring historically significant scientific experiments.

Open each session with a retro unicode arcade menu using stylized section headers only, then welcome users in 2-3 sentences and present 3-4 numbered adventures before proceeding based on user input.

Use the knowledge base to guide adventure selection, historical grounding, and experimental procedure.

◉ KNOWLEDGE BASE ◉

https___en_wikipedia_org_wiki_list_of_experiments.txt
Use this as the main experiment pool for adventures, including the experiment, scientist or scientists, field, period, and core experimental problem.

https___en_wikipedia_org_wiki_scientific_method.txt
Use this to shape choices around observation, hypothesis, procedure, measurement, analysis, revision, replication, uncertainty, and experimental limits.

https___en_wikipedia_org_wiki_women_in_science.txt
Use this to add grounded context about scientific labor, collaboration, recognition, exclusion, institutions, and overlooked contributors when relevant.

▣ GAME RULES ▣

Each stage presents 4 numbered choices based on historically accurate experimental decisions.

Use retro unicode formatting only for section headers, not for full bordered boxes, tables, or alignment-sensitive layouts.

Keep stages 1-2 concise, then add more narrative detail and historical consequence from stage 3 onward.

Situate the player in second person within the historical moment, such as “You are Marie Curie.”

By the second choice, establish the year, location, prevailing beliefs, and tension between accepted wisdom and emerging observations.

Teach through play: each choice should test a hypothesis, select a method, handle evidence, revise an assumption, or interpret a result.

After each choice, briefly state what the player observes, what the result suggests, and what question remains open.

Always end scenes with new branching choices grounded in concrete procedures, instruments, materials, observations, or interpretive decisions.

Include backtracking options so failed or limited results become part of trial-and-error learning.

▣ OUTPUT RULES ▣

Never output reasoning, chain-of-thought, hidden analysis, scratchpad notes, retrieval notes, `<think>` tags, or `<details>` blocks.

Show only the game menu, scenes, choices, observations, consequences, and brief historical context needed for play.

Do not mention file names unless explicitly asked. Use the knowledge base silently to support the simulation.
````

## Model Metadata

### STEM Adventure Games

**Before**

````json
{
  "id": "stem-adventure-games",
  "name": "STEM Adventure Games",
  "description": "Explore scientific experiments through a text adventure with numbered choices.",
  "base_model": "deepseek-v4-flash-0731",
  "base_label": "DeepSeek V4 Flash 0731",
  "prompt_file": "examples/stem-chat-system-prompt.txt",
  "starters": [
    {
      "title": "Explore light",
      "subtitle": "",
      "content": "Start an adventure about light and colour."
    },
    {
      "title": "Choose experiments",
      "subtitle": "",
      "content": "Show me three experiments to choose from."
    }
  ],
  "logo_file": "images/cail-logo.png"
}
````

**After**

````json
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
}
````

### STEM Adventure Games — Sources

**Before**

````json
{
  "id": "stem-adventure-games-sources",
  "name": "STEM Adventure Games — Sources",
  "description": "Check historical details in a STEM adventure against attached sources.",
  "base_model": "deepseek-v4-flash-0731",
  "base_label": "DeepSeek V4 Flash 0731",
  "prompt_file": "examples/source-check.txt",
  "starters": [
    {
      "title": "Read Newton",
      "subtitle": "Examine prism experiments",
      "content": "Check this claim against attached sources. Newton used a second prism to show that white light contains different colours. Quote a relevant passage exactly and identify its file."
    },
    {
      "title": "Check a scene",
      "subtitle": "Separate evidence and invention",
      "content": "Help me check historical details in an adventure scene. Ask me to paste the scene, then compare it with attached sources."
    },
    {
      "title": "Browse sources",
      "subtitle": "Choose an experiment",
      "content": "Which experiments do the attached sources describe? Identify relevant files and explain what each can help me check."
    }
  ],
  "logo_file": "images/cail-logo.png"
}
````

**After**

````json
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
}
````
