# Finding the sum of the digits of 2^1000

# It's surprisingly quick for computers to do calculations like this :p
a = str(2 ** 1000)
# Splitting the digits in 2^1000 into single digits and putting them into a list
numberList = [int(i) for i in a]

print(sum(numberList))