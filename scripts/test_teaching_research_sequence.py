"""Protect participant choice before cloning in Workshop 1."""
from pathlib import Path
import unittest
from check_workshop import Parser

ROOT = Path(__file__).resolve().parents[1]

class TeachingResearchSequence(unittest.TestCase):
    def test_options_precede_clone_and_configuration(self):
        slides = Parser((ROOT / 'index.html').read_text()).root.all(lambda n: n.has_class('slide'))
        titles = [s.attrs['data-title'] for s in slides]
        sequence = ['Open Workspace', 'Review Custom Models', 'Model Configuration', 'Choose Examples', 'Clone Model Cards']
        positions = [titles.index(title) for title in sequence]
        self.assertEqual(positions, list(range(positions[0], positions[0] + len(sequence))))
        options = slides[titles.index('Choose Examples')]
        links = {n.attrs.get('href') for n in options.all(lambda n: n.tag == 'a')}
        for model in ['stem-adventure-games', 'compare-wikipedia-revisions']:
            self.assertIn('https://chat.ailab.gc.cuny.edu/?model=' + model, links)
        for term in ['Teaching', 'Research']:
            self.assertIn(term, options.text())
        clone = slides[titles.index('Clone Model Cards')].text()
        for term in ['chosen model', 'Clone', 'System Prompt', 'Private', 'Save an initial response']:
            self.assertIn(term, clone)
        agenda = slides[titles.index('Workshop Agenda')].text()
        self.assertIn('Choose teaching or research examples', agenda)
        self.assertIn('Clone model cards and test revisions', agenda)

class ParticipantContinuity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decks = {route: Parser((ROOT / route).read_text()).root for route in ['index.html', 'knowledge/index.html', 'skills/index.html']}

    def slide(self, route, title):
        return self.decks[route].all(lambda n: n.has_class('slide') and n.attrs.get('data-title') == title)[0]

    def test_research_choice_survives_component_exercises(self):
        for title in ['Define Purpose', 'Write Procedures', 'Set Constraints', 'Specify Format']:
            self.assertIn('For research,', self.slide('index.html', title).text(), title)
        self.assertIn('Research', self.slide('index.html', 'Extend Instructions').text())
        self.assertIn('Test User Requests', self.slide('index.html', 'Review Common Problems').text())

    def test_knowledge_continues_chosen_private_model(self):
        review = self.slide('knowledge/index.html', 'Review Model Settings').text()
        for name in ['private copy', 'STEM Adventure Games', 'Compare Wikipedia Edits', 'Leave Skills and Tools unselected']:
            self.assertIn(name, review)
        attach = self.slide('knowledge/index.html', 'Attach Knowledge Collections').text()
        self.assertIn('chosen custom model', attach)
        self.assertNotIn('replace STEM Wikipedia Experiments', attach)
        refs = self.slide('knowledge/index.html', 'Choose Reference Materials')
        links = {n.attrs.get('href') for n in refs.all(lambda n: n.tag == 'a')}
        self.assertTrue({'../examples/research/sample-revisions.md', '../examples/research/system-prompt.txt'} <= links)

    def test_original_wikipedia_sources_remain_distinct(self):
        roles = self.slide('knowledge/index.html', 'Review Source Roles').text()
        for source in ['List of experiments', 'Scientific method', 'Women in science']:
            self.assertIn(source, roles)

    def test_save_precedes_prompt_retest(self):
        exercise = self.slide('index.html', 'Extend Instructions').text()
        self.assertLess(exercise.index('Save & Update'), exercise.index('new chat'))
        self.assertLess(exercise.index('save again'), exercise.index('repeat your request'))

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
