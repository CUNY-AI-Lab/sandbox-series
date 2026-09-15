"""Run independent cases against corrected Tool Creator output."""
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location('validator', Path(__file__).with_name('record-validator.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
validate = module.Tools().validate_play_record

normal = {'commands': ['look', 'jump'], 'events': [{'command': 'look', 'valid': True}, {'command': 'jump', 'valid': False}]}
assert validate(json.dumps(normal)) == {'total_commands': 2, 'failed_commands': ['jump']}
invalid = [123, '{', 'x' * 50001]
for commands, events in [([42], [{'command': 42, 'valid': False}]), (['42'], [{'command': 42, 'valid': False}]), (['look'], []), (['look'] * 301, [{'command': 'look', 'valid': True}] * 301)]:
    invalid.append(json.dumps({'commands': commands, 'events': events}))
for value in invalid:
    assert 'error' in validate(value), value
print('Passed 8 independent creator-output checks.')
