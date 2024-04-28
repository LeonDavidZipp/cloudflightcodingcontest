import csv

def read_file(filename):
	with open(filename, 'r') as file:
		return file.read()

def read_lines(filename):
	with open(filename, 'r') as file:
		lines = [line for line in file]
	return lines


def read_csv(filename):
	with open(filename, 'r') as file:
		reader = csv.reader(file)
		rows = [row for row in reader]
	return rows
