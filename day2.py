file = open("day2input.text", 'r')

def part1_check(num_pair, character, password):
    char_counter = 0
    for char_ in password:
        if char_ == character:
            char_counter += 1
    if (char_counter >= num_pair[0]) and (char_counter <= num_pair[1]):
        return True
    return False

def part2_check(num_pair, character, password):
    char_counter = 0
    if password[num_pair[0]-1] == character:
        char_counter += 1
    if password[num_pair[1]-1] == character:
        char_counter += 1
    if char_counter == 1:
        return True
    return False

file_lines = file.readlines()
num_valid = 0
for line in file_lines:
    # Lines are in format "#1-#2 char: password".
    rule_password = line.split(':')
    nums_char = rule_password[0].split(' ')
    num_pair = [int(num) for num in nums_char[0].split('-')]
    character = nums_char[1]
    password = rule_password[1].strip()
    if part2_check(num_pair, character, password):
        num_valid += 1

print("Valid count: %d"%(num_valid))

