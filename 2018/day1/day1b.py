import sys
import itertools
lines = [line.rstrip() for line in open(sys.argv[1])]

freq = 0
historical_frequencies = set()
historical_frequencies.add(0)
for line in itertools.cycle(lines):
    sign = line[0]
    amount = int(line[1:])
    if sign == '+':
        freq += amount
    else:
        freq -= amount
    if freq in historical_frequencies:
        print(freq)
        break
    historical_frequencies.add(freq)
