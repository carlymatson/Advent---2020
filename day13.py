inFile = open("day13input.text", 'r')

lines = inFile.readlines()

minTime = int(lines[0])

minWait = -1

ID = 0

busIDsRaw = lines[1].split(',')
busIDs = list()
for idx in busIDsRaw:
    if idx == "x":
        continue
    else:
        mins = int(idx)
        busIDs.append(mins)
    timeTil = mins - (minTime % mins)
    if (minWait < 0) or (timeTil < minWait):
        minWait = timeTil
        ID = mins

print "--- Part 1 ---"
print busIDs
print minWait*ID
print "--- Part 2 ---"

modulus = 1
n = 0

prod = 1
for id in busIDs:
    prod *= id
print prod

for i in range(0, len(busIDsRaw)):
    idx = busIDsRaw[i]
    if idx == "x":
        continue
    else:
        id = int(idx)
        while (n+i) % id != 0:
            n += modulus
        print "n: " + str(n)
        print "n mod %d = %d"%(id, n % id)
        modulus *= id

print n
