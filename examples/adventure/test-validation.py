"""Validate source scenarios and reject malformed or unsafe inputs."""
from copy import deepcopy
from pathlib import Path
import json
import unittest
from validation import validate_scenario

ROOT = Path(__file__).parent

class ScenarioValidation(unittest.TestCase):
    def setUp(self):
        self.scenario = json.loads((ROOT / 'prism.json').read_text())

    def test_published_scenarios(self):
        for name in ('prism.json', 'aperture.json'):
            validate_scenario(json.loads((ROOT / name).read_text()))

    def test_invalid_references(self):
        for field, value in [('room', 'missing'), ('requires_items', ['missing']), ('requires_flags', ['missing'])]:
            candidate = deepcopy(self.scenario)
            candidate['actions'][0][field] = value
            with self.assertRaises(ValueError):
                validate_scenario(candidate)

    def test_duplicate_commands(self):
        self.scenario['actions'][1]['command'] = self.scenario['actions'][0]['command']
        with self.assertRaises(ValueError):
            validate_scenario(self.scenario)

    def test_unreachable_room(self):
        self.scenario['rooms']['isolated'] = {'name': 'Isolated', 'description': 'No route enters.', 'items': [], 'exits': {}}
        with self.assertRaises(ValueError):
            validate_scenario(self.scenario)

    def test_blank_text_and_missing_goal(self):
        for field, value in [('title', ''), ('goal_flags', []), ('actions', None), ('rooms', [])]:
            candidate = deepcopy(self.scenario)
            candidate[field] = value
            with self.assertRaises(ValueError):
                validate_scenario(candidate)

    def test_reserved_command(self):
        self.scenario['actions'][0]['command'] = 'go north'
        with self.assertRaises(ValueError):
            validate_scenario(self.scenario)

if __name__ == '__main__':
    unittest.main()
