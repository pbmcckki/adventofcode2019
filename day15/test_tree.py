from unittest import TestCase
from Tree import Tree

class TestStep(TestCase):
    def setUp(self):
        self.root = Tree(None)
        self.leaf1 = self.root.add_leaf()
        self.leaf2 = self.root.add_leaf()
        self.leaf11 = self.leaf1.add_leaf()
        self.leaf12 = self.leaf1.add_leaf()

    def test_init(self):
        self.assertEqual(self.root.get_terminal_leafs(), self.leaf12.terminal_leafs)
        self.assertEqual(len(self.root.get_terminal_leafs()), 3)

    def test_depth(self):
        self.assertEqual(self.root.get_depth(), 1)
        self.assertEqual(self.leaf2.get_depth(), 2)
        self.assertEqual(self.leaf11.get_depth(), 3)
        self.assertEqual(self.leaf12.get_depth(), 3)

    def test_iterate(self):
        for node in self.root.get_terminal_leafs():
            print("Going from depth",node.get_depth())
            count = 0
            for leaf in node.go_upstream():
                print(leaf, leaf.get_depth())
                count += 1
            self.assertEqual(count, node.get_depth())
