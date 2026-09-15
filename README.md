# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Composing system prompts begins the series. Use **Outline** to move to Curating knowledge collections and Configuring skills and tools. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](SLIDES.md)
- [Presenter lesson plans and access requirements](WORKSHOP.md)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Latest copy refinements and before/after](review/streamline-review.md)
- [Source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

Participants learn how user prompts and system prompts differ, then compare how two small models interpret a sentence about a nurse and doctor. They ask whether to walk or drive to a car wash and save both responses. After reading sample system prompt instructions, participants locate System Prompt in Chat Controls, add those instructions, and regenerate responses to their original prompt. Participants compare responses, check citations, and test tools in teaching and research tasks. STEM Adventure Games connects the workshops through its system prompt, STEM Wikipedia Experiments collection, and a playable adventure tool with a complementary skill for experimental variations.

## Workshop Artifacts

- [STEM Adventure tool](examples/tools/stem_adventure.py) and [playable preview](examples/adventure/preview.html)
- [Extend STEM Adventures skill](examples/stem-game-skill.md)
- [System prompt](examples/stem-system-prompt.txt)
- [Prism Laboratory scenario](examples/adventure/prism.json), [aperture variation](examples/adventure/aperture.json), and [winning commands](examples/adventure/winning-commands.json)
- [Additional knowledge entries](WORKSHOP.md#additional-knowledge-entries)
- [Skill Creator instructions](examples/creators/skill-creator-system-prompt.txt) and [Tool Creator instructions](examples/creators/tool-creator-system-prompt.txt)

Both creators accept requirements for any suitable task. STEM Adventure is a workshop request, not a default in either creator.

The engine checks moves, inventory, and prerequisites. Exported records can be restored by replaying commands. Type `discuss` to place a run in the Sandbox message box for review and sending. A game’s programmed observations are distinct from historical evidence.

## Development

Static HTML, CSS, and JavaScript. No build step or runtime dependencies.

```sh
python3 -m http.server 8766
python3 scripts/check_series.py
python3 scripts/test_copy_regressions.py
node scripts/test_deck_interactions.cjs
node examples/adventure/test-engine.cjs
python3 examples/adventure/test-validation.py
```

After changing game sources, run `python3 examples/adventure/build_tool.py` to rebuild the Open WebUI tool and preview. After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, the slider, or **Outline** to navigate. On mobile, the slider occupies a full row above the navigation buttons. Text selection does not advance slides. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Outline** links to each workshop, prompt examples, and the complete transcript, including screenshot instructions. Presenter lesson plans remain available through this README.

## Sources

Developed by Zach Muhlbauer from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools). Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. Reused comparison screenshots exclude obsolete controls. Capture provenance and source limitations remain in review files.
