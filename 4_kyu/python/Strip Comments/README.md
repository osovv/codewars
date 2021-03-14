# Strip Comments

### Small task description
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

### Link to Kata:
[link](https://www.codewars.com/kata/51c8e37cee245da6b40000bd)

### Comment
A simple task. There's nothing more to say.

### Top voted soltuion:
```
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
```
