#!/usr/bin/env python3
"""Build readable HTML copies from authoritative slide markup."""
from html import escape
from pathlib import Path
import sys
import struct
import re
import xml.etree.ElementTree as ET

from check_workshop import Parser, VOID
from reading_pages import relative, reading_href, page, link

ROOT = Path(__file__).resolve().parents[1]
DECKS = [('', 'Composing system prompts'),
         ('knowledge', 'Curating knowledge collections'),
         ('skills', 'Configuring skills and tools')]
EXCLUDED_TAGS = {'canvas', 'script', 'style'}
EXCLUDED_CLASSES = {'slide-notes', 'progression-dots', 'sr-only'}


def attribute(name, value):
    return f' {name}="{escape(str(value), quote=True)}"'


def render(node, slide_heading, route='', destination='workshop-copy.html'):
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
        path = ROOT / route / attrs['src']
        if path.suffix.lower() == '.png':
            attrs['width'], attrs['height'] = struct.unpack('>II', path.read_bytes()[16:24])
        elif path.suffix.lower() == '.svg':
            viewbox = ET.parse(path).getroot().attrib.get('viewBox', '').split()
            if len(viewbox) == 4:
                attrs['width'], attrs['height'] = (round(float(value)) for value in viewbox[2:])
    for name in ('href', 'src'):
        if name not in attrs:
            continue
        if 'download' in attrs:
            attrs[name] = relative(str(Path(route) / attrs[name]), destination)
        else:
            attrs[name] = reading_href(attrs[name], str(Path(route) / 'index.html'), destination)
    if tag == 'a' and attrs.get('href', '').lstrip('#').isdigit():
        attrs['href'] = relative(str(Path(route) / 'index.html'), destination) + attrs['href']
    opening = '<' + tag + ''.join(attribute(k, v) for k, v in attrs.items()) + '>'
    if tag in VOID:
        html = opening
    else:
        html = opening + ''.join(render(child, slide_heading, route, destination) for child in node.children) + '</' + tag + '>'
    if tag == 'img' and node.attrs.get('alt'):
        html += '<p class="image-alt"><strong>Alt text:</strong> ' + escape(node.attrs['alt']) + '</p>'
    return html


def deck_content(route, destination, prefix=''):
    source = Parser((ROOT / route / 'index.html').read_text()).root
    slides = source.all(lambda node: node.has_class('slide'))
    sections = []
    contents = []
    for number, slide in enumerate(slides, 1):
        title = slide.attrs['data-title']
        heading = slide.all(lambda node: node.tag in {'h1', 'h2'})[0]
        slide_id = f'{prefix}slide-{number}'
        deck_href = relative(str(Path(route) / 'index.html'), destination)
        contents.append(f'<li><a href="#{slide_id}">{escape(title)}</a></li>')
        sections.append(
            f'<section class="copy-section" id="{slide_id}" aria-labelledby="{prefix}copy-heading-{number}">\n'
            f'<p class="slide-link"><a href="{deck_href}#{number}">Slide {number}</a></p>\n'
            f'<h2 id="{prefix}copy-heading-{number}">{escape(title)}</h2>\n' +
            ''.join(render(child, heading, route, destination) for child in slide.children) + '\n</section>')
    return '\n\n'.join(sections), ''.join(contents)


def build(route=''):
    destination = str(Path(route) / 'workshop-copy.html')
    content, contents = deck_content(route, destination)
    title = 'Full Workshop Copy' if not route else dict(DECKS)[route]
    source_copy = 'SLIDES.md' if route else 'PROMPTS.md'
    nav = [link('./', 'Return to workshop'),
           link(relative('examples.html', destination), 'Prompt examples'),
           link(source_copy, 'Download Markdown', source_copy)]
    outline = '<nav class="copy-outline" aria-label="Workshop outline"><ol>' + contents + '</ol></nav>'
    return page(title, content, destination, nav, outline)


def build_series():
    destination = 'SLIDES.html'
    sections, contents = [], []
    for number, (route, label) in enumerate(DECKS, 1):
        content, outline = deck_content(route, destination, f'workshop-{number}-')
        # Prompt IDs must remain unique in a document containing all three decks.
        content = re.sub(r'(\bid|data-example-copy)="(?!workshop-)([^"]+)"',
                         rf'\1="workshop-{number}-\2"', content)
        sections.append(f'<section id="workshop-{number}"><h2>{escape(label)}</h2>{content}</section>')
        contents.append(f'<li>{link(f"#workshop-{number}", label)}</li>')
    nav = [link('index.html', 'Return to workshop'), link('examples.html', 'Prompt examples'),
           link('SLIDES.md', 'Download Markdown', 'SLIDES.md')]
    outline = '<nav class="copy-outline" aria-label="Workshop outline"><ol>' + ''.join(contents) + '</ol></nav>'
    return page('Full Series Copy', '\n'.join(sections), destination, nav, outline)


def main():
    outputs = {str(Path(route) / 'workshop-copy.html'): build(route) for route, _ in DECKS}
    outputs['SLIDES.html'] = build_series()
    output = outputs['workshop-copy.html']
    source = Parser((ROOT / 'index.html').read_text()).root
    copied = Parser(output).root
    source_prompts = [node.text() for node in source.all(lambda node: node.tag == 'pre')]
    copied_prompts = [node.text() for node in copied.all(lambda node: node.tag == 'pre')]
    if copied_prompts != source_prompts:
        raise ValueError('Workshop HTML copy changed prompt text.')
    # Shared navigation branding is outside slide content and its transcript.
    source_images = [node.attrs['src'] for slide in source.all(lambda node: node.has_class('slide'))
                     for node in slide.all(lambda node: node.tag == 'img' and node.attrs.get('src'))]
    copied_images = [node.attrs['src'] for node in copied.all(lambda node: node.tag == 'img')]
    if copied_images != source_images:
        raise ValueError('Workshop HTML copy changed image sources.')
    if copied.all(lambda node: 'hidden' in node.attrs or node.has_class('slide-notes')):
        raise ValueError('Workshop HTML copy contains hidden content.')
    for name, output in outputs.items():
        destination = ROOT / name
        if '--write' in sys.argv:
            destination.write_text(output)
        elif not destination.exists() or destination.read_text() != output:
            print(f'{name} is out of sync; run scripts/check_series.py --write.')
            return 1
    print('Four workshop HTML copies ' + ('synchronized.' if '--write' in sys.argv else 'checked.'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
