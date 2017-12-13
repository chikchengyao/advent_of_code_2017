#Brute force

from inp import inp

inp = [list(map(int, i.split(": "))) for i in inp.split("\n")]

walls = [-1] * (inp[-1][0]+1)

for i in inp:
    walls[i[0]] = i[1]

def check_caught(delay): # SEVERITY == 0 DOES NOT FULFIL THE CONDITIONS!!! MUST **NOT BE CAUGHT** AT **ALL**
    for i in range(len(walls)):
        if walls[i] == -1:
            continue
        if (i+delay) % ((walls[i]-1)*2) == 0:
            return True
    return False

d = 0 
while check_caught(d):
    #print(d,"failed")
    d += 1
print(d) # 3970918  # i hope your computer is fast

