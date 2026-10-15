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


def jpeg_size(data):
    """Read dimensions from the original JPEG frame without recompressing it."""
    if data[:2] != b'\xff\xd8':
        raise ValueError('Screenshot must contain JPEG pixels')
    offset = 2
    frame_markers = {0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7,
                     0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf}
    while offset < len(data):
        if data[offset] != 0xff:
            break
        while offset < len(data) and data[offset] == 0xff:
            offset += 1
        if offset >= len(data):
            break
        marker = data[offset]
        offset += 1
        if marker in {0xd9, 0xda}:
            break
        if marker == 0x01 or 0xd0 <= marker <= 0xd7:
            continue
        if offset + 2 > len(data):
            break
        length = int.from_bytes(data[offset:offset + 2], 'big')
        if length < 2 or offset + length > len(data):
            break
        if marker in frame_markers and length >= 8:
            height, width = struct.unpack('>HH', data[offset + 3:offset + 7])
            if width and height:
                return width, height
            break
        offset += length
    raise ValueError('JPEG screenshot has no valid frame dimensions')


def display_limit(path):
    """Return CSS width at which no embedded raster is enlarged beyond 1:1."""
    if path.suffix.lower() == '.png':
        return png_size(path.read_bytes())[0]
    if path.suffix.lower() in {'.jpg', '.jpeg'}:
        return jpeg_size(path.read_bytes())[0]
    root = ET.parse(path).getroot()
    _, _, width, _ = map(float, root.attrib['viewBox'].split())
    scales = []
    for element in root.iter():
        if element.tag.rsplit('}', 1)[-1] != 'image':
            continue
        source = element.get('href') or element.get('{http://www.w3.org/1999/xlink}href')
        if not source or not source.startswith(('data:image/png;base64,', 'data:image/jpeg;base64,')):
            raise ValueError('SVG screenshot must embed its original PNG or JPEG')
        read_size = png_size if source.startswith('data:image/png;') else jpeg_size
        pixels_w, pixels_h = read_size(base64.b64decode(source.split(',', 1)[1], validate=True))
        scales.append(min(pixels_w / float(element.attrib['width']),
                          pixels_h / float(element.attrib['height'])))
    if not scales:
        raise ValueError('SVG screenshot has no raster source')
    return math.floor(width * min(scales))


def main():
    write = '--write' in sys.argv
    problems = []
    count = 0
    for relative in ['basics/index.html', 'knowledge/index.html', 'skills/index.html']:
        path = ROOT / relative
        html = path.read_text()

        def check(match):
            nonlocal count
            tag = match.group()
            if 'screenshot-img' not in tag:
                return tag
            count += 1
            source = re.search(r'\bsrc="([^"]+)"', tag).group(1)
            limit = display_limit(path.parent / source.split('?', 1)[0])
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
