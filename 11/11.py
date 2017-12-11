from inp import inp

inp = inp.split(",")

x = 0
y = 0

maxdist = 0

for step in inp:
    if step == "n":
        y += 1
    elif step == "s":
        y -= 1
    elif step == "se":
        x += 1
    elif step == "nw":
        x -= 1
    elif step == "ne":
        x += 1
        y += 1
    elif step == "sw":
        x -= 1
        y -= 1
    else:
        print("ERRORRRR")
    maxdist = max(x,y) if max(x,y) > maxdist else maxdist

# Current distance
print(max(x,y))

# Max distance
print(maxdist)
