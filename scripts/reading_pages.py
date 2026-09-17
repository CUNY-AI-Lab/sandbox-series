"""Shared paths and markup for public reading pages."""
from hashlib import sha256
from html import escape
from pathlib import Path
import posixpath
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]

# Values are page titles for sources that do not already have a Markdown H1.
SOURCES = {
    'examples/model-cards.md': 'Sandbox Model Cards',
    'examples/model-cards.json': 'Model Card Data',
    'examples/research/model-card.md': 'Compare Wikipedia Edits',
    'examples/research/system-prompt.txt': 'Research System Prompt',
    'examples/research/sample-revisions.sources.json': 'Revision Sources',
    'examples/stem-game-skill.md': 'Extend STEM Adventures',
    'examples/stem-chat-system-prompt.txt': 'STEM Adventure Games',
    'examples/stem-system-prompt.txt': 'Advanced System Prompt',
    'examples/assumption-check.txt': 'Examine Assumptions',
    'examples/car-wash.txt': 'Compare Outputs',
    'examples/comparison-task.txt': 'Comparison Prompt',
    'examples/source-check.txt': 'Check Sources',
    'examples/system-prompt-framework.txt': 'System Prompt Framework',
    'examples/knowledge/newton-light-colour.md': 'Light and Colour',
    'examples/knowledge/newton-experimental-variants.md': 'Experimental Variants',
    'examples/knowledge/game-procedure-evaluation.md': 'Evaluate Game Procedures',
    'examples/knowledge/source-register.md': 'STEM Source Register',
    'examples/adventure/prism-scenario.md': 'Prism Laboratory',
    'examples/adventure/prism.json': 'Prism Laboratory',
    'examples/adventure/aperture.json': 'Aperture Test',
    'examples/adventure/winning-commands.json': 'Game Commands',
    'examples/tools/stem_adventure.py': 'STEM Adventure Tool',
    'examples/creators/record-interpreter-skill.md': 'Record Interpreter',
    'examples/creators/record-validator.py': 'Record Validator',
    'examples/creators/skill-creator-system-prompt.txt': 'Skill Creator Instructions',
    'examples/creators/tool-creator-system-prompt.txt': 'Tool Creator Instructions',
    'review/live/skill-builder-consistency-failure.md': 'Initial Skill Response',
    'review/live/record-validator-before.py': 'Initial Tool Draft',
    'review/live/tool-creator-corrected-tests.json': 'Tool Test Results',
    'WORKSHOP.md': 'Workshop Lesson Plans',
}

DESTINATIONS = {source: str(Path(source).with_suffix('.html')) for source in SOURCES}
DESTINATIONS['examples/model-cards.json'] = 'examples/model-cards-data.html'
DESTINATIONS.update({
    'PROMPTS.md': 'workshop-copy.html',
    'SLIDES.md': 'SLIDES.html',
    'knowledge/SLIDES.md': 'knowledge/workshop-copy.html',
    'skills/SLIDES.md': 'skills/workshop-copy.html',
    'knowledge/REFERENCE.md': 'knowledge/reference.html',
    'skills/REFERENCE.md': 'skills/reference.html',
    'examples/research/sample-revisions.md': 'examples/research/sample-revisions.html',
})


def relative(target, destination):
    return posixpath.relpath(target, posixpath.dirname(destination) or '.')


def reading_href(href, source, destination=None):
    """Rebase relative URLs and route source-file links to formatted pages."""
    url = urlsplit(href)
    if url.scheme or url.netloc or not url.path or url.path.startswith('/'):
        return href
    path = posixpath.normpath(posixpath.join(posixpath.dirname(source), url.path))
    target = DESTINATIONS.get(path, path)
    return urlunsplit(('', '', relative(target, destination or source), url.query, url.fragment))


def page(title, content, destination, links, outline=''):
    css_version = sha256((ROOT / 'css/workshop-copy.css').read_bytes()).hexdigest()[:12]
    css = relative('css/workshop-copy.css', destination)
    favicon = relative('images/cail-favicon.svg', destination)
    script = relative('js/examples.js', destination)
    navigation = ' · '.join(links)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | CUNY AI Lab</title>
<link rel="icon" type="image/svg+xml" href="{favicon}">
<link rel="stylesheet" href="{css}?v={css_version}">
</head>
<body>
<a class="skip-link" href="#workshop-copy">Skip to content</a>
<header class="page-header"><h1>{escape(title)}</h1>
<nav aria-label="Workshop links">{navigation}</nav>{outline}</header>
<main id="workshop-copy" class="reading-content">
{content}
</main>
<p aria-live="polite" role="status" id="copy-status"></p>
<script src="{script}" defer></script>
</body>
</html>
'''


def link(href, label, download=None):
    attr = f' download="{escape(download, quote=True)}"' if download else ''
    return f'<a href="{escape(href, quote=True)}"{attr}>{escape(label)}</a>'
