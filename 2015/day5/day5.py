import sys

lines = [line.rstrip('\n') for line in open(sys.argv[1])]
vowels = ['a','e','i','o','u']
badStrings = ['ab', 'cd', 'pq', 'xy']

def isNiceString(input):
    # Does it contain at least 3 unique vowels?
    vowelCount = 0
    for char in input:
        if (char in vowels):
    if (vowelCount < 3):
        return False
    # Does it have at least one double-letter?
    lastLetter = input[0]
    hasDoubleLetter = False
    print(input)
    for x in range(1, len(input)):
        currLetter = input[x]
        print("Comparing " + currLetter + " to " + lastLetter)
        if currLetter == lastLetter:
            hasDoubleLetter = True
            break
        lastLetter = currLetter
    if (not hasDoubleLetter):
        return False
    # Does it contain a bad string?
    for badString in badStrings:
        if (badString in input):
            return False
    return True

niceStringsCount = 0
for line in lines:
    if (isNiceString(line)):
        niceStringsCount += 1
print(str(niceStringsCount))
