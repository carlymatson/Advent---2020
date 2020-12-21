file = open("day18input.text", 'r')
file_lines = file.readlines()

import re

# This is necessary for finding and substituting, since regex treats "()+*" as special characters.
def get_literal(expression):
    expression = re.sub("\*", r"\*", expression)
    expression = re.sub("\+", r"\+", expression)
    expression = re.sub("\(", r"\(", expression)
    expression = re.sub("\)", r"\)", expression)
    return expression


def eval(expression):
    # If there are parentheses, resolve those first.
    while re.search(r"\([0-9+* ]*\)", expression):
        parenthetical = re.findall(r"\([0-9+* ]*\)", expression)[0]
        value = eval(parenthetical[1:-1])
        expression = re.sub(get_literal(parenthetical), str(value), expression)
    while re.search(r"\*", expression):
        # Split and evaluate each part, then return product.
        product_parts = expression.split("*")
        product = 1
        for p in product_parts:
            try:
                value = int(p)
            except:
                value = eval(p)
            product *= value
        return product
    # If there are no parentheses or multiplication, split and add.
    summands = expression.split("+")
    sum_ = 0
    for s in summands:
        try:
            value = int(s)
        except:
            print("Something went wrong")
            value = 0
        sum_ += value
    return sum_

# Main.
total = 0
for expression in file_lines[:2]:
    value = eval(expression)
    total += value
print(total)
