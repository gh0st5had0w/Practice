# Finding the number under a million that produces the longest collatz sequence

longestLength = 0
journey = []

for n in range(2, 1000000):
    while n > 1:
        if n % 2 == 0:
            journey.append(n)
            n = int(n / 2)
        else:
            journey.append(n)
            n = 3 * n + 1
    journey.append(1)
    if len(journey) > longestLength:
        longestLength = len(journey)
        print(longestLength)
        print(journey[0])
    journey = []