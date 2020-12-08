inFile = open("day7input.text", 'r')

import re

# I wonder what it will be!

ruleList = inFile.readlines()
contentsOf = dict()
parentBags = dict()

exceptionCounter = 0

for rule in ruleList:
    pair = rule.split("s contain ")
    thisPattern = pair[0]
    contentsList = pair[1].split(',')
    contentsOfBag = dict()
    for item in contentsList:
        item = item.strip('. \n')
        patObj = re.search('\D+', item)
        pat = ((patObj.group()).strip()).rstrip('s')
        try:
            numObj = re.search('\d+', item)
            num = int(numObj.group())
            contentsOfBag[pat] = num
        except:
            exceptionCounter += 1
        if not parentBags.has_key(pat):
            parentBags[pat] = set()
        parentBags[pat].add(thisPattern)
    contentsOf[thisPattern] = contentsOfBag

#shinyHolders = parentBags['shiny gold bag']
#frontier = list()
#frontier = list(shinyHolders)
#while len(frontier) > 0:
#    bag = frontier.pop()
#    if not parentBags.has_key(bag):
#        continue
#    ancestors = parentBags[bag]
#    for oldy in ancestors:
#        if oldy not in shinyHolders:
#            shinyHolders.add(oldy)
#            frontier.append(oldy)
#print(len(shinyHolders))

def bagCount(_pattern): # Let's use recursion.
    contents = contentsOf[_pattern]
    numBags = 1
    if len(contents) == 0:
        "Recursion bottomed out"
        return numBags
    for subBag in contents.keys():
        numBags += contents[subBag]*bagCount(subBag)
    "Number of bags in " + str(_pattern) + ": " + str(numBags)
    return numBags

print bagCount('shiny gold bag')-1
