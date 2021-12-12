# Advent of Code 2021 - Day: 12	
# Imports (Always imports data based on the folder and file name)
from collections import Counter, defaultdict
from aocd import data, submit

def create_graph(data):
	edges = defaultdict(list)
	for line in data:
		v1, v2 = line.split('-')
		edges[v1].append(v2)
		edges[v2].append(v1)
	return edges

def solve_recursive(edges, curr, prev, doubles = False):
	if not curr.isupper():
		prev = prev + [curr]
	if curr == 'end':
		return 1
	total = 0
	for n in edges[curr]:
		if n not in prev or (doubles and max(Counter(prev).values()) == 1 and n != 'start'):
			total += solve_recursive(edges, n, prev, doubles)
	return total

def solve(graph):
	edges = create_graph(graph)
	star1 = solve_recursive(edges, 'start', [])
	star2 = solve_recursive(edges, 'start', [], True)
	print("Star 1: {}".format(star1))
	print("Star 2: {}".format(star2))
	submit(star1, part='a', day=12, year=2021)
	submit(star2, part='b', day=12, year=2021)

# Solution
def main():
	solve(data.splitlines())
		
# Call the main function.
if __name__ == '__main__':
	res = 0
	main()