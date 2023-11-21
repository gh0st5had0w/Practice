# Finding the total number of paths in a lattice grid

import math

r = int(input("What is the size of the grid? "))
n = r * 2

# Equation for finding combinations or the number is Pascal's triangle is nCr = n! / (r! * (n-r)!)
nCr = int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

print(nCr)