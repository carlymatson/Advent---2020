inFile = open("day7input.text", 'r')

import re

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
        patObj = re.search('\D+', item) # Create a "match object" and get the string of the bag patternon the next line.
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

# ----------Part One-----------
#shinyHolders = parentBags['shiny gold bag']
#frontier = list()
#frontier = list(shinyHolders)
#while len(frontier) > 0:
#    bag = frontier.pop()
#    if not parentBags.has_key(bag): # If this can't be contained in any bags, just go to the next one.
#        continue
#    ancestors = parentBags[bag] # What are the bags that can hold the holder? 
#    for oldy in ancestors:
#        if oldy not in shinyHolders: 
#            shinyHolders.add(oldy)
#            frontier.append(oldy)
#print(len(shinyHolders))

# ----------Part Two----------

def bagCount(_pattern): # Let's use recursion.
    contents = contentsOf[_pattern]
    numBags = 1
    if len(contents) == 0: # If this bag can't hold anything, just return the number one (for itself).
        return numBags
    for subBag in contents.keys(): # This function calls itself to determine how many bags are inside the inner bags.
        numBags += contents[subBag]*bagCount(subBag) # (How many of this pattern)*(Number of bags inside this pattern)
    return numBags

print bagCount('shiny gold bag')-1 # Subtract one, since we don't want to count the shiny bag itself.
