"""Scope the October 15 revision without changing earlier workshops' copy rules.

These headings implement the user's later requests for definitions, the exact
Adventure Kit heading, and a choice between creating or revising tools or skills.
See review/skills-review-validation.md for the changed requirements.
"""

SKILLS_TITLE_EXCEPTIONS = frozenset({
    'Choose Your Own Adventure',
    'What Is a Skill?',
    'What Is a Tool?',
    'Check Tool Binding',
    'Add the ‘Adventure Kit’ tool',
    'Add Tools or Skills',
})

SKILLS_CORE_SEQUENCE = (
    'Configuring skills and tools', 'Choose Your Own Adventure',
    'What Is a Skill?', 'Add Your Skill', 'Add Skill Instructions',
    'Test Your Skill', 'What Is a Tool?', 'Check Tool Binding',
    'Add the ‘Adventure Kit’ tool', 'Prepare Your Adventure',
    'Add Tool Instructions', 'Test Your Tool', 'Choose Your Task',
    'Work With Support', 'Situate Your Adventure',
    'Add Tools or Skills', 'Series Reflections',
)
