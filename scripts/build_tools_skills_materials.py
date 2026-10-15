#!/usr/bin/env python3
"""Build October 15 materials with the series' existing reading-page renderer."""
import sys

from build_reading_pages import build
from reading_pages import ROOT, SOURCES, DESTINATIONS, relative


MATERIALS = {
    'skills/REFERENCE.md': ('Workshop References', 'skills/reference.html'),
    'skills/FACILITATOR.md': ('Facilitator Notes', 'skills/facilitator.html'),
    'skills/EXERCISES.md': ('Participant Exercises', 'skills/exercises.html'),
    'examples/adventure-kit/prepare-source-adventure.md': (
        'Prepare Source Adventures', 'examples/adventure-kit/prepare-source-adventure.html'
    ),
    'examples/adventure-kit/conclude-adventure.md': (
        'Conclude Adventures', 'examples/adventure-kit/conclude-adventure.html'
    ),
    'examples/adventure-kit/scenario-contract.md': (
        'Adventure Kit Contract', 'examples/adventure-kit/scenario-contract.html'
    ),
    'examples/adventure-kit/scenario-template.json': (
        'Custom Scenario Template', 'examples/adventure-kit/scenario-template.html'
    ),
    'examples/adventure-kit/source.md': (
        'Current Tool Source', 'examples/adventure-kit/source.html'
    ),
}


def main():
    for source, (title, destination) in MATERIALS.items():
        SOURCES[source] = title
        DESTINATIONS[source] = destination
    errors = []
    for source, (_, destination) in MATERIALS.items():
        output = build(source)
        if destination.startswith('examples/adventure-kit/'):
            # The shared renderer predates this example directory
            old = relative('basics/index.html', destination)
            new = relative('skills/index.html', destination)
            output = output.replace(f'href="{old}"', f'href="{new}"')
        if source.endswith('scenario-template.json'):
            output = output.replace(
                '<main id="workshop-copy" class="reading-content">',
                '<main id="workshop-copy" class="reading-content">'
                '<p>This template contains placeholders for your saved adventure '
                'and source passages. It is not a completed participant scenario '
                'or evidence of play. Replace every placeholder and adapt '
                'generic choices before execution. '
                '<a href="scenario-contract.html">Read input contract</a></p>'
            )
        path = ROOT / destination
        if '--write' in sys.argv:
            path.write_text(output)
        elif not path.exists() or path.read_text() != output:
            errors.append(destination)
    if errors:
        print('Tools and Skills materials out of sync: ' + ', '.join(errors))
        return 1
    print(f'{len(MATERIALS)} Tools and Skills reading pages '
          + ('synchronized' if '--write' in sys.argv else 'checked'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
