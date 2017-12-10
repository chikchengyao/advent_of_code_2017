from input import input

input = [i.split() for i in input.split("\n")]

register = {}

global_max = [0]

def myexec(instr):
	try:
		register[instr[0]]
	except:
		register[instr[0]] = 0
	try:
		register[instr[4]]
	except:
		register[instr[4]] = 0
	to_exec = "register['%s'] %s %s if register['%s'] %s %s else 0"%(instr[0], "+=" if instr[1] == "inc" else "-=", instr[2], instr[4], instr[5], instr[6])
	exec(to_exec)
	if register[instr[0]] > global_max[0]:
		global_max[0] = register[instr[0]]

for instr in input:
	myexec(instr)

print(global_max[0])