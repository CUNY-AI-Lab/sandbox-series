"""October 15 workflow: attach orchestration skill and tool in one model card, then test."""
SKILLS_TITLE_EXCEPTIONS = frozenset({
    'Choose Your Own Adventure', 'What Is a Skill?', 'What Is a Tool?',
    'Check Tool Binding', 'Add the ‘Adventure Kit’ tool', 'Add Tools or Skills',
})
SKILLS_CORE_SEQUENCE = ('Configuring skills and tools', 'Choose Your Own Adventure', 'What Is a Skill?', 'Add Your Skill', 'What Is a Tool?', 'Check Tool Binding', 'Add the ‘Adventure Kit’ tool', 'Add Skill Instructions', 'Test Your Adventure', 'Explore Other Skills', 'Choose Your Task', 'Work With Support', 'Adapt Your Adventure', 'Add Tools or Skills', 'Series Reflections')
