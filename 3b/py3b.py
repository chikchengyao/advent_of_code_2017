# Brute force solution, but expect answer to be ~= O(sqrt(n)) so it's still kinda okay
import numpy as np

STOP_NUM = 289326

def rotateClockwise(m):
	# Returns another matrix
	return np.rot90(m, 3)

def newSide(m):
	# Adds new row to m, returns pair (n, m) where n = 0 if terminating condition not fulfilled, 
	# otherwise returns the result in n.
	h = len(m)
	w = len(m[0])
	newrow = np.array([0 for i in range(w)])
	m = np.vstack([m, newrow])
	for i in range(w):
		# Assign element the sum of above 3 elems, taking care of boundaries
		m[h][i] = (m[h-1][i-1] if i-1 >= 0 else 0) + m[h-1][i] + (m[h-1][i+1] if i+1 <= w-1 else 0) + (m[h][i-1] if i-1 >= 0 else 0)

		# check if requirement fulfilled
		if m[h][i] > STOP_NUM:
			return (m[h][i], m)

	return (0, m)

def loop(matrix):
	n, m = newSide(matrix)
	print(n,m)
	if n != 0:
		print("Solution =", n)
		return n
	else:
		m = rotateClockwise(m)
		return loop(m)

init = np.array([[1]])
print(loop(init))

