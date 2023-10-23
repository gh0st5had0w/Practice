n = int(input("What number do you want to stop at?"))

myList = [0]
term0 = 0
term1 = 1
term2 = 1

while term2 <= n:
	if term2%2 ==0:
		myList.append(term2)
		term2 = term0 + term1
		term0 = term1
		term1 = term2
	else:
		term2 = term0 + term1
		term0 = term1
		term1 = term2

print(myList)
print(sum(myList))