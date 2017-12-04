import sys
data = open(sys.argv[1]).read().rstrip()

sum = 0

def get_char_at_ring_position(data, pos):
    return data[pos % len(data)]

for x in range(0, len(data)):
    if (get_char_at_ring_position(data, x) == get_char_at_ring_position(data, x+(len(data)//2))):
        sum += int(data[x])

print(str(sum))