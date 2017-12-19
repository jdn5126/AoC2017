# Permutation Promenade

import sys

# Globals
num_iters = int(sys.argv[2])
line = list("abcdefghijklmnop")


# num_move programs from the back move to the front
def spin(num_move):
    global line
    if num_move == 0:
        return
    line = line[-num_move:] + line[0:len(line)-num_move]


# Programs a and b swap places
def exhange(a, b):
    global line
    line[a], line[b] = line[b], line[a]


# Programs named a and b swap places
def partner(a, b):
    global line
    index_a = line.index(a)
    index_b = line.index(b)
    exhange(index_a, index_b)


# Iterate until original pattern is repeated
def find_repeat(orig, moves):
    sequence = None
    count = 0
    while sequence != orig:
        count += 1
        sequence = dance(moves)
    return count


def dance(moves):
    # Apply moves
    for move in moves:
        operation = move[0]
        if operation == 's': # Spin
            spin(int(move[1:]))
        elif operation == 'x': # Exchange
            indices = move[1:].split('/')
            exhange(int(indices[0]), int(indices[1]))
        elif operation == 'p': # Partner
            indices = move[1:].split('/')
            partner(indices[0], indices[1])
        else:
            print "Unknown operation %s" % move
            sys.exit()
    # Cast back to string
    res = ""
    for char in line:
        res += char
    return res
            

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    moves = f.read().strip().split(',')
    # Find repeating iteration
    repeat = find_repeat("abcdefghijklmnop", moves)
    # Find how many times to call dance
    dance_num = num_iters % repeat
    for i in range(0, dance_num - 1):
        dance(moves)
    print dance(moves)

