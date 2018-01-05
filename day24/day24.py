# Electromagnetic Moat

import sys

class Port( object ):
    def __init__(self, comp1, comp2):
        self.comp1 = comp1
        self.comp2 = comp2

    def __str__(self):
        return "comp1: {0}, comp2: {1}".format(
                self.comp1, self.comp2)
    
    def __repr__(self):
        return "comp1: {0}, comp2: {1}".format(
                self.comp1, self.comp2)


def buildPortMap(lines):
    port_map = {}
    for line in lines:
        line = line.strip().split('/')
        comp1, comp2 = int(line[0]), int(line[1])
        # forward and reverse map (if not equal)
        my_port = Port(comp1, comp2)
        if comp1 in port_map:
            port_map[comp1].append(my_port)
        else:
            port_map[comp1] = [ my_port ]
        # Do not want to insert duplicates with same hash
        if comp1 != comp2:
            if comp2 in port_map:
                port_map[comp2].append(my_port)
            else:
                port_map[comp2] = [ my_port ]
    return port_map


def recurseDfs(port, val, bridges, visited, port_map):
    # Visit port
    visited.append(port)
    # DFS
    for x in port_map[val]:
        if x not in visited:
            if val == x.comp1:
                new_val = x.comp2
            else:
                new_val = x.comp1
            recurseDfs(x, new_val, bridges, visited[:], port_map)
    # Append visited to bridges
    bridges.append(visited[:])


def generateBridges(port_map):
    bridges = []
    for port in port_map[0]:
        visited = []
        # Recursive DFS
        recurseDfs(port, port.comp2, bridges, visited, port_map)
    return bridges


def strongestBridge(bridges):
    max_strength = 0
    for bridge in bridges:
        cur_sum = 0
        for port in bridge:
            cur_sum += ( port.comp1 + port.comp2 )
        if cur_sum > max_strength:
            max_strength = cur_sum
    return max_strength


def strongestLongestBridge(bridges):
    max_length = 0
    for bridge in bridges:
        if len(bridge) > max_length:
            max_length = len(bridge)
    return max_length, strongestBridge( [ bridge for bridge in bridges if len(bridge) == max_length ] )



if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    port_map = buildPortMap(f.readlines())
    # Generate all valid bridges
    bridges = generateBridges(port_map)
    # Find strongest bridge
    print "Strongest bridge: {0}".format(
            strongestBridge(bridges))
    print "Strongest longest bridge: {0}".format(
            strongestLongestBridge(bridges))
