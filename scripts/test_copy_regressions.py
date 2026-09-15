#!/usr/bin/env python3
"""Participant-copy contracts derived from explicit workshop corrections.

These tests protect known requirements. They do not score prose or identify AI writing.
Historical before/after records and quoted test outputs are deliberately excluded.
"""
import json
import re
import unittest
from unittest.mock import patch
from pathlib import Path
from check_workshop import Parser, Node

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ('index.html', 'knowledge/index.html', 'skills/index.html')
SECTION_NAMES = ('Composing system prompts', 'Curating knowledge collections', 'Configuring skills and tools')
SELECTOR = 'Select model ID on bottom right of message box.'
NURSE = 'The nurse yelled at the doctor because she was late. Who was late?'
CAR = 'The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.'
SHORT_SYSTEM = 'Identify purpose and separate facts from assumptions. Ask one clarifying question when needed. Answer briefly without inventing context.'
# Exact rejected passages from this chat, not a vocabulary blacklist.
REJECTED = (
 'Keep a record of what changes as you build. Evaluation runs through all three workshops.',
 'Workspace access is enabled during guided practice.',
 'Current Sandbox. Model names and available controls depend on your account.',
 'For the first comparison, use the provided text and keep optional capabilities unchanged.',
 'Use the same prompt and chat history for both models. Note which models you selected.',
 'Compare the evidence in the answers. A confident explanation can still rest on an unsupported assumption.',
 'Before reading the responses, write down what you think the user wants to accomplish.',
 'GCDI showcase, May 2026. Gemma recommends walking.',
 'If the purpose is to wash the car, the car must get there. The original wording leaves the purpose unstated',
 'Add a follow-up stating your purpose, such as washing the car or asking about prices.',
 'What should your model request before responding?',
 'How should it respond to each student input?',
 'Select the model name on the right inside the message box.',
 'care-wash prompts', 'two-model', 'system instructions', 'Compare Recommendations',
 'Women in science discusses on',
)

def normalized(s): return ' '.join(s.split())
def authored(node):
    if isinstance(node, str): return node
    if node.tag in {'pre','script','style','button','svg'}: return ''
    if node.has_class('prompt-block') or node.has_class('quoted-prompt'): return ''
    if node.tag == 'img': return node.attrs.get('alt','')
    return ' '.join(authored(child) for child in node.children)
def prose_colons(s):
    # Resource titles, URLs, and code notation are literal identifiers, not prose hinges.
    s = re.sub(r'https?://\S+', '', s)
    s = re.sub(r'Newton: (?:Light and Colour|Experimental Variants)', '', s)
    s = re.sub(r'`[^`]+`', '', s)
    return ':' in s

def general_builder(text):
    return not re.search(r'STEM Adventure|stem_adventure|Prism Laboratory|aperture',text,re.I)

class CopyRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trees = {r:Parser((ROOT/r).read_text()).root for r in ROUTES}
        cls.decks = {r:t.all(lambda n:n.has_class('slide')) for r,t in cls.trees.items()}
        cls.example = Parser((ROOT/'examples.html').read_text()).root
    def slide(self, route, title):
        matches=[s for s in self.decks[route] if s.attrs['data-title']==title]
        self.assertEqual(len(matches),1, (route,title))
        return matches[0]
    def by_id(self, id):
        return self.trees['index.html'].all(lambda n:n.attrs.get('id')==id)[0]
    def assert_order(self, route, titles):
        sequence=[s.attrs['data-title'] for s in self.decks[route]]
        positions=[sequence.index(t) for t in titles]
        self.assertEqual(positions, sorted(set(positions)),titles)

    def test_01_section_names_and_titles(self):
        for route,name in zip(ROUTES,SECTION_NAMES):
            self.assertEqual(self.decks[route][0].attrs['data-title'],name)
            for s in self.decks[route]:
                title=s.attrs['data-title']
                if title in (*SECTION_NAMES,'Situating System Prompts'):continue
                self.assertTrue(2<=len(re.findall(r"[\w]+(?:[’'-][\w]+)*",title))<=3,title)
                self.assertNotRegex(title,r'(?i)\b(a|an|the)\b')
                self.assertFalse(any(w.lower().endswith('ing') for w in title.split()),title)
    def test_02_heading_outline_and_labels_agree(self):
        for route,slides in self.decks.items():
            for i,s in enumerate(slides,1):
                title=s.attrs['data-title'];heading=s.all(lambda n:n.tag in {'h1','h2'})[0]
                self.assertEqual(heading.text(),title)
                self.assertEqual(s.attrs['aria-label'],f'Slide {i}: {title}')
    def test_03_participant_copy_excludes_editorial_instructions(self):
        for tree in [*self.trees.values(),self.example]:
            copy=authored(tree)
            self.assertNotRegex(copy,r'(?i)\b(the|facilitator|presenter)\b')
            self.assertFalse(prose_colons(copy))
            self.assertFalse(tree.all(lambda n:n.tag=='a' and n.attrs.get('href','').endswith('WORKSHOP.md')))
    def test_04_explicit_deletions_stay_deleted(self):
        for tree in [*self.trees.values(),self.example]:
            copy=normalized(tree.text()).casefold()
            for phrase in REJECTED:self.assertNotIn(phrase.casefold(),copy)
    def test_05_prompts_remain_exact(self):
        for id,expected in [('comparison-task',NURSE),('car-wash-task',CAR),('car-wash-exercise',CAR),('sample-system',SHORT_SYSTEM)]:
            self.assertEqual(self.by_id(id).text(),expected)
        self.assertEqual((ROOT/'examples/comparison-task.txt').read_text().strip(),NURSE)
        self.assertEqual((ROOT/'examples/assumption-check.txt').read_text().strip(),SHORT_SYSTEM)
        self.assertLess(len(SHORT_SYSTEM),280)
    def test_06_comparison_scaffolding(self):
        self.assert_order('index.html',['System Prompts','Select Models','Who Was Late?','Examine Assumptions','Compare Outputs','Gemma’s Response','Qwen’s Response','Add System Prompt','Open Chat Controls','Regenerate Responses','Compare Responses','Open Workspace','Review Custom Models','Model Configuration'])
        self.assertIn('Base Models',self.slide('index.html','System Prompts').text())
        self.assertIn('What do you think this person wants to accomplish?',self.slide('index.html','Compare Outputs').text())
        handoff=self.by_id('car-wash-exercise')
        self.assertEqual(handoff.text(),CAR)
    def test_07_controls_and_regeneration_are_explicit(self):
        sequence=self.decks['index.html'][14:17]
        self.assertEqual([s.attrs['data-title'] for s in sequence],['Add System Prompt','Open Chat Controls','Regenerate Responses'])
        add,controls,regenerate=[s.text() for s in sequence]
        for term in ['Copy','in-chat','System Prompt']:self.assertIn(term,add)
        for term in ['Controls','top right','Paste','System Prompt','close Controls']:self.assertIn(term,controls)
        for term in ['Regenerate','Try Again','original response','original question, selected models, and other settings unchanged']:self.assertIn(term,regenerate)
        # These are consecutive actions, not repeated walkthroughs.
        self.assertNotIn('Controls',add)
        self.assertNotIn('Regenerate',add+controls)
        self.assertNotIn('System Prompt',regenerate)
        self.assertNotIn('Test System Prompts',[s.attrs['data-title'] for s in self.decks['index.html']])
        for slide in sequence:self.assertFalse(slide.all(lambda n:n.has_class('slide-notes')))
        compare=self.slide('index.html','Compare Responses').text()
        self.assertNotIn('settings unchanged',compare)
    def test_08_exact_selector_instruction(self):
        for route,title in [('index.html','Select Models'),('index.html','Select STEM Games'),('knowledge/index.html','Review Model Settings'),('skills/index.html','Draft Skills')]:
            self.assertIn(SELECTOR,self.slide(route,title).text())
    def test_09_access_and_stable_links(self):
        root=self.decks['index.html'];self.assertEqual(root[3].attrs['data-title'],'Request Access');self.assertEqual(self.slide('index.html','Situating System Prompts').attrs['data-source-slide'],'7')
        links=root[3].all(lambda n:n.tag=='a');self.assertIn('https://ailab.gc.cuny.edu/request-access/',[n.attrs['href'] for n in links]);self.assertFalse(root[3].all(lambda n:n.tag=='img'))
        for route in ROUTES:
            agenda=self.slide(route,'Workshop Agenda');copy=agenda.text().lower()
            self.assertIn('individual access',copy);self.assertTrue('sign in' in copy or 'sign-in' in copy or 'sign into' in copy)
        self.assertNotIn('Workspace access',self.slide('index.html','Workshop Agenda').text())
        for term in ['Workspace','Knowledge']:self.assertIn(term,self.slide('knowledge/index.html','Workshop Agenda').text())
        self.assertIn('Skills and Tools access',self.slide('skills/index.html','Workshop Agenda').text())
    def test_10_agendas_and_next_steps_use_verbs(self):
        verbs={'Request','Define','Compare','Revise','Explore','Save','Confirm','Select','Create','Attach','Check','Choose','Play','Inspect','Configure','Prepare','Review','Continue','Verify','Retest'}
        for route in ROUTES:
            for s in [self.slide(route,'Workshop Agenda'),self.decks[route][-1]]:
                for li in s.all(lambda n:n.tag=='li'):
                    self.assertIn(li.text().split()[0],verbs);self.assertNotRegex(li.text(),r'(?i)\b(a|an|the)\b')
    def test_11_knowledge_prerequisites(self):
        self.assert_order('knowledge/index.html',['Knowledge Collections','Open Workspace','Review Model Settings','Select Documents','Open STEM Collection','Review Attached Knowledge','Check Game Sources','Check Citations','Build Knowledge Collections','Create Knowledge Collections','Attach Knowledge Collections','Test Retrieval'])
        attach=self.slide('knowledge/index.html','Attach Knowledge Collections').text()
        self.assertLess(attach.index('Add Content'),attach.index('Save & Update'))
        self.assertIn('processing',attach)
    def test_12_game_and_skill_orientation(self):
        self.assert_order('skills/index.html',['Tools & Skills','Review Previous Work','Connect Resources','Enable Tools','Inspect Game Rules','Test Game Commands','Discuss Play Records','Define Skills','Draft Skills','Create Skills','Attach Skills','Extend Procedures'])
        self.assertIn('Scenario JSON is a text file',self.slide('skills/index.html','Connect Resources').text())
        self.assertIn('Prism Laboratory is its starting game',self.slide('skills/index.html','Review Previous Work').text())
        self.assertIn('Send Begin Prism Laboratory',self.slide('skills/index.html','Inspect Game Rules').text())
        self.assertIn('Send Begin Prism Laboratory',self.slide('index.html','STEM Adventure Games').text())
    def test_13_save_load_and_handoff_sequence(self):
        copy=self.slide('skills/index.html','Test Game Commands').text()
        self.assertLess(copy.index('save'),copy.index('download'))
        self.assertLess(copy.index('download'),copy.index('load'))
        self.assertIn('choose your saved file',copy)
        self.assertIn('discuss',self.slide('skills/index.html','Discuss Play Records').text())
        self.assertIn('then send it',self.slide('skills/index.html','Discuss Play Records').text())
    def test_14_skill_comparisons_remove_attached_skill(self):
        copy=self.slide('skills/index.html','Test Skills').text()
        for term in ['private model copy','Remove your skill','Attach your skill again','new chat','unchanged']:self.assertIn(term,copy)
        extend=self.slide('skills/index.html','Extend Procedures')
        self.assertTrue(extend.all(lambda n:n.tag=='a' and n.attrs.get('href')=='../examples/adventure/prism.json'))
        self.assertIn('Integrations → Skills',extend.text())
    def test_15_reference_files_match(self):
        for id,file in [('stem-system-copy','examples/stem-system-prompt.txt'),('stem-skill-copy','examples/stem-game-skill.md')]:
            expected=re.sub(r'^---[\s\S]*?---\s*','',(ROOT/file).read_text()).strip()
            actual=self.example.all(lambda n:n.attrs.get('id')==id)[0].text().strip()
            self.assertEqual(actual,expected)
        for paragraph in self.by_id('stem-game-excerpt').text().split('\n\n'):
            self.assertIn(paragraph,(ROOT/'examples/stem-system-prompt.txt').read_text())
    def test_16_creators_remain_general_purpose(self):
        config=json.loads((ROOT/'examples/creators/builder-copy.json').read_text())
        for record in config.values():
            text=(ROOT/'examples/creators'/record['prompt_file']).read_text()
            self.assertTrue(general_builder(text))
            self.assertTrue(general_builder(json.dumps(record)))
            self.assertIn('Do not default to a particular subject',text)
        for title,name in [('Draft Skills','Kale Skill Builder'),('Create Adventure Tools','Tool Creator')]:
            self.assertIn(name+' is a custom model',self.slide('skills/index.html',title).text())
    def test_17_no_phantom_tool_or_missing_inputs(self):
        text=' '.join(s.text() for s in self.decks['skills/index.html'])
        self.assertNotIn('Check Source Imports',text)
        self.assertIn('separate draft tool',self.slide('skills/index.html','Check Generated Code').text())
        self.assertIn('Attach saved play records',self.slide('skills/index.html','Compare Game Records').text())
    def test_18_screenshots_and_controls_preserve_requested_evidence(self):
        for title,term in [('Compare Models','Compare'),('Open Chat Controls','System Prompt'),('Regenerate Responses','Regenerate')]:
            matches=[s for s in self.decks['index.html'] if s.attrs['data-title']==title and s.has_class('screenshot-slide')]
            im=matches[0].all(lambda n:n.tag=='img')[0]
            self.assertIn('arrow',im.attrs['alt']);self.assertIn(term,im.attrs['alt']);self.assertTrue(im.attrs['src'].endswith('.svg'))
        for route in ['index.html','knowledge/index.html']:
            workspace=self.slide(route,'Open Workspace')
            im=workspace.all(lambda n:n.tag=='img')[0]
            self.assertIn('left sidebar',im.attrs['alt'])
            self.assertIn('arrow',im.attrs['alt'])
            self.assertTrue(im.attrs['src'].endswith('workspace-sidebar-2026-09-15-annotated.svg'))
            self.assertNotIn('Workspace tab',workspace.text())
        for tree in self.trees.values():
            self.assertFalse(tree.all(lambda n:n.has_class('slide-notes')))
            for slide in tree.all(lambda n:n.has_class('slide')):
                self.assertFalse(slide.all(lambda n:'hidden' in n.attrs))
            for s in tree.all(lambda n:n.has_class('screenshot-slide')):
                self.assertTrue(s.all(lambda n:n.tag=='img'))
            self.assertFalse(tree.all(lambda n:n.attrs.get('id') in {'notes-button','series-button'}))
    def test_19_copy_controls_are_inside_prompt_containers(self):
        def visit(n,parent=None):
            if isinstance(n,str):return
            if 'data-copy' in n.attrs or 'data-example-copy' in n.attrs:
                self.assertTrue(parent and parent.has_class('prompt-container'))
                self.assertTrue(parent.all(lambda c:c.tag=='pre'))
            for child in n.children:visit(child,n)
        for tree in [*self.trees.values(),self.example]:visit(tree)
    def test_20_ninety_minute_plans(self):
        text=(ROOT/'WORKSHOP.md').read_text()
        plans=re.findall(r'### Lesson Plan\n(.*?)(?=\n\n[^|]|\Z)',text,re.S)
        self.assertEqual(len(plans),3)
        for plan in plans:
            slots=[tuple(map(int,m)) for m in re.findall(r'\| (\d+)–(\d+) \|',plan)]
            self.assertEqual(slots[0][0],0);self.assertEqual(slots[-1][1],90)
            self.assertTrue(all(a[1]==b[0] for a,b in zip(slots,slots[1:])))
    def test_21_regression_detectors_reject_mutations(self):
        self.assertFalse(general_builder('Default to STEM Adventure for every request.'))
        self.assertFalse(general_builder(json.dumps({'starter':'Create Prism Laboratory'})))
        self.assertTrue(general_builder('Create tools for the task the user describes.'))
        self.assertTrue(prose_colons('Expected: reject numeric commands.'))
        self.assertFalse(prose_colons('Read Newton: Light and Colour at https://example.org/'))
        mutations = [
            ('index.html', '<figcaption>', '<figcaption hidden>', self.test_18_screenshots_and_controls_preserve_requested_evidence),
            ('index.html', NURSE, NURSE.replace('she','he'), self.test_05_prompts_remain_exact),
            ('index.html', 'Try Again', 'Continue', self.test_07_controls_and_regeneration_are_explicit),
            ('index.html', 'Compare and configure models for teaching and research', REJECTED[0], self.test_04_explicit_deletions_stay_deleted),
            ('index.html', 'class="prompt-container"', 'class="outside-prompt"', self.test_19_copy_controls_are_inside_prompt_containers),
            ('skills/index.html', 'Remove your skill', 'Toggle this skill', self.test_14_skill_comparisons_remove_attached_skill),
        ]
        for route,before,after,test in mutations:
            with self.subTest(mutation=after):
                trees=dict(self.trees);trees[route]=Parser((ROOT/route).read_text().replace(before,after)).root
                decks={r:t.all(lambda n:n.has_class('slide')) for r,t in trees.items()}
                with patch.object(self,'trees',trees),patch.object(self,'decks',decks),self.assertRaises(AssertionError):test()
        decks={r:list(slides) for r,slides in self.decks.items()}
        root=decks['index.html'];definition=root.pop(4);root.insert(12,definition)
        with patch.object(self,'decks',decks),self.assertRaises(AssertionError):self.test_06_comparison_scaffolding()
        reference=Parser((ROOT/'examples.html').read_text().replace('Run STEM Adventure Games as','Run an unrelated model as')).root
        with patch.object(self,'example',reference),self.assertRaises(AssertionError):self.test_15_reference_files_match()

if __name__=='__main__':unittest.main(verbosity=2)
