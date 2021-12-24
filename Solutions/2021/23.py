# Advent of Code 2021 - Day: 23
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit

def solve():
	# Did this completely by hand.
	print("Star 1:", 14346)
	print("Star 2:", 48984)
	submit(14346, part="a", day=23, year=2021)
	submit(48984, part="b", day=23, year=2021)

# Solution
def main():
	solve()

# Call the main function.
if __name__ == '__main__':
	main()