def interpreter(code, tape):
    tape = list(tape)
    pointer_index = 0
    command_index = 0
    matching_bracket = matching_brackets(code)
    while command_index < len(code):
        command = code[command_index]
        if command == '>':
            pointer_index += 1
        elif command == '<':
            pointer_index -= 1
        elif command == '*':
            tape[pointer_index] = '1' if tape[pointer_index] == '0' else '0'
        elif command == '[':
            if tape[pointer_index] == '0':
                command_index = matching_bracket[command_index]
        elif command == ']':
            if tape[pointer_index] == '1':
                command_index = matching_bracket[command_index]
        if pointer_index >= len(tape) or pointer_index < 0:
            return ''.join(tape)
        command_index += 1
    return ''.join(tape)

def matching_brackets(code):
    bracket_positions = []
    result = dict()
    for i, item in enumerate(code):
        if item == '[':
            bracket_positions.append(i)
        elif item ==']':
            if len(bracket_positions) > 0:
                opening_position = bracket_positions.pop()
                result[opening_position] = i
                result[i] = opening_position
    return result
