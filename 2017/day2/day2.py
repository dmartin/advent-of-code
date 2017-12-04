import sys
lines = [line.rstrip('\n') for line in open(sys.argv[1])]
sum = 0
for x in range(len(lines)):
    lines[x] = list(map(int, lines[x].split('\t')))
    sum += (max(lines[x]) - min(lines[x]))
print(sum)