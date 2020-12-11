inFile = open("day11input.text", 'r')

inList = inFile.readlines()

grid = [list(_str) for _str in inList]


nRows = len(grid)
nCols = len(grid[0])


def occupiedCount(_seats, _i, _j):
    count = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    for v in dirs:
        _ch = '.'
        y = _i
        x = _j
        while _ch == '.':
            y += v[0]
            x += v[1]
            if (x < 0) or (x >= nCols) or (y < 0) or (y >= nRows):
                _ch = '?'
                break
            else:
                _ch = _seats[y][x]
            if _ch == '#':
                count += 1
                break
            if _ch == 'L':
                break
    return count

def totalOcc(_str):
    count = 0
    for ch in _str:
        if ch == '#':
            count += 1
    return count

def toString(_seats):
    concat = ""
    for row in _seats:
        concat += "".join(row)
    return concat


timer = 0
seats = grid

while True:
    newSeats = [[s for s in row] for row in seats]
    for i in range(nRows):
        for j in range(nCols):
            numOccupied = occupiedCount(seats,i,j)
            if (seats[i][j] == '#') and (numOccupied >= 5):
                newSeats[i][j] = 'L'
            elif (seats[i][j] == 'L') and (numOccupied == 0):
                newSeats[i][j] = '#'
    newSeatString = toString(newSeats)
    #print "New seats: \n" + newSeatString
    if toString(seats) == newSeatString:
        #print "We are done!"
        break
    seats = newSeats
    timer += 1


print "Count: " + str(totalOcc(toString(newSeats)))
