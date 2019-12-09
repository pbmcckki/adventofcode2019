layers=dict()
layer_size = 25*6
with open('input.txt') as f:
    while True:
        layer = f.read(layer_size)
        if len(layer)<layer_size:
            break
        num_zeros = layer.count('0')
        layers[num_zeros]=layer.count('1')*layer.count('2')

min_zeros = min(layers.keys())
print(layers[min_zeros])

