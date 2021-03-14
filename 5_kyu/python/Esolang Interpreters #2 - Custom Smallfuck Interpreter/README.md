# Esolang Interpreters #2 - Custom Smallfuck Interpreter

### Small description
Implement a custom interpreter for [Smallfuck](https://esolangs.org/wiki/Smallfuck) programming language.

### Link to Kata:
[link](https://www.codewars.com/kata/58678d29dbca9a68d80000d7)

### Comment
It was interesting to design bracket matching algorithm.

### Top voted soltuion:
```
def interpreter(code, tape):
    tape = list(map(int, tape))
    ptr = step = loop = 0
    
    while 0 <= ptr < len(tape) and step < len(code):
        command = code[step]
        
        if loop:
            if   command == "[": loop += 1
            elif command == "]": loop -= 1
        
        elif command == ">": ptr += 1
        elif command == "<": ptr -= 1
        elif command == "*": tape[ptr] ^= 1        
        elif command == "[" and tape[ptr] == 0: loop += 1
        elif command == "]" and tape[ptr] == 1: loop -= 1
    
        step += 1 if not loop else loop // abs(loop)
    
    return "".join(map(str, tape))
```
