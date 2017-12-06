import math

def getLayer(n):
	# Gets the "shell number" or layer number of the number n. 
	# For example, 9 is the largest number in layer 1. 10 is the first number in layer 2.
	return math.ceil((math.sqrt(n)-1)/2)

def layerMin(layer):
	# Returns the smallest number in a given layer
	return (2*layer - 1)**2 + 1

def sideLength(layer):
	return 2*layer

def getDist(n):
	layer = getLayer(n)
	layer_min = layerMin(layer)
	index = n - layer_min # The index of a number along its layer. 10 is the 0th number of layer 2.
	side_index = index % sideLength(layer) # The index of a number along its side. 

	# Now, shift the indices to reflect distance from the "centre" of each side.
	side_index -= layer-1
	side_index = abs(side_index)

	return side_index + layer

print(getDist(289326))



