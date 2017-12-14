#!/usr/bin/env python

from knot_hash import knot_hash

#puzzle_input = "flqrgnkx"
puzzle_input = "hxtvlmkl"

tally = ""
for i in range(128):
    print(puzzle_input + "-" + str(i))
    tally += bin(int(knot_hash(puzzle_input + "-" + str(i)),16))

sum = 0
for char in tally:
    if char == "1":
        sum += 1

print(sum)
