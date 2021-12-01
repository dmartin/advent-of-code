with open("input.txt") as f:
    last = None
    count = 0
    for line in f.readlines():
        current = int(line)
        if last and current > last:
            count += 1
        last = current
print(count)
