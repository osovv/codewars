# Find the unknown digit

### Small task description
Need to parse string and find suitable digit.

### Link to Kata:
[link](https://www.codewars.com/kata/546d15cebed2e10334000ed9)

### Comment
Refreshed my knowledge of regular expressions. Also could've written much cleaner code.

### Top voted soltuion:
```
import re

def solve_runes(runes):
    for d in sorted(set("0123456789") - set(runes)):
        toTest = runes.replace("?",d)
        if re.search(r'([^\d]|\b)0\d+', toTest): continue
        l,r = toTest.split("=")
        if eval(l) == eval(r): return int(d)
    return -1
```
