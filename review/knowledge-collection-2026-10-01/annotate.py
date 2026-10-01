"""White SVG annotations over unchanged, decoded Firefox captures."""
from pathlib import Path
from PIL import Image
import base64, hashlib, html, json
R=Path(__file__).resolve().parents[2]
D=R/'images/knowledge-collection-2026-10-01'
specs={
 'navigation':([90,180,1560,500],[(95,535,535,73),(900,196,239,67),(710,423,910,113)],[]),
 'root':([215,320,1285,555],[(240,665,640,78),(240,746,670,77)],[(985,712,'Source files'),(985,796,'Source directions')]),
 'wikipedia':([215,320,1285,680],[(245,965,650,82),(240,1082,0,0)],[]),
 'root-mobile':([225,345,750,490],[(240,665,640,78),(240,746,670,77)],[]),
 'wikipedia-mobile':([225,345,750,640],[(735,652,165,66),(244,729,590,245)],[]),
 'select-original-mobile':([1295,1285,810,215],[(1403,1366,467,81)],[(1330,1333,'STEM Adventure Games')]),
 'select-original':([415,995,1680,510],[(1403,1366,467,81)],[])
}
specs['wikipedia']=([215,320,1285,680],[(735,652,165,66),(244,729,590,245)],[(960,858,'Article files')])
manifest=[]
for name,(view,boxes,labels) in specs.items():
 cap=D/(name.replace('-mobile','')+'-capture.jpg'); im=Image.open(cap).convert('RGB'); raw=D/(name+'-raw.png'); im.save(raw)
 boxes=[b for b in boxes if b[2]>0 and b[3]>0]
 x,y,w,h=view
 rects=''.join(f'<rect x="{a}" y="{b}" width="{c}" height="{d}" rx="10"/>' for a,b,c,d in boxes)
 texts=''.join(f'<text x="{a}" y="{b}">{html.escape(t)}</text>' for a,b,t in labels)
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{name.title()}</title><desc id="desc">Firefox screenshot captured October 1, 2026. White annotations over unchanged capture pixels.</desc><image x="0" y="0" width="{im.width}" height="{im.height}" href="data:image/png;base64,{base64.b64encode(raw.read_bytes()).decode()}"/><g fill="none" stroke="#fff" stroke-width="4">{rects}</g><g fill="#fff" stroke="#171717" stroke-width="6" paint-order="stroke" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="600">{texts}</g></svg>'''
 (D/(name+'.svg')).write_text(svg)
 manifest.append(dict(name=name,raw=str(raw.relative_to(R)),sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),capture_file=str(cap.relative_to(R)),capture_sha256=hashlib.sha256(cap.read_bytes()).hexdigest(),dimensions=list(im.size),view_box=view,capture='Firefox native CUA screenshot',annotation='SVG overlay on decoded capture pixels'))
(Path(__file__).parent/'screenshots.json').write_text(json.dumps(manifest,indent=2)+'\n')
