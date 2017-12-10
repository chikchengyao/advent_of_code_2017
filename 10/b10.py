from input import input

# The sequence of lengths
input = list(map(ord, list(input))) + [17, 31, 73, 47, 23]

skip = 0
current = 0

# The sequence of 256 numbers
xs = [i for i in range(256)]

#Recursively reverses numbers between start and end
def reverse(start, end):
    if start >= end:
        return
    xs[start%256] , xs[end%256] = xs[end%256] , xs[start%256]
    reverse(start+1, end-1)

# Applies 64 times
for i in range(64):
    for l in input:
        reverse(current, current+l-1)
        current = (current + l + skip) % 256
        skip += 1

# Computes hash
hsh = []
for i in range(16):
    ch = xs[16*i]
    for j in range(1,16):
        ch = ch ^ xs[16*i + j]
    hsh.append(ch)

# Print as 2-DIGIT hex number
print("".join("%02x"%i for i in hsh))


