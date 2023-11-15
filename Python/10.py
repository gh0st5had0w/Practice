import math

primes = [2]
n = 3
limit = int(input("What number do you want to stop at? "))

def isPrime(n):
	m = 0
	while m < len(primes) and primes[m] <= math.sqrt(n):
		if n % primes[m] == 0:
			return False
		m += 1
	return True

while n <= limit:
	if isPrime(n):
		# Adds the prime to a list
		primes.append(n)
	n += 2

print(sum(primes))