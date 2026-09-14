#!/usr/bin/env python3
"""Validate all decks and keep complete copy/diffs synchronized. Standard library only."""
from pathlib import Path
import re,json,difflib,hashlib,sys,subprocess
from check_workshop import Parser,Node,render
R=Path(__file__).resolve().parents[1];write='--write' in sys.argv;issues=[];sections=[]
def clean(text):
 return re.sub(r'\n{3,}', '\n\n', '\n'.join(line.rstrip() for line in text.splitlines())).strip()+'\n'
retained=json.loads((R/'review/imported-copy.json').read_text()); found={};count=0
for route,label in [('', 'Compose System Prompts'),('knowledge','Curate Knowledge Collections'),('skills','Skills & Tools')]:
 base=R/route;tree=Parser((base/'index.html').read_text()).root;slides=tree.all(lambda n:n.has_class('slide'));count+=len(slides)
 for heading in tree.all(lambda n:n.tag in {'h1','h2','h3','h4'}):
  title=heading.text().strip()
  if not 2 <= len(re.findall(r"[\w]+(?:[’'-][\w]+)*",title)) <= 3:issues.append(route+' heading length: '+title)
  if re.search(r'\b(a|an|the)\b',title,re.I):issues.append(route+' article in heading: '+title)
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
   if not s.has_class('screenshot-slide'):issues.append(route+' screenshot layout regression')
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
 sections.append(content)
 if route:
  mirror='# '+label+'\n\nGenerated from index.html. Screenshot instructions are included below.\n\n'+content
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
for key,record in retained.items():
 expected=record['before']
 for e in record['changes']:expected=expected.replace(e['before'],e['after'])
 if re.sub(r'\s+','',expected)!=re.sub(r'\s+','',found.get(key,'')):issues.append('Unrecorded source change '+key)
for manifest,folder in [('screenshot-sources.json','current'),('showcase-sources.json','showcase')]:
 for x in json.loads((R/'review'/manifest).read_text())['images']:
  if hashlib.sha256((R/'images'/folder/x['file']).read_bytes()).hexdigest()!=x['sha256']:issues.append('Image hash mismatch '+x['file'])
full='# Sandbox workshop series — full slide copy\n\nGenerated from all three HTML decks. This includes screenshot captions and supporting instructions.\n\n'+'\n\n'.join(sections)
if write:(R/'SLIDES.md').write_text(full)
elif not (R/'SLIDES.md').exists() or (R/'SLIDES.md').read_text()!=full:issues.append('Full copy out of sync')
example_tree=Parser((R/'examples.html').read_text()).root
for heading in example_tree.all(lambda n:n.tag in {'h1','h2','h3','h4'}):
 title=heading.text().strip()
 if not 2 <= len(re.findall(r"[\w]+(?:[’'-][\w]+)*",title)) <= 3 or re.search(r'\b(a|an|the)\b',title,re.I):issues.append('examples heading: '+title)
r=subprocess.run([sys.executable,str(R/'scripts/check_workshop.py')]+(['--write'] if write else []),capture_output=True,text=True)
if r.returncode:issues.append(r.stdout)
print(f'{count} slides across three workshops; {len(retained)} imported sections checked; image provenance and links checked.')
if issues:print('\n'.join(issues));raise SystemExit(1)
print('Series checks passed.')
