# Advent of Code 2021 - Day: 17
# Imports (Always imports data based on the folder and file name)
from cmath import inf
from aocd import data, submit
import numpy

def simulate(vel_x, vel_y, x, y):
	x += vel_x
	y += vel_y
	vel_x += -numpy.sign(vel_x)
	vel_y -= 1
	return vel_x, vel_y, x, y

def solve(lines):
	target = lines[0].split(': ')[1].split(', ')
	x1, x2 = int(target[0].split('=')[1].split('..')[0]), int(target[0].split('=')[1].split('..')[1])
	y1, y2 = int(target[1].split('=')[1].split('..')[0]), int(target[1].split('=')[1].split('..')[1])
	total, best_height = 0, 0
	for vx in range(0, x2 + 1):
		for vy in range(y1, 1000):
			x, y = 0, 0
			vel_x, vel_y = vx, vy
			max_y = 0
			while x <= x2 and y >= y1:
				vel_x, vel_y, x, y = simulate(vel_x, vel_y, x, y)
				if y > max_y:
					max_y = y
				if x >= x1 and x <= x2 and y >= y1 and y <= y2:
					total += 1
					if max_y > best_height:
						best_height = max_y
					break
				if vel_x == 0 and x < x1: # If we're not moving horizontally, and we're still before the start of the target, we're done.
					break

	print("Star 1:", best_height)
	submit(best_height, part='a', day=17, year=2021)
	print("Star 2:", total)
	submit(total, part='b', day=17, year=2021)
	
# Solution
def main():
	solve(data.strip().split('\n'))

# Call the main function.
if __name__ == '__main__':
	main()