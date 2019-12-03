def calculate_fuel(mass):
    fuel = int(mass / 3) - 2
    if fuel > 0:
        fuel = fuel + calculate_fuel(fuel)
        return fuel
    return 0


accumulator = 0
with open('input.txt') as f:
    for line in f:
        val = int(line.strip())
        accumulator += calculate_fuel(val)

print(accumulator)
