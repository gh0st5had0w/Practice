# Finding the first triangular number that has over 500 divisors

import math

n = 0
factors = []
increment = 1

while len(factors) < 500:
	# Finding the next triangular number
	n += increment
	increment +=1

	# Finding the number of factors that the number has
	for i in range(1, math.ceil(math.sqrt(n))):
		if n % i == 0:
			if n == i:
				factors.append(i)
			else:
				factors.append(i)
				factors.append(int(n/i))


	# Checking if the number of factors reaches 500
	if len(factors) < 500:
		factors = []

print(sorted(factors))
print(len(factors))