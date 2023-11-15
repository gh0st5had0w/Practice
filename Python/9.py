# Finding the sum of a pythagorean triplet

import math

# for a in range(1, 500):
# 	for b in range(a, 500):
# 		print(b)
# 		c = math.sqrt(a**2 + b**2)
# 		if a + b + c > 1000:
# 			break
# 		if type(c) == int:
# 			if a + b + c == 1000:
# 				print(a, b, c)
# 				print(a * b * c)
# 				exit()

numberListSquared = [i**2 for i in range(1, 999)]

for i in numberListSquared:
	for j in numberListSquared:
		a = i + j
		for k in numberListSquared:
			if a == k:
				if math.sqrt(i) + math.sqrt(j) + math.sqrt(k) == 1000:
					print(math.sqrt(i), math.sqrt(j), math.sqrt(k))
					exit()