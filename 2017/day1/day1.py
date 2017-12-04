import sys
data = open(sys.argv[1]).read().rstrip()

sum = 0

print(data)
# Check every char -> next except the last
for x in range(0, len(data)-1):
    if (data[x] == data[x+1]):
        sum += int(data[x])

# Special case for last char
last = data[len(data)-1]
if (last == data[0]):
    sum += int(last)

print(str(sum))