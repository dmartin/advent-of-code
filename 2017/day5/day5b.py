import sys
offsets = [line.rstrip('\n') for line in open(sys.argv[1])]

curr_index = 0
prev_index = 0
steps = 0

while(True):
    try:
        # Get the offset at the current index
        offset = int(offsets[curr_index])
        # The current index becomes the previous index
        prev_index = curr_index
        # Move the current index by the offset
        curr_index += offset
        # Modify the offset at the previous index
        prev_offset = int(offsets[prev_index])
        if (prev_offset >= 3):
            offsets[prev_index] = str(prev_offset - 1)
        else:
            offsets[prev_index] = str(prev_offset + 1)
        # Increment the step count
        steps += 1
    except IndexError:
        print(steps)
        exit()