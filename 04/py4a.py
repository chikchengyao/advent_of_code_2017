def isValid(xs):
	xs.sort()
	for i in range(len(xs) - 1):
		if xs[i] == xs[i+1]:
			return False
	return True

# Check for duplicates
n = 0
f = open("input.txt")
for line in f:
	if isValid(line.split()):
		n+=1

print(n)