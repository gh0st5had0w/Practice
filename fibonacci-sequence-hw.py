n = int(input("What number do you want to stop at?"))

myList = [0]
term0 = 0
term1 = 1
term2 = 1

while term2 in range(n):
	myList.append(term2)
	term2 = term0 + term1
	term0 = term1
	term1 = term2

print(myList)