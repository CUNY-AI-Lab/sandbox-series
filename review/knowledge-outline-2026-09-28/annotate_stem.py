"""Add SVG callouts over unchanged, dated Firefox captures."""
from pathlib import Path
import base64, hashlib, html, json
ROOT = Path(__file__).resolve().parents[2]
IMAGES = ROOT / 'images/knowledge-stem-2026-09-28'
# Coordinates refer to original 1919 x 1049 captures. ViewBox crops omit browser chrome.
SPECS = {'clone-model': {'title': 'Clone Models', 'view': [48, 85, 1871, 600], 'boxes': [[55, 265, 42, 42], [122, 218, 710, 45], [1687, 370, 196, 40]], 'arrows': [['Workspace', 190, 560, [[380, 536], [98, 295]]], ['Clone', 1330, 620, [[1450, 576], [1680, 394]]]]}, 'review-clone': {'title': 'Review Settings', 'view': [108, 171, 1790, 640], 'boxes': [[208, 180, 550, 63], [120, 267, 600, 64]], 'arrows': [['Rename copy', 840, 225, [[823, 214], [770, 211]]], ['Base Model', 840, 317, [[824, 307], [734, 307]]]]}, 'create-collection': {'title': 'Create Collections', 'view': [526, 275, 900, 590], 'boxes': [[557, 366, 818, 42], [557, 431, 830, 180], [1187, 785, 205, 60]], 'arrows': []}, 'add-content': {'title': 'Add Sources', 'view': [110, 190, 1786, 510], 'boxes': [[1849, 250, 41, 38], [1634, 337, 242, 39]], 'arrows': [['Upload files', 1260, 605, [[1422, 560], [1622, 361]]]]}, 'collection-documents': {'title': 'Check Documents', 'view': [110, 170, 1786, 505], 'boxes': [[140, 329, 525, 122]], 'arrows': [['Open source documents', 786, 561, [[964, 513], [680, 403]]]]}, 'attach-knowledge': {'title': 'Attach Knowledge', 'view': [109, 505, 1767, 306], 'boxes': [[208, 531, 142, 35], [125, 565, 270, 33]], 'arrows': [['Select Knowledge', 799, 698, [[980, 656], [362, 551]]]]}, 'focused-retrieval': {'title': 'Focus Retrieval', 'view': [368, 465, 1220, 346], 'boxes': [[1383, 548, 155, 72]], 'arrows': [['Keep switch off', 890, 745, [[1180, 709], [1503, 630]]]]}, 'native-retrieval': {'title': 'Enable Retrieval', 'view': [108, 789, 820, 246], 'boxes': [[118, 882, 572, 35]], 'arrows': [['Select Native', 375, 989, [[546, 950], [646, 926]]]]}, 'retrieval-capabilities': {'title': 'Enable Knowledge', 'view': [105, 297, 1490, 420], 'boxes': [[1305, 401, 185, 73], [1305, 548, 185, 35]], 'arrows': [['Enable Knowledge Base', 570, 659, [[1018, 621], [1295, 567]]]]}, 'test-retrieval': {'title': 'Test Retrieval', 'view': [48, 86, 1871, 950], 'boxes': [[1264, 974, 239, 45]], 'arrows': [['Select your copy', 1257, 863, [[1451, 877], [1430, 964]]]]}}
SPECS['check-citations'] = dict(title='Check Citations',view=[376,285,1195,562],boxes=[[409,311,920,35],[411,505,1092,99]],arrows=[])

SPECS['find-knowledge'] = dict(title='Find Knowledge collection',view=[48,85,850,370],boxes=[[55,262,270,45],[452,98,129,34],[359,215,246,31]],arrows=[])
SPECS['create-custom-collection'] = dict(title='Create Your Collection',view=[538,280,879,577],boxes=[[557,366,818,42],[557,431,830,180],[1187,785,205,60]],arrows=[])
SPECS['upload-custom-sources'] = dict(title='Upload Your Sources',view=[110,170,1786,510],boxes=[[1849,250,41,38],[1634,337,242,39]],arrows=[['Upload your files',1210,605,[[1422,560],[1622,361]]]])

manifest=[]
for name,spec in SPECS.items():
 raw=IMAGES/(name+'-raw.png'); data=raw.read_bytes()
 title=html.escape(spec['title']); view=' '.join(map(str,spec['view']))
 overlay=[]
 for x,y,w,h in spec['boxes']:
  overlay.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>')
 paths=[]; labels=[]
 for label,x,y in spec.get('labels',[]):
  labels.append(f'<text x="{x}" y="{y}">{html.escape(label)}</text>')
 for label,x,y,points in spec['arrows']:
  d='M'+' L'.join(f'{px} {py}' for px,py in points)
  paths.append(f'<path d="{d}" marker-end="url(#arrow)"/>')
  labels.append(f'<text x="{x}" y="{y}">{html.escape(label)}</text>')
 desc=f'{spec["title"]}. White annotations over a Firefox screenshot captured on 28 September 2026.'
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{spec['view'][2]}" height="{spec['view'][3]}" viewBox="{view}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{html.escape(desc)}</desc>
<defs><marker id="arrow" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="8" markerHeight="8" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="#fff" stroke-width="2"/></marker></defs>
<image x="0" y="0" width="1919" height="1049" href="data:image/png;base64,{base64.b64encode(data).decode()}"/>
<g fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{''.join(overlay+paths)}</g>
<g fill="#fff" stroke="#171717" stroke-width="8" paint-order="stroke" stroke-linejoin="round" font-family="Arial, Helvetica, sans-serif" font-size="42" font-weight="600">{''.join(labels)}</g>
</svg>'''
 (IMAGES/(name+'.svg')).write_text(svg)
 manifest.append(dict(name=name,raw=str(raw.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),dimensions=[1919,1049],view_box=spec['view'],capture='Firefox native CUA screenshot',annotation='SVG overlay; PNG preserves decoded capture pixels',capture_file=str((IMAGES/(name+'-capture.jpg')).relative_to(ROOT)),capture_sha256=hashlib.sha256((IMAGES/(name+'-capture.jpg')).read_bytes()).hexdigest()))
(Path(__file__).parent/'stem-screenshots.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Created {len(manifest)} annotated images from unchanged captures.')
