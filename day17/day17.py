# Spinlock

import sys


def create_buffer(steps):
    circ_buffer = [0]
    current_position = 0
    for i in range(1, 2018):
        # Calculate position to insert
        insert_pos = (current_position + steps) % i
        circ_buffer.insert(insert_pos + 1, i)
        # Inserted position is new index
        current_position = insert_pos + 1
    return circ_buffer[current_position + 1]


# Record each insert to position 1 over iterations
def find_pos_1(iterations):
    spinlock = 0
    current_position = 0
    for i in range(1, iterations):
        insert_position = (current_position + steps) % i
        if insert_position == 0:
            spinlock = i
        current_position = insert_position + 1
    return spinlock


if __name__ == "__main__":
    # Number of steps before inserting next value: puzzle input
    steps = input("Steps: ")
    # Number of iterations
    iterations = input("Iterations: ")
    # Part 1
    print create_buffer(steps)
    # Part 2
    print find_pos_1(iterations)
