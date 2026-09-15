# Verification

Checked on September 14, 2026. These observations distinguish local checks, authenticated Firefox behavior, and model-generated proposals.

## Workshop Checks

All 103 slides were inspected at 1280×720 and in a 390×844 browser iframe. Checks found no horizontal overflow, unloaded images, screenshot clipping, or headings above 32 pixels on desktop and 28 pixels on mobile. Receipts are in `live/desktop-*-checks.json`, `live/mobile-root-checks.json`, `live/mobile-knowledge-checks.json`, and `live/mobile-slide-checks.json`.

Mobile Outline measured 366 pixels wide with a 44-pixel Close target; the slider measured 358×44 pixels. Copy controls sit inside prompt containers. Slide and reference copy actions reported success, and reference text matched its source; clipboard readback was unavailable through the browser-control API. Physical mobile hardware was not used. Navigation and text-selection code is unchanged from the preceding verified release.

Source checks cover all decks, full Markdown and alt text, retained passages, accessible slide labels, local links, screenshot hashes, participant-facing copy, and short titles. JavaScript syntax checks pass.

## Installed Configuration

STEM Adventure Games uses DeepSeek V4 Pro 0813, STEM Wikipedia Experiments, STEM Adventure, and Extend STEM Adventures. The saved model prompt and all three attachments were read back in Firefox. [Receipt](live/stem-model-readback.json).

STEM Adventure 0.2.1 provides a Unicode terminal interface with one command line. Typed commands replace the control-button row. The tool returns an inline HTMLResponse and model context. No server credentials, external services, or relaxed iframe permissions were added.

Firefox checks covered a winning sequence, blocked prerequisites, undo, restart, save, load, and discuss. Reload begins a fresh game; load recomputes progress from saved commands. A keyboard-focus bug in 0.2.0 was corrected in 0.2.1; typed discuss now fills the message box without submitting it. [Keyboard receipt](live/keyboard-handoff-check.json), [saved record](live/stem-command-final.json), and [model interpretation](live/stem-final-discussion.md).

The complementary skill was loaded through `view_skill` in an actual chat. The model retrieved Newton entries and generated an aperture comparison. A blocked action and a 14-command completion sequence were tested in Firefox; reloading and loading the exported record restored completion. [Generated scenario](../examples/adventure/generated-aperture.json), [play record](live/stem-aperture-firefox.json), [response](live/stem-extension-response.md), and [reload receipt](live/extension-reload-check.txt).

Local engine checks cover deterministic replay, completion, prerequisites, duplicate pickups, invalid commands, undo, reset, shutter-dependent flags, record limits, references, and untrusted saved results. Six Python scenario-validation tests and eight independent tests of corrected creator output pass.

## General-Purpose Creators

Kale Skill Builder retains its existing name and model ID. Tool Creator is newly configured. Both use Gemma 4 26B A4B IT. Their final prompts, descriptions, and starter suggestions contain no STEM Adventure defaults. Saved prompts matched local source files. [Skill readback](live/skill-creator-general-readback.json) · [Tool readback](live/tool-creator-general-readback.json).

An independent bibliography request produced a four-step skill that preserved entries and flagged a missing year as uncertain. A line-counting request produced a Python tool that passed seven local execution checks. Neither response included game content. These checks establish behavior for those requests, not general reliability. [Skill response](live/skill-creator-general-task.md) · [Tool response](live/tool-creator-general-task.md) · [Checks](live/general-builder-tests.json).

Earlier game-specific trials exposed real failures. Skill Creator treated an empty history with a reported completion value as evidence of success. Feedback corrected its proposed test expectations. Tool Creator initially accepted numeric commands; feedback corrected validation and eight independent checks passed. These failures and corrections remain workshop examples, not hard-coded creator instructions. Proposed skill tests were not executed. The generated record interpreter and validator are downloadable drafts; they were not installed as additional live resources.

The Skill Builder baseline used DeepSeek, while later trials used Gemma and revised instructions. Those trials do not isolate the effect of the prompt change. Timing values are single observations, not performance benchmarks.

## Knowledge Entries

Four entries were added: Newton: Light and Colour, Newton: Experimental Variants, Evaluate Game Procedures, and STEM Source Register. Seven files are present. The Newton entries were retrieved in the extension test; the final evaluation entry was saved and read back with typed-command instructions. [Readback](live/knowledge-final-readback.json).

Scientific method and Women in science imports contain article text. List of experiments contains a Wikimedia 429 error, not the article. Its failed status is documented in the register and system prompt; the original file was retained. Newton summaries link to primary source accounts and distinguish game simplifications from historical apparatus.

## Remaining Access Check

Tests used the authorized account. Access from an ordinary participant account has not been verified. No separately named “KL Sandbox” configuration was found in Workspace or a focused Model Selector search; that exact name remains awaiting clarification. The installed game, skill, and both creators were otherwise configured and tested.
