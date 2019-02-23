import sys
from collections import Counter
lines = [line.rstrip() for line in open(sys.argv[1], 'r')]

counters = []
for line in lines:
    curr_counter = Counter(line)
    counters.append(curr_counter)

two_count = 0
three_count = 0
for counter in counters:
    if 2 in counter.values():
        two_count += 1
    if 3 in counter.values():
        three_count += 1

print(two_count * three_count)
