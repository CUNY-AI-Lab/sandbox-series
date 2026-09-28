from pathlib import Path
import sys, re, html, markdown
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from reading_pages import page,link
md_path=ROOT/'knowledge/OUTLINE.md'
s=md_path.read_text()
sections=[];nav=[]
for part in re.split(r'(?m)^## ',s)[1:]:
 title,body=part.split('\n',1);n,label=title.split('. ',1)
 body=re.sub(r'(?m)^---\s*$','',body)
 content=markdown.markdown(body,extensions=['tables','fenced_code'])
 content=re.sub(r'<p>(<img alt="([^"]*)" src="([^"]*)"\s*/>)</p>',lambda m: '<figure>'+m[1]+f'<figcaption class="image-alt">Alt text — {m[2]}</figcaption></figure>',content)
 sections.append(f'<section class="copy-section" id="slide-{n}"><p class="slide-link">Slide {n}</p><h2>{html.escape(label)}</h2><div class="copy-content">{content}</div></section>')
 nav.append(f'<li><a href="#slide-{n}">{html.escape(label)}</a></li>')
out=page('Curating knowledge collections','\n'.join(sections),'knowledge/OUTLINE.html',[link('OUTLINE.md','Download outline', 'OUTLINE.md')],'<nav class="copy-outline" aria-label="Workshop outline"><ol>'+''.join(nav)+'</ol></nav>')
out=out.replace('</head>','''<style>
main{width:min(1640px,100%)}
.copy-content>p:not(:has(img)):not(.image-alt),.copy-content>ul,.copy-content>table{max-width:1040px}
.copy-content p:has(img){margin-bottom:14px}
.copy-content img{width:100%;max-height:80vh;object-fit:contain;object-position:left}
.image-alt{max-width:1040px}
</style></head>''')
(ROOT/'knowledge/OUTLINE.html').write_text(out)
print('Built local HTML outline.')
