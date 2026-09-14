# Copy Review

Latest revisions — [Short system prompt](short-prompt-review.md) · [Direct diff](short-prompt.diff).

Previous revisions — [Prompt sequence and annotated controls](prompt-sequence-review.md) · [Direct diff](prompt-sequence.diff).

The consolidated series preserves the three-workshop order and the substantive disciplinary progressions. Complete before/after passages and direct diffs are retained here.

| Workshop | Original copy | Revised copy | Direct diff |
| --- | --- | --- | --- |
| Compose System Prompts | [Original HTML text](before.md) | [Current copy](../PROMPTS.md) | [Copy diff](copy.diff) |
| Curate Knowledge Collections | [Original HTML text](knowledge/before.md) | [Current copy](../knowledge/SLIDES.md) | [Copy diff](knowledge/copy.diff) |
| Skills & Tools | [Original HTML text](skills/before.md) | [Current copy](../skills/SLIDES.md) | [Copy diff](skills/copy.diff) |

[Read the complete series copy](../SLIDES.md). HTML, rather than the old Markdown mirrors, establishes the original text. The Knowledge mirror had already fallen behind its 34-slide HTML deck. The Skills mirror described a three-part template while its HTML accidentally called the same template four-part.

## Source revisions

- System Prompting original baseline `6e66d3b8bb9fda75dbd3de44ccbabdd68c4a6a20`, developed through PR 1 in the original repository.
- Knowledge Collections `80f5bf07aa8baac752873ad41476caec33404fdf`.
- Skills & Tools `eac817027e63a9a997985b8db822e3b4baa91821`.

Original Knowledge and Skills HTML is retained beside each before-copy file. The preservation manifests check 23 System Prompting sections and 14 prompt blocks, plus 34 imported Knowledge and Skills sections. Listed replacements document corrections to those retained sections. Introductory instructions and closing steps were rewritten around current platform behavior and the user’s access requirements.

## Style and copy audit

| Before | After or decision | Reason |
| --- | --- | --- |
| “Explore the chat. Compare models. Build a classroom tool.” | “Comparing and configuring models for teaching and research” | Removed slogan cadence and teaching-only scope. |
| “Three workshops, one teaching project” | Series roadmap with action-led descriptions | Restored research scope and continuity across sessions. |
| “WeakHelp students write better.” in generated copy | Badge rendered separately from prompt text | Fixed transcript concatenation without changing the prompt. |
| “One large document retrieves poorly” | Check whether the syllabus contains relevant evidence and inspect retrieved passages | Removed an unsupported guarantee based on document size. |
| “It activates automatically in every chat” | Check skill loading and procedure-following with native function calling | Replaced a reliability claim with current configuration instructions and an observable test. |
| “Use the four-part structure” above three components | “Use the three-part structure” | Corrected the source HTML mismatch. |
| Instructions to retrieve an original image from a collection | Ask for the image when unavailable and use a model able to inspect it | Text retrieval does not establish visual access. |
| “Full prompt: scroll to read” and repeated colon labels | Direct sentences or labels without colon punctuation | Applied house style to editable prose. |

The exact user-provided demonstration prompts remain unchanged. Original full prompt examples retain their technical labels, template punctuation, and disciplinary framing. These are quoted artifacts available for adaptation; broad rewriting would change their instructional purpose. The earlier literature correction from “larger themes and cultural moment” to “larger themes” remains documented because that prompt explicitly uses New Criticism.

Mini-agendas and next steps begin with action verbs and omit articles. Short fragments serve navigation and exercise sequencing, as requested. Supporting prose was checked for unsupported certainty, vague references, repeated slogan structures, and generic teaching-only framing. Vocabulary alone was not treated as evidence of poor style.

## Screenshots

Nine current interface captures and two archival comparison excerpts have source hashes and crop coordinates in [current screenshot provenance](screenshot-sources.json) and [showcase provenance](showcase-sources.json). Current captures came from Firefox. They show the composer selector, chat Controls, Integrations, Workspace, model editor, Knowledge creation, Skill editor, and access application.

The two GCDI response excerpts have the obsolete top selector cropped out. The original source’s Qwen selector and response labels differ; the lesson plan identifies that limitation. They are discussion examples, not verified exact-model benchmark results. The unrelated fourth screenshot is excluded. No sample card, collection, or skill was saved in production for these captures.

Screenshot slides now devote the viewport to a modest heading, image, and caption. Supporting instructions remain in the complete copy, linked from Outline. Source pixels are preserved apart from rectangular cropping.

## Additions beyond source refresh

The requested nurse/car-wash sequence, agendas, access mapping, separate examples page, and shared navigation are included. Limited additional material consists of research alternatives, a compact record of evaluation evidence, and a small median calculation with a known answer for checking tool execution. Those additions support the requested research scope and evaluation undercurrent. No fourth workshop was added.

## Current Validation

September 14 checks covered all 118 slides at 1280×720 and 390×844. No missing images, horizontal overflow, clipped headings, or screenshot overlap with the footer were found. Headings stayed within 32px on desktop and 28px on mobile. The mobile slider measured 358×44px in the 390px viewport.

Dragging across prompt text, extending the selection with Shift+Right, and pressing Right preserved the slide. The slider changed slides, Outline opened at its heading, and its links opened the other workshops. The prompt-reference page retained all 16 copy controls. Source checks confirmed that every prompt block and reference-page prompt matches the prior published version. JavaScript syntax checks and the source-preservation checks passed, and browser inspection found no console errors.

The prior release also exercised all 33 prompt-copy controls and screenshot expansion. This revision preserves that copy and image code. Content swipes were removed so that scrolling and text selection use the browser’s normal behavior. A physical mobile touchscreen was not part of this check.

## September Revisions

The [September 14 copy review](2026-09-14-review.md) links the prior published copy, complete revised copy, and direct diff. Notes and Series have been removed from the footer. Outline now links to all workshops and reference material. Slide 4 links directly to the access application; its previous screenshot remains only in the source archive.

## Participant Revision

[Review participant-copy changes](participant-copy-review.md). Presenter instructions and editorial commentary have been removed from the slides, transcript, and examples page. Presenter lesson plans remain in WORKSHOP.md and are no longer linked from participant navigation.

[Latest full before/after copy review](plain-language-review.md) · [Latest direct diff](plain-language.diff)
