# projecteuler.net/archives

#myList = []

#for number in range(1000):
#	if number%3 == 0 or number%5 == 0:
#		myList.append(number)

#print(sum(myList))




def multiplesOf3Or5(n):
	myList = []
	for number in range(n):
		if number%3 == 0 or number%5 == 0:
			myList.append(number)
	return(sum(myList))

N = [1000]

for n in N:
	print(multiplesOf3Or5(n))