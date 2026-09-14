# Project guidance

This repository is the consolidated CUNY AI Lab Sandbox workshop series. HTML is the slide authority. Preserve the distinction between source instructions, observed UI, and model results.

- Read the frontend-design skill before visual changes.
- Keep H1 and H2 at 32px maximum on desktop, with existing smaller mobile sizes. Preserve the neutral dark palette.
- Give screenshots nearly the whole slide. Keep supporting instructions in Notes and the complete transcript.
- Keep mini-agendas and next steps short, beginning with action verbs and containing no definite or indefinite articles.
- Workshop 1 requires only individual access and Sandbox sign-in before attending. Workspace access is enabled during guided practice there. Later access requirements are recorded in WORKSHOP.md.
- Preserve exact demonstration prompts and substantive disciplinary examples. Record justified corrections in review manifests.
- Keep full copy and direct diffs synchronized with `python3 scripts/check_series.py --write`; run without `--write` to verify.
- Use actual screenshots, with documented crops. Never reconstruct platform UI or invent model outputs.
- Keep navigation, keyboard use, focus visibility, image alternatives, and reduced-motion behavior accessible.
- Do not add Co-Authored-By lines to commits.

Routes are `/`, `/knowledge/`, `/skills/`, and `/examples.html` within the Pages project. Shared assets live in css/, js/, images/, and examples/. Each deck opens directly without a build step.
