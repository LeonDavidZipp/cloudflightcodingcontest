import read_lines

# def execute(filename);
# 	inputs = read_lines("input.txt")
# 	interm_res = "..."
# 	return result_arr

def solve(str: line):
	# apply logic to line
	# return result_arr
	return result_arr

def execute(str: infile):
	# read input
	inputs = read_lines(infile)
	# apply logic to each line
	result_arr = []
	for input in inputs:
		interm = solve(input)
		result_arr.append(interm)
	# join results with ' ' and '\n' at end
	results = ' '.join(result_arr) + '\n'
	return results

if __name__ == "__main__":
	level = 1
	filnames = [
		f"level{level}_1.in",
		f"level{level}_2.in",
		f"level{level}_3.in",
		f"level{level}_4.in",
		f"level{level}_5.in"
	]

	for name, i in enumerate(filenames):
		with open(name, 'r') as infile:
			results = execute(infile)
			with open(f"level{level}_{i}.res", 'w') as outfile:
				outfile.write(results)