from inp import inp

# inp[node_number] returns a list of other nodes that that node is connected to
inp = [list(map(int,ln.split(", "))) for ln in ([line.split(" <-> ")[1] for line in inp.split("\n")])]

#dfs for connection to 0
visited = [0] * len(inp)

def recurse(i):
    if not visited[i]:
        visited[i] = 1
        for j in inp[i]:
            recurse(j)

# Count number of distinct groups
count = 0
for i in range(len(inp)):
    if visited[i] == 0:
        recurse(i)
        count += 1


print(count)
