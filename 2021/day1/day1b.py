from collections import deque
from itertools import islice

with open("input.txt") as f:
    history = deque(maxlen=4)
    count = 0
    for i, line in enumerate(f.readlines()):
        history.append(int(line))
        if i >= 3 and sum(islice(history, 1, 4)) > sum(islice(history, 0, 3)):
            count += 1
print(count)
