# Advent of Code 2021 - Day: 16
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit

# Get the next n bits from the data, and remove them from the data. Return the bits.
def next_bits(data, n):
	ret = data[0][:n]
	data[0] = data[0][n:]
	return ret

def parse(data):
	global v_sum

	version = int(next_bits(data, 3), 2)
	v_sum += version
	type_id = int(next_bits(data, 3), 2)

	# Process the data if it is a literal value we are looking at.
	if type_id == 4:
		v_data = [] # Hold the data for the literal value minus the header for each portion.
		while True:
			# Get the first bit, and the rest.
			count, *v = next_bits(data, 5)
			v_data += v
			if count == '0':
				break
		return int("".join(v_data), 2)

	ltype_id = next_bits(data, 1)[0]
	sp_l = [] # Contains the various subpackets info in a list.

	# Recursively parse the subpackets and store them in the list.
	if ltype_id == '0':
		sp_len = int(next_bits(data, 15), 2)
		sp = [next_bits(data, sp_len)]
		while sp[0]:
			sp_l.append(parse(sp))
	else:
		sp_l = [parse(data) for i in range(int(next_bits(data, 11), 2))]

	# Process the data using the rules of the operator type.
	if type_id == 0: # Sum
		return sum(sp_l)
	elif type_id == 1: # Product
		p = 1
		for x in sp_l:
			p *= x
		return p
	elif type_id == 2: # Minimum
		return min(sp_l)
	elif type_id == 3:
		return max(sp_l) # Maximum
	# Next 3 always has only two subpackets.
	elif type_id == 5: # Greater than
		return int(sp_l[0] > sp_l[1])
	elif type_id == 6: # Less than
		return int(sp_l[0] < sp_l[1])
	elif type_id == 7: # Equal
		return int(sp_l[0] == sp_l[1])

def solve(lines):
	global v_sum
	v_sum = 0

	# Parse the data from a string to the required binary format.
	d = bin(int(lines, 16))[2:]

	while len(d) < 4 * len(lines):
		d = '0' + d

	p2 = parse([d])
	print("Star 1:", v_sum)
	submit(v_sum, part='a', day=16, year=2021)
	print("Star 2:", p2)
	submit(p2, part='b', day=16, year=2021)

# Solution
def main():
	solve(data.strip())

# Call the main function.
if __name__ == '__main__':
	main()