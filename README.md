# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Composing system prompts begins the series. Use **Outline** to review slides and open formatted workshop copy. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](https://cuny-ai-lab.github.io/sandbox-series/SLIDES.html)
- [Presenter lesson plans and access requirements](https://cuny-ai-lab.github.io/sandbox-series/WORKSHOP.html)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Latest copy refinements and before/after](review/streamline-review.md)
- [Source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

Participants learn how user prompts and system prompts differ, then compare how two models interpret a sentence about a nurse and doctor. They ask whether to walk or drive to a car wash. After reading sample system prompt instructions, participants locate System Prompt in Chat Controls, add those instructions, and regenerate responses to their original prompt. Participants compare responses, check citations, and test tools in teaching and research tasks. After reviewing Workspace model cards, participants choose [STEM Adventure Games](https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games) for teaching or [Compare Wikipedia Edits](https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions) for research, clone it, and revise its instructions. Workshop 2 adds source documents. Workshop 3 uses a separate advanced game to examine tools and skills.

## Workshop Artifacts

- [STEM Adventure tool](https://cuny-ai-lab.github.io/sandbox-series/examples/tools/stem_adventure.html) and [playable preview](https://cuny-ai-lab.github.io/sandbox-series/examples/adventure/preview.html)
- [Extend STEM Adventures skill](https://cuny-ai-lab.github.io/sandbox-series/examples/stem-game-skill.html)
- [System prompt](https://cuny-ai-lab.github.io/sandbox-series/examples/stem-system-prompt.html)
- [Prism Laboratory scenario](https://cuny-ai-lab.github.io/sandbox-series/examples/adventure/prism.html), [aperture variation](https://cuny-ai-lab.github.io/sandbox-series/examples/adventure/aperture.html), and [winning commands](https://cuny-ai-lab.github.io/sandbox-series/examples/adventure/winning-commands.html)
- [Additional knowledge entries](https://cuny-ai-lab.github.io/sandbox-series/WORKSHOP.html#additional-knowledge-entries)
- [Skill Creator instructions](https://cuny-ai-lab.github.io/sandbox-series/examples/creators/skill-creator-system-prompt.html) and [Tool Creator instructions](https://cuny-ai-lab.github.io/sandbox-series/examples/creators/tool-creator-system-prompt.html)

Both creators accept requirements for any suitable task. STEM Adventure is a workshop request, not a default in either creator.

The engine checks moves, inventory, and prerequisites. Exported records can be restored by replaying commands. Type `discuss` to place a run in the Sandbox message box for review and sending. A game’s programmed observations are distinct from historical evidence.

## Development

Static HTML, CSS, and JavaScript. Published pages have no runtime dependencies. Install the pinned Markdown package to regenerate and check reading pages.

```sh
python3 -m pip install -r requirements-build.txt
python3 -m http.server 8766
python3 scripts/check_series.py
python3 scripts/test_copy_regressions.py
node scripts/test_deck_interactions.cjs
node examples/adventure/test-engine.cjs
python3 examples/adventure/test-validation.py
```

After changing game sources, run `python3 examples/adventure/build_tool.py` to rebuild the Open WebUI tool and preview. After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, the slider, or **Outline** to navigate. On mobile, the slider occupies a full row above the navigation buttons. Text selection does not advance slides. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Outline** links to full workshop copy, prompt examples, and Model Registry. Presenter lesson plans remain available through this README.

## Sources

Developed by Zach Muhlbauer from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools). Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. Reused comparison screenshots exclude obsolete controls. Capture provenance and source limitations remain in review files.
