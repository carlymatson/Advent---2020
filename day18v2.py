inFile = open("day18input.text", 'r')
inLines = inFile.readlines()

import re

# This is necessary for finding and substituting, since regex treats "()+*" as special characters.
def getLiteral(_str):
    _str = re.sub("\*", r"\*", _str)
    _str = re.sub("\+", r"\+", _str)
    _str = re.sub("\(", r"\(", _str)
    _str = re.sub("\)", r"\)", _str)
    return _str


def eval(_str):
    # If there are parentheses, resolve those first.
    while re.search(r"\([0-9+* ]*\)", _str):
        parenBlock = re.findall(r"\([0-9+* ]*\)", _str)[0]
        val = eval(parenBlock[1:-1])
        _str = re.sub(getLiteral(parenBlock), str(val), _str)
    while re.search(r"\*", _str):
        # Split and evaluate each part, then return product.
        prodParts = _str.split("*")
        prod = 1
        for s in prodParts:
            try:
                val = int(s)
            except:
                val = eval(s)
            prod *= val
        return prod
    # If there are no parentheses or multiplication, split and add.
    summands = _str.split("+")
    sum = 0
    for s in summands:
        try:
            val = int(s)
        except:
            print "Something went wrong"
            val = 0
        sum += val
    return sum

# Evaluate each expression and add them all up.
total = 0
for exp in inLines:
    n = eval(exp)
    total += n

print total
