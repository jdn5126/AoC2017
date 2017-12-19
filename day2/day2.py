# Corruption Checksum

import sys

# Part 1
with open(sys.argv[1], 'r') as myfile:
    # Read each line into a list
    rows = myfile.readlines()
    sums = []
    # Find max, min pair in each row
    for row in rows:
        max_num = 0
        min_num = sys.maxint
        for num in row.strip().split(' '):
            val = int(num)
            if val > max_num:
                max_num = val
            if val < min_num:
                min_num = val
        sums.append(max_num - min_num)
    print sum(sums)


# Part 2
with open(sys.argv[1], 'r') as myfile:
    # Read each line into a list
    rows = myfile.readlines()
    sums = []
    # Find divisible nums in each row
    for row in rows:
        row = row.strip().split(' ')
        length = len(row)
        # O(n^2) search
        for i in range(0, length - 1):
            num1 = int(row[i])
            for j in range(i + 1, length):
                # If evenly divisible, add to sums
                num2 = int(row[j])
                if num1 > num2:
                    if num1 % num2 == 0:
                        sums.append(num1 / num2)
                        continue
                else:
                    if num2 % num1 == 0:
                        sums.append(num2 / num1)
                        continue
    print sum(sums)
