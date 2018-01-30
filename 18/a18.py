#!/usr/bin/env python
from puzzle import puzzle

instructions = puzzle.split("\n")
instructions = [line.split(" ") for line in instructions]

register = {}

ptr = 0
last_sound = -1;

def val(x):
    try:
        x = int(x)
    except:
        pass
    if type(x) is str:
        if x in register:
            return register[x]
        else:
            register[x] = 0
            return 0
    else :
        return x

while ptr >= 0 and ptr < len(instructions):
    instr = instructions[ptr]
    oper = instr[0]
    if oper == "snd":
        last_sound = val(instr[1])
    elif oper == "set":
        register[instr[1]] = val(instr[2])
    elif oper == "add":
        if instr[1] not in register:
            register[instr[1]] = 0
        register[instr[1]] += val(instr[2])
    elif oper == "mul":
        if instr[1] not in register:
            register[instr[1]] = 0
        register[instr[1]] *= val(instr[2])
    elif oper == "mod":
        if instr[1] not in register:
            register[instr[1]] = 0
        register[instr[1]] = register[instr[1]] % val(instr[2])
    elif oper == "rcv":
        if val(instr[1]) != 0:
            break
    elif oper == "jgz":
        if val(instr[1]) > 0:
            ptr += val(instr[2])
            continue
    else:
        print("Unknown operation")
    
    print(register)

    ptr+=1

print(last_sound)
