from functools import cmp_to_key
from itertools import cycle


# This is tricky description to find larges common denominator
def find_denominator(a, b):
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return max(a, b)
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


bitmap = []
locations = []
result = dict()
max_visibility = 0
max_angles = dict()

with open('input.txt') as f:
    for line in f:
        bitmap.append(line.strip())

y_size = len(bitmap)
x_size = len(bitmap[0])

locations = [(x, y) for y in range(0, y_size) for x in range(0, x_size) if bitmap[y][x] == "#"]

for location in locations:
    # Calculate vector
    vectors = [(x[0] - location[0], x[1] - location[1]) for x in locations if (x[0], x[1]) != location]

    # Reduce vectors to angles - each angle is separate asteroids, but each does not count twice so we use set
    angles = dict()

    # Reduce each element by largest common denominator (N)
    # Each angle is N*X,N*Y so can be reduced by N and still be the same angle!

    for element in vectors:
        denominator = find_denominator(*element)
        root_element = (element[0] / denominator, element[1] / denominator)

        angle = root_element

        # Add coords to a list of asteroids at the same angle
        vectors_at_angle = angles.get(angle, list())
        vectors_at_angle.append(element)
        angles[angle] = vectors_at_angle

    result[len(angles.keys())] = location
    if max_visibility < len(angles.keys()):
        max_angles = angles
        max_visibility = len(angles.keys())

location = result[max_visibility]


# Now lets figure out how to sort by angle
def get_quarter(x, y):
    if x >= 0 and y < 0:
        return 1
    elif x > 0 and y >= 0:
        return 2
    elif x <= 0 and y > 0:
        return 3
    elif x < 0 and y <= 0:
        return 4
    else:
        raise Exception("Bad angle")


# Seriously no cmp in python 3...
def cmp(a, b):
    return -((a > b) - (a < b))


def compare_angles(a1, a2):
    a1_q = get_quarter(*a1)
    a2_q = get_quarter(*a2)
    if a1_q < a2_q:
        return -1
    elif a1_q > a2_q:
        return 1
    # Now we land in the same quarter so watch out for same angle!
    else:
        try:
            tg_a = a1[1] / a1[0]
        except ZeroDivisionError:
            return -1
        try:
            tg_b = a2[1] / a2[0]
        except ZeroDivisionError:
            return 1
        if tg_a < tg_b:
            return -1
        else:
            return 1


# Lets sort angles
angles_sorted = sorted(max_angles, key=cmp_to_key(compare_angles))
for angle in max_angles.keys():
    sorted(max_angles[angle], key=lambda x: x[0])  # does not really matter whether x or y

counter = 0
relative_coords = None
for angle in cycle(angles_sorted):
    try:
        relative_coords = max_angles[angle].pop()
        coords = (relative_coords[0] + location[0], relative_coords[1] + location[1])
    except IndexError:
        continue
    counter += 1
    if counter == 200:
        break

coords = (relative_coords[0] + location[0], relative_coords[1] + location[1])

print(coords[0] * 100 + coords[1])
