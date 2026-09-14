# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Compose System Prompts begins the series. Use **Outline** to move to Curate Knowledge Collections and Skills & Tools. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](SLIDES.md)
- [Presenter lesson plans and access requirements](WORKSHOP.md)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Copy review and source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

The first session demonstrates two small models on the nurse question before the car-wash demonstration and handoff. Participants compare responses, check citations, and test tools in teaching and research tasks. Long disciplinary examples remain available as reference material; the lesson plans identify a shorter path for live sessions.

## Development

Static HTML, CSS, and JavaScript. No build step or runtime dependencies.

```sh
python3 -m http.server 8766
python3 scripts/check_series.py
```

After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, the slider, or **Outline** to navigate. On mobile, the slider occupies a full row above the navigation buttons. Text selection does not advance slides. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Outline** links to each workshop, prompt examples, and the complete transcript, including screenshot instructions. Presenter lesson plans remain available through this README.

## Sources

Developed from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools), originally developed by Stefano Morello and Zach Muhlbauer. Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. GCDI comparison excerpts are labeled as archival and cropped to remove the obsolete top selector. See the review folder for provenance and the source-label limitation.
