# Copy regression review

Reviewed 14 September 2026 against `8340b03`, including all three HTML decks, their Markdown mirrors, prompt examples, downloadable instructions, lesson plans, alt text, captions, and Sandbox resource copy.

[Complete current copy and alt text](../SLIDES.md) · [Full before/after passages](copy-audit-changes.md) · [Direct copy diff](copy-audit.diff) · [Previous complete copy](copy-audit-before.md)

## What changed

- Define base models, custom models, knowledge collections, skills, and scenario JSON before asking participants to use them.
- Keep initial model comparisons ahead of in-chat system prompt revision and regeneration. Preserve both original questions, response labels, and exact model-selector instructions.
- Introduce existing STEM sources before collection creation. Put uploads and processing ahead of attachment and retrieval checks.
- Name required files and inputs. Explain how to start Prism Laboratory, save a record before restarting, restore it, and return a record to chat.
- Compare skills using a private model copy so an attached skill cannot silently remain available during a trial intended to exclude it.
- Identify a separate validator draft in its code example, remove an instruction to use an unavailable tool, and state what to attach before comparing records.
- Remove a redundant copy button from an instruction-only container. Preserve compact buttons beside actual prompts.

The revision changes 47 passages or artifact sections. Reordering appears in the direct diff. Source quotations, historical model outputs, command syntax, URLs, and resource titles remain literal. No new workshop or participant exercise was added.

## Regression coverage

| Requirement from this chat | Check |
| --- | --- |
| Exact section names; short slide titles; no articles or gerunds in other titles | Automated title, heading, Outline, and accessibility-label checks |
| Participant-facing copy; no definite articles outside quoted prompts; no facilitator directions | Automated prose checks across decks, notes, alt text, and examples |
| Explicit deleted sentences, rejected labels, and exact replacement wording | Automated assertions based on corrections in this chat |
| Nurse question before car wash; unchanged questions and short system prompt | Exact-text and sequence assertions |
| In-chat System Prompt location with original-response regeneration | Assertions for Controls, System Prompt, Regenerate, and Try Again |
| Access requirements; action-led agendas; three 90-minute plans | Access, verb, and contiguous-time checks |
| Definitions and required resources before exercises | Sequence and named-input assertions; manual read of all 103 slides |
| General-purpose builders | Prompt, description, and starter checks against game-specific defaults |
| Consistent HTML, Markdown, prompt examples, and downloadable files | Generated-copy and source-equality checks |
| Current screenshots, annotations, and alt text | Asset hashes, local links, annotation contracts, and browser image checks |
| Compact copy buttons; no Notes or Series footer | Container and footer checks; browser inspection |
| Mobile slider, Outline spacing, readable text, and safe selection | Browser layout checks and shared-engine interaction tests |
| No discipline-specific bad/better/good examples | Manual full-copy review and retained/retired passage manifests |

`test_copy_regressions.py` runs 21 tests, including mutations that deliberately restore rejected copy, alter prompts, move definitions later, drift reference text, or remove required instructions. Those mutations must fail the relevant assertions. These checks protect known corrections; they do not detect authorship or replace editorial judgment.

`test_deck_interactions.cjs` runs 31 checks against the actual shared presentation engine using a small DOM fixture. Coverage includes text selection, modifier keys, editable fields, prompt navigation, slide limits, slider, Outline, copy, and clipboard fallback. GitHub Actions runs both suites alongside existing source, game, and validator checks.

## Browser review

All 103 slides were checked at desktop width and in a 390 × 844 mobile frame. Desktop slides fit without horizontal or vertical overflow. All images loaded. Mobile headings remain 26–28 pixels and no slide has horizontal overflow. Eight longer mobile slides scroll vertically, preserving readable text size. A direct scroll check on Connect Resources reached its final paragraph above navigation without changing slides. Outline retained separated workshop links, reference links, and slide entries.

In-browser selection of prompt text followed by Arrow Right retained Add System Prompt. Copy produced its visible success state. Exact copied bytes and unavailable-clipboard behavior were verified in the engine fixture; the browser clipboard bridge returned an empty value, so that bridge did not independently verify operating-system clipboard contents.

[Desktop measurements](copy-audit-desktop.json) · [Mobile measurements](copy-audit-mobile.json)

## Editorial evaluation

Applied no-ai-slop, humanizer, and milwrite-style to functional problems in the prose. Each check below was reviewed after refinement. Short slide instructions follow the user's explicit length requirements. Literal source titles and technical syntax are exempt from prose punctuation rules. Article-free participant text follows the user's explicit house style.

| No-ai-slop check | Result and evidence |
| --- | --- |
| Lexical 1 — avoid authorship guesses from isolated words | Pass — tests protect explicit requirements, not an AI vocabulary list |
| Lexical 2 — preserve distinctive and technical language | Pass — model names, UI labels, command names, and prompt wording retained |
| Lexical 3 — preserve meaningful scale, stakes, and voice | Pass — no figurative or emphatic language removed merely for its register |
| Lexical 4 — avoid generic substitutions for polish | Pass — refinements supply missing actions, inputs, and referents |
| Syntax 1 — zero prose colons | Pass — participant prose checked; URLs, code notation, and source titles remain literal |
| Syntax 2 — identifiable main clauses | Pass — instructions identify an action and its object |
| Syntax 3 — explicit relations in coordination | Pass — sequence markers clarify saving, restarting, restoring, and comparing |
| Syntax 4 — parallel coordination | Pass — agendas and next steps retain verb-led forms |
| Syntax 5 — clear attachment and reference | Pass — named files and resources replace ambiguous references |
| Syntax 6 — appropriate tense | Pass — saved examples are distinguished from actions participants have yet to perform |
| Syntax 7 — preserve effective longer sentences | Pass — source summaries and prompt qualifications retained |
| Syntax 8 — deliberate fragments and repetition | Pass — concise slide labels and numbered procedures remain purposeful |
| Signposting 1 — transitions name relations | Pass — definition, demonstration, creation, and testing follow a clear order |
| Signposting 2 — preserve useful guidance | Pass — UI locations and repeat-test instructions remain explicit |
| Signposting 3 — bridge abrupt changes | Pass — model, collection, game, skill, and tool roles introduced before use |
| Signposting 4 — one intelligible move per paragraph | Pass — each instruction supplies one step or comparison |
| Voice 1 — preserve cadence and qualification | Pass — concise participant wording and historical limits retained |
| Voice 2 — identify unfamiliar names | Pass — custom models, Prism Laboratory, attached resources, Markdown, and scenario JSON explained |
| Voice 3 — identifiable articles and pronouns | Pass — referents remain explicit within the user's article-free slide style |
| Voice 4 — clear agency | Pass — participants select, attach, save, and compare; models may load skills |
| Voice 5 — preserve facts and evidence | Pass — quotations, sources, claims, and historical test records retained |
| Voice 6 — avoid unsupported additions | Pass — refinements follow existing artifacts, current docs, and observed UI |
| Voice 7 — proportional revision | Pass — no additional workshop or participant exercise |
| Final 1 — natural when read aloud | Pass — manual review of complete participant copy |
| Final 2 — preserve requested voice | Pass — short concrete headings and direct actions |
| Final 3 — full revision and changes available | Pass — complete Markdown, 47 before/after passages, and direct diff linked above |
| Final 4 — concrete diagnosis without authorship scoring | Pass — each finding identifies a missing definition, input, action, or prerequisite |

## Saved Sandbox copy

Native Firefox readback confirmed exact current text for all four added Knowledge entries, STEM Adventure Games, Extend STEM Adventures, Kale Skill Builder, and Tool Creator. Both builders retained generic descriptions and starter suggestions. Model attachments remained present. Two screenshots were recaptured after saving the model and skill text; their provenance and hashes were updated. The source editor temporarily lost its connection during processing; all eight final copies were reopened and checked after recovery.

[Live readback results](copy-audit-live.json) · [Screenshot provenance](screenshot-sources.json)

## Platform sources

Mechanics and terminology were checked against [Sandbox models](https://ailab.gc.cuny.edu/sandbox-docs/models/), [knowledge collections](https://ailab.gc.cuny.edu/sandbox-docs/knowledge-bases/), [tools and skills](https://ailab.gc.cuny.edu/sandbox-docs/tools-skills/), and [Open WebUI skills](https://docs.openwebui.com/features/workspace/skills/). Attached skills may load when needed; enabling a skill directly injects its instructions. A comparison must account for both attachment and in-chat selection.

Historical model trials and executable game checks remain in [prior verification](verification.md). This copy revision does not claim fresh model-quality measurements from those earlier trials.
