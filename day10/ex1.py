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
    angles = set()

    # Reduce each element by largest common denominator (N)
    # Each angle is N*X,N*Y so can be reduced by N and still be the same angle!

    for element in vectors:
        denominator = find_denominator(*element)
        root_element = (element[0] / denominator, element[1] / denominator)

        angle = root_element
        angles.add(angle)

    result[len(angles)] = location

largest_view = max(result.keys())
print(largest_view, result[largest_view])

