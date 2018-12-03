import sys
lines = [line.rstrip() for line in open(sys.argv[1])]

freq = 0
for line in lines:
    sign = line[0]
    amount = int(line[1:])
    if sign == '+':
        freq += amount
    else:
        freq -= amount
print(freq)