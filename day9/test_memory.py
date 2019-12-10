from unittest import TestCase
from Memory import Memory


class TestMemory(TestCase):
    def test_read(self):
        a = Memory([1, 2, 3])
        self.assertEqual(a[2], 3, "Retrieve failed")
        self.assertEqual(a[10], 0, "Retrieve beyond range failed")
        self.assertEqual(len(a), 11, "Invalid length")

    def test_write(self):
        a = Memory([1, 2, 3])
        a[2] = 5
        self.assertEqual(a[2], 5, "Retrieve/save failed")
        a[10] = 7
        self.assertEqual(a[10], 7, "Retrieve/save beyond range failed")
        self.assertEqual(a[9], 0, "Retrieve/save beyond range failed")
        self.assertEqual(len(a), 11, "Invalid length")

    def test_copy(self):
        a = Memory(range(0, 10))
        b = a.copy()
        print(type(b))
        a[3] = 77
        self.assertEqual(b[3], 3, "Failed copy")
        a[99] = 77
        self.assertEqual(len(b), 10, "Failed copy - invalid length")
        self.assertEqual(b[99], 0, "Failed copy")
