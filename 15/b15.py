#!/usr/bin/env python
def nextA(current):
    current = (current * 16807) % 2147483647
    if current % 4 == 0:
        return current
    else:
        return nextA(current)

def nextB(current):
    current = (current * 48271) % 2147483647
    if current % 8 == 0:
        return current
    else:
        return nextB(current)

def eq(a, b):
    p = 2**16
    return a % p == b % p

matches = 0
a = 277
b = 349

#Test
#a = 65
#b = 8921
#Returns 588 - correct

for i in range(5000000):
    a = nextA(a)
    b = nextB(b)
    if i % 10000 == 0:
        print(i)
    if eq(a,b):
        matches += 1

print(matches)
