# Knot Hash

import sys

list_size = int(sys.argv[2])


def reverse(stream, current_position, length):
    front = current_position
    back = (current_position + length - 1) % list_size
    for i in range(0, length / 2):
        stream[front], stream[back] = stream[back], stream[front]
        # Update positions
        front = (front + 1) % list_size
        if back == 0:
            back = list_size
        back -= 1


def apply_mutations(stream, lengths):
    current_position = 0
    skip_size = 0
    for length in lengths:
        # Reverse list
        reverse(stream, current_position, length)
        # Update current position and skip size
        current_position = (current_position + length + skip_size) % list_size
        skip_size += 1


if __name__ == "__main__":
    # Get lengths from file
    f = open(sys.argv[1], 'r')
    content = f.read()
    lengths = [ int(x) for x in content.strip().split(',') ]
    # Initialize stream
    stream = []
    for i in range(0, list_size):
        stream.append(i)
    # Apply mutations
    apply_mutations(stream, lengths) 
    print stream[0] * stream[1]
