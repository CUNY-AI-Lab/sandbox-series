# Workshop Review

Completed September 17, 2026. The local workshop needed further revision after its agenda acquired teaching and research options. Subsequent instructions still directed participants exclusively into STEM Adventure Games. Public Pages also remained behind the local copy at the start of this review.

## Review Order

Cycle 1 followed participant order through Composing system prompts, Curating knowledge collections, and Configuring skills and tools. It checked definitions before exercises, model choice before cloning, source inputs before retrieval, and installed resources before testing. A separate source audit compared earlier CUNY AI Lab and zmuhls workshop materials.

Cycle 2 reversed workshop order and worked backward from saved artifacts through their prerequisites. It then revisited changed sentences and links. This caught missing Save & Update steps, research inputs without direct links, ambiguous references to shared models, and tool naming placed after creation.

## Source Methods

The earlier [Composing System Prompts workshop](https://github.com/CUNY-AI-Lab/system-prompting/blob/6e66d3b8bb/index.html) grounds instructions in a particular task, orders procedures, states constraints, defines response structure, and tests conditional behavior. These methods remain within the user's current four components—Purpose, Procedure, Constraints, and Format. Earlier Context and Tone labels were not restored.

[Prompting in Praxis](https://github.com/zmuhls/cuny-ai-workshops/blob/master/prompting-in-praxis/outline.md) informs comparison through matching inputs, inspecting evidence, and recording differences. [AI Literacy and Disciplinary Thinking](https://github.com/zmuhls/cuny-ai-workshops/blob/master/disciplinary-thinking/outline.md) supports choosing specific work to examine while retaining participant judgment. These sources informed the method; they did not justify adding disciplinary examples that the user removed.

Control names and configuration descriptions were checked against [Sandbox Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/) and [Open WebUI Models](https://docs.openwebui.com/features/workspace/models/). Original prompt excerpts and later explicit user corrections take precedence over stylistic substitutions.

## Changes Applied

| Finding | Revision |
| --- | --- |
| Teaching/research choice disappeared after cloning | Retained both model links; added research equivalents within shared component exercises and evaluation |
| Model form appeared after participants were told to use it | Moved configuration image before model choice and cloning |
| Repeated navigation returned participants to original STEM card | Removed Select STEM Games and Inspect System Prompt slides |
| STEM editor screenshot named an outdated base model | Removed redundant Workshop 1 screenshot and made Workshop 2 settings review explicit text |
| Research exercise lacked a concrete task | Linked paired Wikipedia excerpts and specified classification with quoted evidence |
| Workshop 2 replaced participants' chosen instructions with STEM instructions | Continued either private model and retained its Workshop 1 system prompt |
| Original source roles were displaced by Newton example | Restored List of experiments, Scientific method, and Women in science; kept Newton materials for the worked example |
| Research source materials were named without links | Linked revision excerpts and classification criteria |
| Prompt retest preceded saving | Added Save & Update before testing and saving again after revision |
| Installed tool could differ from attached tool | Required attachment of installed copy and matching system prompt name before testing |
| Unique tool name/ID appeared after creation | Moved naming into creation step |
| Tool slide repeated a code link and exceeded desktop height | Removed duplicate link; retained download and code evaluation links |
| Lesson plan used older agenda and three game choices | Matched revised agenda, both options, four choices, and original 90-minute timing |
| Import warning implied List of experiments was still broken | Updated dated explanation using the separate verified repair record |

The deck has 90 slides—39, 22, and 29 across its three workshops—down from 92 at the start of this review. New research instructions were limited to the existing exercise; no parallel research deck was added.

## Verification

| Check | Result |
| --- | --- |
| Copy regressions | 31 tests passed |
| Teaching/research continuity | 7 tests passed |
| Deck interactions | 31 checks passed |
| Full-copy synchronization | Passed across all three workshops |
| Source preservation | 34 imported sections checked; scoped changes recorded |
| Screenshot resolution limits | 18 assets checked against embedded raster dimensions |
| Whitespace | git diff --check passed |
| Desktop layout | All 90 slides visited at 1280 × 720; one small overflow corrected and rechecked |
| Images and console | No broken slide images or console warnings/errors in desktop sweep |
| Mobile samples | Choice and procedure slides checked at 390 × 844; text readable and navigation accessible |

The desktop sweep used the actual rendered deck, slider navigation, DOM bounds, and image-load state. Screenshots confirmed changed layouts. It did not establish legibility of every detail inside every historical screenshot. Mobile inspection sampled the changed choice and procedure layouts rather than all slides. Browser evidence is saved in `/Users/milwright/Documents/Codex/2026-09-17/workshop-audit/`.

The initial batch navigation attempt timed out before advancing. The recovered sweep used the documented CUA tab and slider APIs and completed all 90 slides. No fallback browser automation or native Firefox interaction was used for this audit.

The original Sandbox task retains live model testing, participant access remains unverified, and that task owns the coordinated commit and publication. This audit changed no base model, live system prompt, skill, tool, or access setting. No publication is claimed here.

## Revision Evidence

- [Cycle 1 complete before and after](cycle1-before-after.md)
- [Cycle 1 isolated diff](cycle1.diff)
- [Cycle 2 complete before and after](cycle2-before-after.md)
- [Cycle 2 isolated diff](cycle2.diff)
- [Full current slide copy](../../SLIDES.md)
- [Current lesson plans](../../WORKSHOP.md)

Historical review records retain superseded wording as evidence. Current participant copy uses Compare Wikipedia Edits throughout; its existing model ID remains stable.
