# Advent of Code 2021 - Day: 1
# Imports (Always imports data based on the folder and file name)
from aocd import submit, numbers

def solve(lines):
	# Convert 
	# Part 1
	star1 = 0
	for num in range(len(lines) - 1):
		if lines[num] < lines[num + 1]:
			star1 += 1
	print("Star 1:", star1)
	submit(star1, part='a', day=1, year=2021)
	# Part 2
	star2 = 0
	for num in range(len(lines) - 3):
		if lines[num] < lines[num + 3]:
			star2 += 1
	print("Star 2:", star2)
	submit(star2, part='b', day=1, year=2021)

# Solution
def main():
	solve(numbers)

# Call the main function.
if __name__ == '__main__':
	main()