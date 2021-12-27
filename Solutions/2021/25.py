# Advent of Code 2021 - Day: 25
# Imports (Always imports data based on the folder and file name)
import itertools
from aocd import data, submit

grid = [list(line) for line in data.split("\n")]
w, h = len(grid[0]), len(grid)

for step in itertools.count():
    totm = 0

    moves = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == ">" and grid[y][(x + 1) % w] == ".":
                moves.append((x, y))

    for x, y in moves:
        grid[y][x] = "."
        grid[y][(x + 1) % w] = ">"

    totm += len(moves)

    moves = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "v" and grid[(y + 1) % h][x] == ".":
                moves.append((x, y))

    for x, y in moves:
        grid[y][x] = "."
        grid[(y + 1) % h][x] = "v"

    totm += len(moves)

    if totm == 0:
        print(step + 1)