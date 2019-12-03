accumulator = 0
with open('input.txt') as f:
    for line in f:
        val = int(line.strip())
        accumulator += int(val/3)-2
print(accumulator)