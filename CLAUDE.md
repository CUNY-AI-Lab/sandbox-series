# Project guidance

This repository is the consolidated CUNY AI Lab Sandbox workshop series. HTML is the slide authority. Preserve the distinction between source instructions, observed UI, and model results.

- Read the frontend-design skill before visual changes.
- Use shared responsive slide-title sizing: 36–44px on desktop and tablet, 32px on mobile. Preserve cover typography and the neutral dark palette.
- Give screenshots nearly the whole slide. Keep supporting instructions in the complete transcript, linked through Outline.
- Keep mini-agendas and next steps short, beginning with action verbs and containing no definite or indefinite articles.
- Workshop 1 requires only individual access and Sandbox sign-in before attending. Later access requirements are recorded in WORKSHOP.md.
- Preserve exact demonstration prompts and substantive disciplinary examples. Record justified corrections in review manifests.
- Keep full copy and direct diffs synchronized with `python3 scripts/check_series.py --write`; run without `--write` to verify.
- Use actual screenshots, with documented crops. Never reconstruct platform UI or invent model outputs.
- Keep navigation, keyboard use, focus visibility, image alternatives, and reduced-motion behavior accessible.
- Do not add Co-Authored-By lines to commits.

Routes are `/`, `/knowledge/`, `/skills/`, and `/examples.html` within the Pages project. Shared assets live in css/, js/, images/, and examples/. Each deck opens directly without a build step.

- Use 2–3 words for slide headings. Omit articles and gerunds. Use documented terms; do not invent conceptual labels.
- Base platform descriptions on the Sandbox docs and Open WebUI docs. Preserve original workshop examples.
- Keep Notes and Series out of the footer. Do not bind slide navigation to content swipes or text-selection gestures.

- Address participants in all slide text, captions, image alternatives, and prompt-reference introductions, including hidden instructions reproduced in transcripts. Keep presenter directions and editorial commentary in WORKSHOP.md or review files, outside participant navigation.
- Verify every slide heading and Outline title uses 2–3 words without articles or gerunds. Keep both titles identical.
- Omit definite articles from participant instructions, captions, image alternatives, agendas, and explanatory prose. Preserve exact demonstration questions and quoted sample prompts. Use "Select model ID on bottom right of message box."
- Read revised passages for meaning as well as checking syntax. Describe actual actions without compressed labels such as "car-wash responses" or "two-model comparison". In Workshop 1, edit in-chat system prompt instructions and regenerate responses to the original prompt; do not substitute a follow-up question.
