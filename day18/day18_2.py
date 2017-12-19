# Duet

import sys


# Globals
# Program queue for each running program
program_queue = [ [], [] ]
# Register file for each running program
global_registers = [{}, {}]
global_registers[0]["p"] = 0
global_registers[1]["p"] = 1
# Target for each running program
targets = [0, 0]
# Sent values
sent_values = [0, 0]
# Master PID
MASTER_PID = 1


def execute_instructions(instructions, registers, process_id, target):
    num_instructions = len(instructions)
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
        if instruction[0] == "snd":
            # Send value X to the other program
            try:
                program_queue[ (process_id + 1) % 2 ].append(int(instruction[1]))
            except ValueError:
                program_queue[ (process_id + 1) % 2 ].append(registers[instruction[1]])
            sent_values[ process_id ] += 1
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
            #if process_id == MASTER_PID:
            #    import pdb
            #    pdb.set_trace()
            other_pid = (process_id + 1) % 2
            # Receive value from other program and place it in X
            if len(program_queue[process_id]) == 0:
                # Check for deadlock
                if len(program_queue[other_pid]) == 0 and instructions[targets[other_pid]].strip().split(' ')[0] == "rcv":
                    print "Deadlock: %s" % sent_values
                    sys.exit()
                else:
                    # Otherwise, let other guy go (but make sure you return back to this instruction!!!)
                    if process_id != MASTER_PID:
                        targets[ process_id ] = target
                        return
                    else:
                        targets[ process_id ] = target
                        execute_instructions( instructions, global_registers[other_pid], other_pid, targets[other_pid] )
                        target -= 1
            else:
                # If we have value to receive, receive it
                registers[instruction[1]] = program_queue[ process_id ][0]
                del program_queue[ process_id ][0]
        elif instruction[0] == "jgz":
            # Check if second argument to jgz is an integer
            if instruction[1] not in registers:
                if int(instruction[1]) > 0:
                    try:
                        target += int(instruction[2]) - 1
                    except ValueError:
                        target += registers[instruction[2]] - 1
            else:
                if registers[instruction[1]] > 0:
                    try:
                        target += int(instruction[2]) - 1
                    except ValueError:
                        target += registers[instruction[2]] - 1
        else:
            print "Instruction %s not recognized" % instruction[0]
            sys.exit()
        # Update target
        target += 1


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    instructions = f.readlines()
    # Call with MASTER_PID
    execute_instructions(instructions, global_registers[MASTER_PID], MASTER_PID, targets[MASTER_PID])
    # If we return normally, print sent_values
    print sent_values
