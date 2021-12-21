# Advent of Code 2021 - Day: 21
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit
from itertools import product
import functools as ft

def roll(p, s, d):
	p += sum(next(d) for _ in range(3))
	while p > 10: # God I hate modulus this is easier.
		p -= 10
	s += p
	return p, s
		
def play_game(p1, p2):
	# Get next number in the roll.
	def load_dice(): 
		while True:
			for n in range(1, 101):
				yield n

	s1, s2, r = 0, 0, 0
	dice = load_dice()

	while True:
		p1, s1 = roll(p1, s1, dice)
		r += 3
		if s1 >= 1000:
			break
		p2, s2 = roll(p2, s2, dice)
		r += 3
		if s2 >= 1000:
			break
	return r, s1, s2

@ft.cache
def universes(p1, p2, s1 = 0, s2 = 0, player = 1):
	u1, u2 = 0, 0
	for r in product((1, 2, 3), repeat=3):
		if player == 1:
			n1 = p1 + sum(r)
			while n1 > 10:
				n1 -= 10
			ns1 = s1 + n1
			if ns1 >= 21:
				u1 += 1
			else:
				sub_u1, sub_u2 = universes(n1, p2, ns1, s2, 2)
				u1 += sub_u1
				u2 += sub_u2
		else:
			n2 = p2 + sum(r)
			while n2 > 10:
				n2 -= 10
			ns2 = s2 + n2
			if ns2 >= 21:
				u2 += 1
			else:
				sub_u1, sub_u2 = universes(p1, n2, s1, ns2, 1)
				u1 += sub_u1
				u2 += sub_u2
				
	return u1, u2

def solve(p1start, p2start):
	r, s1, s2 = play_game(p1start, p2start)
	res = r * min(s1, s2)
	print("Star 1:", res)
	submit(res, part='a', day=21, year=2021)
	
	s1, s2 = universes(p1start, p2start)
	res = max(s1, s2)
	print("Star 2:", res)
	submit(res, part='b', day=21, year=2021)

# Solution
def main():
	data.splitlines()
	p1start = int(data.splitlines()[0].split(':')[1])
	p2start = int(data.splitlines()[1].split(':')[1])
	solve(p1start, p2start)

# Call the main function.
if __name__ == '__main__':
	main()