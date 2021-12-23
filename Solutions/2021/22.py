# Advent of Code 2021 - Day: 22
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit

def parse(lines):
	parsed_lines = []
	for line in lines:
		value, coords = line.split(' ')[0], line.split(' ')[1].split(',')
		curr = []
		for coord in coords:
			coord = coord.split('=')[1].split('..')
			curr.append(int(coord[0]))
			curr.append(int(coord[1]) + 1) # Add 1 to the end so we can use the range function easily
		curr.append(value)
		parsed_lines.append(curr)
	return parsed_lines

def calculate_lights(cubes):
	lights = sum((cube[1] - cube[0]) * (cube[3] - cube[2]) * (cube[5] - cube[4]) for cube in cubes if cube[6] == 'on')
	return lights

def calculate(lines, length = 20): # Used for both parts of the challenge. Len is for number of lines to process.
	all_cubes = []
	for i in range(length):
		cube = lines[i]
		new_cubes = []
		for j in range(len(all_cubes)):
			curr = all_cubes[j]
			if (cube[1] > curr[0] and cube[0] < curr[1]) and (cube[3] > curr[2] and cube[2] < curr[3]) and (cube[5] > curr[4] and cube[4] < curr[5]):
				for i in range(6):
					if (curr[i] > cube[i]) if (i & 1) else (curr[i] < cube[i]):
						nc = curr[:]
						nc[i ^ 1] = curr[i] = cube[i]
						new_cubes.append(nc)
			else:
				new_cubes.append(curr)

		new_cubes.append(cube)
		all_cubes = new_cubes

	return calculate_lights(all_cubes)

def solve(data):
	lines = parse(data.splitlines())
	p1 = calculate(lines)
	lines = parse(data.splitlines())
	p2 = calculate(lines, len(lines))
	print('Star 1:', p1)
	print('Star 2:', p2)
	submit(p1, part='a', day=22, year=2021)
	submit(p2, part='b', day=22, year=2021)

# Solution
def main():
	solve(data)

# Call the main function.
if __name__ == '__main__':
	main()