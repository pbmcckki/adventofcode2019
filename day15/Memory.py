class Memory(list):
    def __getitem__(self, item):
        if (item + 1) > len(self):
            self.resize(item)
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if (key + 1) > len(self):
            self.resize(key)
        return super().__setitem__(key, value)

    def resize(self, pos):
        self.extend([0] * (pos + 1 - len(self)))

    def copy(self):
        return Memory(self)