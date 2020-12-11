inFile = open("day9input.text", 'r')

_numList = inFile.readlines()
numList = [int(n) for n in _numList]

N = 25

def getSums(_list):
    sumSet = set()
    for i in range(N):
        for j in range(i, N):
            sumSet.add(_list[i]+_list[j])
    return sumSet

prevN = numList[:N]

#index = N
#while N < len(numList):
#    prevN = numList[index-N:index]
#    #print "Previous N terms: " + str(prevN)
#    sums = getSums(prevN)
#    if numList[index] not in sums:
#        print "Index: " + str(index)
#        print "Invalid number: " + str(numList[index])
#        break
#    index += 1

index = 0
targetSum = 105950735
while index < len(numList):
    contgSum = 0
    j = 0
    while (contgSum < targetSum) and (index + j < len(numList)):
        contgSum += numList[index + j]
        if (contgSum == targetSum) and (j > 0):
            print "Index and number of terms: " + str(index) + ", " + str(j+1)
            print min(numList[index:index+j+1]), max(numList[index:index+j+1])
            print min(numList[index:index+j+1]) + max(numList[index:index + j+1])
            break
        j += 1
    index += 1
