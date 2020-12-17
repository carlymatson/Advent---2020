inFile = open("day17input.text", 'r')

# I've rotated the grid so that the array numbering coincides with the x and y axes.
grid = inFile.readlines()
xyzwMins = [0,0,0,0]
xyzwMaxs = [len(grid), len(grid[0].strip()), 0, 0]

# Add starting cubes to the active list.
active = set()
for i in range(xyzwMaxs[0]):
    s = grid[i].strip()
    for j in range(xyzwMaxs[1]):
        if s[j] == '#':
            p = tuple([i,j,0, 0])
            active.add(p)

def countActive(_xyzw):
    count = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            for dz in range(-1,2):
                for dw in range(-1,2):
                    dxyzw = [dx, dy, dz, dw]
                    p = tuple([_xyzw[i]+dxyzw[i] for i in range(4)])
                    if p in active and (dx!=0 or dy!=0 or dz!=0 or dw!=0):
                        count += 1
    return count

def expandBounds(_xyzw):
    for index in range(4):
        if (_xyzw[index] < xyzwMins[index]):
            xyzwMins[index] = _xyzw[index]
        if (_xyzw[index] > xyzwMaxs[index]):
            xyzwMaxs[index] = _xyzw[index]
    return True

def printGrid():
    print "----------------"
    for w in range(xyzwMins[3], xyzwMins[3]+1):
        for z in range(xyzwMins[2], xyzwMaxs[2]+1):
            print "--- z = %d, w = %d ---"%(z, w)
            for x in range(xyzwMins[0], xyzwMaxs[0]+1):
                charList = []
                for y in range(xyzwMins[1], xyzwMaxs[1]+1):
                    cube = tuple([x,y,z, w])
                    if cube in active:
                        charList.append('#')
                    else:
                        charList.append('.')
                row = "".join(charList)
                print row
    return True

time = 0
while time < 6:
    nowActive = set(active)
    for x in range(xyzwMins[0]-1, xyzwMaxs[0] + 2):
        for y in range(xyzwMins[1]-1, xyzwMaxs[1] + 2):
            for z in range(xyzwMins[2]-1, xyzwMaxs[2] + 2):
                for w in range(xyzwMins[3]-1, xyzwMaxs[2]+2):
                    thisCube = tuple([x,y,z,w])
                    num = countActive(thisCube)
                    #print "This cube: " + str(thisCube) + ", " + str(num)
                    if (thisCube in active) and (num != 2 and num != 3):
                        #print "Become inactive"
                        nowActive.remove(thisCube)
                    elif (thisCube not in active) and (num == 3):
                        #print "Become active!"
                        nowActive.add(thisCube) #Gotta expand bounds.
                        expandBounds(thisCube)
                        #print "New bounds?: " + str(xyzMins) + ", " + str(xyzMaxs)
                    else:
                        #print "Do nothing"
                        continue
    active = set(nowActive)
    #printGrid()
    time += 1


print len(active)

#print sorted(active, key=lambda cube: cube[2])
