startingNums = [0,3,1,6,7,5]

turn = 0
lastSaid = {}
while turn < len(startingNums)-1:
    turn += 1
    print "Turn %d: %d"%(turn, startingNums[turn - 1])
    lastSaid[startingNums[turn - 1]] = turn

turn += 1
print "Turn %d: %d"%(turn, startingNums[turn - 1])
prev = startingNums[-1]


while turn < 30000000:
    if prev in lastSaid:
        age = turn - lastSaid[prev]
    else:
        age = 0
    lastSaid[prev] = turn
    # New turn
    turn += 1
    if turn % 1000000 == 0:
        print "Turn %d: %d"%(turn, age)
    prev = age

print "Turn %d: %d"%(turn, age)
