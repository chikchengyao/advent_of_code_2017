# parse input as list
f = open("input.txt")
tape = f.read().split()
for i in range(len(tape)):
	tape[i] = int(tape[i])

steps = 0
ptr = 0

while (ptr >= 0 and ptr < len(tape)):
	next_ptr = ptr + tape[ptr]
	tape[ptr] = tape[ptr] + 1 if tape[ptr] < 3 else tape[ptr] - 1
	steps = steps + 1
	ptr = next_ptr

print(steps)