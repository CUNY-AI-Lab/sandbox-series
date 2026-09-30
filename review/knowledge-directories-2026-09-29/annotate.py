"""White callouts on unchanged Firefox captures; crop browser chrome/empty space."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import base64,html,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'images/knowledge-directories-2026-09-29'
specs={
 'directory-workflow':([210,320,2090,410],[(2178,477,70,72),(1780,561,450,66),(241,628,425,70)],[]),
 'paste-excerpt':([230,290,1890,1000],[(244,409,1350,65)],[]),
 'save-excerpt':([230,1710,2040,660],[(2080,2255,165,109)],[]),
 'create-directory':([210,320,2090,750],[(2178,477,70,72),(1780,561,450,66)],[]),
 'open-directory':([210,320,2070,490],[(241,628,425,70)],[(700,655,'Open directory')]),
 'add-text-content':([1740,535,510,520],[(1777,896,455,69)],[]),
 'add-webpages':([590,1030,1180,510],[(642,1180,1065,183),(1560,1390,149,95)],[]),
 'create-instructions':([230,280,1890,625],[(244,303,580,89)],[]),
 'instructions-root':([210,320,2070,545],[(240,624,640,152)],[(970,744,'Collection root')]),
}
manifest=[]
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',42)
for name,(view,boxes,labels) in specs.items():
 cap=D/(('create-directory' if name=='add-text-content' else name)+'-capture.jpg'); im=Image.open(cap).convert('RGB'); raw=D/(name+'-raw.png');im.save(raw)
 data=raw.read_bytes();x,y,w,h=view
 overlays=''.join(f'<rect x="{a}" y="{b}" width="{c}" height="{d}" rx="12"/>' for a,b,c,d in boxes)
 texts=''.join(f'<text x="{a}" y="{b}">{html.escape(t)}</text>' for a,b,t in labels)
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{name.replace('-',' ').title()}</title><desc id="desc">Firefox screenshot captured 29 September 2026. White annotations over unchanged capture pixels.</desc><image x="0" y="0" width="{im.width}" height="{im.height}" href="data:image/png;base64,{base64.b64encode(data).decode()}"/><g fill="none" stroke="white" stroke-width="5">{overlays}</g><g fill="white" font-family="Arial, Helvetica, sans-serif" font-size="42">{texts}</g></svg>'''
 (D/(name+'.svg')).write_text(svg)
 crop=im.crop((x,y,x+w,y+h));draw=ImageDraw.Draw(crop)
 for a,b,c,d in boxes:draw.rounded_rectangle((a-x,b-y,a-x+c,b-y+d),radius=12,outline='white',width=5)
 for a,b,t in labels:draw.text((a-x,b-y),t,font=font,fill='white',anchor='ls',stroke_width=2,stroke_fill='#171717')
 crop.save(D/(name+'-doc.png'))
 manifest.append(dict(name=name,raw=str(raw.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest(),dimensions=list(im.size),view_box=view,capture='Firefox native CUA screenshot',capture_file=str(cap.relative_to(ROOT)),capture_sha256=hashlib.sha256(cap.read_bytes()).hexdigest(),annotation='White SVG overlay and matching PNG for Google Docs; no reconstructed UI.'))
(Path(__file__).parent/'screenshots.json').write_text(json.dumps(manifest,indent=2)+'\n')
