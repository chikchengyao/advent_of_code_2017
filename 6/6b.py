input = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"
#input = "0 2 7 0"
input = input.split()
for i in range(len(input)):
	input[i] = int(input[i])

memo = {}

n = 0;
while (str(input) not in memo):
	memo[str(input)] = n

	# find max
	max_i = 0
	for i in range(1, len(input)):
		if input[i] > input[max_i]:
			max_i = i

	# Redistribute
	holder = input[max_i]
	input[max_i] = 0

	offset = 1
	while holder > 0:
		holder -= 1
		input[(max_i + offset) % len(input)] += 1
		offset += 1

	n += 1

	

print(n - memo[str(input)])