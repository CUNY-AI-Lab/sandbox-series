# Readability and live Sandbox checks

Checked 16 September 2026.

## Workshop progression

- Workshops 1–2 use **STEM Adventure Games**, with Gemma 3 4B IT, the introductory system prompt, ordinary chat, and attached Knowledge. Tools and Skills are empty. Web Search, Memory, and Builtin Tools are disabled. Function Calling is Legacy for Knowledge retrieval.
- Workshop 3 uses **STEM Adventure Games — Advanced**. Its exported base model, parameters, tool IDs, skill IDs, Knowledge, capabilities, active status, and access match the original advanced configuration. Its name and description distinguish it from the introductory model.
- Live Newton: Light and Colour and Source Register entries were updated and reopened to verify the revised text. Workshop 2's source summary no longer prescribes game-engine commands or records.

## Observed chat behavior

Inputs were entered in Firefox using the saved introductory model.

| Input | Observed result |
| --- | --- |
| Start an adventure about light and colour. | Offered three experiments in chat. |
| 1 | Described a room, prism, sunlight, and screen; offered three numbered choices. |
| Give me one hint. | Explained the prism's purpose and returned choices without advancing the scene. |
| Which objects in this scene appear in Newton: Light and Colour? Quote a relevant passage. Which details were invented for this game? | Retrieved attached sources and displayed clickable citations. It did not supply the requested exact quotation and made an unsupported claim about the screen. |

The source-question failure prompted an explicit pause/quote/check/resume instruction. A fresh-chat retest still omitted the quotation and continued offering choices. This remains a model limitation to evaluate through the workshop's source-comparison exercise; citation display does not establish that an answer is supported.

Successful introductory replies observed in these runs took 2.49–5.38 seconds. One new chat returned a catalog error after a transient Sandbox gateway failure; reopening a new chat recovered without changing the model. These are observed timings, not performance guarantees.

Configuration and chat checks used an administrator account. Participant-account access testing remains deferred at the user's direction.

## Presentation checks

- Body text is 26–32px on desktop; supporting text and captions are 22–27px. At 1280×720, measured source text is 24.32px and navigation is 20px.
- Mobile body text is 23px, with 20px supporting text. Slide 5 was visually checked at 390×844.
- All 93 slides were checked for layout at 1280×720, 1024×768, 1920×1080, and 390×844. No desktop overflow or mobile horizontal overflow was found. Long mobile slides scroll vertically.
- Final browser checks covered root slides 5, 6, 7, 12, 21, 25, 26, and 27, Knowledge 17, and Skills 6. New image assets were inspected individually as well.
- Nine fresh interface captures replace small or outdated assets. Screenshot provenance records actual pixel dimensions, transformations, hashes, and source pages. No active screenshot is narrower than 1000 source pixels.
- Slides 12–13 typeset the exact recommendation visible in each original response image, with links to those originals.
- CSS URLs carry a new version so previously opened decks load the larger typography.

Repository checks passed: series synchronization, 25 copy regressions, 31 interaction checks, JavaScript syntax checks, game engine and extension checks, six validation tests, eight creator checks, tool compilation, and whitespace checks.
