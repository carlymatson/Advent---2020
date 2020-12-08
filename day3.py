inFile = open("day3input.text", 'r')

_grid = inFile.readlines()
_length = len(_grid)
_width = len(_grid[0]) - 1

print "Width: " + str(_width)

vecList = [(1,1), (1,3), (1,5), (1,7), (2,1)]



_product = 1
for vec in vecList:
    _row = 0
    _col = 0
    treeCount = 0
    while _row < _length:
        #print _row, _col
        if _grid[_row][(_col) % _width] == '#':
            treeCount += 1
            #print "Hit a tree"
        _row += vec[0]
        _col = (_col + vec[1]) % _width
    print treeCount
    _product = _product * treeCount

print "Product: " + str(_product)
