# Packet Scanners

import sys


def hit(picosecond, depth):
    return picosecond % (2 *(depth - 1)) == 0


# Iterate across firewall and calculate severity
# of running into scanner
def calc_severity(layers):
    severity = 0
    for row in range(0, len(layers)):
        # Does this row have a scanner?
        if layers[row] == 0:
            continue
        # Is scanner at 0 at this point in time?
        if hit(row, layers[row]):
            severity += row * layers[row]
    return severity


# Calculate minimum delay needed to safely cross firewall
def calc_delay(layers):
    delay = 0
    bad_val = True
    while bad_val:
        bad_val = False
        for row in range(0, len(layers)):
            # Ignore empty rows
            if layers[row] == 0:
                continue
            # Calculate scanner at current time
            if hit(row + delay, layers[row]):
                bad_val = True
                delay += 1
                break
    return delay


def traverse_firewall(lines):
    layers = []
    # Build 2-D array
    for i in range(0, len(lines)):
        line = lines[i].strip().split(": ")
        entry = int(line[0])
        depth = int(line[1])
        num_layers = len(layers)
        if entry > num_layers:
            for j in range(num_layers, entry):
                layers.append(0)
        layers.append(depth)
    # Get severity
    print calc_severity(layers)
    # Get delay
    print calc_delay(layers)


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    traverse_firewall(lines)
