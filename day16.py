inFile = open("day16input.text", 'r')
inLines = inFile.readlines()

import re

validNums = set()
validFor = dict()
fields = set()

# Parse ticket fields and their valid ranges.
l = inLines.pop(0).strip()
while l != "":
    #print l
    field_ranges = l.split(':')
    field = field_ranges[0].strip()
    fields.add(field)
    ranges = (field_ranges[1]).split(" or ")
    validSet = set()
    for interval in ranges:
        start_end = interval.split('-')
        start = int(start_end[0])
        end = int(start_end[1])
        validSet = validSet.union(range(start, end+1))
    validFor[field] = validSet
    validNums = validNums.union(validSet)
    l = inLines.pop(0).strip()

def invalidSum(_nums):
    invalidSum = 0
    for n in _nums:
        if n not in validNums:
            invalidSum += n
    return invalidSum

# Parse my ticket
while not re.match("your ticket:", l):
    l = inLines.pop(0)
l = inLines.pop(0)
myTicket = [int(n) for n in l.split(',')]
nFields = len(myTicket)
indexOf = {}

# Start by assuming that any number in the list could be any field.
posFields = [set(fields) for j in range(nFields)]

# This function will "cross off" possibilities.
def crossOff(_ind, _fld):
    if _fld in posFields[_ind]:
        if len(posFields[_ind]) == 1:
            print "Something is wrong: I shouldn't be removing the last option."
            return False
        posFields[_ind].remove(_fld)
        if len(posFields[_ind]) == 1:
            _onlyFld = list(posFields[_ind])[0]
            indexOf[_onlyFld] = _ind
            for _j in range(nFields):
                if _j != _ind:
                    crossOff(_j, _onlyFld)
        return True
    return False

# Parse other tickets
while not re.match("nearby tickets:", l):
    l = inLines.pop(0)
l = inLines.pop(0).strip()

count = 0
while True:
    nums = [int(n) for n in l.split(',')]
    if invalidSum(nums) != 0:
        l = inLines.pop(0).strip()
        continue
    for i in range(nFields):
        n = nums[i]
        couldBe = list(posFields[i])
        for fld in couldBe:
            if n not in validFor[fld]:
                #print l.strip() + " --> " + str(n) + " not valid for \"" + fld + "\""
                crossOff(i, fld)
    try:
        l = inLines.pop(0).strip()
    except:
        break


print indexOf

prod = 1
for fld in list(fields):
    if re.match("departure", fld):
        prod *= myTicket[indexOf[fld]]

print "Product: %d"%(prod)

#print posFields
