# Definitions and Winograd context

Changed root slides 5 and 10, slide 5’s copy-preservation record, and the matching lesson-plan definition. The nurse question on slide 9 remains verbatim. Response slides 12 and 13 remain untouched by this edit.

## Sources and decisions

- [Original workshop wording](../before.md) describes a system prompt as “setup instructions.” The revision retains that explanation while removing earlier claims that instructions are hidden or fixed before a conversation.
- [Sandbox Basic Concepts](https://ailab.gc.cuny.edu/sandbox-docs/basic-concepts/) defines a custom model as a configuration that uses a chosen base model, instructions, and documents. [Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/) describes choosing a base model and attaching instructions and sources. Slide 5 now states that relationship positively.
- [Sandbox System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/) defines instructions in terms of model behavior. Slide 5 uses the prior workshop’s concrete wording to introduce that relationship.
- [Levesque, Davis, and Morgenstern (2012), section 4](https://www.cs.nyu.edu/faculty/davise/papers/WSKR2012.pdf) describes paired sentences where a small wording change reverses pronoun interpretation. The challenge was designed to test context and common-sense reasoning. Slide 10 introduces that method and retains uncertainty about the workshop’s single nurse question. It does not identify that question as a validated benchmark item.

Applied humanizer, no-ai-slop, and milwrite-style in order. Short definitions and questions serve projected slides. Headers contain two or three words without definite articles. No new exercise was added.

The isolated [direct diff](copy.diff) contains these two slides and the matching lesson-plan paragraph.

## Slide 5

### Before

### System Prompts



A system prompt gives a model instructions for its role, behavior, and focus.



### User Prompts



Questions or tasks you enter in chat.



### Base Models



A base model generates responses. A custom model adds instructions and resources without training a new base model.



[System Prompts](https://ailab.gc.cuny.edu/sandbox-docs/system-prompts/) · [Open WebUI model configuration](https://docs.openwebui.com/features/workspace/models/)

### After

### System Prompts



System prompts are setup instructions that describe how a model should behave.



### User Prompts



Questions or tasks you enter in chat.



### Custom Models



You create a custom model by choosing a base model, such as Gemma, and adding instructions and documents for it to use.



[Basic Concepts](https://ailab.gc.cuny.edu/sandbox-docs/basic-concepts/) · [Custom Models](https://ailab.gc.cuny.edu/sandbox-docs/models/)

## Slide 10

### Before

### Examine Assumptions



“She” could refer to either person. This sentence does not establish who was late.



- Does each model acknowledge ambiguity?

- What assumption supports its answer?

- Does either explanation add information absent from this sentence?

### After

### Winograd Schema Challenge



This challenge tests how models interpret ambiguous pronouns using context and common-sense knowledge. Changing one or two words between paired sentences changes who a pronoun refers to.



In our question, either person could be late.



- Which person does each model choose?

- What assumption supports its answer?



[Levesque, Davis, and Morgenstern (2012)](https://www.cs.nyu.edu/faculty/davise/papers/WSKR2012.pdf)

## Lesson-plan definition

### Before

Participants learn how user prompts and system prompts differ before comparing models. A system prompt gives a model instructions for its role, behavior, and focus. Begin comparisons with two small models interpreting a sentence about a nurse and doctor, then ask whether to walk or drive to a car wash. Participants save both responses, read sample system prompt instructions, locate System Prompt in Chat Controls, and regenerate responses to their original prompt after adding those instructions.

### After

Participants learn how user prompts and system prompts differ before comparing models. System prompts are setup instructions that describe how a model should behave. Begin comparisons with two small models interpreting a sentence about a nurse and doctor, then ask whether to walk or drive to a car wash. Participants save both responses, read sample system prompt instructions, locate System Prompt in Chat Controls, and regenerate responses to their original prompt after adding those instructions.
