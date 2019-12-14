import math


# WHY PYTHON 3 DOES NOT HAVE CMP!?!?
def cmp(a, b):
    return (a > b) - (a < b)


# Use just one history to save memory
history = []

# Input so plain that just pasted instead loading from file

x_coords = [9, -3, -4, 0]
x_velocity = [0, 0, 0, 0]
# x_gravity = 0

y_coords = [13, 16, 11, -2]
y_velocity = [0, 0, 0, 0]
# y_gravity = 0

z_coords = [-8, -17, -10, -2]
z_velocity = [0, 0, 0, 0]
# z_gravity = 0

x_cycle, y_cycle, z_cycle = 0, 0, 0

# Every dimension is independent so it has also its own cycle.
# Lets find the cycle for X
while True:
    history.append(x_coords + x_velocity)
    for x in range(0, 4):
        x_gravity = sum((cmp(coord, x_coords[x]) for coord in x_coords))
        x_velocity[x] += x_gravity
    x_coords = list(map(lambda a, b: a + b, x_coords, x_velocity))

    if x_coords + x_velocity in history:
        # print("X",history.index(x_coords + x_velocity), x_coords, x_velocity)
        x_cycle = len(history)
        break
print(x_cycle)
history = []

# Now lets find the cycle for Y
while True:
    history.append(y_coords + y_velocity)
    for y in range(0, 4):
        y_gravity = sum((cmp(coord, y_coords[y]) for coord in y_coords))
        y_velocity[y] += y_gravity
    y_coords = list(map(lambda a, b: a + b, y_coords, y_velocity))

    if y_coords + y_velocity in history:
        y_cycle = len(history)
        break
print(y_cycle)
history = []

# Now eventually find the cycle for Z
while True:
    history.append(z_coords + z_velocity)
    for z in range(0, 4):
        z_gravity = sum((cmp(coord, z_coords[z]) for coord in z_coords))
        z_velocity[z] += z_gravity
    z_coords = list(map(lambda a, b: a + b, z_coords, z_velocity))

    if z_coords + z_velocity in history:
        z_cycle = len(history)
        break
print(z_cycle)
history = []

# Now lets find lowest common multiply
xy_cycle = x_cycle * y_cycle // math.gcd(x_cycle, y_cycle)
xzy_cycle = xy_cycle * z_cycle // math.gcd(xy_cycle, z_cycle)
print(xzy_cycle)
