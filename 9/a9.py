f = open("input.txt")

input = f.read()

score = 0
depth = 0
is_garbage = False
ignore_next = False

for char in input:
    print(char)
    if ignore_next:
        ignore_next = False
    elif char == "!":
        ignore_next = True
    elif is_garbage:
        if char == ">":
            is_garbage = False
    elif char == "<":
        is_garbage = True
    elif char == "{":
        depth += 1
        score += depth
    elif char == "}":
        depth -= 1
    elif char == ",":
        continue
    else:
        print("Unexpected error")

print(score, depth, is_garbage, ignore_next)
