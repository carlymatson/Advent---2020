inFile = open("day4input.text", 'r')

# We will be using regular expressions!
import re

def isValid(_ID):
    try:
        byr = int(_ID["byr"])
        iyr = int(_ID["iyr"])
        eyr = int(_ID["eyr"])
        hgt = _ID["hgt"]
        hcl = _ID["hcl"]
        ecl = _ID["ecl"]
        pid = _ID["pid"]
    except:
        print "Missing a required data field"
        return False
    if  (byr < 1920) or (byr > 2002):
        print "Invalid birth year: " + str(byr)
        return False
    if  (iyr < 2010) or (iyr > 2020):
        print "Invalid issue year: " + str(iyr)
        return False
    if  (eyr < 2020) or (eyr > 2030):
        print "Invalid expiration year: " + str(eyr)
        return False
    if re.match("[0-9]+(cm|in)$", hgt):
        hgtNum = int(hgt[:-2])
        if hgt[-2:] == "cm": 
            if (hgtNum < 150) or (hgtNum > 193):
                print "Invalid height: " + str(hgt)
                return False
        else:
            if (hgtNum < 59) or (hgtNum > 76):
                print "Invalid height: " + str(hgt)
                return False
    else:
        print "Invalid height format: " + str(hgt)
        return False
    if not re.match("#[0-f]{6}$", hcl):
        print "Invalid hair color: " + str(hcl)
        return False
    if not re.match("(amb|blu|brn|gry|grn|hzl|oth)$", ecl):
        print "Invalid eye color: " + str(ecl)
        return False
    if not re.match("[0-9]{9}$", pid):
        print "Invalid passport ID: " + str(pid)
        return False
    return True



# This will be used to put the data of each ID field into a list, which we will then parse into a dictionary.
fields = []
validCount = 0
endOfFile = False
while not endOfFile:
    s = inFile.readline()
    # A truly empty string is the end of the file.
    if s == "":
        endOfFile = True
    # We remove the newline character from the end of each string.
    s = s.strip()
    # Blank line - Create an ID (a dictionary) out of previous entries.
    if s == "":
        newID = {}
        for entry in fields:
            newID.update({entry.split(':')[0] : entry.split(':')[1]})
        # Check validity of this ID.
        if isValid(newID):
            validCount += 1
        # Start a new list of ID fields and repeat.
        fields = []
    # If the line isn't blank, split up the ID fields and add them to the running list.
    else:
        fields.extend(s.split(" "))

print validCount
