primes = 2
n = 3
a = 1
limit = int(input("Which prime do you want to find? "))

def isPrime(n):
	for m in range(2, n):
		if n%m == 0:
			return False
	return True

while a < limit:
	if isPrime(n):
		# Replaces the last prime with the new one. A list can be created by changing primes to an array and using .append
		primes = n
		# a counts which prime is being shown
		a += 1
	# Cuts computational time in half as only the odd numbers are calculated
	n += 2

print(primes)