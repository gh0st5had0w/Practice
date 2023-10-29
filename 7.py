numbersOfPrime = int(input("Which prime do you want to find?: "))
myList = [2]
n = 2

while len(myList) < numbersOfPrime:
	n += 1
	for a in range(2, n+1):
		print(a)
		tempValue = n%a
		if tempValue == 0 and a != n:
			break
		elif tempValue == 0 and a == n:
			myList.append(n)

#del myList [:-1]
print(myList)

# ============================================

# myList = [2]
# limit = int(input("What number do you want to go to?: "))

# def isPrime(n):
# 	for m in range(2, n):
# 		if n%m == 0:
# 			return False
# 	return True

# for n in range(3,limit):
# 	if isPrime(n) == True:
# 		myList.append(n)

# print(myList)
