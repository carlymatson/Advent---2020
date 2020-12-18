inFile = open("day17input.text", 'r')

import operator

gridList = inFile.readlines()

dim = 4 # Must be an integer greater than or equal to 2. Printing only works for dim=2,3,4.
mins = [0]*dim
maxs = [len(gridList), len(gridList[0].strip())] + [0]*(dim-2)

# Returns a list of tuples representing the points of the grid.
def getGrid(_mins, _maxs):
    tupList = [[]]
    for d in range(dim):
        dTupList = []
        for x in range(_mins[d], _maxs[d]+1):
            tupListX = [tup + [x] for tup in tupList]
            dTupList.extend(tupListX)
        tupList = dTupList
    return [tuple(tup) for tup in tupList]

# Counts the active cubes adjacent to this one, excluding itself.
def countActive(_cube):
    count = 0
    for delt in deltas:
        if delt == tuple([0]*dim):
            continue
        p = tuple(map(operator.add, _cube, delt))
        if p in active:
            count += 1
    return count

# Increases the size of the grid if needed.
def expandBounds(_cube):
    for index in range(dim):
        if (_cube[index] < mins[index]):
            mins[index] = _cube[index]
        if (_cube[index] > maxs[index]):
            maxs[index] = _cube[index]
    grid = getGrid(mins, maxs)
    return True

def printGrid(): # This print function only works for dimensions 2, 3, and 4.
    paneList = getGrid([0]*2+mins[2:], [0]*2+maxs[2:])
    for pane in paneList:
        if dim == 2:
            print "---"
        elif dim == 3:
            print "--- z = %d ---"%(pane[2])
        elif dim == 4:
            print "--- z=%d, w=%d ---"%(pane[2],pane[3])
        for x in range(mins[0], maxs[0]+1):
            charList = []
            for y in range(mins[1], maxs[1]+1):
                cube = tuple([x,y]+list(pane[2:]))
                if cube in active:
                    charList.append('#')
                else:
                    charList.append('.')

            row = "".join(charList)
            print row




## --------------- Main --------------- ##


grid = getGrid(mins, maxs)
deltas = getGrid([-1]*dim, [1]*dim)

active = set()
for i in range(maxs[0]):
    s = gridList[i].strip()
    for j in range(maxs[1]):
        if s[j] == '#':
            p = tuple([i,j]+[0]*(dim-2))
            active.add(p)

time = 0
print "---------------- Cycle %d -----------------"%(time)
printGrid()
while time < 3:
    nowActive = set(active)
    for thisCube in getGrid([m-1 for m in mins], [M+1 for M in maxs]):
        num = countActive(thisCube)
        if (thisCube in active) and (num != 2 and num != 3):
            nowActive.remove(thisCube)
        elif (thisCube not in active) and (num == 3):
            nowActive.add(thisCube)
            expandBounds(thisCube)
        else:
            continue
    active = set(nowActive)
    time += 1
    print "---------------- Cycle %d -----------------"%(time)
    printGrid()


print "Number of active cubes: %d"%(len(active))
