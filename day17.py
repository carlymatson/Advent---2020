inFile = open("day17input.text", 'r')

# I've rotated the grid so that the array numbering coincides with the x and y axes.
grid = inFile.readlines()
xyzMins = [0,0,0]
xyzMaxs = [len(grid), len(grid[0].strip()), 0]

# Add starting cubes to the active list.
active = set()
for i in range(xyzMaxs[0]):
    s = grid[i].strip()
    for j in range(xyzMaxs[1]):
        if s[j] == '#':
            p = tuple([i,j,0])
            active.add(p)

def countActive(_xyz):
    count = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            for dz in range(-1,2):
                dxyz = [dx, dy, dz]
                p = tuple([_xyz[i]+dxyz[i] for i in range(3)])
                if p in active and (dx!=0 or dy!=0 or dz!=0):
                    count += 1
    return count

def expandBounds(_xyz):
    for index in range(3):
        if (_xyz[index] < xyzMins[index]):
            xyzMins[index] = _xyz[index]
        if (_xyz[index] > xyzMaxs[index]):
            xyzMaxs[index] = _xyz[index]
    return True

def printGrid():
    print "----------------"
    for z in range(xyzMins[2], xyzMaxs[2]+1):
        print "--- z = %d ---"%(z)
        for x in range(xyzMins[0], xyzMaxs[0]+1):
            charList = []
            for y in range(xyzMins[1], xyzMaxs[1]+1):
                cube = tuple([x,y,z])
                if cube in active:
                    charList.append('#')
                else:
                    charList.append('.')
            row = "".join(charList)
            print row

time = 0
while time < 6:
    nowActive = set(active)
    for x in range(xyzMins[0]-1, xyzMaxs[0] + 2):
        for y in range(xyzMins[1]-1, xyzMaxs[1] + 2):
            for z in range(xyzMins[2]-1, xyzMaxs[2] + 2):
                thisCube = tuple([x,y,z])
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
    printGrid()
    time += 1

#print active

cube = tuple([1,1,1])
print countActive(cube)

print len(active)

print sorted(active, key=lambda cube: cube[2])
