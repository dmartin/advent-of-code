import sys

banks = open(sys.argv[1], 'r').readline().strip().split("\t")
banks = list(map(lambda x: int(x), banks))

configurations = set()
cycles = 0

def redistibute():
    global banks
    global configurations
    global cycles

    index_of_max = banks.index(max(banks))

    buf = banks[index_of_max]
    banks[index_of_max] = 0

    curr_index = (index_of_max + 1) % len(banks)
    while (buf > 0):
        banks[curr_index] += 1
        buf -= 1
        curr_index = ((curr_index + 1) % len(banks))

while (True):
    if (str(banks) in configurations):
        break
    else:
        configurations.add(str(banks))
        redistibute()
        cycles += 1
print(str(cycles))