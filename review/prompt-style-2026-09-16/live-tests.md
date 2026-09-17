# Live Model Checks

Recorded 17 September 2026 from live Sandbox checks in Firefox. Configuration names follow [model-cards.json](../../examples/model-cards.json).

## Current Configuration

Authenticated Firefox readback verified the latest saved configuration for both **STEM Adventure Games** and **STEM Adventure Games — Sources**. Each uses the full game prompt organized under Purpose, Procedure, Constraints, and Format, with DeepSeek V4 Flash 0731 through Gateway. Saved prompt text, description, and starters match the current local files. Both have the CUNY AI Lab logo and attached Knowledge, with no custom Tools or Skills attached. Both now use Legacy function calling with Builtin Tools disabled.

The latest [shared game prompt](../../examples/stem-chat-system-prompt.txt) has SHA-256 `93e9a68f88c21c1d0e6dff2b93e2b4e561ddbc39883ad6b3ae62319aaa7ca459`. Exact saved text includes this final constraint:

> Check dates, locations, and experimental claims against source passages; distinguish documented details from invented scenes and choices, and state what cannot be verified.

The original game instructions were restored at the user's request, then reorganized within the workshop framework. The constraint above followed the gameplay failures recorded below. A fresh plain-game test after that addition confirmed the requested menu and scene structure, while exposing a remaining inconsistency in the narrated play history.

Live selections for **CAIL Tool Creator** and **Compare Wikipedia Edits** are now **Kimi K2.7 Code** and **DeepSeek V4 Flash 0731**, respectively. Those external selections were preserved. The earlier Qwen and Gemma 4 tests below do not validate the current bases.

## Knowledge Repair

The original List of experiments entry was repaired with article text from revision [1371680817](https://en.wikipedia.org/w/index.php?title=List_of_experiments&oldid=1371680817). After saving and reopening, its complete text matched the prepared article text. The earlier Wikimedia error is no longer its current content.

The [source register](../../examples/knowledge/source-register.md) was also saved and reopened. Its editor text matched the prepared 1,402-character entry, including the repaired article's revision ID. These checks establish saved content, not successful retrieval or accurate interpretation in every model response.

## Final Game Test

This fresh chat used **STEM Adventure Games** with the final prompt identified above and DeepSeek V4 Flash 0731.

| Request | Observed result |
| --- | --- |
| Open adventure menu | Offered four adventures involving Newton, Pasteur, Michelson–Morley, and Curie. Acknowledged that only a subset of source material had been provided rather than claiming to have read all three Wikipedia articles. |
| Choose option 2 | Opened a Pasteur scene set in Paris in 1861, with four experimental choices. |
| Choose option 2 again | Described clear broth in a swan-neck flask, followed by Observation, What this suggests, and Question still open. Offered four new choices, including Backtrack. |

The menu, numbered choices, scene progression, response sections, and backtracking option appeared as requested in this sequence. Backtracking itself was not exercised in this run. The second scene nevertheless referred to growth supposedly observed in earlier straight-necked flasks, although the player had not performed that branch. That invented play history remains a failure of narrative consistency.

This run verifies the observed game structure, not every adventure or historical and scientific claim. It does not establish that the final constraint eliminated factual errors. The separate Sources card has the same saved prompt, but its recorded menu trial below preceded the last constraint.

## Current Research Test

**Compare Wikipedia Edits**, using its current DeepSeek V4 Flash 0731 base, requested before-and-after passages, revision IDs, and links when invoked through its starter.

For [sample revisions](../../examples/research/sample-revisions.md) 1346428851 → 1346430780, it quoted both sentences exactly, classified removal of “outside” as Changed qualification, and explained how that broadens the definition's scope. It also overstated certainty by treating complete supplied passages as grounds for saying no unresolved questions remained. Its interpretation still requires review.

A subsequent political-motivation request was declined. The response distinguished the visible change from “outside interference” to “interference” from any explanation of why an editor made it, and stated that passages alone cannot establish political motivation. These observations concern this revision pair and follow-up, not general classification reliability.

## Game Tests Before Final Constraint

These runs used the full four-section game prompt before its added date, location, and experimental-claim constraint.

| Configuration and request | Observed result |
| --- | --- |
| Sources menu with native function calling | Stalled after listing Knowledge, viewing two files, and searching source text. The run was canceled; Sources was returned to Legacy function calling. |
| Sources menu after returning to Legacy | Produced four adventures in 30.47 seconds. |
| Plain game menu | Produced four choices in 13.99 seconds. |
| Plain game, choose option 4 | Initial request returned a Gateway JSON parsing error. A retry produced a scene with four choices in 15.39 seconds. |
| Plain game, next choice | Produced observations, an open question, and four choices including backtracking in 23.39 seconds. The response also contained unsupported date and optics claims. |

The unsupported claims prompted the final constraint now saved in both introductory cards. A prompt change alone does not establish that those failures are fixed. Timings describe these individual responses, not typical performance.

## Other Recorded Runs

| Model | Base model | Observed result |
| --- | --- | --- |
| STEM Adventure Games — Advanced | DeepSeek V4 Pro 0813 | Called `render_stem_adventure` and opened embedded game. `help` and `go` commands worked. `record result` stayed blocked before prerequisites were met; a subsequent winning sequence completed the game. |
| Kale Skill Builder | DeepSeek V4 Flash 0731 | Generic starter asked about task, inputs, and expected output. Bibliography request produced four fields, five steps, quotations of original entries, and ordinary-input and already-clean-input tests. Inline `$` appeared without a KaTeX error. |
| Compare Wikipedia Edits | Gemma 4 26B A4B IT, previous base | Asked for missing revision IDs, passages, and links. Classified removal of “outside” as Changed qualification and quoted before-and-after passages exactly. A later request to infer political motivation was declined. These results do not validate its current Flash base. |

## Superseded Introductory Tests

These tests used prompts replaced after the user requested the original game. They remain historical observations, not current results for the full four-section game prompt.

| Earlier configuration | Base model | Historical result |
| --- | --- | --- |
| STEM Adventure Games with the rewritten three-choice prompt | DeepSeek V4 Flash 0731 through Gateway | Explore light produced a short opening scene and three numbered choices. No tool or skill controls appeared. |
| STEM Adventure Games — Sources with the standalone source-checking prompt | DeepSeek V4 Flash 0731 through Gateway | Native function calling retrieved attached sources. Response cited Newton: Light and Colour.txt and newton-experimental-variants.md, identifying them as summaries rather than primary texts. Quotation check appears below. |

In that source-checking test, native function calling and Builtin Tools had to be enabled. Earlier disabled capability settings prevented native retrieval. Successful retrieval called `list_knowledge`, `query_knowledge_files`, `grep_knowledge_files` twice, and `view_file` twice. This records the earlier configuration, not a fresh retrieval test of the restored game.

## Historical Quotation Check

The superseded source-checking configuration produced this passage.

> He then used two pierced boards and another prism to compare refraction of light selected from different parts of the spectrum. His account argues that sunlight contains rays with different refrangibility.

Both sentences match line 9 of [newton-light-colour.md](../../examples/knowledge/newton-light-colour.md) verbatim. This verifies that earlier quotation from a workshop source summary. It does not verify quotation from Newton's primary text or behavior of the current full game prompt.

Verified local file SHA-256 is `92d8e125b6011e4238e74903d07b5759220cc800ad6bbb728b5253c476bfb7a7`.

## Current Tool Creator Test

CAIL Tool Creator, using Kimi K2.7 Code, returned the requested line-counting tool in 33.06 seconds. It proposed Tool Name and Tool ID without asking an unnecessary naming question, supplied installation instructions, and explicitly marked its proposed tests **UNEXECUTED**. This is one observed response, not a general reliability or timing result.

Its [exact generated source](line-counter-kimi-generated.py) was saved unchanged and executed locally with isolated Python startup (`python3 -I`). All ten independent checks passed.

| Check | Expected and observed result |
| --- | --- |
| Ordinary input with three nonblank lines and 21 characters | `{"success": true, "count": 3, "length": 21}` |
| Whitespace-only input, including Unicode spaces, 8 characters | `{"success": true, "count": 0, "length": 8}` |
| Empty string | `{"success": true, "count": 0, "length": 0}` |
| Chinese text, Greek text, and emoji on three nonblank lines, 10 characters | `{"success": true, "count": 3, "length": 10}` |
| 10,000 non-whitespace characters | `{"success": true, "count": 1, "length": 10000}` |
| Integer input `42` | `success` false; `Expected a string, got int.` |
| List input `["line"]` | `success` false; `Expected a string, got list.` |
| `None` input | `success` false; `Expected a string, got NoneType.` |
| 10,001 characters | `success` false; `Input is 10001 characters; maximum allowed is 10000.` |
| Five calls on the same `Tools` instance | Counts `2, 0, 2, 0, 1` and lengths `7, 0, 7, 2, 4`; values did not carry between calls |

The initial proposed test table contained two mistakes, separate from these passing code checks. For `名前\n\n漢字\n`, it expected length 9; the actual length is 7. For the boundary expression `"a\n" * 5001`, a comment said 10,001 characters although the expression produces 10,002. Its expected error for 10,002 was correct. Direct local rechecks confirmed that the generated code returns count 2 and length 7 for the Unicode example, and correctly rejects the 10,002-character input.

After feedback, Kimi corrected the expected Unicode length to 7 and supplied `('a\n' * 5000) + 'a'` for an exact 10,001-character boundary input. It continued to label the proposed tests unexecuted. This corrects the table; local execution evidence remains the independent checks recorded above.

Source SHA-256 is `cc5c3c1110c776ba799b5bac147ff50f3af51305683c6943fdc5976f9975f74d`. Source bytes were unchanged after execution. The generated code was not installed in Sandbox, and an Open WebUI tool invocation was not tested. Live evidence covers generation and proposed setup instructions; execution evidence comes from local tests.

## Earlier Qwen Checks

These checks concern code produced when CAIL Tool Creator used Qwen3 Coder Next. Its current Kimi K2.7 Code selection has not been validated by these runs. An initial Qwen draft contained an incorrect expected-results table. Revised system prompt instructions require checking expected results against stated behavior and generated code.

The final Qwen response in that test generated a line-counting tool. Its [exact source](line-counter-generated.py) was saved unchanged and executed locally with isolated Python startup (`python3 -I`). All ten checks passed.

| Check | Expected and observed result |
| --- | --- |
| Ordinary input, three nonblank lines separated by blank and space-only lines | `{"count": 3}` |
| Whitespace-only input, including tabs, line breaks, em space, and nonbreaking space | `{"count": 0}` |
| Empty string | `{"count": 0}` |
| Chinese text, Greek text, and emoji on three lines, with blank and whitespace-only lines | `{"count": 3}` |
| 10,000 non-whitespace characters | Accepted with `{"count": 1}` |
| Integer input `42` | `TypeError`, `Input must be a string` |
| List input `["line"]` | `TypeError`, `Input must be a string` |
| `None` input | `TypeError`, `Input must be a string` |
| 10,001 characters | `ValueError`, `Input exceeds maximum allowed length of 10,000 characters` |
| Five calls on the same `Tools` instance | Counts `2, 0, 2, 0, 1`; counts did not carry between calls |

Source SHA-256 is `cd3333f47c594def51a78f9652111a82adebe49be993d13bbfe4a4a6aa09236c`. Source bytes were unchanged after execution. These checks establish local behavior of this generated tool. The code was not installed as a public Sandbox tool, and its execution through Open WebUI was not tested.

## Remaining Checks

The earlier Qwen-based CAIL Tool Creator asked for a name despite instructions to propose Tool Name and Tool ID when absent. That unnecessary question did not occur in the current Kimi run, and its test-table errors were corrected after feedback. Current evidence does not establish unattended completion of creation, installation, and testing.

The final plain-game run still invented an earlier player action. Research interpretation also requires review despite accurate quotation and the successful motivation check. No run validates every game branch, all source claims, or repeated reliability. Participant-account verification remains deferred at the user's direction. Administrator-account readback does not establish participant access.

## Earlier Failures

- A Gemma 3 source quotation failed verification.
- A Mistral Small Skill Creator test invented a skill.

These failures remain part of evaluation history. Current cards use replacement bases; [model-cards.json](../../examples/model-cards.json) contains no Gemma 3 base models.

Replacement screenshots and publication are outside this test record.

## Final Sources Retrieval

After the final prompt and repaired source register were saved, a fresh Sources chat asked what List of experiments says about Pasteur’s S-shaped flasks. It identified the original Wikipedia filename and quoted the complete matching passage exactly. A literal check against the repaired import passed. This verifies retrieval of repaired article text in Legacy mode with Builtin Tools disabled; it does not establish that every game turn retrieves all three original articles.
