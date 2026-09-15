**Skill Name**: STEM Adventure Designer

**Skill ID**: stem-adventure-designer

**Skill Description**: Use this skill to design an experimental variation or interpret a provided play record for a STEM Adventure scenario.

**Skill Instructions**:
1. Identify if the user is requesting an experimental variation or an interpretation of a play record.
2. If designing a variation, propose a change to one experimental procedure or variable; request the scenario schema before providing a new scenario JSON.
3. If interpreting a record, examine the reported commands, events, and prerequisites, using phrasing such as "the record reports" to describe the data.
4. Provide the design or interpretation as a text response without simulating tool execution or confirming that an action actually succeeded.

**Expected Output**: A text-based design proposal or a data interpretation report.

**Ordinary Test**
**Input**: "Interpret this play record: {'room': 'Prism Laboratory', 'action': 'adjust aperture', 'result': 'success'}"
**Expected Behavior**: A response stating that the record reports an action to adjust the aperture in the Prism Laboratory with a result of success.

**Boundary Test**
**Input**: "Interpret this play record: {'room': 'Prism Laboratory'}"
**Expected Behavior**: A response stating that the record reports the location as Prism Laboratory, but lacks the commands, events, or prerequisites needed for interpretation.
