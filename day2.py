inFile = open("day2input.text", 'r')


inputLines = inFile.readlines()

validCount = 0

for _str in inputLines:
    _str_pair = _str.split(':')
    _rule_pair = _str_pair[0].split(' ')
    _min_max = [int(num) for num in _rule_pair[0].split('-')]
    _character = _rule_pair[1]
    _password = _str_pair[1].strip()
    #print _min_max
    #print _character
    #print _password
    charCount = 0
    #for i in range(len(_password)):
    #    if _password[i] == _character:
    #        charCount += 1
    if _password[_min_max[0]-1] == _character:
        charCount += 1
    if _password[_min_max[1]-1] == _character:
        charCount += 1
    #print charCount
    #if (charCount >= _min_max[0]) and (charCount <= _min_max[1]):
    if charCount % 2 == 1:
        validCount += 1
        #print "It's valid"

print "Valid count: " + str(validCount)
