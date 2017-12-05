import sys
lines = [line.rstrip('\n') for line in open(sys.argv[1])]

count = 0
for x in range(len(lines)):
    line_list = lines[x].split(' ')
    letterset_set = set()
    num_phrases = len(line_list)

    for y in range(len(line_list)):
        letterset_set.add(frozenset(line_list[y]))
    num_unique_lettersets = len(letterset_set)
    if (num_phrases == num_unique_lettersets):
        count += 1
print(count)
