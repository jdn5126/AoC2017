# Coprocessor Conflagration

import sys


def execute_instructions(instructions, registers, target):
    num_instructions = len(instructions)
    num_mul = 0
    # Iterate while target is within instruction range
    while target >= 0 and target < num_instructions:
        instruction = instructions[target].strip().split(' ')
        # Initialize register(s)
        try:
            int(instruction[1])
        except ValueError:
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
        if instruction[0] == "set":
            # Set register X equal to the value in Y
            try:
                registers[instruction[1]] = int(instruction[2])
            except ValueError:
                registers[instruction[1]] = registers[instruction[2]]
        elif instruction[0] == "sub":
            # Decrease register X by the value of Y
            try:
                registers[instruction[1]] -= int(instruction[2])
            except ValueError:
                registers[instruction[1]] -= registers[instruction[2]]
        elif instruction[0] == "mul":
            # Set register X to the product of X*Y
            try:
                registers[instruction[1]] = registers[instruction[1]] * int(instruction[2])
            except ValueError:
                registers[instruction[1]] = registers[instruction[1]] * registers[instruction[2]]
            # Count number of times that mul is called
            num_mul += 1
        elif instruction[0] == "jnz":
            # Check if second argument to jnz is an integer
            if instruction[1] not in registers:
                if int(instruction[1]) != 0:
                    try:
                        target += int(instruction[2]) - 1
                    except ValueError:
                        target += registers[instruction[2]] - 1
            else:
                if registers[instruction[1]] != 0:
                    try:
                        target += int(instruction[2]) - 1
                    except ValueError:
                        target += registers[instruction[2]] - 1
        else:
            print "Instruction %s not recognized" % instruction[0]
            sys.exit()
        # Update target
        target += 1
    return num_mul


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    instructions = f.readlines()
    num_mul = execute_instructions(instructions, registers={}, target=0)
    print num_mul
