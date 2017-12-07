##########################################################
##        Disgusting hacky code pls don't judge         ##
##########################################################
# legit this will give you a fucking headache to read
#
# ABANDON HOPE ALL YE WHO ENTER HERE
#
# no, seriously, ask me to explain IRL it'll probably be easier


from input import input
from py7a import root

raw = input.split("\n")
for i in range(len(raw)):
	raw[i] = raw[i].split()
	raw[i][1] = int(raw[i][1][1:-1])
	for j in range(3, len(raw[i]) - 1):
		raw[i][j] = raw[i][j][0:-1]

total_weight = {}
nodes = {}

# Populate `nodes`
for node in raw:
	nodes[node[0]] = node

# get weight, memoising along the way
def get_total_weight(name):
	if name in total_weight:
		pass
	elif len(nodes[name]) <= 2:
		total_weight[name] = nodes[name][1]
	else:
		sum = nodes[name][1]
		for i in range(3, len(nodes[name])): #i.e., for each child of this node
			sum += get_total_weight(nodes[name][i])
		total_weight[name] = sum
	return total_weight[name]

root_name = root()

def all_equal(xs):
	if xs == []:
		return True
	else:
		return max(xs) == min(xs)

def is_balanced(name):
	# Returns bool

	# Finds weights of current children and checks if they're all equal.
	weight_list = []
	for i in range(3, len(nodes[name])):
		weight_list.append(get_total_weight(nodes[name][i]))

	return all_equal(weight_list)

def odd_one_out(xs):
	if len(xs) <= 2:
		print("STOP AT TWO!")
	else:
		xs.sort()
		if xs[0] == xs[1]:
			return xs[-1]
		else:
			return xs[0]

def find_unbalanced(name):
	if len(nodes[name]) == 5:
		print("STOP AT TWO")

	if is_balanced(name):
		print("%s is balanced, returning True"%(name))
		return True
	else:
		# look for the odd one out and return find_unbalanced on it
		weight_list = []
		for i in range(3, len(nodes[name])):
			weight_list.append(get_total_weight(nodes[name][i]))
		
		print("weight_list of %s is"%(name), weight_list)

		odd_weight = odd_one_out(weight_list)
		print("Odd weight is", odd_weight)

		for i in range(3, len(nodes[name])):
			if odd_weight == get_total_weight(nodes[name][i]):
				print("Found odd node is %s"%i)
				if find_unbalanced(nodes[name][i]) == True:
					print("Return value is True, performing one-off operations")
					for j in range(3,len(nodes[name])):
						if j != i:
							print("Found some j = %d not equal to i = %d"%(j,i))
							diff = get_total_weight(nodes[name][j]) - get_total_weight(nodes[name][i])
							return nodes[nodes[name][i]][1] + diff
				else:
					return find_unbalanced(nodes[name][i])

		return "FATAL ERROR"

print(find_unbalanced(root_name))






#############################################################
# THE FOLLOWING ARE ALL DEPRECATED
#############################################################

# from input import input

# #print(input)
# nodes = input.split("\n")
# for i in range(len(nodes)):
# 	nodes[i] = nodes[i].split()
# total_weights = {} #memo table for weights

# def getTotalWeight(index):
# 	if index in total_weight:
# 		pass
# 	elif len(nodes[index]) <= 2:  # i.e., has no children
# 		total_weights[index] = int(nodes[index][1][1:-1])
# 		print("Weight of %s at index %d is %d"%(nodes[index][0],index,total_weights[index]))
# 	else 
# 		sum = int(nodes[index][1][1:-1])
# 		for i in range(3, len(nodes[index])):

# 	return total_weight[index]

# calculateWeight(2)
# Procedure
# Read list of nodes
# run checkBalanced
# part of checkBalanced is a recursive memoising function called calculateWeight









# #SETUP

# f = open("input2.txt")

# # The set of nodes
# # 	Structure: Takes a string (the name of the node) and returns an object, which has the properties:
# #		name: string name
# # 		parent: None OR string name
# # 		children: list of string name
# # 		weight : int weight
# # 		total_weight: int total_weight
# # 		balanced: None OR bool is_balanced
















# # Construct two trees represented by dicts, one giving the name of its parent, other giving a list of
# # its children.
# parent_of = {}
# children_of = {}
# weight_of = {}

# for line in f:
# 	# Parse line info into node details and children
# 	line = line[:-1] # Get rid of trailing newline
# 	line = line.split(" -> ")
# 	details = line[0].split()

# 	children = []
# 	if len(line) > 1:
# 		children = line[1].split(", ")

# 	# Point parent_of[child] to parent
# 	for child in children:
# 		parent_of[child] = details[0]

# 	# Point children_of[parent] to [children]
# 	children_of[details[0]] = children

# 	# Save weight
# 	weight = int(details[1][1:-1])

# # Walk up parent_of to find root
# # First get any element of the tree
# root = next(iter(parent_of.keys()))
# while root in parent_of:
# 	root = parent_of[root]


# # Approach: Traverse the tree, at each node flag it as balanced or not. 