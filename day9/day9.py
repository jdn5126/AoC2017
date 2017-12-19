# Stream Processing

import sys

def parse(stream):
    brackets = []
    garbage_count = 0
    in_garbage = False
    ignore_char = False
    # Iterate across stream
    for char in stream:
        # '!' always nullifies next char
        if ignore_char:
            ignore_char = False
            continue
        # Are we in garbage?
        if in_garbage:
            # End of garbage can be nullified
            if char == '!':
                ignore_char = True
            elif char == '>':
                in_garbage = False
            else:
                garbage_count += 1
            continue
        # What is the char?
        if char == '<':
            in_garbage = True
        elif char == '!':
            ignore_char = True
        elif char == '{' or char == '}': # "Outside garbage, you will only find well formed groups"
            brackets.append(char)
        elif char == ',':
            continue
        else:
            print "Stumbled upon %c" % char
            sys.exit(1)
    return brackets, garbage_count


def get_score(brackets):
    # Score is calculated as one more than score of group that immediately contains pair
    # Outermost group has a score of one
    score = 0
    while brackets:
        count = 0
        for i in range(0, len(brackets)):
            if brackets[i] != '}':
                count += 1
            else:
                score += count
                # pop indices
                del brackets[i-1:i+1]
                break
    return score


with open(sys.argv[1], 'r') as myfile:
    # Pass file contents, ignore newline
    brackets, garbage_count = parse(myfile.read()[:-1])
    print get_score(brackets), garbage_count
