from inp import inp

inp = [list(map(int, i.split(": "))) for i in inp.split("\n")]

walls = [-1] * (inp[-1][0]+1)

for i in inp:
    walls[i[0]] = i[1]

severity = 0
#step through
for i in range(len(walls)):
    if walls[i] == -1:
        continue
    if i % ((walls[i]-1)*2) == 0:
        severity += i * walls[i]

print(severity)

