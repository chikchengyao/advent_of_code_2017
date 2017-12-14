#!/usr/bin/env python

from knot_hash import knot_hash

puzzle_input = "hxtvlmkl"
#puzzle_input = "flqrgnkx"

# Construct table

table = [list("{:0128b}".format(int(knot_hash(puzzle_input + "-" + str(i)),16))) for i in range(128)]

def floodfill(fill, x, y):
    if table[x][y] == "1":
        table[x][y] = fill
        if x >= 1:
            floodfill(fill, x-1, y)
        if y < 127:
            floodfill(fill, x, y+1)
        if y >= 1:
            floodfill(fill, x, y-1)
        if x < 127 :
            floodfill(fill, x+1, y)

filler = 1 # Starts off at 1 to avoid conflict with existing "1"s, remember to subtract 1 later before return answer
for x in range(len(table)):
    for y in range(len(table[x])):
        if table[x][y] == "1":
            filler += 1
            floodfill(filler, x, y)

print(filler - 1)

