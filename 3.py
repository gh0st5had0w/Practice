# Finding the largest prime factor of any positive integer

yourNumber = int(input("What is your number?"))
n = 2

# To get the largest prime of an integer, we can divide it by larger
# and larger primes until it can't divide any further. Note that the
# number we divide with must be smaller than the integer, else the code
# will always return yourNumber as 1.

while n < yourNumber:
	if yourNumber%n == 0:
		yourNumber = yourNumber/n
	else:
		# For the sake of making the code simpler, we divide by every integer.
		n += 1

print(yourNumber)

# -=-=-=-=-=-=-=-=-=-=-  =====   *   =====  -=-=-=-=-=-=-=-=-=-=- #

# Attempt 1: I tried combing through all the factors of the chosen integer 
# largest to smallest and then figure out if the factor was prime. This in
# theory works but it takes much longer

#factors = []
#yourNumber = int(input("What is your number?"))

#for n1 in range(yourNumber-1, 0, -1):
#	if yourNumber%n1 == 0:
#		for n2 in range(2, n1):
#			if not n2%n1 == 0:
#				factors.append(n1)

#print(factors)