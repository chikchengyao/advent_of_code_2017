from inp import inp

inp = inp.split(",")

x = 0
y = 0

maxdist = 0

def get_dist(x,y):
    if x*y >= 0:
        x, y = abs(x), abs(y)
        return max(x,y)
    else:
        x, y = abs(x), abs(y)
        return x + y

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
    if get_dist(x,y) > maxdist:
        maxdist = get_dist(x,y)

# Current distance
print(get_dist(x,y))

# Max distance
print(maxdist)
