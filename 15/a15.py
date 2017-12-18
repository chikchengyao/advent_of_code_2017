#!/usr/bin/env python
def nextA(current):
    return (current * 16807) % 2147483647

def nextB(current):
    return (current * 48271) % 2147483647

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

for i in range(40000000):
    a = nextA(a)
    b = nextB(b)
    if i % 10000 == 0:
        print(i)
    if eq(a,b):
        matches += 1

print(matches)
