# Review STEM Prompts

This records the earlier style pass. The user subsequently requested the original game within [the workshop framework](stem-framework.md). The failed List of experiments import was later [repaired and verified](knowledge-repair/README.md), superseding the Advanced prompt’s error warning shown in this historical record.

Applied humanizer, no-ai-slop, and milwrite-style in that order to `examples/stem-chat-system-prompt.txt` and `examples/stem-system-prompt.txt`. These are operational system prompts. Short commands retain their function; no sentence was expanded merely to meet a length target.

## Humanizer Pass

Most existing sentences already gave concrete instructions. Unicode headings, source names, necessary lists, and functional prohibitions were retained. No finding rests on an isolated word or presumed authorship.

- “Grounded in scientific sources” left source use abstract. “Use scientific sources to explain its experiments” names what the model should do.
- Plain chat repeated its instruction to acknowledge unsupported details. One instruction now follows requests to quote evidence and distinguish invented details.
- “A generated scenario is a candidate” used a status label without specifying what could be claimed. “Mark generated scenarios as untested until their commands run successfully” preserves the boundary directly.

## Syntax Pass

- “Review the message box, and send their record” separated the object to inspect from the object to send. Revised wording identifies the record in the message box and refers to it consistently.
- “A winning sequence and a blocked-action check” compressed two different checks. Revised wording identifies commands that complete a game and an action that stays blocked until its prerequisites are met.
- “A source comparison” did not identify the objects being compared. Revised wording asks for a comparison between an observation and a source passage.
- Instructions to inspect records precede interpretation. Tool calls, playback, source checks, and response rules remain in their original order.

## Voice Pass

Revisions use actions and named objects. Extend STEM Adventures is introduced as a skill and STEM Wikipedia Experiments as a knowledge collection. The advanced prompt still distinguishes game output, historical accounts, and interpretation. Teaching and research remain supported without assigning users a purpose.

Original source titles `Newton: Light and Colour` and `Newton: Experimental Variants` retain their punctuation. No other colon appears in either prompt. Uppercase Unicode headings retain the requested game appearance.

## Preserve Behavior

- Plain chat still offers three experiments, accepts an experiment named by a player, describes connected locations, tracks earlier choices and observations, permits revisiting, and gives one hint at a time.
- The full scene excerpt is byte-for-byte unchanged, including three numbered choices, ordinary-language actions, and waiting for a response.
- Plain chat still pauses for source questions, quotes relevant passages exactly, distinguishes invented details, and resumes when asked. No tool, skill, JSON, or engine contract was added.
- Advanced play retains `render_stem_adventure` with empty `scenario_json`, Prism Laboratory, Integrations > Tools, `help`, `discuss`, `save`, `load`, `view_skill`, scenario requirements, completion checks, and the ban on executable scenario data.
- Named sources, the failed List of experiments import, Web Search attribution, limits on interpreting game results, and protections against invented moves and exposed scratchpad text remain.

## Compare Text

Plain chat changed from 310 to 301 words. Advanced changed from 481 to 532 words because abbreviated checks and unfamiliar resource names now have explicit instructions. No new game feature or historical assertion was added.

[Complete before and after](stem-before-after.md) contains both full prompts. [Isolated diff](stem-revision.diff) includes only changes made in this pass. Original and revised files are also saved separately with `.before.txt` and `.after.txt` suffixes. [Checks](stem-checks.json) records hashes and preservation results.

[Card copy](stem-card-copy.json) contains draft descriptions and beginner starters for plain chat, attached sources, and advanced play. Plain chat starters require no documents or tools. Source starters ask about the attached collection. Advanced starters cover starting Prism Laboratory, saving progress, and changing an experiment.

These edits passed exact-excerpt, named-contract, Unicode, punctuation, JSON, and whitespace checks. HTML integration and live Sandbox testing belong to the parent task and were not performed here.
