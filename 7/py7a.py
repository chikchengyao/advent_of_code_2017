from input import input

f = input.split("\n")

# Construct tree represented by a dictionary of names, with each node pointing towards their parent
tree = {}
for line in f:
	# Parse line info into node details and children
	line = line.split(" -> ")
	details = line[0].split()

	children = []
	if len(line) > 1:
		children = line[1].split(", ")

	# Point children towards this node (who is their parent)
	for child in children:
		tree[child] = details[0]

# Now walk up the tree
# First get any element of the tree
e = next(iter(tree.keys()))
while e in tree:
	e = tree[e]

def root():
	return e