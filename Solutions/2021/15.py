# Advent of Code 2021 - Day: 15
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit

def solve(lines, expanded = False):
	ll = [[int(y) for y in x] for x in lines.strip().split('\n')]

	# Lambda function
	def in_ls(pos, ls):
		return pos[0] in range(len(ls)) and pos[1] in range(len(ls[0]))

	expanded_arr = []
	
	if expanded == True:
		expanded_arr = [[0 for x in range(5*len(ll[0]))] for y in range(5*len(ll))]
		for x in range(len(expanded_arr)):
			for y in range(len(expanded_arr)):
				distance = x//len(ll) + y//len(ll[0])
				new = ll[x%len(ll)][y%len(ll[0])]
				for i in range(distance):
					new += 1
					if new == 10:
						new = 1
				expanded_arr[x][y] = new

		ll = expanded_arr

	q = [(0, 0, 0)] # value, x, y

	costs = {}

	while True:
		cost,x,y = q[0]
		if x == len(ll) - 1 and y == len(ll[0]) - 1:
			if expanded == False:
				print("Star 1:", cost)
				submit(cost, part='a', day=15, year=2021)
			else:
				print("Star 2:", cost)
				submit(cost, part='b', day=15, year=2021)
			break

		q = q[1:]

		for dx,dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
			if in_ls((dx, dy), ll) and (dx, dy) not in costs:
				costs[(dx, dy)] = cost + ll[dx][dy]
				q.append((cost + ll[dx][dy], dx, dy))

		q.sort(key=lambda x: x[0])

# Solution
def main():
	solve(data, False)
	solve(data, True)

# Call the main function.
if __name__ == '__main__':
	main()