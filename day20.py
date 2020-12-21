inFile = open("day20input2.text", 'r')
inLines = inFile.readlines()

import time
startClock = time.time()

# Parse tiles into dictionary.
idList = []
picture = []
N = 0
tileDict = {}
endOfFile =  False
while not endOfFile:
    l = inLines.pop(0).strip()
    tileID = int(l[5:9])
    l = inLines.pop(0).strip()
    N = len(l)
    tile = []
    while l != "":
        tile.append(l)
        try:
            l = inLines.pop(0).strip()
        except:
            endOfFile = True
            break
    tileDict[tileID] = tile
    idList.append(tileID)

### --- Functions for Part 2 --- ###

# Rotate a tile or picture counterclockwise by 90 degrees.
def rotate(_tile):
    L = len(_tile)
    # Make the picture rectangular by adding z's to shorter rows.
    W = 0
    for row in _tile:
        if len(row) > W:
            W = len(row)
    zFill = [row + "z"*(W - len(row)) for row in _tile]
    newTile = ["".join([_tile[j][W-1-i] for j in range(L)]) for i in range(W)]
    newTile = [row.rstrip('z') for row in newTile] # Trim z's from the right.
    return newTile

# Flip a tile or picture along the i=j diagonal.
def flip(_tile):
    L = len(_tile)
    W = len(_tile[0])
    newTile = ["".join([_tile[j][i] for j in range(L)]) for i in range(W)]
    return newTile

# Display a tile or the full picture.
def printPic(_tile):
    print "-"*20
    for row in _tile:
        print row
    return True

# See if the tile with given ID can be added to any of the rightmost edges.
def tryToMatch(_id):
    _tile = tileDict[_id]
    # Get string version of (one of) the right-most edge(s).
    for y in range(len(picture)/N):
        W = len(picture[y*N]) # Rows of tiles may be uneven lengths.
        rEdge = "".join([picture[y*N + j][W-1] for j in range(N)])
        # Begin checking sides of the tile for a match.
        flips = 0
        while flips < 2:
            for turn in range(4):
                lEdge = "".join(_tile[j][0] for j in range(N))
                if rEdge == lEdge:
                    # Add this tile on the right.
                    for j in range(N):
                        picture[y*N + j] = picture[y*N + j] + _tile[j]
                    # Remove this tile from the list of available tiles.
                    looseTiles.remove(_id)
                    return True
                _tile = rotate(_tile)
            _tile = flip(_tile)
            flips += 1
    return False



### --- Part 1 --- ###
# I got the corner IDs by counting which tiles had only 2 edges with matches.
# This assembles the picture, but doesn't save the IDs.

tile1 = tileDict[idList[0]]
picture = list(tile1)
looseTiles = list(idList) # The IDs of tiles that have not been attached to the picture.
looseTiles.remove(idList[0])

while len(looseTiles) > 0:
    foundMatch = False
    for id in looseTiles:
        if tryToMatch(id):
            printPic(picture)
            foundMatch = True
            break
    if not foundMatch:
        picture = rotate(picture)

### --- Functions for Part 2 --- ###

# Get rid of tile borders in final picture.
def trim(_pic):
    newPic = []
    # Get rid of rows 0 and N-1 (mod N).
    for i in range(len(_pic)/N):
        newPic.extend(_pic[N*i+1: N*i+N-1])
    # Get rid of columns  0 and N-1 (mod N).
    for i in range(len(newPic)):
        row = newPic[i]
        W = len(row)
        newRow = ""
        for j in range(W/N):
            newRow += row[N*j+1: N*j+N-1] # Splice up the list and skip columns.
        newPic[i] = newRow
    return newPic

# Get coordinates of all pixels that equal '#'.
def getPoundXYs(_mon):
    xyTuples = []
    for i in range(len(_mon)):
        row = _mon[i]
        for j in range(len(row)):
            if _mon[i][j] == '#':
                xyTuples.append((i,j))
    return xyTuples

# Return set of coordinates (if any) that are part of a monster based at (i,j).
def isMonster(_i, _j):
    global picture
    monSet = set()
    checks = [picture[_i + tup[0]][_j+tup[1]] == '#' for tup in monsterCoords]
    if all(checks):
        monSet = set([(_i + tup[0], _j + tup[1]) for tup in monsterCoords])
    return monSet

# Go through entire picture, possibly flipping and rotating, and look for monsters.
def scanForMonsters():
    global picture
    global monster
    picL = len(picture)
    picW = len(picture[0])
    monL = len(monster)
    monW = len(monster[0])
    xySet = set()
    flips = 0
    while flips < 2:
        for turn in range(4):
            for i in range(picL + 1 - 3): # Be careful, these dimensions were entered manually.
                for j in range(picW + 1 - 20):
                    xySet = xySet.union(isMonster(i,j))
            if len(xySet) > 0:
                return xySet
            print "Looking for monsters: Rotated the picture"
            picture = rotate(picture)
        print "Looking for monsters: Flipped the picture"
        picture = flip(picture)
        flips += 1
    return xySet # If there are monsters, this line should never end up being called.


### --- Part 2 --- ###

### Trim the borders from the tiles in the picture.
picture = trim(picture)
print "Trimmed borders from picture."

### Read in the sea monster from a text file.
inMonster = open("day20seamonster.text", 'r') # This didn't copy and paste correctly due to the spaces.
monsterList = inMonster.readlines()
monster = [row.rstrip('\n') for row in monsterList] # Do not strip spaces.
monsterCoords = getPoundXYs(monster) # Find relative positions of monster parts.
monXYs = scanForMonsters() # Find all locations that have sea monsters.

count = len(set(getPoundXYs(picture)) - monXYs)

print "Number of #-tiles not in a sea monster: %d"%(count)

endClock = time.time()
print "Time to run: %d seconds"%(endClock - startClock)
