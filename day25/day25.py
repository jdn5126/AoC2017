# Halting Problem

import sys

# Accessed by current state
# Returns next_state, tape value, cursor increment
next_states = {
    "A": {
        0: (1, 1, "B"),
        1: (0, -1, "E")
    }, "B": {
        0: (1, -1, "C"),
        1: (0, 1, "A")
    }, "C": {
        0: (1, -1, "D"),
        1: (0, 1, "C")
    }, "D": {
        0: (1, -1, "E"),
        1: (0, -1, "F")
    }, "E": {
        0: (1, -1, "A"),
        1: (1, -1, "C")
    }, "F": {
        0: (1, -1, "E"),
        1: (1, 1, "A")
    }
}


def turingMachine(tape, cursor, state, num_iters):
    for i in range(0, num_iters):
        # Inifinitely extending tape
        if cursor < 0:
            tape = [0] + tape
            cursor = 0
        elif cursor == len(tape):
            tape = tape + [0]
        # Modifications based on state
        tape[cursor], cursor_inc, state = next_states[state][tape[cursor]]
        cursor += cursor_inc
    return tape.count(1)


if __name__ == "__main__":
    tape = [0]
    num_steps = input("Number of steps before diagnostic checksum: ")
    print "Diagnostic checksum: {0}".format(
            turingMachine(tape, 0, "A", num_steps) )
