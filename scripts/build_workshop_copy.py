#!/usr/bin/env python3
"""Build readable Workshop 1 HTML from the authoritative slide markup."""
from hashlib import sha256
from html import escape
from pathlib import Path
import sys
import struct
import xml.etree.ElementTree as ET

from check_workshop import Parser, VOID

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / 'workshop-copy.html'
EXCLUDED_TAGS = {'canvas', 'script', 'style'}
EXCLUDED_CLASSES = {'slide-notes', 'progression-dots', 'sr-only'}


def attribute(name, value):
    return f' {name}="{escape(str(value), quote=True)}"'


def render(node, slide_heading):
    """Retain source wording and prompt bytes while removing deck behavior."""
    if isinstance(node, str):
        return escape(node, quote=False)
    if node is slide_heading or node.tag in EXCLUDED_TAGS:
        return ''
    if any(node.has_class(name) for name in EXCLUDED_CLASSES):
        return ''
    if node.tag == 'button':
        target = node.attrs.get('data-copy') or node.attrs.get('data-example-copy')
        if not target:
            return ''
        return ('<button type="button" class="copy-prompt"' +
                attribute('data-example-copy', target) + '>' +
                escape(node.text()) + '</button>')

    tag = {'h1': 'h3', 'h2': 'h3', 'h3': 'h3'}.get(node.tag, node.tag)
    attrs = {}
    for name, value in node.attrs.items():
        if name in {'id', 'class', 'href', 'src', 'alt', 'title', 'target', 'rel',
                    'download', 'width', 'height', 'datetime', 'scope', 'colspan',
                    'rowspan'}:
            attrs[name] = value
    if node.has_class('slide-inner'):
        attrs['class'] = 'copy-content'
    if 'data-fragment-step' in node.attrs:
        attrs['class'] = (attrs.get('class', '') + ' copy-stage').strip()
    if tag == 'img':
        attrs['loading'] = 'lazy'
        attrs['decoding'] = 'async'
        path = ROOT / attrs['src']
        if path.suffix.lower() == '.png':
            attrs['width'], attrs['height'] = struct.unpack('>II', path.read_bytes()[16:24])
        elif path.suffix.lower() == '.svg':
            viewbox = ET.parse(path).getroot().attrib.get('viewBox', '').split()
            if len(viewbox) == 4:
                attrs['width'], attrs['height'] = (round(float(value)) for value in viewbox[2:])
    if tag == 'a' and attrs.get('href', '').lstrip('#').isdigit():
        attrs['href'] = './' + attrs['href']
    opening = '<' + tag + ''.join(attribute(k, v) for k, v in attrs.items()) + '>'
    if tag in VOID:
        html = opening
    else:
        html = opening + ''.join(render(child, slide_heading) for child in node.children) + '</' + tag + '>'
    if tag == 'img' and node.attrs.get('alt'):
        html += '<p class="image-alt"><strong>Alt text:</strong> ' + escape(node.attrs['alt']) + '</p>'
    return html


def build():
    source = Parser((ROOT / 'index.html').read_text()).root
    slides = source.all(lambda node: node.has_class('slide'))
    sections = []
    contents = []
    for number, slide in enumerate(slides, 1):
        title = slide.attrs['data-title']
        heading = slide.all(lambda node: node.tag in {'h1', 'h2'})[0]
        contents.append(f'<li><a href="#slide-{number}">{escape(title)}</a></li>')
        sections.append(
            f'<section class="copy-section" id="slide-{number}" aria-labelledby="copy-heading-{number}">\n'
            f'<p class="slide-link"><a href="./#{number}">Slide {number}</a></p>\n'
            f'<h2 id="copy-heading-{number}">{escape(title)}</h2>\n' +
            ''.join(render(child, heading) for child in slide.children) + '\n</section>')

    css_version = sha256((ROOT / 'css/workshop-copy.css').read_bytes()).hexdigest()[:12]
    return '\n'.join([
        '<!doctype html>',
        '<html lang="en">',
        '<head>',
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<title>Full Workshop Copy | CUNY AI Lab</title>',
        '<link rel="icon" type="image/svg+xml" href="images/cail-favicon.svg">',
        f'<link rel="stylesheet" href="css/workshop-copy.css?v={css_version}">',
        '</head>',
        '<body>',
        '<a class="skip-link" href="#workshop-copy">Skip to workshop copy</a>',
        '<header class="page-header"><h1>Full Workshop Copy</h1>',
        '<nav aria-label="Workshop links"><a href="./">Return to workshop</a> · <a href="examples.html">Prompt examples</a> · <a href="PROMPTS.md">Markdown copy</a></nav>',
        '<nav class="copy-outline" aria-label="Workshop outline"><ol>' + ''.join(contents) + '</ol></nav></header>',
        '<main id="workshop-copy">',
        '\n\n'.join(sections),
        '</main>',
        '<p aria-live="polite" role="status" id="copy-status"></p>',
        '<script src="js/examples.js" defer></script>',
        '</body>',
        '</html>',
        '',
    ])


def main():
    output = build()
    source = Parser((ROOT / 'index.html').read_text()).root
    copied = Parser(output).root
    source_prompts = [node.text() for node in source.all(lambda node: node.tag == 'pre')]
    copied_prompts = [node.text() for node in copied.all(lambda node: node.tag == 'pre')]
    if copied_prompts != source_prompts:
        raise ValueError('Workshop HTML copy changed prompt text.')
    source_images = [node.attrs['src'] for node in source.all(lambda node: node.tag == 'img' and node.attrs.get('src'))]
    copied_images = [node.attrs['src'] for node in copied.all(lambda node: node.tag == 'img')]
    if copied_images != source_images:
        raise ValueError('Workshop HTML copy changed image sources.')
    if copied.all(lambda node: 'hidden' in node.attrs or node.has_class('slide-notes')):
        raise ValueError('Workshop HTML copy contains hidden content.')
    if '--write' in sys.argv:
        DESTINATION.write_text(output)
        print('Workshop HTML copy synchronized.')
    elif not DESTINATION.exists() or DESTINATION.read_text() != output:
        print('Workshop HTML copy is out of sync; run scripts/check_series.py --write.')
        return 1
    else:
        print('Workshop HTML copy checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
