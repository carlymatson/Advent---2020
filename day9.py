file = open("day9input.text", 'r')

file_lines = file.readlines()
num_list = [int(line) for line in file_lines]

def get_pair_sums(sub_list):
    pair_sums = set()
    N = len(sub_list)
    for i in range(N):
        for j in range(i, N):
            pair_sums.add(sub_list[i]+sub_list[j])
    return pair_sums

def part1():
    n = 25
    prev_n_terms = num_list[:n]
    index = n
    while n < len(num_list):
        prev_n_terms = num_list[index-n:index]
        pair_sums = get_pair_sums(prev_n_terms)
        if num_list[index] not in pair_sums:
            print("Index: %d"%(index))
            print("Invalid number: %d"%(num_list[index]))
            break
        index += 1
    return num_list[index]

def part2():
    index = 0
    target_sum = part1()
    while index < len(num_list):
        contiguous_sum = 0
        j = 0
        while (contiguous_sum < target_sum) and (index + j < len(num_list)):
            contiguous_sum += num_list[index + j]
            if (contiguous_sum == target_sum) and (j > 0):
                print("Starting index: %d; Number of terms: %d"%(index, j+1))
                sub_list = num_list[index: index+j+1]
                print("Min + Max: %d" %(min(sub_list) + max(sub_list)))
                break
            j += 1
        index += 1


part2()
