import re

count = 0
pattern = re.compile('(\d+ \w+)')

chemicals = dict()
chemicals.items()


class Chemical:
    def __init__(self, name, batch, ingredients):
        self.name = name
        self.quantity = 0
        self.batch = batch
        self.ingredients = ingredients
        self.composed = 0

    def compose(self, number):
        print("Composing", number, self.name)
        if number % self.batch == 0:
            batches_to_create = number // self.batch
        else:
            batches_to_create = number // self.batch + 1
        print("Batches to create:", batches_to_create, "by", self.batch, "of", self.name)
        if self.ingredients:
            for chemical, quantity in self.ingredients.items():
                print("Need", quantity * batches_to_create, "of", chemical)
                chemicals[chemical].use(quantity * batches_to_create)

        self.quantity += batches_to_create * self.batch
        self.composed += batches_to_create * self.batch
        print(self.name, "- Currently available", self.quantity, "Total produced", self.composed)

    def use(self, number):
        print("Using ", number, " of ", self.name)
        if self.quantity < number:
            self.compose(number - self.quantity)
        self.quantity -= number
        print("Left ", self.quantity,"of", self.name)


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
chemicals['FUEL'].use(1)
print(chemicals['ORE'].composed)
