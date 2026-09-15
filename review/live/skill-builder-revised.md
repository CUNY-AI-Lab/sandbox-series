**Skill Name**: STEM Adventure Designer

**Skill ID**: stem-adventure-designer

**Skill Description**: Use this skill when you need to design a variation of an experimental procedure or interpret a provided play record for a STEM Adventure scenario.

**Skill Instructions**:
Task: Design an experimental variation or interpret a provided play record.
1. Identify if the user is requesting an experimental variation or an interpretation of a play record.
2. If designing a variation, propose a single change to one experimental variable or procedure step based on the provided scenario context.
3. If interpreting a record, analyze the provided play log for completion status, inventory changes, and prerequisite fulfillment.
4. Provide the design or interpretation as a text-based response without simulating tool execution or clicks.
Expected Output: A concise design proposal or a structured analysis of the provided record.

**Ordinary Test**
Input: "Interpret this play record: { 'room': 'Prism Laboratory', 'action': 'open aperture', 'result': 'success' }"
Expected Behavior: A text-based analysis confirming the aperture was opened successfully in the Prism Laboratory.

**Boundary Test**
Input: "How do I make a peanut butter sandwich?"
Expected Behavior: A general response providing sandwich instructions, as the request does not trigger STEM Adventure design or interpretation logic.
