# Restore Game Excerpts

Restored excerpt uses three complete paragraphs quoted verbatim from `review/live/stem-system-prompt-before.txt`. Procedure and format examples change only “three numbered choices” to “four numbered choices.” No original system prompt text was edited.

## stem-game-excerpt

### Before

```text
End each scene with three numbered choices. Accept a number or an action in ordinary language, such as looking around, examining an object, or asking for a hint. Wait for a response before continuing.
```

### After

```text
Simulate an interactive game-based learning experience through Choose Your Own STEM Adventure games featuring historically significant scientific experiments.

Each stage presents 4 numbered choices based on historically accurate experimental decisions.

After each choice, briefly state what the player observes, what the result suggests, and what question remains open.
```

## tpl-procedure

### Before

```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer three numbered choices and wait.
4. Describe what players observe after each choice.
```

### After

```text
1. Introduce an experiment about light and colour.
2. Describe an opening scene and a question to investigate.
3. Offer four numbered choices and wait.
4. Describe what players observe after each choice.
```

## tpl-format

### Before

```text
Write a short scene followed by three numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```

### After

```text
Write a short scene followed by four numbered choices.
Use simple Unicode headings.
Wait for a reply before continuing.
```

## Source Custody

Appended allowed replacements for source slides 23 and 26 and updated their current prompt replacements. Original disciplinary baselines remain unchanged. Full affected custody records are preserved in [before snapshot](restored-stem-excerpts.before.json) and [after snapshot](restored-stem-excerpts.after.json).

[Isolated excerpt diff](restored-stem-excerpts.diff)
