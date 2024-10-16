from reads import read_lines
import os

def solve(line):
	w = 0
	d = 0
	s = 0
	a = 0
	chars = list(line)
	for el in chars:
		if el == 'W':
			w += 1
		elif el == 'D':
			d += 1
		elif el == 'S':
			s += 1
		elif el == 'A':
			a += 1
	return [str(w), str(d), str(s), str(a)]

def execute(infile):
	# read input
	inputs = read_lines(infile)
	inputs = inputs[1:]
	# apply logic to each line
	result_arr = []
	for input in inputs:
		# print(f"input: {input}")
		interm = solve(input)
		result_arr.append(' '.join(interm))
	# join results with ' ' and '\n' at end
	results = '\n'.join(result_arr)
	return results

if __name__ == "__main__":
	level = 1
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
		print(f"name: {name}")
		# try:
		# with open(name, 'r') as infile:
		results = execute(name)
		with open(f"./{outdir}/level{level}_{i + 1}.res", 'w') as outfile:
			outfile.write(results)
		# except:
		# 	print(f"actual name {name}")
		# 	continue
