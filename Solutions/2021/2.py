# Advent of Code 2021 - Day: 2
# Imports (Always imports data based on the folder and file name)
from dis import dis
from aocd import data, submit

def solve(lines):
	# Take the lines and put them in a list of tuples
	# Each tuple is a line of the input (direction, distance)
	# Direction is 'forward', 'down', 'up'
	course = [(line.split()[0], int(line.split()[1])) for line in lines]
	hoz, aim_depth, depth, aim = 0, 0, 0, 0
	for direction, distance in course:
		if direction == 'forward':
			hoz += distance
			aim_depth += distance * aim
		elif direction == 'down':
			depth -= distance
			aim -= distance
		elif direction == 'up':
			depth += distance
			aim += distance
	# Part 1
	print("Star 1: {}".format(abs(hoz * depth)))
	submit(abs(hoz * depth), part='a', day=2, year=2021)
	# Part 2
	print("Star 2: {}".format(abs(aim_depth* hoz)))
	submit(abs(aim_depth* hoz), part='b', day=2, year=2021)

# Solution
def main():
	solve(data.splitlines())

# Call the main function.
if __name__ == '__main__':
	main()