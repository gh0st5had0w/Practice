# Finding the sum of a pythagorean triplet

import math

for a in range(1, 500):
	for b in range(a, 500):
		print(b)
		c = math.sqrt(a**2 + b**2)
		if a + b + c > 1000:
			break
		if type(c) == int:
			if a + b + c == 1000:
				print(a, b, c)
				print(a * b * c)
				exit()