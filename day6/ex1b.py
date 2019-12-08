def count_orbits(system, item):
    orbits = 1
    if system[item] == 'COM':
        return orbits
    else:
        return orbits + count_orbits(system, system[item])


system = dict()

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        core, satellite = line.split(')')
        system[satellite] = core

total = 0
for item in system.keys():
    total = total + count_orbits(system, item)

print(total)
