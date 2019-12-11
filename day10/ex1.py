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
with open('test2.txt') as f:
    for line in f:
        bitmap.append(line.strip())

y_size = len(bitmap)
x_size = len(bitmap[0])

locations = [(x, y) for y in range(0, y_size) for x in range(0, x_size) if bitmap[y][x] == "#"]

for location in locations:
    # Calculate vector
    vectors = [(x[0] - location[0], x[1] - location[1]) for x in locations if (x[0], x[1]) != location]
    # print(location, vectors)
    # Reduce vectors
    vectors_reduced = vectors
    for element in vectors:

        denominator = find_denominator(*element)
        root_element = (element[0] / denominator, element[1] / denominator)
        # print(" ELEMENT: {} ROOT: {}".format(element,root_element))
        for element_tested in vectors:
            if element_tested == element:
                continue

            # Root is horizontal and element is horizontal
            if (root_element[0] != 0) and (element_tested[1] == root_element[1] == 0):
                # Root and tested element have same X direction
                if root_element[0] * element_tested[0] > 0:
                    vectors_reduced.remove(element_tested)
                    # print("REMOVING {}   ".format(element_tested),end="")

            # Root is vertical and element is vertical
            elif (root_element[0] == element_tested[0] == 0) and (root_element[1] != 0):
                # Root and tested element have same Y direction
                if root_element[1] * element_tested[1] > 0:
                    vectors_reduced.remove(element_tested)
                    # print("REMOVING {}   ".format(element_tested),end="")

            # Root is not perpendicular ;-)
            elif (element_tested[0] != 0) and (element_tested[1] != 0):
                # Root and tested element have same directions
                if (root_element[0] * element_tested[0] > 0) and (root_element[1] * element_tested[1] > 0):
                    # Element is multiplication of root (same factor for x and y)
                    if (element_tested[0] % root_element[0] == 0) and (element_tested[1] % root_element[1] == 0) and (
                            element_tested[0] / root_element[0] == element_tested[1] / root_element[1]):
                        # print("REMOVING {}   ".format(element_tested),end="")
                        vectors_reduced.remove(element_tested)
            # print(vectors_reduced)
    # print('-'*20)

    view = len(vectors_reduced)
    print(location, view)
    result[view] = location
largest_view = max(result.keys())
print(largest_view, result[largest_view])
