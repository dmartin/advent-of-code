import sys
lines = [line.rstrip('\n') for line in open(sys.argv[1])]
sum = 0
for x in range(len(lines)):
    lines[x] = list(map(int, lines[x].split('\t')))
    
    result_found = False
    multiplicand = 1
    while(not result_found):
        for multiplier in lines[x]:
            copy = list(lines[x])
            copy.remove(multiplier)
            if (multiplier * multiplicand in copy):
                sum += multiplicand
                result_found = True
                break
        multiplicand += 1
print(sum)