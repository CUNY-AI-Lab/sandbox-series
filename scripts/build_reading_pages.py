#!/usr/bin/env python3
"""Publish source-faithful HTML views without changing downloadable artifacts."""
from html import escape
import re
import sys

import markdown

from check_workshop import Parser, VOID
from reading_pages import ROOT, SOURCES, DESTINATIONS, relative, reading_href, page, link


def serialize(node):
    if isinstance(node, str):
        return escape(node, quote=False)
    attrs = ''.join(f' {name}="{escape(value or "", quote=True)}"' for name, value in node.attrs.items())
    if node.tag == 'root':
        return ''.join(serialize(child) for child in node.children)
    opening = f'<{node.tag}{attrs}>'
    if node.tag in VOID:
        return opening
    return opening + ''.join(serialize(child) for child in node.children) + f'</{node.tag}>'


def build(source):
    destination = DESTINATIONS[source]
    text = (ROOT / source).read_text()
    title = SOURCES[source]
    outline = ''
    if source.endswith('.md'):
        # Display skill metadata as ordinary page content, preserving both values.
        text = re.sub(r'\A---\nname: (.+)\ndescription: (.+)\n---\n',
                      lambda m: f'# {m[1]}\n\n{m[2]}\n', text)
        converter = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc', 'sane_lists'])
        tree = Parser(converter.convert(text)).root
        headings = tree.all(lambda node: node.tag == 'h1')
        if headings:
            title = headings[0].text()
            tree.children.remove(headings[0])
        for node in tree.all(lambda node: node.tag == 'a'):
            href = node.attrs.get('href', '')
            node.attrs['href'] = reading_href(href, source, destination)
            # Historical review files remain explicit source downloads, outside
            # participant navigation. Current examples always have HTML views.
            if source == 'WORKSHOP.md' and href.startswith('review/') and href not in DESTINATIONS:
                node.attrs['download'] = href.rsplit('/', 1)[-1]
                node.children.insert(0, 'Download ')
        for node in tree.all(lambda node: node.tag == 'img'):
            node.attrs['src'] = reading_href(node.attrs['src'], source, destination)
            if 'cail-logo' in node.attrs['src']:
                node.attrs['class'] = 'reference-logo'
        for node in tree.all(lambda node: node.tag == 'table'):
            node.attrs['class'] = 'reference-table'
        for number, node in enumerate(tree.all(lambda node: node.tag == 'pre'), 1):
            node.attrs.update({'id': f'copy-{number}', 'class': 'reference-code'})
        content = serialize(tree)
        content = re.sub(r'(<pre id="(copy-\d+)"[^>]*>.*?</pre>)',
                         lambda m: '<div class="prompt-container"><button type="button" class="copy-prompt" '
                         f'data-example-copy="{m[2]}">Copy text</button>{m[1]}</div>', content, flags=re.S)
        sections = tree.all(lambda node: node.tag == 'h2')
        if len(sections) > 2:
            items = ''.join(f'<li>{link("#" + node.attrs["id"], node.text())}</li>' for node in sections)
            outline = f'<nav class="copy-outline" aria-label="Page outline"><ul>{items}</ul></nav>'
    else:
        # Keep every source byte, including final newlines, available for copying.
        content = ('<div class="prompt-container"><button type="button" class="copy-prompt" '
                   'data-example-copy="source-copy">Copy text</button>'
                   '<pre class="reference-code" id="source-copy">' + escape(text) + '</pre></div>')

    download_label = {'.md': 'Download Markdown', '.txt': 'Download text',
                      '.json': 'Download JSON', '.py': 'Download Python'}
    suffix = '.' + source.rsplit('.', 1)[-1]
    nav = [link(relative('index.html', destination), 'Return to workshop'),
           link(relative('examples.html', destination), 'Prompt examples'),
           link(relative(source, destination), download_label[suffix], source.rsplit('/', 1)[-1])]
    return page(title, content, destination, nav, outline)


def main():
    errors = []
    for source in SOURCES:
        destination = ROOT / DESTINATIONS[source]
        output = build(source)
        if '--write' in sys.argv:
            destination.write_text(output)
        elif not destination.exists() or destination.read_text() != output:
            errors.append(str(destination.relative_to(ROOT)))
    if errors:
        print('Reading pages out of sync: ' + ', '.join(errors))
        return 1
    print(f'{len(SOURCES)} HTML reading pages ' + ('synchronized.' if '--write' in sys.argv else 'checked.'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
