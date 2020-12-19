inFile = open("day19input.text", 'r')
inLines = inFile.readlines()

import re


l = inLines.pop(0).strip()
ruleDict = {}
time = 0

# Parse rules into dictionary.
while l != "":
    index_rule = l.split(':')
    indexStr = index_rule[0]
    index = int(indexStr)
    rule = index_rule[1] + " "
    # Place "or" statments in a non-capturing group
    if re.search("\|", rule):
        rule = "(?:" + rule + ")"
    # If a rule references itself, sub back in a few times.
    if re.search(indexStr, rule):
        depth = 0
        while depth < 5: # I chose 5 somewhat randomly, but it was enough.
            rule = re.sub(" " + indexStr + " ", " " + rule + " ", rule)
            depth += 1
        rule = re.sub(" " + indexStr + " ", " ", rule)
    # Put it in the dictionary
    ruleDict[index] = rule
    time += 1
    try:
        l = inLines.pop(0).strip()
    except:
        print "No more lines to pop. Shouldn't happen."
        break

rule0 = ruleDict[0]

# Repeeatedly substitute into rule 0.
while re.search("\d+", rule0):
    numList = re.findall("\d+", rule0)
    n = numList[0]
    ruleN = ruleDict[int(n)]
    rule0 = re.sub(" " + n + " ", " " + ruleN + " ", rule0)
    # Remove extra spaces and quotation marks for the sake of length and readability.
    rule0 = re.sub("  ", " ", rule0)
    rule0 = re.sub("\"", "", rule0)
    time += 1
    if time > 1000000: # Kill switch on infinite loops.
        print "Ya looped"
        break

rule0 = re.sub("\"| ", "", rule0) #Get rid of all spaces and quotes.

l = inLines.pop(0).strip()
matchCount = 0
while l != "":
    if re.match("(" + rule0 + ")$", l):
        print "Match: " + l
        matchCount += 1
    try:
        l = inLines.pop(0).strip()
    except:
        break
print matchCount
