from functools import reduce
import re


# WHY PYTHON 3 DOES NOT HAVE CMP!?!?
def cmp(a, b):
    return (a > b) - (a < b)


class Moon:

    def __init__(self, x, y, z, system):
        self.coords = [x, y, z]
        self.velocity = [0, 0, 0]
        self.system = system

    def update_velocity(self):
        for g in range(0, len(self.velocity)):
            for item in self.system:
                self.velocity[g] += cmp(item.coords[g], self.coords[g])

    def move(self):
        self.coords = list(map(lambda x, y: x + y, self.coords, self.velocity))

    def get_potential_energy(self):
        return reduce(lambda a, b: abs(a) + abs(b), self.coords)

    def get_kinetic_energy(self):
        return reduce(lambda a, b: abs(a) + abs(b), self.velocity)

    def get_total_energy(self):
        return self.get_kinetic_energy() * self.get_potential_energy()


# Input so plain that just pasted instead loading from file
jupiter_system = []
coords = [[9, 13, -8], [-3, 16, -17], [-4, 11, -10], [0, -2, -2]]
for item in coords:
    satellite = Moon(*item, jupiter_system)
    jupiter_system.append((satellite))

for i in range(0, 1000):
    for satellite in jupiter_system:
        satellite.update_velocity()
    for satellite in jupiter_system:
        satellite.move()

print(reduce(lambda a, b: a + b, (satellite.get_total_energy() for satellite in jupiter_system)))
