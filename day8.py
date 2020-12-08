inFile = open("day8input.text", 'r')

def run(_code):
    accumulator = 0
    seen = set()
    pointer = 0
    looping = False
    while not looping:
        # Determine whether the program has finished running.
        if pointer >= len(_code):
            print "Terminated correctly"
            return True, accumulator
        if pointer in seen:
            #print "Looping"
            return False, accumulator
        seen.add(pointer)
        # Compute next operation.
        instr = _code[pointer]
        pair = instr.split(" ")
        oper = pair[0]
        val = int(pair[1])
        if oper == "nop":
            pointer += 1
        elif oper == "acc":
            accumulator += val
            pointer += 1
        elif oper == "jmp":
            pointer += val
        else:
            print "Oh no! Invalid operation:" + str(oper)

instructionOriginal = inFile.readlines()
accumulatorFinal = 0

for i in range(len(instructionOriginal)):
    codeCopy = list(instructionOriginal)
    changed = False
    inst = instructionOriginal[i]
    if inst.split(" ")[0] == "nop":
        codeCopy[i] = "jmp" + str(" ") + inst.split(" ")[1]
        changed = True
    elif inst.split(" ")[0] == "jmp":
        codeCopy[i] = "nop" + str(" ") + inst.split(" ")[1]
        changed = True
    if changed:
        m = run(codeCopy)
        if m[0]: # If it terminated correctly, this should be True.
            accumulatorFinal = m[1]
            break
    else:
        continue

print "Accumulator: " + str(accumulatorFinal)
