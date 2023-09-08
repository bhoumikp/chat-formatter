import pyparsing as pp

def format_to_chat(input_text):
    gen_command = pp.Literal('{{gen') + pp.SkipTo('}}') + pp.Literal('}}')
    gen_commands_found = gen_command.searchString(input_text)

    user_text = input_text
    assistant_text = ""

    for gen_command in gen_commands_found:
        command = ''.join(gen_command).replace('n', 'n ')

        user_text = user_text.replace(command, "")

        formatted_command = " {{#assistant}}" + command + "{{/assistant}}"
        assistant_text += formatted_command

    if not gen_commands_found:
        assistant_text = "{{#assistant}}{{gen 'write' }}{{/assistant}}"

    user_text = ' '.join(user_text.split())

    formatted_output = "{{#user}}" + user_text + "{{/user}}" + assistant_text
    return formatted_output

