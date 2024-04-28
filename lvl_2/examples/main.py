from reads import read_lines
import os
import math

def solve(line):
	max_height = 0
	max_width = 0
	min_height = 0
	min_width = 0
	curr_height = 0
	curr_width = 0
	for el in line:
		if el == 'W':
			curr_height += 1
		elif el == 'S':
			curr_height -= 1
		elif el == 'A':
			curr_width -= 1
		elif el == 'D':
			curr_width += 1
		if curr_height > max_height:
			max_height = curr_height
		if curr_height < min_height:
			min_height = curr_height
		if curr_width > max_width:
			max_width = curr_width
		if curr_width < min_width:
			min_width = curr_width
	height = abs(max_height -min_height) + 1
	width = abs(max_width - min_width) + 1
	return [str(width), str(height)]

def execute(infile):
	# read input
	inputs = read_lines(infile)
	inputs = inputs[1:]
	# apply logic to each line
	result_arr = []
	for input in inputs:
		# print(f"input: {input}")
		interm = solve(input)
		# print(f"interm: {' '.join(interm)}")
		result_arr.append(' '.join(interm))
	# join results with ' ' and '\n' at end
	results = '\n'.join(result_arr)
	return results

if __name__ == "__main__":
	level = 2
	indir = "inputs"
	filenames = [
		"level2_example.in",
	]

	outdir = "./results"
	if not os.path.exists(outdir):
		os.mkdir(outdir)
	for i, name in enumerate(filenames):
		# print(f"name: {name}")
		# try:
		# with open(name, 'r') as infile:
		results = execute(name)
		with open(f"./{outdir}/level{level}_{i + 1}.res", 'w') as outfile:
			outfile.write(results)
		# except:
		# 	print(f"actual name {name}")
		# 	continue
