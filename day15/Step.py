from Tree import Tree


class Step(Tree):
    def __init__(self, upstream, coords, value):
        super(Step, self).__init__(upstream)
        self.coords = coords
        self.value = value
        if value is not None:
            if upstream:
                self.value_dict = upstream.value_dict
                self.value_dict[value] = self.value_dict.get(value, list())
                self.value_dict[value].append(self)
            else:
                self.value_dict = {value: [self]}

    def add_leaf(self, direction, value=None):
        if direction == 1:
            coords = (self.coords[0], self.coords[1] - 1)
        elif direction == 2:
            coords = (self.coords[0], self.coords[1] + 1)
        elif direction == 3:
            coords = (self.coords[0] - 1, self.coords[1])
        elif direction == 4:
            coords = (self.coords[0] + 1, self.coords[1])

        # Anti loop
        for leaf in self.go_upstream():
            if leaf.coords == coords:
                return None

        new_leaf = Step(self, coords, value)
        self.leafs.append(new_leaf)
        return new_leaf

    def set_value(self, value):
        self.value = value

    def search_by_value(self, value):
        return self.value_dict.get(value, None)

    def __str__(self):
        return "{} - {}".format(self.coords, self.value)
