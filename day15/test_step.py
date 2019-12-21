from unittest import TestCase
from Step import Step


class TestTree(TestCase):
    def setUp(self):
        self.root = Step(None, (0, 0), "O")
        self.leaf1 = self.root.add_leaf(1, ".")
        self.leaf11 = self.leaf1.add_leaf(1, ".")
        self.leaf113 = self.leaf11.add_leaf(3, ".")
        self.leaf1132 = self.leaf113.add_leaf(2, ".")

    def test_terminal(self):
        self.assertSequenceEqual([self.leaf1132], self.root.get_terminal_leafs())

    def test_loop(self):
        self.leaf11324 = self.leaf1132.add_leaf(4, 'X')
        self.assertIsNone(self.leaf11324)

    def test_traverse(self):
        for node in self.leaf1132.go_upstream():
            print(node.coords, node.depth, node.value)
