# Creator prompt review

Reviewed only Skill Creator and Tool Creator system prompts, with descriptions and starter prompts in `builder-copy.json`. Applied humanizer, no-ai-slop, then milwrite-style. Short instructions remain where brevity makes requirements easier to follow.

## Changed wording

- Replaced “Keep research, teaching, and other uses open” with an instruction to follow the user's stated purpose. The original phrase left “open” undefined.
- Named Skill Description and Skill Instructions in their respective directions, and made missing tool contracts explicit where “they” had an unclear referent.
- Replaced “immediate $ invocation” with a direct description of invoking a skill with `$`.
- Named tool code as the item users review, connected public methods to their `Tools` class, and clarified that size checks apply to input.
- Combined repeated directions about unavailable documentation. Missing details must still be identified as unverified.
- Required error messages to explain what failed, preserving the restriction on disclosing secrets. Clarified the ban on executable code passed in by a model.
- Added “revise” to both descriptions and the Tool Creator opening. Added a second Tool Creator starter for revising existing code using test input and an observed result. Existing starters remain verbatim, with two starters now available for each creator.

## Live Test Corrections

Live tests in the parent task showed Skill Creator inventing an unspecified task and formatting literal `$` as mathematics. Its prompt now asks for the task and waits before drafting, and formats `$` and `view_skill` as inline code. The card now uses DeepSeek V4 Flash 0731.

Tool Creator asked for a name when the requested operation was already clear. Its prompt now proposes Tool Name and Tool ID when missing, reserving questions for inputs, expected output, or data access needed for a useful draft. Existing code and evidence guards remain unchanged. A later test found expected results that contradicted generated code. Tool Creator now reconciles expected results with stated behavior and generated code, and labels unexecuted tests. See [isolated test-expectation correction](tool-test-expectations.md). These changes await live retesting by the parent task.

[Complete before-and-after correction record](live-corrections.md) includes these prompt edits and model settings.

## Preserved requirements

IDs, source URLs, literal UI labels, installation paths, and API syntax are unchanged. The local builder record now uses “CAIL Tool Creator,” preserving the name confirmed through live readback. The original local “Tool Creator” label remains visible in before snapshots. Both creators remain general purpose. The prompts retain validation before processing, wrong-type tests, helpers outside `Tools`, credential protection, restricted execution, evidence for claimed actions, separate expected and observed results, participant access checks, and testing before claims of success. Interactive tool requirements still cover escaping, iframe isolation, keyboard behavior, height reporting, reload persistence, and user review before sending a record.

No editable prose contains colon punctuation. Colons remain only in URLs and required API syntax, including `Content-Disposition: inline` and `input:prompt`. No source claims or platform behavior were added. Technical prohibitions and qualifications remain direct because they define required behavior.

## Verification

The initial pass passed all 29 copy regression checks then present. Additional checks confirmed unchanged source URLs, IDs, prompt file references, and existing starters; two starters per creator; and absence of colons in editable prose. The final review also checks current card names against the manifest. See [final review](final-review.md) for current results. Live model changes and behavior tests belong to the parent task and are not claimed here.

## Complete comparison

- [Full original text](creators-before.md)
- [Full revised text](creators-after.md)
- [Isolated direct diff](creators.diff)
- [Original text as JSON](creators-before.json)
- [Revised text as JSON](creators-after.json)

Original text was captured before edits. The diff contains this creator revision and the verified model-name correction, independent of other work in the shared checkout. No HTML, test source, or other prompt was edited in this pass.
