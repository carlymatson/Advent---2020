inFile = open("day6input.text", 'r')

formList = inFile.readlines()

sum = 0
yesSet = set()
firstForm = True

for form in formList:
    form = form.strip()
    if form == "":
        sum += len(yesSet)
        #print "Set intersection: " + str(yesSet)
        #print "Sum: " + str(sum)
        yesSet = set()
        firstForm = True
    else:
        #print "Form: " + str(set(form))
        if firstForm:
            yesSet = set(form)
            firstForm = False
        else:
            yesSet = yesSet.intersection(set(form))
#print "Set intersection: " + str(yesSet)
sum += len(yesSet)
print "Total: " + str(sum)
