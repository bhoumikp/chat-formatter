
# Chat Template Formatter

The format_to_chat utility function takes a text and converts it into a structured chat template using specific handlebars tags. 
It identifies {{gen ..}} commands and wrap each of them in seperate {{#assistant}...{{/assistant}} tag, Then it wraps the remainig text in the {{#user}}...{{/user}} tag.


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

```
  Test Case #3:
  Input: 
  Today we going to a trip{{gen write}}
  
  Output:
  {{#user}}Today we going to a trip{{/user}} {{#assistant}}{{gen write}}{{/assistant}}
```

```
  Testcase #4:
  Input: 
  You should go to walk. It is healthy{{gen recommend}}
  
  Output:
  {{#user}}You should go to walk. It is healthy{{/user}} {{#assistant}}{{gen recommend}}{{/assistant}}
```


