# Esolang Interpreters #2 - Custom Smallfuck Interpreter

### Small task description
Form a string with human readable duration from seconds. \
Example: \
62 -> 1 minute and 2 seconds \
3662 -> 1 hour, 1 minute and 2 seconds

### Link to Kata:
[link](https://www.codewars.com/kata/52742f58faf5485cae000b9a)

### Comment
Gained experience with OrderedDict.

### Top voted soltuion:
```
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
```
