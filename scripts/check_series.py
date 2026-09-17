#!/usr/bin/env python3
"""Validate all decks and keep complete copy/diffs synchronized. Standard library only."""
from pathlib import Path
import re,json,difflib,hashlib,sys,subprocess,posixpath
from check_workshop import Parser,Node,render
R=Path(__file__).resolve().parents[1];write='--write' in sys.argv;issues=[];sections=[]
# Exact event title requested by Zach; general slide-title constraints still apply elsewhere.
COVER_TITLE='Getting Started with the CUNY AI Lab Sandbox'
def clean(text):
 return re.sub(r'\n{3,}', '\n\n', '\n'.join(line.rstrip() for line in text.splitlines())).strip()+'\n'
def check_title(title,location):
 if title in {'Composing system prompts','Curating knowledge collections','Configuring skills and tools','Situating System Prompts',COVER_TITLE}:return
 words=re.findall(r"[\w]+(?:[’'-][\w]+)*",title)
 if not 2 <= len(words) <= 3:issues.append(location+' heading length: '+title)
 if re.search(r'\b(a|an|the)\b',title,re.I):issues.append(location+' article in heading: '+title)
 if any(w.lower().endswith('ing') for w in words):issues.append(location+' -ing form in heading: '+title)

def participant_text(node):
 if isinstance(node,str):return node
 if node.tag in {'h1','title'} and node.text().strip() in {COVER_TITLE,COVER_TITLE+' | CUNY AI Lab'}:return ''
 if node.tag in {'pre','script','style'} or node.has_class('prompt-block') or node.has_class('quoted-prompt'):return ''
 if node.tag=='img':return node.attrs.get('alt','')
 return ' '.join(participant_text(child) for child in node.children)

def check_participant_copy(tree,location):
 for heading in tree.all(lambda n:n.tag in {'h1','h2','h3','h4'}):check_title(heading.text().strip(),location)
 for slide in tree.all(lambda n:n.has_class('slide')):
  if slide.all(lambda n:n.has_class('slide-notes') or 'hidden' in n.attrs):issues.append(location+' hidden slide content')
  check_title(slide.attrs.get('data-title',''),location+' outline')
  headings=slide.all(lambda n:n.tag in {'h1','h2'})
  if not headings or headings[0].text().strip()!=slide.attrs.get('data-title'):issues.append(location+' heading and outline disagree')
 text=participant_text(tree)
 if re.search(r'\bthe\b',text,re.I):issues.append(location+' definite article in participant copy outside quoted prompts')
 if re.search(r'\b(facilitator|presenter)\b',text,re.I):issues.append(location+' presenter directions in participant copy')
 for phrase in ['preserve their original disciplinary purposes','instruction drafts, not measured outcomes','these excerpts are discussion material']:
  if phrase in text.lower():issues.append(location+' editorial commentary in participant copy: '+phrase)
 if tree.all(lambda n:n.tag=='a' and n.attrs.get('href','').endswith('WORKSHOP.md')):issues.append(location+' presenter plan linked from participant material')

retained=json.loads((R/'review/imported-copy.json').read_text()); found={};count=0
for route,label in [('', 'Composing system prompts'),('knowledge','Curating knowledge collections'),('skills','Configuring skills and tools')]:
 base=R/route;tree=Parser((base/'index.html').read_text()).root;slides=tree.all(lambda n:n.has_class('slide'));count+=len(slides)
 check_participant_copy(tree,route or 'prompts')
 if tree.all(lambda n:n.attrs.get('id') in {'notes-button','series-button'}):issues.append(route+' removed footer control returned')
 ids=[n.attrs['id'] for n in tree.all(lambda n:'id' in n.attrs)]
 if len(ids)!=len(set(ids)):issues.append(route+' duplicate ids')
 for i,s in enumerate(slides,1):
  if s.attrs.get('aria-label')!=f'Slide {i}: '+s.attrs['data-title']:issues.append(route+' incorrect slide label')
  for n in s.all(lambda n:'data-copy' in n.attrs):
   if n.attrs['data-copy'] not in ids:issues.append(route+' missing copy target')
  if s.attrs.get('data-original'):found[s.attrs['data-original']]=s.text()
  for n in s.all(lambda n:n.tag=='img'):
   if not n.attrs.get('alt'):issues.append(route+' missing image alternative')
   if not s.has_class('screenshot-slide') and not (s.has_class('workshop-cover') and n.has_class('cover-wordmark')):issues.append(route+' screenshot layout regression')
  if s.attrs.get('data-agenda'):
   for li in s.all(lambda n:n.tag=='li'):
    if re.search(r'\b(a|an|the)\b',li.text(),re.I):issues.append(route+' article in mini-agenda')
 for n in tree.all(lambda n:n.tag in {'img','script','link','a'}):
  target=n.attrs.get('src') or n.attrs.get('href','')
  if target and not re.match(r'^(https?:|mailto:|#)',target):
   p=base/target.split('#')[0].split('?')[0]
   if not p.exists():issues.append(route+' missing resource '+target)
 content='\n\n---\n\n'.join('## '+label+' — '+str(i)+'\n\n'+re.sub(r'\n{3,}','\n\n',render(s)).strip() for i,s in enumerate(slides,1))+'\n'
 content=clean(content)
 sections.append(re.sub(r'\]\((?!https?:|mailto:|#)([^)]+)\)',lambda m:']('+posixpath.normpath(route+'/'+m.group(1))+')',content) if route else content)
 if route:
  mirror='# '+label+'\n\n'+content
  dest=base/'SLIDES.md'
  if write:dest.write_text(mirror)
  elif not dest.exists() or dest.read_text()!=mirror:issues.append(route+' mirror out of sync')
  source_tree=Parser((R/'review'/route/'source.html').read_text()).root
  before='\n\n---\n\n'.join(render(x) for x in source_tree.all(lambda n:n.has_class('slide')))
  before=clean(before)
  beforefile=R/'review'/route/'before.md';afterfile=R/'review'/route/'copy.diff'
  diff=''.join(difflib.unified_diff(before.splitlines(True),mirror.splitlines(True),fromfile='before original HTML',tofile='after consolidated workshop'))
  if write:beforefile.write_text(before);afterfile.write_text(diff)
  elif not afterfile.exists() or afterfile.read_text()!=diff:issues.append(route+' copy diff out of sync')
# Optional material stays visible on ordinary reference pages and retains source custody.
for route in ['knowledge','skills']:
 base=R/route; tree=Parser((base/'reference.html').read_text()).root
 check_participant_copy(tree,route+' reference')
 if tree.all(lambda n:n.has_class('slide-notes') or n.tag=='details' or 'hidden' in n.attrs):issues.append(route+' hidden reference content')
 ids=[n.attrs['id'] for n in tree.all(lambda n:'id' in n.attrs)]
 if len(ids)!=len(set(ids)):issues.append(route+' duplicate reference ids')
 for n in tree.all(lambda n:'data-example-copy' in n.attrs):
  if n.attrs['data-example-copy'] not in ids:issues.append(route+' missing reference copy target')
 for n in tree.all(lambda n:n.has_class('reference-example')):
  if n.attrs.get('data-original'):found[n.attrs['data-original']]=n.text()
 for n in tree.all(lambda n:n.tag in {'img','script','link','a'}):
  target=n.attrs.get('src') or n.attrs.get('href','')
  if target and not re.match(r'^(https?:|mailto:|#)',target):
   if not (base/target.split('#')[0].split('?')[0]).exists():issues.append(route+' missing reference resource '+target)
 content=clean(render(tree.all(lambda n:n.tag=='main')[0]))
 dest=base/'REFERENCE.md'
 if write:dest.write_text(content)
 elif not dest.exists() or dest.read_text()!=content:issues.append(route+' reference mirror out of sync')
retired=json.loads((R/'review/retired-sections.json').read_text())['imported']
for key,record in retained.items():
 if key in retired:
  if key in found:issues.append('Retired example returned: '+key)
  continue
 expected=record['before']
 for e in record['changes']:expected=expected.replace(e['before'],e['after'])
 if re.sub(r'\s+','',expected)!=re.sub(r'\s+','',found.get(key,'')):issues.append('Unrecorded source change '+key)
for manifest,folder in [('screenshot-sources.json','current'),('showcase-sources.json','showcase')]:
 for x in json.loads((R/'review'/manifest).read_text())['images']:
  if hashlib.sha256((R/'images'/folder/x['file']).read_bytes()).hexdigest()!=x['sha256']:issues.append('Image hash mismatch '+x['file'])
for asset in json.loads((R/'review/cover-media.json').read_text())['images']:
 if hashlib.sha256((R/asset['file']).read_bytes()).hexdigest()!=asset['sha256']:issues.append('Cover media hash mismatch '+asset['file'])
full='# Sandbox Workshops\n\n'+'\n\n'.join(sections)
# Print image alternatives as copy, so they remain visible in rendered Markdown.
image_pattern=r'(\[!\[([^\]]*)\]\([^)]+\)\]\([^)]+\)|!\[([^\]]*)\]\([^)]+\))'
full=re.sub(image_pattern,lambda m:m.group(1)+'\n\n**Alt text:** '+(m.group(2) or m.group(3)),full)
if write:(R/'SLIDES.md').write_text(full)
elif not (R/'SLIDES.md').exists() or (R/'SLIDES.md').read_text()!=full:issues.append('Full copy out of sync')
example_tree=Parser((R/'examples.html').read_text()).root
check_participant_copy(example_tree,'examples')
research_tree=Parser((R/'examples/research/sample-revisions.html').read_text()).root
check_participant_copy(research_tree,'research samples')
r=subprocess.run([sys.executable,str(R/'scripts/check_workshop.py')]+(['--write'] if write else []),capture_output=True,text=True)
if r.returncode:issues.append(r.stdout)
r=subprocess.run([sys.executable,str(R/'scripts/build_workshop_copy.py')]+(['--write'] if write else []),capture_output=True,text=True)
if r.returncode:issues.append(r.stdout)
print(f'{count} slides across three workshops; {len(retained)} imported sections checked; image provenance and links checked.')
if issues:print('\n'.join(issues));raise SystemExit(1)
print('Series checks passed.')
