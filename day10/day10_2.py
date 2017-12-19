# Knot Hash 2

import sys

# Globals
list_size = 256


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


def apply_mutations(stream, lengths, num_rounds):
    current_position = 0
    skip_size = 0
    for i in range(0, num_rounds):
        for length in lengths:
            # Reverse list
            reverse(stream, current_position, length)
            # Update current position and skip size
            current_position = (current_position + length + skip_size) % list_size
            skip_size += 1


# Calculate dense hash from sparse hash
def get_dense_hash(stream):
    dense_hash = []
    for i in range(0, list_size, 16):
        hash_val = 0
        for j in range(i, i + 16):
            hash_val ^= stream[j]
        dense_hash.append(hash_val)
    return dense_hash


# Convert each entry to two hexadecimal characters
def print_hex_string(dense_hash):
    string = ""
    for entry in dense_hash:
        string += hex(entry)[2:].zfill(2)
    return string


def hash_string(input_string, num_rounds=64):
    # Get ASCII values for each character
    lengths = [ ord(x) for x in input_string ]
    # Append standard length suffix values to lengths
    lengths += [17, 31, 73, 47, 23]
    # Initialize stream
    stream = []
    for i in range(0, list_size):
        stream.append(i)
    # Apply mutations to get sparse hash
    apply_mutations(stream, lengths, num_rounds)
    # Get dense hash from sparse_hash
    dense_hash = get_dense_hash(stream)
    # Print hex_string from dense hash
    hex_string = print_hex_string(dense_hash)
    return hex_string


if __name__ == "__main__":
    # Get lengths from file
    f = open(sys.argv[1], 'r')
    content = f.read().strip()
    print hash_string(content)
