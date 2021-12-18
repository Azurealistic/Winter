# Advent of Code 2021 - Day: 18
# Imports (Always imports data based on the folder and file name)
from functools import reduce
import itertools
import math
from aocd import data, submit
import ast

# Recursivelly add two lists together with left or right bias
def recursive_addition(ll, num, left = True):
	if num is None:
		return ll
	if isinstance(ll, int):
		return ll + num
	if left:
		return [recursive_addition(ll[0], num), ll[1]]
	else:
		return [ll[0], recursive_addition(ll[1], num)]

# Explode list by doing it recursively
def explode(ll, lvl = 4):
	# Check if is instance of int
	if isinstance(ll, int):
		return False, None, ll, None
	if lvl == 0: # We are at the end of our recursion
		return True, ll[0], 0, ll[1]
	first, second = ll # Get the first and second elements of the list
	# Explode recursively
	explosion, delta, first, gamma = explode(first, lvl - 1)
	# If we exploded, we need to add to left and right of the list respectively
	if explosion == True:
		return True, delta, [first, recursive_addition(second, gamma, True)], None
	# Explode recursively again
	explosion, delta, second, gamma = explode(second, lvl - 1)
	# This time we go down the right side of the list
	if explosion == True:
		return True, None, [recursive_addition(first, delta, False), second], gamma
	# Base case and returns
	return False, None, ll, None

# Follows similiar style to explode going recursively if we have a list, or processing the int if we have an int
def split(ll):
	if isinstance(ll, int):
		if ll >= 10:
			return True, [ll // 2, math.ceil(ll / 2)]
		return False, ll
	first, second = ll
	delta, first = split(first)
	if delta == True:
		return True, [first, second]
	delta, second = split(second)
	return delta, [first, second]

# Add two lists together and explode or split them as needed till we finished.
def add(first, second):
	ll = [first, second]
	while True: # Loop until we explode or split
		delta, _, ll, _ = explode(ll) # The _ are ignored since they're only relevant during the explode function recursion
		if delta == True:
			continue
		delta, ll = split(ll)
		if not delta:
			break
	return ll

def magnitude(ll):
	if isinstance(ll, int):
		return ll
	return 3 * magnitude(ll[0]) + 2 * magnitude(ll[1])

def solve(lines):
	# For each line in the input, process it using ast.literal_eval and put it into a list
	lines = [ast.literal_eval(line) for line in lines]
	p1 = magnitude(reduce(add, lines))
	print("Star 1:", p1)
	submit(p1, part='a', day=18, year=2021)
	p2 = max(magnitude(add(a, b)) for a, b in itertools.permutations(lines, 2))
	print("Star 2:", p2)
	submit(p2, part='b', day=18, year=2021)
	pass

# Solution
def main():
	solve(data.splitlines())

# Call the main function.
if __name__ == '__main__':
	main()