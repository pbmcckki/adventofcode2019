import re

pattern = re.compile('(\d+ \w+)')

chemicals = dict()
chemicals_one_cycle = dict()


class Chemical:
    def __init__(self, name, batch, ingredients):
        self.name = name
        self.quantity = 0
        self.batch = batch
        self.ingredients = ingredients
        self.composed = 0

    def compose(self, number):
        if number % self.batch == 0:
            batches_to_create = number // self.batch
        else:
            batches_to_create = number // self.batch + 1
        if self.ingredients:
            for chemical, quantity in self.ingredients.items():
                chemicals[chemical].use(quantity * batches_to_create)

        self.quantity += batches_to_create * self.batch
        self.composed += batches_to_create * self.batch

    def use(self, number):
        if self.quantity < number:
            self.compose(number - self.quantity)
        self.quantity -= number


with open("input2.txt") as f:
    for line in f:
        line = line.strip()
        groups = pattern.findall(line)
        ingredients = dict()
        for group in groups[:-1]:
            quantity, chemical = group.split()
            quantity = int(quantity)
            ingredients[chemical] = quantity
        batch, name = groups[-1].split()
        batch = int(batch)
        chemicals[name] = Chemical(name, batch, ingredients)
        chemicals_one_cycle[name] = Chemical(name, batch, ingredients)

chemicals['ORE'] = Chemical('ORE', 1, None)

chemicals_one_cycle = {chemical: chemicals[chemical].quantity for chemical in chemicals}

count = 0
while True:
    count += 1
    chemicals['FUEL'].use(1)
    for chemical in chemicals:
        if chemicals[chemical].quantity == chemicals_one_cycle[chemical]:
            continue
        else:
            break
    else:
        break

total = 1000000000000
ore_used = chemicals['ORE'].composed
cycles = total // ore_used
chemicals['FUEL'].composed = count * cycles
chemicals['ORE'].quantity = total % ore_used

ore_used = chemicals['ORE'].composed
while ore_used == chemicals['ORE'].composed:
    chemicals['FUEL'].use(1)

print(chemicals['FUEL'].composed - 1)
