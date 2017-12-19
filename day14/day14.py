# Disk Defragmentation
# Run as: $ PYTHONPATH=../day10/ python day14.py

import sys

from day10_2 import hash_string


def num_used(disk):
    num_used = 0
    for hex_string in disk:
        for char in hex_string:
            hex_val = int(char, 16)
            num_used += "{0:b}".format(hex_val).count('1')
    return num_used


def visit_all(grid, x, y):
    # Find eligible neighbors
    # Left, Right
    for a in [-1, 1]:
        # Skip if neighbor is out of bounds
        if (x + a) >= 0 and (x + a) < 128:
            if grid[x+a][0][y] == '1' and grid[x+a][1][y] == False:
                grid[x+a][1][y] = True
                visit_all(grid, x+a, y)
    for b in [-1, 1]:
        # Skip if neighbor is out of bounds
        if (y + b) >= 0 and (y + b) < 128:
            if grid[x][0][y+b] == '1' and grid[x][1][y+b] == False:
                grid[x][1][y+b] = True
                visit_all(grid, x, y+b)


def num_regions(disk):
    # Build Grid
    grid = []
    for i in range(0, 128):
        byte = ""
        for char in disk[i]:
            hex_val = int(char, 16)
            byte += "{0:b}".format(hex_val).zfill(4)
        grid.append([byte, [False]*128])
    # Determine regions
    num_regions = 0
    for x in range(0, 128):
        for y in range(0, 128):
            # If square is used and unvisited, add a new group and mark all of its neighbors
            if grid[x][0][y] == '1' and grid[x][1][y] == False:
                num_regions += 1
                grid[x][1][y] = True
                # Visit all unvisited neighbors
                visit_all(grid, x, y)
    print num_regions
                

def main(key_string):
    # Calculate hash string for each disk row
    disk = []
    for i in range(0, 128):
        input_str = "{hs}-{i}".format(hs=key_string, i=i)
        disk.append(hash_string(input_str))
    # Calculate number of used squares
    print num_used(disk)
    # Calculate number of regions
    num_regions(disk)


if __name__ == "__main__":
    # Get key string
    key_string = raw_input("Input string: ")
    main(key_string)
