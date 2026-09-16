# Workshop revision

Implemented the approved clarity review on September 16, 2026, from baseline `6aba309ea2fa3959901e2bc37a9b833c020e67db`.

[Complete before/after passages](passages.md) · [Direct copy diff](copy.diff) · [Implementation diff](implementation.diff) · [Original slide destinations](slide-map.json) · [Full copy and alt text](../../SLIDES.md)

## Sequence and copy

The series contains 93 slides: 42 for Composing system prompts, 22 for Curating knowledge collections, and 29 for Configuring skills and tools. All three lesson plans allocate 90 minutes.

- Workshop 1 preserves the nurse and car-wash comparisons, in-chat system prompt, and regeneration sequence. The game is a preview of Workshop 3. The redundant game exercise is removed.
- Workshop 2 uses a system prompt and knowledge collection without attached skills or adventure tools. Participants inspect a readable scenario document, check source passages, create a collection, and repeat their saved question. Function Calling is explicitly set to Legacy for automatic retrieval.
- Workshop 3 keeps one private model copy and one saved skill draft throughout. Creator output remains a draft; participants install the provided tested tool, then inspect its actual call and result.
- Alternative examples are on visible [source](../../knowledge/reference.html) and [skill/tool](../../skills/reference.html) pages. There are no hidden notes or collapsed instructions.
- System-prompt examples and skill instructions have separate destinations. Download links supply named files; readable previews remain available.

The user's later instruction that skills and tools begin only in Workshop 3 supersedes recommendation 03's earlier proposal to run the game in Workshop 1. Recommendations 12 and 21 were checked in an administrator account; the user explicitly deferred participant-account access checks.

## Screenshots and layout

Six new Firefox captures show model creation, populated source-model settings, knowledge-only attachments, Clone, private access without inherited grants, and skill creation. Neutral annotations identify the relevant controls. [Provenance](../screenshot-sources.json) records original image hashes and crops.

A CSS specificity conflict capped screenshot height at 160 pixels. Screenshot-slide rules now take precedence. Existing Controls, Regenerate, and sidebar annotations remain intact.

[Browser measurements](browser.json) cover all 93 slides at 1280×720 and 390×844. Desktop slides fit without horizontal or vertical overflow. Mobile slides have no horizontal overflow; longer text slides scroll vertically. Headings remain at most 32 pixels on desktop and 28 on mobile. All screenshots load, and screenshot slides use the available slide area. [Reference-page measurements](reference-browser.json) confirm no mobile horizontal overflow and 44-pixel copy controls. Clone, private access, the mobile outline, and creation forms were also inspected visually.

## Verification

- Series validation: 93 slides, synchronized Markdown mirrors, retained-source custody, image hashes, links, headings, participant copy, and no hidden content.
- Copy regressions: 24 checks, including Workshop 2 without game-running instructions and both creators remaining general-purpose.
- Deck interactions: 31 checks, including selection, slider, outline, copy controls, and fallback behavior.
- Game engine, six scenario validation tests, and eight independent creator-output checks pass. JavaScript syntax and Python compilation pass. Rebuilding the adventure tool and preview produces no changes.
- Firefox downloaded `prism-scenario.md` with the expected filename. Downloaded bytes match the repository file; upload to Sandbox succeeded.

Runtime observations and remaining access checks are recorded in [live verification](live-verification.md). Layout checks do not establish participant permissions or guarantee model answers.

## Added material

New material is limited to six screenshots, visible reference pages containing existing examples, a readable scenario extracted from the existing JSON, a text download of the existing source-checking prompt, explicit configuration and download instructions, and regression coverage. A private source-only model was created for Workshop 2 verification. The shared STEM Adventure Games model, game engine, full game system prompt, skill implementation, and creator prompts were not changed.
