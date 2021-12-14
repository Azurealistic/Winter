# Advent of Code 2021 - Day: 13
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit

def solve(data):
	# Parse input
	# Split the input into two lists, based on where the empty line is
	# Find the index of the line that is '', and use that to split the list
	# Return the two lists	
	coordinates, instructions = data.strip().split("\n\n")

	coordinates = [[int(x) for x in ln.split(",")] for ln in coordinates.strip().split("\n")]
	instructions = [ln.split() for ln in instructions.strip().split("\n")]
	
	for iteration, fold in enumerate(instructions):
		direction, location = fold[-1].split('=')
		location = int(location)

		points = set()

		# PLace the point based on the current fold.
		for (x, y) in coordinates:
			if direction == 'y':
				if y < location:
					points.add((x, y))
				else:
					points.add((x, location - (y - location)))
			elif direction == 'x':
				if x < location:
					points.add((x, y))
				else:
					points.add((location - (x - location), y))

		coordinates = points

		if iteration == 0:
			print("Star 1:", len(coordinates))
			submit(len(coordinates), part="a", day=13, year=2021)

	grid = []
	for n in range(10):
		grid.append(list(" " * 80))
	
	for (x, y) in coordinates:
		grid[y][x] = '█'

	# Print the grid, by using each row as a string, and then joining them with newlines, only include rows that have a '#' and print up to the final '#'
	print("Star 2:")
	print("\n".join(["".join(row) for row in grid if '█' in row]))
	# This has to be manually submitted, because it's a visual representation of the grid.
	submit("RHALRCRA", part="b", day=13, year=2021)

# Solution
def main():
	solve(data)

# Call the main function.
if __name__ == '__main__':
	main()