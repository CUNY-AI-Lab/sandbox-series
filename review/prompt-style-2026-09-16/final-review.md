# Final Prompt Review

Reviewed six model cards and their complete system prompts on September 17, 2026, after refreshing references from `examples/model-cards.json`. The initial copy review changed no active prompt. Subsequent live failures prompted bounded corrections. The user then requested the original game prompt for both introductory STEM cards and clarified that its tone and Wikipedia sources should be retained within Purpose, Procedure, Constraints, and Format.

## Findings

The initial local review found no further wording defect. Live tests then identified missing-task and routine-naming behavior that required more explicit instructions. Current prompts identify what users provide, what models should do, and where conclusions depend on source material or observed results. Short sentences serve operational requirements. The game prompt now preserves the original register while organizing instructions into the workshop framework. Its archived source remains verbatim. In other prompts, colon punctuation remains only in source titles, URLs, and required API syntax. Exact model IDs and display labels remain source-bound.

| Model | Scope and evidence limits checked |
| --- | --- |
| STEM Adventure Games | Organizes the original prompt into Purpose, Procedure, Constraints, and Format while preserving three or four menu adventures, four choices per stage, historical roles, backtracking, and silent knowledge use. |
| STEM Adventure Games — Sources | Uses the same game prompt and framework. The source-checking prompt remains a separate exercise. |
| STEM Adventure Games — Advanced | Retains named tool and skill contracts, explicit transfer of play records into chat, untested-scenario limits, and separate treatment of game observations, historical evidence, and interpretation. |
| Kale Skill Builder | Remains general purpose, requests missing contracts, treats records as data, and distinguishes claimed success from observed behavior. |
| CAIL Tool Creator | Remains general purpose, retains validation and restricted execution, and separates drafted code, expected results, and observed tests. |
| Compare Wikipedia Edits | Uses Purpose, Procedure, Constraints, and Format. Retains exact quotation, revision identifiers, multiple applicable categories, uncertainty, and limits on inferences about editors. |

## Metadata Correction

Current creator records and comparison headings use “CAIL Tool Creator,” preserving the name confirmed through live readback in the parent task. Its local base record now preserves the parent task’s live Kimi K2.7 Code selection, with canonical ID `kimi-k2.7-code`. Compare Wikipedia Edits likewise preserves the observed DeepSeek V4 Flash 0731 selection. Earlier behavior tests used Qwen for Tool Creator and Gemma 4 for research; they do not verify these current bases. [Complete metadata comparison](live-base-readback.md) records both changes. The original local before snapshot still records “Tool Creator” because that was the captured text.

Creator after snapshots, isolated diff, and combined comparison now include this correction. The temporary reference generator also includes complete before-and-after creator metadata, so another synchronization will preserve that comparison.

## Live Test Follow-up

Skill Creator now asks for a task before drafting and formats `$` and `view_skill` as inline code. Tool Creator proposes missing names and IDs without delaying code for routine naming. It checks expected test results against stated behavior and generated code, resolves mismatches, and labels unexecuted tests. Skill Creator uses DeepSeek V4 Flash 0731. At the user’s request, plain STEM Adventure Games and Sources use DeepSeek V4 Flash 0731 through Gateway. Both introductory STEM cards now use the original game menu starters. The source-checking exercise remains unchanged.

[Complete before-and-after correction record](live-corrections.md) and [isolated diff](live-corrections.diff) document these changes. Current card-inputs JSON and HTML match the manifest and complete prompt files. Final Firefox readback confirmed exact saved prompts, descriptions, starters, base IDs, and custom logos for all six cards. Both introductory game cards include the evidence constraint, which asks the game to verify dates, locations, and experimental claims against passages and distinguish documented details from invention. [Complete before and after](stem-evidence.md) and [isolated diff](stem-evidence.diff) record that addition. A fresh playtest confirmed the four-choice game structure but still invented an earlier player action. [Live checks](live-tests.md) distinguish passing observations from remaining failures.

## Original Restoration

The user first requested restoration of the original game prompt, then clarified that it should retain its tone and three Wikipedia articles within the workshop framework. Both introductory STEM cards now use that revision and remain on DeepSeek Flash through Gateway. [Complete framework comparison](stem-framework.md) shows the original and revised prompt, exact hashes, and source-preservation checks. The [earlier restoration record](original-restoration.md) preserves that prior step.

## Knowledge Repair

The parent task replaced the failed List of experiments content in its existing Knowledge file, saved it, closed it, and reopened it. Persisted text matched the complete prepared article after trimming surrounding whitespace, including revision 1371680817; the rate-limit error was absent. The local source register and Advanced prompt now use the repaired article as an overview for selecting experiments and checking relevant passages. After that readback, a fresh Sources chat quoted the matching Pasteur passage exactly from the repaired article and identified its original filename. This verifies that retrieval in Legacy mode with Builtin Tools disabled, not retrieval of every attached file in every turn.

[Repair provenance](knowledge-repair/provenance.json), [copy diff](knowledge-repair/repair-copy.diff), and [source-register transfer page](knowledge-repair/source-register-import.html) preserve the evidence and updated wording. Other original article entries remain unchanged.

## Verification

All 32 copy regression tests and seven teaching-and-research sequence tests passed. Series checks passed for the current 90 slides and 34 imported sections, and `git diff --check` passed. Additional checks confirmed complete prompt and starter text in the model-card catalogue, both introductory cards’ shared game-prompt assignment, two or three starters per card, and absence of colons in editable prose. Current hashes are recorded in [final-review.json](final-review.json).

These checks cover local copy and synchronization in the merged 90-slide version. The completed slide audit found no broken images or console errors across all slides at 1280 × 720, with additional mobile samples. All 31 interaction checks and 19 background checks passed.

Current live checks cover the game sequence, repaired-source quotation, advanced game completion, Skill Creator response, Kimi Tool Creator output, and Flash research comparison. Ten independent local tests passed for Kimi’s generated code; two proposed test expectations needed correction. Research quoted accurately and declined an unsupported motive inference, but overstated certainty elsewhere. The generated tool was not installed in Sandbox. Participant-account verification remains deferred at the user’s direction. [Live checks](live-tests.md) record these boundaries; [saved-card readback](live-readback.json) records exact configuration matches.

- [Complete comparison](COMPARISON.md)
- [Combined direct diff](PROMPTS.diff)
- [Creator comparison](creators-review.md)
- [Current model cards](../../examples/model-cards.md)
