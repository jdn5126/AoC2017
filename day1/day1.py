# Inverse Captcha

import sys

# Part 1
with open(sys.argv[1], 'r') as myfile:
    data = myfile.read().replace('\n', '')
    sum = 0
    for i in range(0, len(data)):
        if data[i] == data[(i - 1) % len(data)]:
            sum += int(data[i])
    print sum

# Part 2
with open(sys.argv[1], 'r') as myfile:
    data = myfile.read().replace('\n', '')
    sum = 0
    num_elements = len(data)
    for i in range(0, num_elements):
        if data[i] == data[(i + (num_elements / 2)) % num_elements]:
            sum += int(data[i])
    print sum
