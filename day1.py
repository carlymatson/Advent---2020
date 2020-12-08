# 'r' indicates that this is a 'read only' file
inFile = open("day1input.text", 'r')
# int() attempts to convert (or "cast") the string into an integer
numList = [int(numString) for numString in inFile.readlines()]

numList.sort()

product = 0
N = len(numList)
for i in range(N):
    if product != 0: # If the product value has been set, stop looping.
        break
    for j in range(i, N):
        if product != 0:
            break
        difference = 2020 - numList[i] - numList[j]
        if difference in numList: # Check list membership
            product = numList[i]*numList[j]*difference
            print numList[i], numList[j], difference
            print product
