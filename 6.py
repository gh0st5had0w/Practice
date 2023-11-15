# Finding the difference between the sum of squares and the square of the sum.

n = 1
number = int(input("What number do you want to stop at?: "))
squaredList = []
sumList = []

while n <= number:
	sumList.append(n)
	squaredList.append(n**2)
	n += 1

print(sum(squaredList))
print(sum(sumList)**2)
print("The sum of squares - sum^2 = ", sum(squaredList) - sum(sumList)**2)
print("Sum^2 - the sum of squares = ", sum(sumList)**2 - sum(squaredList))