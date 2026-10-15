"""October 15 workflow: attach orchestration skill and tool in one model card, then test."""
SKILLS_TITLE_EXCEPTIONS = frozenset({
    'Choose Your Own Adventure', 'What Is a Skill?', 'What Is a Tool?',
    'Add the ‘Adventure Kit’ tool', 'Add Tools or Skills',
    'Update Model for Tool Calling',
    'Add Skill Instructions to the Bottom of Your System Prompt',
})
SKILLS_CORE_SEQUENCE = ('Configuring skills and tools', 'Choose Your Own Adventure', 'What Is a Skill?', 'Add Your Skill', 'What Is a Tool?', 'Update Model for Tool Calling', 'Enable Filter', 'Add the ‘Adventure Kit’ tool', 'Model Card Check-In', 'Add Skill Instructions to the Bottom of Your System Prompt', 'Test Your Adventure', 'Explore Other Skills', 'Choose Your Task', 'Work With Support', 'Adapt Your Adventure', 'Add Tools or Skills', 'Series Reflections')
