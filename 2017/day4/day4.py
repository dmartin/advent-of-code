import sys
lines = [line.rstrip('\n') for line in open(sys.argv[1])]

count = 0
for x in range(len(lines)):
    line_list = lines[x].split(' ')
    num_phrases = len(line_list)
    num_unique_phrases = len(set(line_list))
    if (num_phrases == num_unique_phrases):
        count += 1
print(count)
