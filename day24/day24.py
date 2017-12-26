# Electromagnetic Moat

import sys


# Globals
port_map = {}


def buildPortMap(lines):
    for line in lines:
        line = line.strip().split('/')
        comp1, comp2 = int(line[0]), int(line[1])
        # forward and reverse map
        port_map[comp1] = comp2
        port_map[comp2] = comp1


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    buildPortMap(f.readlines())
