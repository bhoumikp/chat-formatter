
# Chat Template Formatter

The format_to_chat utility function takes a text and converts a structured chat template using specific handlebars tags.


## Test Cases

```
  Test Case #1:
  Input:
  how are things going, tell me about Delhi

  Output:
  {{#user}}how are things going, tell me about Delhi{{/user}} {{#assistant}}{{gen 'write' }}{{/assistant}}
```

```
  Test Case #2:
  Input:
  Tweak this proverb to apply to model instructions instead. Where there is no guidance{{gen 'rewrite'}} {{gen 'write'}}

  Output:
  {{#user}}Tweak this proverb to apply to model instructions instead. Where there is no guidance{{/user}} {{#assistant}}{{gen 'rewrite'}}{{/assistant}} {{#assistant}}{{gen 'write'}}{{/assistant}}
```

