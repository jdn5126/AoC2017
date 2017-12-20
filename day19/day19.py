# A Series of Tubes

import sys


# Return index of starting path
def find_start(diagram):
    return diagram[0].index("|")


# Traverse diagram, enqueue each character
def traverse_diagram(diagram, start):
    row, index = 0, start
    last_row, last_index = -1, index
    steps = 0
    letters = []
    end = False

    while not end:
        steps += 1
        # What is around me?
        if row == 0:
            above_me = " "
        else:
            above_me = diagram[row - 1][index]
        try:
            below_me = diagram[row + 1][index]
        except IndexError:
            below_me = " "
        if index == 0:
            left_of_me = " "
        else:
            left_of_me = diagram[row][index - 1]
        try:
            right_of_me = diagram[row][index + 1]
        except IndexError:
            right_of_me = " "
        # Am I on a letter?
        my_char = diagram[row][index]
        if my_char.isalpha():
            letters.append(my_char)
            # Check for end here for this function to work... empty on three sides
            sides = above_me + below_me + left_of_me + right_of_me
            if sides.count(" ") > 2:
                end = True
                return letters, steps
        # Where did I come from?
        if row > last_row:
            last_row = row
            # I came from above. Can I keep going down?
            if below_me == " ":
                # Empty space is the only way I stop going down
                last_index = index
                # Do I go right or left?
                if right_of_me == " ":
                    index -= 1
                else:
                    index += 1
            else:
                row += 1
        elif row < last_row:
            last_row = row
            # I came from below. Can I keep going up?
            if above_me == " ":
                # Empty space is the only way I stop going up
                last_index = index
                # Do I go right or left?
                if right_of_me == " ":
                    index -= 1
                else:
                    index += 1
            else:
                row -= 1
        elif index > last_index:
            last_index = index
            # I came from the left. Can I keep going right?
            if right_of_me == " ":
                # Empty space is the only way I stop going right
                last_row = row
                # Do I go up or down?
                if above_me == " ":
                    row += 1
                else:
                    row -= 1
            else:
                index += 1
        elif index < last_index:
            last_index = index
            # I came from the right. Can I keep going left?
            if left_of_me == " ":
                # Empty space is the only way I stop going left
                last_row = row
                # Do I go up or down?
                if above_me == " ":
                    row += 1
                else:
                    row -= 1
            else:
                index -= 1
        else:
            print "You came from the same spot (%s, %s)... wtf?" % (last_row, last_index)
            sys.exit(1)
    # Return letters visited
    return letters, steps

                
if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    diagram = [ x.strip("\n") for x in f.readlines() ]
    # Find starting index
    start = find_start(diagram)
    # Traverse, traverse
    letters, steps = traverse_diagram(diagram, start)
    output = ""
    for letter in letters:
        output += letter
    print output, steps
