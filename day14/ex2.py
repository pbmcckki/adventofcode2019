import re

pattern = re.compile('(\d+ \w+)')

chemicals = dict()


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


with open("input.txt") as f:
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

chemicals['ORE'] = Chemical('ORE', 1, None)

total = 1000000000000
chemicals['ORE'].quantity = total
high = total
low = 0
current = total
previous = 0

# Just binary search
while True:
    for chemical in chemicals:
        chemicals[chemical].quantity = 0
        chemicals[chemical].composed = 0
    chemicals['ORE'].quantity = total
    previous = current
    current = low + (high - low) // 2
    if previous == current:
        break

    chemicals['FUEL'].use(current)

    if chemicals['ORE'].composed > 0:
        high = current
    elif chemicals['ORE'].composed == 0 and chemicals['ORE'].quantity > 0:
        low = current

print(current)
