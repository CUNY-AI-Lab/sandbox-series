#!/usr/bin/env python3
"""Keep screenshot display limits within actual raster resolution, including SVGs."""
from pathlib import Path
import base64
import math
import re
import struct
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def png_size(data):
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('Screenshot must contain lossless PNG pixels')
    return struct.unpack('>II', data[16:24])


def display_limit(path):
    """Return CSS width at which no embedded raster is enlarged beyond 1:1."""
    if path.suffix.lower() == '.png':
        return png_size(path.read_bytes())[0]
    root = ET.parse(path).getroot()
    _, _, width, _ = map(float, root.attrib['viewBox'].split())
    scales = []
    for element in root.iter():
        if element.tag.rsplit('}', 1)[-1] != 'image':
            continue
        source = element.get('href') or element.get('{http://www.w3.org/1999/xlink}href')
        if not source or not source.startswith('data:image/png;base64,'):
            raise ValueError('SVG screenshot must embed its original PNG')
        pixels_w, pixels_h = png_size(base64.b64decode(source.split(',', 1)[1]))
        scales.append(min(pixels_w / float(element.attrib['width']),
                          pixels_h / float(element.attrib['height'])))
    if not scales:
        raise ValueError('SVG screenshot has no raster source')
    return math.floor(width * min(scales))


def main():
    write = '--write' in sys.argv
    problems = []
    count = 0
    for relative in ['index.html', 'knowledge/index.html', 'skills/index.html']:
        path = ROOT / relative
        html = path.read_text()

        def check(match):
            nonlocal count
            tag = match.group()
            if 'screenshot-img' not in tag:
                return tag
            count += 1
            source = re.search(r'\bsrc="([^"]+)"', tag).group(1)
            limit = display_limit(path.parent / source)
            expected = f'--screenshot-max-width:{limit}px'
            if expected not in tag:
                if not write:
                    problems.append(f'{relative}: missing resolution limit for {source}')
                style = re.search(r'\bstyle="([^"]*)"', tag)
                if style:
                    declarations = [value.strip() for value in style.group(1).split(';')
                                    if value.strip() and not value.strip().startswith('--screenshot-max-width:')]
                    declarations.append(expected)
                    tag = tag[:style.start(1)] + ';'.join(declarations) + tag[style.end(1):]
                else:
                    tag = tag.replace(' src=', f' style="{expected}" src=', 1)
            return tag

        updated = re.sub(r'<img\b[^>]*>', check, html)
        if write and updated != html:
            path.write_text(updated)
    if problems:
        raise SystemExit('\n'.join(problems))
    print(f'{count} screenshots checked against original raster dimensions.')


if __name__ == '__main__':
    main()
