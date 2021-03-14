def my_first_interpreter(code):
    cell = 0
    output = ''
    for instruction in code:
        if instruction == '+':
            cell = (cell + 1 ) % 256
        elif instruction == '.':
            output = '{}{}'.format(output, chr(cell))
        else:
            pass
    return output

