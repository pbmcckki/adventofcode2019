system = dict()

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        core, satellite = line.split(')')
        system[satellite] = core


def traverse(path, start):
    if start != 'COM':
        traverse(path, system[start])
        path.append((system[start]))
    return path


total = 0
our_path = []
santa_path = []
# Traverse from you
our_path = list(reversed(traverse(our_path, "YOU")))
# Traverse from Santa
santa_path = list(reversed(traverse(santa_path, "SAN")))

# Find first common node
santa_length = 0
our_length = 0
for item in our_path:
    print(item)
    try:
        santa_length = santa_path.index(item)
        print("FINAL", santa_length, item)
        break
    except ValueError:
        pass
    our_length += 1

print(santa_length + our_length)
