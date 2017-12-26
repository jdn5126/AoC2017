# Sporifica Virus

import sys
#from debug import info

# Globals
# sys.excepthook = info
grid = []


def walk_grid(num_iters):
    num_infected = 0
    x = len(grid) / 2
    y = x
    facing = 0 # 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT
    for i in range(0, num_iters):
        # Is the node infected?
        if grid[x][y] == "#":
            # Yes: turn to right
            facing = (facing + 1) % 4
            # Clean node
            grid[x][y] = "."
        else:
            # No: Turn to left
            if facing == 0:
                facing = 3
            else:
                facing -= 1
            # Infect node, count
            grid[x][y] = "#"
            num_infected += 1
        # Move
        row_len = len(grid[0])
        column_len = len(grid)
        if facing == 0:
            # Create new row above?
            if x == 0:
                grid.insert(0, ['.']*row_len)
                x = 0
            else:
                x -= 1
        elif facing == 1:
            # Create new column to the right?
            if y == row_len - 1:
                for row in grid:
                    row.insert(row_len, ".")
                y = row_len
            else:
                y += 1
        elif facing == 2:
            # Create new row below?
            if x == column_len - 1:
                grid.insert(column_len, ['.']*row_len)
            else:
                x += 1
        else:
            # Create new column to the left?
            if y == 0:
                for row in grid:
                    row.insert(0, ".")
                y = 0
            else:
                y -= 1
    return num_infected


# Count number of infected nodes in grid
def count_infected_nodes():
    infected_nodes = 0
    for row in grid:
        infected_nodes += row.count("#")
    return infected_nodes



if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    num_iters = int(sys.argv[2])
    grid = [ list(x.strip()) for x in f.readlines() ]
    print "Number of infected nodes at start {0}".format(
            count_infected_nodes())
    num_infected = walk_grid(num_iters)
    print "Number of bursts causing infection: {0}".format(
            num_infected)
    print "Number of infected nodes at end {0}".format(
            count_infected_nodes())
