def solve_runes(runes):
    import re
    import operator
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }
    digits_given = set()
    for char in runes:
        if char.isdigit():
            digits_given.add(int(char))
    splitted = re.split(r'^(.*[^-*+])([-*+])(.*)=(.*)$', runes)
    splitted.pop(0)
    splitted.pop(4)
    first, op, second, right = splitted
    s = 0
    if (len(first) >= 2 and first[0] == '?') or \
        (len(second) >= 2 and second[0] == '?') or \
        (len(right) >= 2 and right[0] == '?'):
        s = 1
    if (len(first) >= 2 and first.startswith('-?')) or \
        (len(second) >= 2 and second.startswith('-?')) or \
        (len(right) >= 2 and right.startswith('-?')):
        s = 1

    for i in range(s, 10):
        if i not in digits_given:
            if ops[op](int(first.replace('?',str(i))),int(second.replace('?',str(i)))) == int(right.replace('?', str(i))):
                return i
    return -1
