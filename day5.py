inFile = open("day5input.text", 'r')

seatList = inFile.readlines()

def getID(seat):
    row = 0
    col = 0
    for i in range(7):
        if seat[6-i] == 'B':
            row += 2**i
    for j in range(3):
        if seat[9-j] == 'R':
            col += 2**j
    id = 8*row + col
    return id


maxId = 0
idList = range(879)
for seat in seatList:
    id = getID(seat)
    #if id > maxId:
        #maxId = id
        #print "New max ID: " + str(id)
    idList.remove(id)

print idList
