# Fractal Art

import sys


# Globals
in_rules = []
out_rules = []


# Return flipped square
def flip(square):
    len_sq = len(square)
    square[0], square[ len_sq - 1 ] = square[ len_sq - 1 ], square[0]


# Return reflected square
def reflect(square):
    for i in range(0, len(square)):
        rev = list(square[i])
        rev.reverse()
        square[i] = ''.join(rev)


# Rotate square
def rotate(square):
    # Rotate 90 degrees
    temp = zip(*square[::-1])
    # Cast back to usable form
    for i in range(0, len(square)):
        line = ""
        for char in temp[i]:
            line += char
        square[i] = line


# Build input/output rules for transformations
def build_rules(lines):
    for line in lines:
        line = line.strip().split(" => ")
        # Get input rule
        in_rule = line[0].split('/')
        # Append all transforms as well
        in_rules.append(in_rule[:])
        reflect(in_rule)
        in_rules.append(in_rule[:])
        flip(in_rule)
        in_rules.append(in_rule[:])
        reflect(in_rule)
        in_rules.append(in_rule[:])
        rotate(in_rule)
        in_rules.append(in_rule[:])
        reflect(in_rule)
        in_rules.append(in_rule[:])
        flip(in_rule)
        in_rules.append(in_rule[:])
        reflect(in_rule)
        in_rules.append(in_rule[:])
        # Output rules
        out_rule = line[1].split('/')
        for _ in range(0, 8):
            out_rules.append(out_rule)


def check_rule(grid, v, h, square_len):
    # Build square
    my_square = []
    for row in grid[v:v+square_len]:
        my_square.append(row[h:h+square_len])
    # Check for pattern match
    for i in range(0, len(in_rules)):
        if my_square == in_rules[i]:
            return i


def fractal_art(grid, num_iters):
    for _ in range(0, num_iters):
        # Get size of grid
        size = len(grid)
        if size % 3 == 0:
            square_sz = 3
        elif size % 2 == 0:
            square_sz = 2
        else:
            print "Size of %d not valid" % size
            sys.exit()
        # Break pixels into 3x3 or 2x2 squares and convert each
        # to 4x4 or 3x3 squares
        new_grid = []
        for v in range(0, size, square_sz):
            for h in range(0, size, square_sz):
                # Check for rule match on square size
                out_index = check_rule(grid, v, h, square_sz)
                out_square = out_rules[out_index]
                out_v = (v / square_sz) * (square_sz + 1)
                out_h = (h / square_sz) * (square_sz + 1)
                # Append square to new_grid
                if out_v == 0 and out_h == 0:
                    for i in range(0, square_sz + 1):
                        new_grid.insert(i, out_square[i])
                else:
                    for i in range(out_v, out_v + square_sz + 1):
                        if h == 0:
                            new_grid.insert(i, out_square[ i % (square_sz + 1) ])
                        else:
                            new_grid[i] += out_square[ i % (square_sz + 1) ]
        grid = new_grid[:]
    return grid


def count_on(grid):
    count = 0
    for row in grid:
        count += row.count("#")
    return count
                    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Call as ./day21.py <rules> <num_iters>"
        sys.exit()
    f = open(sys.argv[1], 'r')
    build_rules(f.readlines())
    num_iters = int(sys.argv[2])
    grid = [ ".#.",
             "..#",
             "###" ]
    # Run transformations
    grid = fractal_art(grid, num_iters)
    print count_on(grid)
