import math
import collections
import sys

spiral = collections.OrderedDict()
# The spiral moves left each step, with 2 iterations of each step size (1,1,2,2,3,3,...)
direction_vector = (1,0)
length_step = 1
step_progress = 0
step_iter = 0

# Initalize spiral
spiral[(0,0)] = 1

def addToSpiral():
    global spiral
    global direction_vector
    global length_step
    global step_progress
    global step_iter

    if (step_progress == length_step):
        step_progress = 0
        direction_vector = turnLeft(direction_vector)
        step_iter += 1
    if (step_iter == 2):
        length_step += 1
        step_iter = 0

    # Get the previous entry's position
    last_item = spiral.popitem(last=True)
    prev_x = last_item[0][0]
    prev_y = last_item[0][1]
    spiral[last_item[0]] = last_item[1]

    # Calculate the new entry's position
    new_pos = (prev_x + direction_vector[0], prev_y + direction_vector[1])

    # Calculate the sum of surrounding values (if present)
    val = 0
    # East
    if ((new_pos[0]+1, new_pos[1]) in spiral):
        val += spiral[(new_pos[0]+1, new_pos[1])]
    # Northeast
    if ((new_pos[0]+1, new_pos[1]+1) in spiral):
        val += spiral[(new_pos[0]+1, new_pos[1]+1)]
    # North
    if ((new_pos[0], new_pos[1]+1) in spiral):
        val += spiral[(new_pos[0], new_pos[1]+1)]
    # Northwest
    if ((new_pos[0]-1, new_pos[1]+1) in spiral):
        val += spiral[(new_pos[0]-1, new_pos[1]+1)]
    # West
    if ((new_pos[0]-1, new_pos[1]) in spiral):
        val += spiral[(new_pos[0]-1, new_pos[1])]
    # Southwest
    if ((new_pos[0]-1, new_pos[1]-1) in spiral):
        val += spiral[(new_pos[0]-1, new_pos[1]-1)]
    # South
    if ((new_pos[0], new_pos[1]-1) in spiral):
        val += spiral[(new_pos[0], new_pos[1]-1)]
    # Southeast
    if ((new_pos[0]+1, new_pos[1]-1) in spiral):
        val += spiral[(new_pos[0]+1, new_pos[1]-1)]

    spiral[new_pos] = val

    step_progress += 1

def turnLeft(vector):
    x = vector[0]
    y = vector[1]

    if (x == 1 and y == 0):
        return (0,1)
    if (x == -1 and y == 0):
        return (0,-1)
    if (x == 0 and y == 1):
        return (-1,0)
    if (x == 0 and y == -1):
        return (1,0)

last_value = 0
input_val = int(sys.argv[1])

while (last_value <= input_val):
    addToSpiral()
    last_item = spiral.popitem(last=True)
    last_value = last_item[1]
    spiral[last_item[0]] = last_item[1]
print(last_value)
