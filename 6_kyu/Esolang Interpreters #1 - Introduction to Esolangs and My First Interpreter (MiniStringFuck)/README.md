# Esolang Interpreters #1 - Introduction to Esolangs and My First Interpreter (MiniStringFuck)

## Small description
Implement a custom interpreter for [MiniStringFuck](https://esolangs.org/wiki/MiniStringFuck) programming language.

## Link to Kata:
[link](https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0)

### Comment
Pretty easy task.

### Top voted soltuion:
```
def my_first_interpreter(code):
    memory, output = 0, ""
    
    for command in code:
        if   command == "+":  memory += 1
        elif command == ".":  output += chr(memory % 256)
    
    return output
```
