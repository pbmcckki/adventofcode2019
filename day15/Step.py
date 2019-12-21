from Tree import Tree


class Step(Tree):
    def __init__(self, upstream, coords, value):
        super(Step, self).__init__(upstream)
        self.coords = coords
        self.value = value

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
