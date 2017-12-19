# Duet

import sys


# Globals
registers = {}


def execute_instructions(instructions):
    target = 0
    num_instructions = len(instructions)
    prev_snd = None
    # Iterate while target is within instruction range
    while target >= 0 and target < num_instructions:
        instruction = instructions[target].strip().split(' ')
        # Initialize register(s)
        if instruction[1] not in registers:
            registers[instruction[1]] = 0
        try:
            int(instruction[2])
        except IndexError:
            pass
        except ValueError:
            if instruction[2] not in registers:
                registers[instruction[2]] = 0
        # Execute instruction
        if instruction[0] == "snd":
            # Play sound, record previous sound played
            prev_snd = registers[instruction[1]]
        elif instruction[0] == "set":
            # Set register X equal to the value in Y
            try:
                registers[instruction[1]] = int(instruction[2])
            except ValueError:
                registers[instruction[1]] = registers[instruction[2]]
        elif instruction[0] == "add":
            # Add to register X, the value in Y
            try:
                registers[instruction[1]] += int(instruction[2])
            except ValueError:
                registers[instruction[1]] += registers[instruction[2]]
        elif instruction[0] == "mul":
            # Set register X to the product of X*Y
            try:
                registers[instruction[1]] = registers[instruction[1]] * int(instruction[2])
            except ValueError:
                registers[instruction[1]] = registers[instruction[1]] * registers[instruction[2]]
        elif instruction[0] == "mod":
            # Set register X to the remainder of X/Y
            try:
                registers[instruction[1]] = registers[instruction[1]] % int(instruction[2])
            except ValueError:
                registers[instruction[1]] = registers[instruction[1]] % registers[instruction[2]]
        elif instruction[0] == "rcv":
            # Part 1: return first recovered sound
            if registers[instruction[1]] != 0:
                return prev_snd
        elif instruction[0] == "jgz":
            if registers[instruction[1]] > 0:
                # -1 because of update below
                target += int(instruction[2]) - 1
        else:
            print "Instruction %s not recognized" % instruction[0]
            sys.exit()
        # Update target
        target += 1


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    instructions = f.readlines()
    print execute_instructions(instructions)
