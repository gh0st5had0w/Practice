# Checking for the largest product of a set of consequetive numbers in a larger number 

import math

answer = 0

# Splitting the large number into a list
number = str(input("Which number do you want to check? "))
numberList = [int(i) for i in number]

# Finding the product of 13 consequetive numbers and outputting the largest product
for n in range(len(numberList) - 12):
	tempSum = math.prod(numberList[0 + n:13 + n])
	if tempSum > answer:
		answer = tempSum

print(answer)