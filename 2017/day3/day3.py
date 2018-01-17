import sys
import math

index = int(sys.argv[1])

def layer(index):
    return (math.ceil((math.sqrt(index) - 1) / 2) * 2) + 1

def steps_from_end_of_layer(index):
    return abs(index - layer(index) ** 2)

def step_difference(index):
    acc = 0
    flip_val = (layer(index) - 1) / 2
    count = 0
    increment = True
    for x in range(0, steps_from_end_of_layer(index)):
        if increment:
            acc += 1
        else:
            acc -= 1
        count += 1
        if count == flip_val:
            increment = not increment
            count = 0
    return acc

def solve(index):
    return (layer(index) - 1) - step_difference(index)

print(solve(index))