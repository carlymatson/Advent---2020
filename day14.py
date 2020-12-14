inFile = open("day14input.text", 'r')
inLines = inFile.readlines()

import re


def toBin(n):
    bits = [int( (n % 2**(36-i)) / 2**(35-i) ) for i in range(36)]
    return bits

def toInt(_bin):
    total = 0
    for i in range(36):
        total += _bin[i]*(2**(35-i))
    return total

def mask1(_val, _mask):
    _binary = toBin(_val)
    for j in range(36):
        if _mask[j] == 'X':
            continue
        elif _mask[j] == '0':
            _binary[j] = 0
        elif _mask[j] == '1':
            _binary[j] = 1
        else:
            print "Something went wrong with the mask."
    _newVal = toInt(_binary)
    return _newVal

def mask2(_val, _mask):
    _binary = toBin(_val)
    memList = list()
    floatInds = list()
    for j in range(36):
        if _mask[j] == '0':
            continue
        elif _mask[j] == '1':
            _binary[j] = 1
        elif _mask[j] == 'X':
            _binary[j] = 0
            floatInds.append(j)
        else:
            print "Something went wrong with the mask."
    baseN = toInt(_binary)
    memList.append(baseN)
    for ind in floatInds:
        memList2 = [n + 2**(35-ind) for n in memList]
        memList.extend(memList2)
    return memList


mask = ""
mem = dict()

for i in range(0, len(inLines)):
    s = inLines[i].strip()
    if re.match("mask", s):
        mask = s[7:]
    else:
        digits = re.findall("[0-9]+", s)
        index = int(digits[0])
        val = int(digits[1])
        #newVal = mask1(val, mask)
        indexList = mask2(index, mask)
        for ind in indexList:
            mem[ind] = val

total = 0
for key in mem.keys():
    total += mem[key]

print "Total: " + str(total)
