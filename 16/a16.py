#!/usr/bin/env python
from ii import ii

progs = []
for i in range(16):
    progs.append(chr(97 + i))

ii = ii.split(",")

start = 0 #Tracks start point for O(1) implementation of spin

def printer():
    for i in range(16):
        print(progs[(start + i)%16], end="")


for ins in ii:
    print("Received instruction", ins)
    if ins[0] == "s":
        start = (start - int(ins[1:])) % 16
    elif ins[0] == "x":
        ins = list(map(int, ins[1:].split("/")))
        progs[(start+ins[0])%16], progs[(start+ins[1])%16] = progs[(start+ins[1])%16], progs[(start+ins[0])%16]
    elif ins[0] == "p":
        ins = ins[1:].split("/")
        for i in range(len(progs)):
            if progs[i] == ins[0]:
                progs[i] = ins[1]
            elif progs[i] == ins[1]:
                progs[i] = ins[0]
    print("Result: ", end="")
    printer()
    print()

#print results
printer()
