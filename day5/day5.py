# Maze

import sys

with open(sys.argv[1], 'r') as myfile:
    lines = [ int(x.strip()) for x in myfile.readlines() ]
    size = len(lines)
    pos = 0
    steps = 0
    while(pos < size):
        new_pos = pos + lines[pos]
        if lines[pos] > 2:
            lines[pos] -= 1
        else:
            lines[pos] += 1
        pos = new_pos
        steps += 1
    print steps
