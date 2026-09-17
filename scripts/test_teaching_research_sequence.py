"""Protect exercise order and participant continuity across all workshops."""
from pathlib import Path
import unittest
from check_workshop import Parser

ROOT = Path(__file__).resolve().parents[1]

class TeachingResearchSequence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.slides = Parser((ROOT / 'index.html').read_text()).root.all(lambda n: n.has_class('slide'))
        cls.titles = [slide.attrs['data-title'] for slide in cls.slides]

    def slide(self, title):
        matches = [slide for slide in self.slides if slide.attrs.get('data-title') == title]
        self.assertEqual(len(matches), 1, title)
        return matches[0]

    def stages(self, title='Compare Custom Models'):
        stages = self.slide(title).all(lambda node: 'data-fragment-step' in node.attrs)
        self.assertEqual([node.attrs['data-fragment-step'] for node in stages], ['0', '1'], title)
        return stages

    def test_introductions_preserve_exercise_order(self):
        self.assertEqual(len(self.slides), 24, 'Add Introductions after Workshop Agenda')
        self.assertEqual(self.titles[2:5], ['Workshop Agenda', 'Introductions', 'Sign In'])
        self.assertEqual(self.titles[17:], [
            'Compare Custom Models', 'Clone Models', 'Compare Configurations',
            'Record Comparisons', 'Draft System Prompts', 'Create Models', 'Workshop Resources',
        ])
        labels = ['Try Examples', 'Review Settings']
        for stage, label in zip(self.stages(), labels):
            self.assertIn(label, stage.text())
        agenda = self.slide('Workshop Agenda').text()
        for item in ['Choose teaching or research examples', 'Review system prompts and base models',
                     'Clone models and compare responses', 'Draft instructions and create models']:
            self.assertIn(item, agenda)

    def test_both_examples_and_sources_open_without_leaving_exercise(self):
        stage = self.stages()[0]
        links = {node.attrs.get('href'): node for node in stage.all(lambda node: node.tag == 'a')}
        expected = [
            'https://chat.ailab.gc.cuny.edu/?model=stem-adventure-games',
            'https://chat.ailab.gc.cuny.edu/?model=compare-wikipedia-revisions',
            'examples/research/sample-revisions.html',
        ]
        for href in expected:
            self.assertIn(href, links)
            self.assertEqual(links[href].attrs.get('target'), '_blank', href)
            self.assertIn('noopener', links[href].attrs.get('rel', '').split(), href)
        for term in ['Teaching', 'Research']:
            self.assertIn(term, stage.text())

    def test_review_includes_complete_settings_for_either_example(self):
        stage = self.stages()[1]
        links = {node.attrs.get('href'): node for node in stage.all(lambda node: node.tag == 'a')}
        for anchor in ['stem-chat', 'wikipedia-revisions']:
            href = 'examples.html#' + anchor
            self.assertIn(href, links)
            self.assertEqual(links[href].attrs.get('target'), '_blank', href)
            self.assertIn('noopener', links[href].attrs.get('rel', '').split(), href)
        for term in ['System Prompt', 'Base Model', 'Purpose', 'Procedure', 'Constraints', 'Format']:
            self.assertIn(term, stage.text())

    def test_clone_is_saved_before_testing(self):
        illustration, instructions = self.stages('Clone Models')
        clone = ' '.join(self.slide('Clone Models').text().split())
        for term in ['Workspace', 'Models', 'Clone']:
            self.assertIn(term, illustration.text())
        self.assertRegex(illustration.text().lower(), r'left sidebar')
        self.assertTrue(illustration.all(lambda node: node.tag == 'img'))
        self.assertFalse(instructions.all(lambda node: node.tag == 'img'))
        self.assertRegex(clone.lower(), r'(rename|name your copy)')
        self.assertNotIn('and give it a unique ID', clone)
        self.assertRegex(clone.lower(), r'(revise|change) one instruction')
        self.assertRegex(clone.lower(), r'base model.{0,80}(unchanged|same)')
        self.assertRegex(clone.lower(), r'settings.{0,35}(unchanged|same)')
        self.assertIn('Scroll to bottom and select', clone)
        self.assertLess(clone.index('Save & Create'), clone.lower().index('new chat'))
        self.assertNotIn('remove copied access grants', clone)

    def test_comparison_reuses_request_with_original_and_copy(self):
        illustration, instructions = self.stages('Compare Configurations')
        self.assertTrue(illustration.all(lambda node: node.tag == 'img'))
        self.assertFalse(instructions.all(lambda node: node.tag == 'img'))
        comparison = ' '.join(self.slide('Compare Configurations').text().split()).lower()
        self.assertRegex(comparison, r'(new|fresh) chat')
        self.assertIn('original', comparison)
        self.assertRegex(comparison, r'(copy|clone)')
        self.assertRegex(comparison, r'(same|saved|original) (request|prompt)')
        self.assertRegex(comparison, r'(source|research) passages')
        self.assertRegex(comparison, r'save.{0,45}(both|responses)')
        self.assertLess(comparison.index('original'), comparison.index('?'))
        self.assertLess(comparison.index('request'), comparison.index('?'))

    def test_drafting_precedes_creation_and_uses_four_components(self):
        draft = self.slide('Draft System Prompts')
        prompts = draft.all(lambda node: node.has_class('prompt-block'))
        self.assertEqual(len(prompts), 1)
        self.assertEqual(prompts[0].text().strip(), (ROOT / 'examples/system-prompt-framework.txt').read_text().strip())
        labels = [line for line in prompts[0].text().splitlines() if line and not line.endswith('?')]
        self.assertEqual(labels, ['Purpose', 'Procedure', 'Constraints', 'Format'])
        self.assertNotRegex(prompts[0].text(), r'(?i)\b(tone|context)\b')
        illustration, instructions = self.stages('Create Models')
        self.assertTrue(illustration.all(lambda node: node.tag == 'img'))
        for term in ['Workspace', 'Models', 'Create']:
            self.assertIn(term, illustration.text())
        create = ' '.join(instructions.text().split())
        self.assertNotIn('and give it a unique ID', create)
        for term in ['Base Model', 'System Prompt', 'Save & Create', 'new chat']:
            self.assertIn(term, create)
        self.assertLess(create.index('Base Model'), create.index('Save & Create'))
        self.assertLess(create.index('System Prompt'), create.index('Save & Create'))
        self.assertLess(create.index('Save & Create'), create.index('new chat'))
        self.assertLess(self.titles.index('Draft System Prompts'), self.titles.index('Create Models'))

    def test_component_tutorials_and_setup_extras_stay_removed(self):
        # Draft System Prompts is intentionally restored as one four-component slide.
        removed = {
            'Add Prompt Suggestions', 'Situating System Prompts',
            'Refine Instructions', 'Define Prompt Components', 'Define Purpose',
            'Write Procedures', 'Set Constraints', 'Specify Format', 'Extend Instructions',
            'Read Game Instructions', 'Adapt Research Prompts', 'Review Common Problems',
            'Choose Model Cards', 'Clone Model Cards', 'Model Configuration', 'Prepare Source Documents',
        }
        self.assertFalse(removed.intersection(self.titles))

class ParticipantContinuity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decks = {route: Parser((ROOT / route).read_text()).root for route in ['index.html', 'knowledge/index.html', 'skills/index.html']}

    def slide(self, route, title):
        return self.decks[route].all(lambda n: n.has_class('slide') and n.attrs.get('data-title') == title)[0]

    def test_knowledge_continues_chosen_private_model(self):
        review = self.slide('knowledge/index.html', 'Review Model Settings').text()
        for name in ['private copy', 'STEM Adventure Games', 'Compare Wikipedia Edits', 'Leave Skills and Tools unselected']:
            self.assertIn(name, review)
        attach = self.slide('knowledge/index.html', 'Attach Knowledge Collections').text()
        self.assertIn('chosen custom model', attach)
        self.assertNotIn('replace STEM Wikipedia Experiments', attach)
        refs = self.slide('knowledge/index.html', 'Choose Reference Materials')
        links = {n.attrs.get('href') for n in refs.all(lambda n: n.tag == 'a')}
        self.assertTrue({'../examples/research/sample-revisions.html', '../examples/research/system-prompt.html'} <= links)

    def test_original_wikipedia_sources_remain_distinct(self):
        roles = self.slide('knowledge/index.html', 'Review Source Roles').text()
        for source in ['List of experiments', 'Scientific method', 'Women in science']:
            self.assertIn(source, roles)

    def test_installed_tool_is_attached_before_testing(self):
        installation = self.slide('skills/index.html', 'Install Tool Code').text()
        self.assertLess(installation.index('unique Name and ID'), installation.index('Save & Create'))
        self.assertIn('private model', installation)
        self.assertIn('installed copy', installation)
        self.assertIn('Update System Prompt to name it', installation)
        self.assertIn('Save & Update', installation)
        self.assertIn('CAIL Tool Creator', self.slide('skills/index.html', 'Create Adventure Tools').text())

    def test_lesson_agenda_matches_participant_slides(self):
        import re
        plan = (ROOT / 'WORKSHOP.md').read_text().split('## Composing system prompts')[1].split('## Curating knowledge collections')[0]
        agenda = plan.split('### Workshop Agenda')[1].split('### Lesson Plan')[0]
        plan_items = re.findall(r'^- (.+)$', agenda, re.M)
        slide_items = [li.text() for li in self.slide('index.html', 'Workshop Agenda').all(lambda n: n.tag == 'li')]
        self.assertEqual(plan_items, slide_items)

if __name__ == '__main__':
    unittest.main()
