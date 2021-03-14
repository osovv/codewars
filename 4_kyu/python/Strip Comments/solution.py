def solution(string,markers):
    lines = string.split('\n')
    for i in range(len(lines)):
        for marker in markers:
            if lines[i].find(marker) >= 0:
                lines[i] = lines[i][:lines[i].find(marker)].strip()
    return '\n'.join(lines)
