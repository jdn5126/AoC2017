# Sporifica Virus


import sys


def virus_cleaner(grid, num_bursts):
    center = len(grid) / 2
    x = center
    y = center
    num_infected = 0
    facing = 0 # 0 - UP, 1 - RIGHT, 2 - DOWN, 3 - LEFT
    for _ in range(0, num_bursts):
        # Is current node infected?
        if grid[y][x] == "#":
            # Turn to the right
            facing = (facing + 1) % 4
            # Clean node
            grid[y][x] = "."
        else:
            # Turn to the left
            if facing == 0:
                facing = 3
            else:
                facing -= 1
            # Infect node
            grid[y][x] = "#"
            num_infected += 1
        # Move forward one in direction facing
        if facing == 0:
            if y == 0:
                # Insert row above
                grid.insert(0, list("."*len(grid[0])) )
                y = 0
            else:
                y -= 1
        elif facing == 1:
            if x == len(grid[y]) - 1:
                # Add column to the right
                for row in grid:
                    row.append(".")
            x += 1
        elif facing == 2:
            if y == len(grid) - 1:
                # Add row below
                grid.insert(len(grid), list("."*len(grid[0])) )
            y += 1
        elif facing == 3:
            if x == 0:
                # Add column to the left
                for row in grid:
                    row.insert(0, ".")
                x = 0
            else:
                x -= 1
    return num_infected


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Call as ./day22.py <file> <num_iters>"
        sys.exit()
    f = open(sys.argv[1], 'r')
    grid = [ list(line.strip()) for line in f.readlines() ]
    num_bursts = int(sys.argv[2])
    print virus_cleaner(grid, num_bursts)
