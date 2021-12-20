# Advent of Code 2021 - Day: 19
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit
import numpy as np

def add(a, b):
  return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def neg(a):
	return (-a[0], -a[1], -a[2])

def orient(pos, o): 
	return (np.dot(pos, o[0]), np.dot(pos, o[1]), np.dot(pos, o[2]))

def solve(lines):
	for scanner in lines:
		for fb in scanner: # Now we go through each set of beacons. Fb = first beacon, sb = second beacon. We essentially are calculating distances between the two beacons.
			fb.append({np.linalg.norm(np.array(fb[0]) - np.array(sb[0])) for sb in scanner}) 
	
	t = ((1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1))
	os = [(x,y,z) for x in t for y in t for z in t if np.linalg.det((x,y,z)) == 1]

	beacons, ts = {}, {}

	for i in range(len(lines)):
		for j in range(i + 1, len(lines)):
			for fb in lines[i]:
				for sb in lines[j]:
					if len(fb[1] & sb[1]) >= 12:
						beacons.setdefault((i, j), set()).add((fb[0], sb[0]))

	for b, values in beacons.items():
		for o in os:
			s = set()
			for v in values:
				s.add(np.linalg.norm(np.array(v[0]) - orient(v[1], o)))
			if len(s) == 1:
				ts[b] = [(add(v[0], neg(orient(v[1], o))), o)]
				break

	while len([*filter(lambda x : x[0] == 0, ts)]) < len(lines) - 1:
		for b in range(len(lines)):
			for x in range(len(lines)):
				for y in range(len(lines)):
					if x == y or b == y:
						continue
					if (p := ts.get((b, x))) and not (b, y) in ts and (s := ts.get((x, y))):
						ts[(b, y)] = [*s, *p]
					if (p := ts.get((b, x))) and not (b, y) in ts and (s := ts.get((y, x))):
						ts[(b, y)] = [*[(orient(neg(v[0]), iv := np.linalg.inv(v[1])), iv) for v in reversed(s)], *p]

	pts, pos = {p[0] for p in lines[0]}, []
	for i in range(1, len(lines)):
		for p in lines[i]:
			rf = (0, 0, 0)
			pt = p[0]
			for t in ts[(0, i)]:
				rf = add(t[0], orient(rf, t[1]))
				pt = add(t[0], orient(pt, t[1]))
			pts.add(pt)
		pos.append(rf)

	return len(pts), int(max([sum(map(abs,add(x, neg(y)))) for x in pos for y in pos]))

# Solution
def main():
	lines = [ # Read the data into a format similar to something like [[(x, y, z)], [(x, y, z)], [(x, y, z)]].. etc for each individual scanner.
		[[tuple(int(v) for v in l.split(','))] 
		for l in l[1:]] 
		for l in[l.strip().split('\n') 
		for l in data.split('\n\n')]
	]
		
	p1, p2 = solve(lines)
	print("Star 1:", p1)
	submit(p1, part="a", day=19, year=2021)
	print("Star 2:", p2)
	submit(p2, part="b", day=19, year=2021)

# Call the main function.
if __name__ == '__main__':
	main()