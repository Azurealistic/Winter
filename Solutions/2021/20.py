# Advent of Code 2021 - Day: 20
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit
import numpy as np

def blowup(lookup, image, empty = 0):
	image = np.pad(image, 3, constant_values = empty)
	if empty == 0:
		res = np.zeros(image.shape, dtype = np.uint8)
	else:
		res = np.ones(image.shape, dtype = np.uint8)
	yl, xl = image.shape
	for y in range(1, yl - 1):
		for x in range(1, xl - 1):
			i = image[y - 1:y+2, x - 1:x+2].flatten()
			i = int("".join(map(str, i)), 2)
			res[y, x] = lookup[i]
	return res[1:-1, 1:-1], lookup[0] if empty == 0 else lookup[int("111111111", 2)]

def solve(lines):	
	mapping = {
		'.': 0,
		'#': 1,
	}
	lookup, image = lines.split('\n\n')
	lookup = np.array([mapping[x] for x in lookup], dtype=np.uint8)
	image = np.array([list(map(lambda z: mapping[z], x)) for x in image.splitlines()], dtype=np.uint8)
	empty = 0
	for i in range(50):
		image, empty = blowup(lookup, image, empty)
		if i == 1:
			p1 = image.sum()
	p2 = image.sum()
	print("Star 1:", p1)
	submit(p1, part="a", day=20, year=2021)
	print("Star 2:", p2)
	submit(p2, part="b", day=20, year=2021)
	pass

# Solution
def main():
	solve(data)

# Call the main function.
if __name__ == '__main__':
	main()