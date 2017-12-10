from input import input

# Get length sequence
input = list(map(int, input.split(",")))
skip = 0
current = 0

# Sequence of 256 numbers
xs = [i for i in range(256)]

# Recursively reverses between start and end
def reverse(start, end):
    if start >= end:
        return
    xs[start%256] , xs[end%256] = xs[end%256] , xs[start%256]
    reverse(start+1, end-1)

# Applies transformation
for l in input:
    reverse(current, current + l - 1)
    current = (current + l + skip) % 256
    skip += 1

print(xs[0] * xs[1])

