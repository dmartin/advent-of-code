import sys
import re
import collections
import operator

# Construct string -> operator lookup table
operators = { '<': operator.lt,
        '>': operator.gt,
        '<=': operator.le,
        '>=': operator.ge,
        '==': operator.eq,
        '!=': operator.ne
}

def main():
    # Parse the input
    p = re.compile(r'^(\w*) (inc|dec) (-?\d*) if (\w*) (<|>|<=|>=|==|!=) (-?\d*)$')
    infile = [line.rstrip() for line in sys.stdin]
    parsed = []
    for line in infile:
        parsed.append(p.findall(line)[0])
    
    # Update the registers, keeping track of the highest-ever value
    registers = collections.defaultdict(lambda: 0)
    highest_ever = 0
    for instruction in parsed:
        register = instruction[0]
        increase = True if instruction[1] == 'inc' else False
        amount = int(instruction[2])
        test_register = instruction[3]
        test_operator = instruction[4]
        test_amount = int(instruction[5])

        if (operators[test_operator](registers[test_register], test_amount)):
            if increase:
                registers[register] += amount
            else:
                registers[register] -= amount
                
            if (registers[register] > highest_ever):
                    highest_ever = registers[register]

    print(highest_ever)

if (__name__ == "__main__"):
    main()