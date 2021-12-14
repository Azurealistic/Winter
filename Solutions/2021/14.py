# Advent of Code 2021 - Day: 14
# Imports (Always imports data based on the folder and file name)
from aocd import data, submit
from collections import Counter

def solve(lines):
	# part 1 and 2
	p1, p2 = 0, 0
	# Get the first line of the data and put it into a string called template
	template = lines[0]
	pairs = {}
	lines = lines[2:] # Remove the first two lines
	for line in lines:
		key, val = line.split(' -> ')
		pairs[key] = val

	# Count each pair of letters in the template, initial pairs start at 1.
	CharCounter = Counter()
	for i in range(len(template) - 1):
		CharCounter[template[i] + template[i+1]] += 1

	for i in range(41):
		# Now get the count of first character in each pair
		# And update the count of the last character in the string by 1 since we never add to the end of the string.
		if i in [10, 40]:
			AppearCounter = Counter()
			for k in CharCounter:
				AppearCounter[k[0]] += CharCounter[k]
			AppearCounter[template[-1]] += 1
			if p1 == 0:
				p1 = max(AppearCounter.values())-min(AppearCounter.values())
			else:
				p2 = max(AppearCounter.values())-min(AppearCounter.values())

		# For each pair we have in the template such as AZ -> J 
		# We end up with the pairs of AJ and JZ.
		UpdateCounter = Counter()
		for k in CharCounter:
			# So basically here we are going to take the key and split it into two
			# And then update the count of each new pair that we now have made.
			# And add the existing count of the pair to the new pair count.
			UpdateCounter[k[0]+pairs[k]] += CharCounter[k]
			UpdateCounter[pairs[k]+k[1]] += CharCounter[k]
		# Finally just set the old counter to the new counter and have an updated counter.
		CharCounter = UpdateCounter

	# Submit the answer to the website
	print("Star 1:" + str(p1))
	submit(p1, part="a", day=14, year=2021)
	print("Star 2: " + str(p2))
	submit(p2, part="b", day=14, year=2021)

# Solution
def main():
	solve(data.splitlines())

# Call the main function.
if __name__ == '__main__':
	main()