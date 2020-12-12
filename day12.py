inFile = open("day12input.text", 'r')
codes = inFile.readlines()


posX = 0
posY = 0
wayX = 10
wayY = 1
#facing = 1

for co in codes:
    cha = co[0]
    num = int(co[1:])
    NESWvecs = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
    NESWlist = ['N', 'E', 'S', 'W']
    #v = NESWvecs[NESWlist[facing]]
    if cha in NESWlist:
        v = NESWvecs[cha]
        wayX += v[0]*num
        wayY += v[1]*num
    elif cha=='R' or cha == 'L':
        if cha=='R':
            ang = num/90
        else:
            ang = -num/90
        newN = NESWvecs[NESWlist[ang % 4]]
        newE = NESWvecs[NESWlist[(ang+1)%4]]
        newWayX = wayX*newE[0]+wayY*newN[0]
        newWayY = wayX*newE[1] + wayY*newN[1]
        wayX = newWayX
        wayY = newWayY
        #facing = (facing + ang) % 4
    elif cha == 'F':
        posX += wayX*num
        posY += wayY*num
    else:
        print "Invalid code"
    print "Code: " + str(cha) + str(num)
    print("Pos: (%d, %d)"%(posX, posY))
    print("Way: (%d, %d)"%(wayX, wayY))


manhattan = abs(posX) + abs(posY)
print manhattan
