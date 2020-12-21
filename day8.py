inFile = open("day8input.text", 'r')

def run(code):
    accumulator = 0
    history = set()
    pointer = 0
    looping = False
    while not looping:
        if pointer >= len(code):
            print("Terminated correctly.")
            return True, accumulator
        if pointer in history:
            #print("Looping.")
            return False, accumulator
        history.add(pointer)
        instruction = code[pointer]
        oper_arg = instruction.split(" ")
        operator = oper_arg[0]
        argument = int(oper_arg[1])
        if operator == "nop":
            pointer += 1
        elif operator == "acc":
            accumulator += argument
            pointer += 1
        elif operator == "jmp":
            pointer += argument
        else:
            print("Oh no! Invalid operatoration: %s"%(instruction))

code_original = inFile.readlines()
accumulator_final = 0

def part1():
    result = run(code_original)
    print("Accumulator value just before looping: %d"%(result[1]))
    return True

def part2():
    for i in range(len(code_original)):
        code_copy = list(code_original)
        changed = False
        instruction = code_original[i]
        if instruction.split(" ")[0] == "nop":
            code_copy[i] = "jmp" + str(" ") + instruction.split(" ")[1]
            changed = True
        elif instruction.split(" ")[0] == "jmp":
            code_copy[i] = "nop" + str(" ") + instruction.split(" ")[1]
            changed = True
        if changed:
            result = run(code_copy)
            if result[0]: # If it terminated correctly, this should be True.
                accumulator_final = result[1]
                break
        else:
            continue
    print("Accumulator after terminating correctly: %d"%(accumulator_final))

part1()
part2()
