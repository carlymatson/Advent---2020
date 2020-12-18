inFile = open("day18input.text", 'r')
inLines = inFile.readlines()

import re

def eval2(_str):
    result = None
    oper = None
    ptr = 0
    while ptr < len(_str):
        # --- Cases --- #
        if oper == "*": # Use the rest of the string as the second operator.
            num = eval2(_str[ptr:])
            ptr = len(_str)
        elif re.match("\(", _str[ptr:]): # Found parentheses. Scan until close and evaluate.
            parenCount = 1
            start = ptr
            while parenCount > 0:
                ptr += 1
                if _str[ptr] == "(":
                    parenCount += 1
                if _str[ptr] == ")":
                    parenCount -= 1
            ptr += 1
            end = ptr
            num = eval2(_str[start+1:end-1])
        elif re.match("\d+", _str[ptr:]): # Found a number. Scan until end and parse.
            start = ptr
            while re.match("\d+", _str[ptr:]):
                ptr += 1
            end = ptr
            num = int(_str[start: end])
        elif re.match("\*|\+", _str[ptr:]): # Found an operator.
            oper = _str[ptr]
            ptr += 1
            continue
        elif re.match(" ", _str[ptr:]): # Ignore blank spaces.
            ptr += 1
            continue
        elif re.match("\n", _str[ptr:]): # End of string, return result.
            return result
        else:
            print "Well I didn't expect that. Funky string: " + _str[ptr:]
            break
        # --- What operation to perform, if any. --- #
        if result == None:
            result = num
        elif oper == "*":
            result = result * num
        elif oper == "+":
            result = result + num
        else:
            print "Something is off. Maybe the operator isn't defined."
    return result


total = 0
for exp in inLines:
    n = eval2(exp)
    #print exp.strip() + " = %d"%(n)
    total += n

print total
