from reads import read_lines
import os
import math

def up(vert, horiz):
	return (vert - 1, horiz)

def down(vert, horiz):
	return (vert + 1, horiz)

def left(vert, horiz):
	return (vert, horiz - 1)

def right(vert, horiz):
	return (vert, horiz + 1)

def read_next_exercise(inputs):
	width, height = map(int, inputs[0].split())
	matrix = []
	for i in range(1, 1 + height):
		matrix.append(list(inputs[i][:-1]))
	commands = list(inputs[1 + height])
	return matrix, commands, width, height, height + 2

def apply_algo(start, matrix, commands):
	vert, horiz = start
	visited_matrix = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
	visited_matrix[vert][horiz] = True
	# print(f"start: {start}")
	commands = commands[:-1]
	for command in commands:
		# print("step: ", command)
		if command == 'W':
			vert, horiz = up(vert, horiz)
		elif command == 'S':
			vert, horiz = down(vert, horiz)
		elif command == 'A':
			vert, horiz = left(vert, horiz)
		elif command == 'D':
			vert, horiz = right(vert, horiz)
		# check if new position is valid
		if vert < 0 or vert >= len(matrix) or horiz < 0 or horiz >= len(matrix[0]):
			# print(f"because of vert: {vert} and horiz: {horiz}")
			return "INVALID"
		# check if new position is a tree
		if matrix[vert][horiz] == 'X':
			# print(f"because of tree")
			return "INVALID"
		# check if new position has been visited
		if visited_matrix[vert][horiz] == True:
			# print(f"because of visited")
			return "INVALID"
		visited_matrix[vert][horiz] = True
	# print(f"vert: {vert} and horiz: {horiz}")
	# check if all positions have been visited
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])):
			if not visited_matrix[i][j] and matrix[i][j] != 'X':
				return "INVALID"
	# print("VALID")
	return "VALID"

def solve(inputs, start):
	matrix, commands, width, height, end = read_next_exercise(inputs)
	for i in range(0, height):
		for j in range(0, width):
			start = (i, j)
			if matrix[i][j] == 'X':
				continue
			valid = apply_algo(start, matrix, commands)
			if valid == "VALID":
				# print("valid is valid")
				return valid, end
	return "INVALID", end

def execute(infile):
	# read input
	inputs = read_lines(infile)
	repetitions = int(inputs[0])
	inputs = inputs[1:]
	result_arr = []
	for _i in range(repetitions):
		valid, start = solve(inputs, 0)
		result_arr.append(valid)
		inputs = inputs[start:]
		# print("-------\n")
	results = '\n'.join(result_arr)
	return results

if __name__ == "__main__":
	level = 3
	indir = "inputs"
	filenames = [
		f"./{indir}/level{level}_1.in",
		f"./{indir}/level{level}_2.in",
		f"./{indir}/level{level}_3.in",
		f"./{indir}/level{level}_4.in",
		f"./{indir}/level{level}_5.in"
	]

	outdir = "./results"
	if not os.path.exists(outdir):
		os.mkdir(outdir)
	for i, name in enumerate(filenames):
		# # print(f"name: {name}")
		# trhoriz:
		# with open(name, 'r') as infile:
		results = execute(name)
		with open(f"./{outdir}/level{level}_{i + 1}.res", 'w') as outfile:
			outfile.write(results)
		# evertcept:
		# 	# print(f"actual name {name}")
		# 	continue


# logic: test from everhoriz starting point but the tree
# apllhoriz the algorithm to each starting point
# if anhoriz result comes back valid, return valid
# else return invalid