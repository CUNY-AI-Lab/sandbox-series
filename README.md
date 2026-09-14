# Sandbox workshop series

[Open the workshop series](https://cuny-ai-lab.github.io/sandbox-series/)

Composing System Prompts begins the series. Use **Series** to move to Curating Knowledge Collections and Customizing Skills & Tools. All three share one repository, presentation engine, and neutral dark design.

- [Full slide copy](SLIDES.md)
- [Lesson plans and access requirements](WORKSHOP.md)
- [System-prompt examples](https://cuny-ai-lab.github.io/sandbox-series/examples.html)
- [Copy review and source history](review/README.md)

Workshop 1 requires individual access and Sandbox sign-in. Workshop 2 adds Workspace and Knowledge collection access. Workshop 3 adds Skills and Tools access, with Workspace authoring permissions for creation and editing. Knowledge access is needed in Workshop 3 when a chosen procedure retrieves from a collection.

The first session demonstrates two small models on the nurse question before the car-wash demonstration and handoff. Teaching and research examples retain evaluation through saved responses, source checks, and actual tool results. Long disciplinary examples remain available as reference material; the lesson plans identify a shorter path for live sessions.

## Development

Static HTML, CSS, and JavaScript. No build step or runtime dependencies.

```sh
python3 -m http.server 8766
python3 scripts/check_series.py
```

After changing slide text, run `python3 scripts/check_series.py --write` to update the complete transcript, per-session mirrors, and direct copy diffs. Review the generated diff before committing. The checker protects retained source passages and verifies local links, screenshot hashes, accessible slide labels, and article-free mini-agendas.

Use arrow keys, slide progress, or **Outline** to navigate. **Notes** displays supporting instructions. Screenshot slides reserve the viewport for the image, heading, and caption. Clicking an image expands it. **Series** includes the prompt reference page and lesson plans.

## Sources

Developed from [system-prompting](https://github.com/CUNY-AI-Lab/system-prompting), [knowledge-collections](https://github.com/CUNY-AI-Lab/knowledge-collections), and [skills-tools](https://github.com/CUNY-AI-Lab/skills-tools), originally developed by Stefano Morello and Zach Muhlbauer. Original repositories remain available.

Platform instructions follow the [CUNY AI Lab Sandbox documentation](https://ailab.gc.cuny.edu/sandbox-docs/). Current UI screenshots were captured in Firefox. GCDI comparison excerpts are labeled as archival and cropped to remove the obsolete top selector. See the review folder for provenance and the source-label limitation.
