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

for pixel in layers_stacked:
    for color in pixel:
        if color != '2':
            image.append(color)
            break
# Do some repainting for clearer view :)
image=[' ' if x =='0' else "X" for x in image]

for y in range(0, 6):
    for x in range(0, 25):
        print(image[x + 25 * y], sep="", end="")
    print("")
