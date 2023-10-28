# numbersOfPrime = int(input("Which prime do you want to find?: "))
# myList = [2, 3]
# listLength = len(myList)
# n = 2

# while listLength < numbersOfPrime:
# 	n += 1
# 	a = 2
# 	if a < n:
# 		tempValue = n%a
# 		if tempValue == 0 and a != n:
# 			break
# 		elif tempValue == 0 and a == n:
# 			myList.append(n)
# 			listLength = len(myList)
# 		else:
# 			a += 1

# del myList [:-1]
# print(myList)

# ============================================

# numberOfPrime = int(input("How many prime numbers do you want?: "))
# myList = []
# n = 2

# while len(myList) < numberOfPrime:
# 	for a in range(2, n, 1):
# 		myList.append(n)
# 		break
# 	n += 1

# print(myList)

# ============================================

# numbersOfPrime = int(input("Which prime do you want to find?: "))
# myList = [2]
# checkPrime = 3
# length = len(myList)

# while length < numbersOfPrime:
# 	i = 0
# 	while i < len(myList):
# 		primeInList = myList[i]
# 		if checkPrime%primeInList == 0 and primeInList != checkPrime:
# 			break
# 		elif checkPrime%primeInList == 0 and primeInList == checkPrime-1:
# 			myList.append(checkPrime)
# 		else:
# 			i += 1
# 	length = len(myList)

# #del myList [:-1]
# print(myList)

# ============================================

myList = [2]
limit = int(input("What number do you want to go to?: "))

def isPrime(n):
	for m in range(2, n):
		if n%m == 0:
			return False
	return True

for n in range(3,limit):
	if isPrime(n) == True:
		myList.append(n)

print(myList)