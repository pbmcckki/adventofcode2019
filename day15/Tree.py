class Tree:
    def __init__(self, upstream):
        self.upstream = upstream
        self.leafs = []

        if upstream:
            self.depth = upstream.depth + 1
            self.terminal_leafs = upstream.terminal_leafs
            self.terminal_leafs.append(self)
            try:
                self.terminal_leafs.remove(upstream)
            except ValueError:
                pass
        else:
            self.terminal_leafs = [self]
            self.depth = 1

    def add_leaf(self):
        new_leaf = Tree(self)
        self.leafs.append(new_leaf)
        return new_leaf

    def get_terminal_leafs(self):
        return self.terminal_leafs

    def go_upstream(self):
        current = self
        while current:
            yield current
            current = current.upstream

    def get_depth(self):
        return self.depth
