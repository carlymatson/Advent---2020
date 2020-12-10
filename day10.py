inFile = open("day10input.text", 'r')

inList = inFile.readlines()
nums = [int(n) for n in inList]

nums.append(0)
_max = max(nums)
nums.append(_max+3)
nums.sort()
print "Nums: " + str(nums)


count1s = 0
count3s = 0

for i in range(len(nums) - 3):
    diff = nums[i+1] - nums[i]
    if diff == 1:
        count1s += 1
    if diff == 3:
        count3s += 1

#print count1s, count3s
#print count1s*count3s

N = len(nums)
numOptions = [0]*N
numOptions[N-1] = 1
for i in range(2, N+1):
    options = 0
    for j in range(1,4):
        if (j < i) and (nums[N-i+j] - nums[N-i] <= 3):
            options += numOptions[N-i+j]
    numOptions[N-i] = options

print numOptions

print "Number of options: " + str(numOptions[0])
