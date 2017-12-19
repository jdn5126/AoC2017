# High-Entropy Passphrases

import sys

# Part 1
# Iterate line by line, determine if line is valid
valid_passphrases = 0
with open(sys.argv[1], 'r') as myfile:
    lines = myfile.readlines()
    for line in lines:
        line = line.strip().split(' ')
        valid_line = True
        words = []
        for word in line:
            if word in words:
                valid_line = False
                break
            else:
                words.append(word)
        if valid_line:
            valid_passphrases += 1

print valid_passphrases


# Part 2
valid_passphrases = 0
with open(sys.argv[1], 'r') as myfile:
    lines = myfile.readlines()
    for line in lines:
        line = line.strip().split(' ')
        valid_line = True
        words = []
        for word in line:
            word = ''.join(sorted(word))
            if word in words:
                valid_line = False
                break
            else:
                words.append(word)
        if valid_line:
            valid_passphrases += 1

print valid_passphrases
