# Finding the largest palindrome from the product of two three-digit numbers.
# Needs changing & notation

# [::-1] is a slice with segments start, end, step. This effectively displays the function backwards.
def palindrome(number):
	strNumber = str(number)
	return(strNumber == strNumber[::-1])

myList = []

for n in range(999, 100, -1):
	for m in range(999, 100, -1):
		product = n * m
		if palindrome(product) == True:
			myList.append(product)

# List comprehensions help to filter out any unwanted terms from the list of factors.
# https://note.nkmk.me/en/python-list-clear-pop-remove-del/#remove-an-item-by-value-remove
# alteredList = [i for i in myList if i < 1000]
# del alteredList [:-2]

# Sorted function puts the numbers in order of their size
print(sorted(myList))

# -=-=-=-=-=-=-=-=-=-=-  =====   *   =====  -=-=-=-=-=-=-=-=-=-=- #

# yourInput = int(input("Test a number under 1000: "))
# myList = []

# for a in range (999, 0, -1):
# 	number = yourInput * a

#	strNumber = str(number)
#	numberInverse = strNumber[::-1]

#	if strNumber == numberInverse:
#		for n in range(1, number):
#			number%n == 0
#			myList.append(n)

#alteredList = [i for i in myList if i < 1000]
#del alteredList [:-2]

# print(a)
# print(number)
#print(alteredList)