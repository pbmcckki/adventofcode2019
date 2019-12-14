import math
from concurrent.futures import ThreadPoolExecutor


# WHY PYTHON 3 DOES NOT HAVE CMP!?!?
def cmp(a, b):
    return (a > b) - (a < b)


def calc_cycle(x_coords):
    history = []
    x_velocity = [0, 0, 0, 0]

    while True:
        history.append(x_coords + x_velocity)
        for x in range(0, 4):
            x_gravity = sum((cmp(coord, x_coords[x]) for coord in x_coords))
            x_velocity[x] += x_gravity
        x_coords = list(map(lambda a, b: a + b, x_coords, x_velocity))

        if x_coords + x_velocity in history:
            x_cycle = len(history)
            break
    print(x_cycle)
    return x_cycle


# Input so plain that just pasted instead loading from file
coordinates = [[9, -3, -4, 0], [13, 16, 11, -2], [-8, -17, -10, -2]]
cycles = []
# Every dimension is independent so it has also its own cycle.
with ThreadPoolExecutor(max_workers=3) as executor:
    cycles = list(executor.map(calc_cycle, coordinates))


x_cycle = cycles[0]
y_cycle = cycles[1]
z_cycle = cycles[2]

# Now lets find lowest common multiply
xy_cycle = x_cycle * y_cycle // math.gcd(x_cycle, y_cycle)
xzy_cycle = xy_cycle * z_cycle // math.gcd(xy_cycle, z_cycle)
print(xzy_cycle)
