# I Heard You Like Registers
import sys


def main(lines):
    registers = {}
    highest_val = -sys.maxint
    for line in lines:
        line = line.split(" if ")
        # Evaluate expression
        check = False
        expression = line[1].split(' ')
        register = expression[0]
        # Get register contents
        try:
            reg_val = registers[register]
        except KeyError:
            registers[register] = 0
            reg_val = 0
        cond = expression[1]
        value = int(expression[2].strip())
        if cond == ">":
            check = reg_val > value
        elif cond == ">=":
            check = reg_val >= value
        elif cond == "==":
            check = reg_val == value
        elif cond == "!=":
            check = reg_val != value
        elif cond == "<=":
            check = reg_val <= value
        elif cond == "<":
            check = reg_val < value
        else:
            print "Condition %s unknown" % cond
            sys.exit(1)
        # Perform operation
        if not check:
            continue
        else:
            expression = line[0].split(' ')
            register = expression[0]
            operation = expression[1]
            value = int(expression[2].strip())
            if operation == "inc":
                try:
                    registers[register] += value
                except KeyError:
                    registers[register] = value
            elif operation == "dec":
                try:
                    registers[register] -= value
                except KeyError:
                    registers[register] = 0 - value
            else:
                print "Operation %s unknown" % operation
                sys.exit(1)
            # Update highest val
            if registers[register] > highest_val:
                highest_val = registers[register]

    # Find largest value in any register 
    largest_val = -sys.maxint
    for register in registers:
        if registers[register] > largest_val:
            largest_val = registers[register]
    print largest_val, highest_val


if __name__ == "__main__":
    f = open(sys.argv[1])
    main(f.readlines())
