from functools import reduce

layers = []
layer_size = 25 * 6
count = 0
with open('input.txt') as f:
    while True:
        layer = f.read(layer_size)
        if len(layer) < layer_size:
            break
        layers.append(layer)

image = []
layers_stacked = list(zip(*layers))


def flatten(i, j):
    if i != '2':
        return i
    else:
        return j


for pixel in layers_stacked:
    image.append(reduce(flatten, pixel))

# Do some repainting for clearer view :)
image = [' ' if x == '0' else "X" for x in image]

for y in range(0, 6):
    for x in range(0, 25):
        print(image[x + 25 * y], sep="", end="")
    print("")
