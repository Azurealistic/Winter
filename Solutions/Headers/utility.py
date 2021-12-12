# This is a utility file for AoC 2021.
# Mostly to deal with file I/O, and other useful functions.
# Can only be used as a module.

# Imports

# Useful defines.
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRS = [UP, DOWN, LEFT, RIGHT]
DIRS_DIAG = [UP, DOWN, LEFT, RIGHT, (1, 1), (1, -1), (-1, 1), (-1, -1)]

# Get neighbors of a given point
def get_neighbors(point):
	x, y = point
	return [(x + dx, y + dy) for dx, dy in DIRS]

# Get neighbors of a given point, including diagonals.
def get_neighbors_diag(point):
	x, y = point
	return [(x + dx, y + dy) for dx, dy in DIRS_DIAG]

# Gridify a 2D list. 
def gridify(lst):
	return {(x, y): v for x, row in enumerate(lst) for y, v in enumerate(row)}

# Get the value of neighbors of a given point, given a point and a mapping.
def get_neighbors_value(point, mapping):
	return [mapping[p] for p in get_neighbors(point)]

# Can only be used as a module.
if __name__ == "__main__":
	print("This file cannot be run as a program.")
	print("Import it instead.")
	exit(1)