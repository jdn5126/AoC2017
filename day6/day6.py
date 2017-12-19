import sys

with open(sys.argv[1], 'r') as myfile:
    line = [ int(x) for x in myfile.read().strip().split('\t') ]
    seen_lines = [ line[:] ]
    count = 0
    new_line = line
    # Loop until we see repeated line
    while True:
        count += 1
        max_index = 0
        length = len(line)
        # Find max index in current line
        for i in range(0, length):
            if line[i] > line[max_index]:
                max_index = i
        # Distribute value
        value = line[max_index]
        line[max_index] = 0
        index = (max_index + 1) % length
        while value > 0:
            line[index] += 1
            index = (index + 1) % length
            value -= 1
        # Check if line has been seen before
        if line in seen_lines:
            init_state = seen_lines.index(line)
            break
        else:
            seen_lines.append(line[:])
    cycle = count - init_state
    print count, cycle
