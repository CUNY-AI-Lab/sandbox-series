#!/usr/bin/env python3
"""Check public reading routes, source fidelity, and downloadable originals."""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

from check_workshop import Parser
from build_reading_pages import build
from build_workshop_copy import build as build_deck, build_series, DECKS
from reading_pages import ROOT, SOURCES, DESTINATIONS


class ReadingPages(unittest.TestCase):
    def test_generated_views_match_sources(self):
        for source in SOURCES:
            with self.subTest(source=source):
                output = (ROOT / DESTINATIONS[source]).read_text()
                self.assertEqual(output, build(source))
                tree = Parser(output).root
                pre = tree.all(lambda node: node.tag == 'pre')
                if not source.endswith('.md'):
                    self.assertEqual(len(pre), 1)
                    self.assertEqual(pre[0].text(), (ROOT / source).read_text())
                else:
                    fences = re.findall(r'^(`{3,}|~{3,})[^\n]*\n(.*?)^\1\s*$',
                                        (ROOT / source).read_text(), re.M | re.S)
                    self.assertEqual([node.text().rstrip('\n') for node in pre],
                                     [body.rstrip('\n') for _, body in fences])
                downloads = tree.all(lambda node: node.tag == 'a' and 'download' in node.attrs)
                self.assertTrue(any((ROOT / DESTINATIONS[source]).parent.joinpath(
                    node.attrs['href']).resolve() == ROOT / source for node in downloads))

    def test_transcripts_cover_every_deck(self):
        for route, _ in DECKS:
            with self.subTest(route=route):
                source = Parser((ROOT / route / 'index.html').read_text()).root
                copied = Parser((ROOT / route / 'workshop-copy.html').read_text()).root
                slides = source.all(lambda node: node.has_class('slide'))
                sections = copied.all(lambda node: node.has_class('copy-section'))
                self.assertEqual(len(slides), len(sections))
                self.assertEqual((ROOT / route / 'workshop-copy.html').read_text(), build_deck(route))
                for slide, section in zip(slides, sections):
                    self.assertEqual([node.text() for node in slide.all(lambda node: node.tag == 'pre')],
                                     [node.text() for node in section.all(lambda node: node.tag == 'pre')])
                    images = slide.all(lambda node: node.tag == 'img')
                    self.assertEqual([node.attrs['alt'] for node in images],
                                     [node.attrs['alt'] for node in section.all(lambda node: node.tag == 'img')])
                    for image in images:
                        self.assertIn(image.attrs['alt'], section.text())
        self.assertEqual((ROOT / 'SLIDES.html').read_text(), build_series())

    def test_every_reading_link_opens_formatted_html(self):
        pending = [ROOT / path for path in [
            'index.html', 'knowledge/index.html', 'skills/index.html',
            'examples.html', 'workshop-copy.html', 'knowledge/workshop-copy.html',
            'skills/workshop-copy.html', 'SLIDES.html', 'WORKSHOP.html',
            *DESTINATIONS.values(),
        ]]
        seen = set()
        while pending:
            path = pending.pop().resolve()
            if path in seen:
                continue
            seen.add(path)
            self.assertTrue(path.is_relative_to(ROOT), str(path))
            self.assertTrue(path.exists(), str(path))
            tree = Parser(path.read_text()).root
            self.assertTrue(tree.all(lambda node: node.tag == 'main' or node.attrs.get('id') == 'deck')
                            or path.name == 'preview.html', str(path))
            self.assertTrue(tree.all(lambda node: node.tag == 'style' or
                            (node.tag == 'link' and node.attrs.get('rel') == 'stylesheet')), str(path))
            ids = [node.attrs['id'] for node in tree.all(lambda node: 'id' in node.attrs)]
            self.assertEqual(len(ids), len(set(ids)), 'Duplicate ID: ' + str(path))
            for button in tree.all(lambda node: 'data-example-copy' in node.attrs):
                self.assertIn(button.attrs['data-example-copy'], ids, str(path))
            for node in tree.all(lambda node: node.tag in {'a', 'img', 'script', 'link'}):
                href = node.attrs.get('href') or node.attrs.get('src', '')
                url = urlsplit(href)
                if not href or url.scheme or url.netloc:
                    continue
                target = path.parent / unquote(url.path) if url.path else path
                if target.is_dir():
                    target /= 'index.html'
                target = target.resolve()
                self.assertTrue(target.exists(), f'{path.relative_to(ROOT)}: {href}')
                if node.tag != 'a':
                    continue
                if 'download' in node.attrs:
                    self.assertIn('download', node.text().lower(), f'{path}: {href}')
                    continue
                self.assertIn(target.suffix, {'.html', '.png', '.svg', '.jpg'},
                              f'Unformatted reading link in {path.relative_to(ROOT)}: {href}')
                if target.suffix != '.html':
                    continue
                pending.append(target)
                if url.fragment:
                    other = tree if target == path else Parser(target.read_text()).root
                    other_ids = {node.attrs['id'] for node in other.all(lambda node: 'id' in node.attrs)}
                    if url.fragment.isdigit():
                        slides = other.all(lambda node: node.has_class('slide'))
                        self.assertTrue(1 <= int(url.fragment) <= len(slides), href)
                    else:
                        self.assertIn(unquote(url.fragment), other_ids, f'{path}: {href}')
        self.assertGreaterEqual(len(seen), 40)

    def test_first_workshop_stays_self_contained(self):
        for name in ['index.html', 'workshop-copy.html']:
            tree = Parser((ROOT / name).read_text()).root
            for node in tree.all(lambda node: node.tag == 'a' and 'download' not in node.attrs):
                href = node.attrs.get('href', '')
                self.assertNotIn(href, ['SLIDES.html', 'WORKSHOP.html'])
                self.assertFalse(href.startswith(('knowledge/', 'skills/')), href)


if __name__ == '__main__':
    unittest.main()
