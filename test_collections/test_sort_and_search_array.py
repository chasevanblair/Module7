import unittest
import array as arr
from fun_with_collections.sort_and_search_array import *


class TestArrays(unittest.TestCase):

    def test_search_fail(self):
        a = arr.array('i', [0, 3, 23, 22])
        self.assertEqual(-1, search_array(a, 44))

    def test_search_found(self):
        a = arr.array('i', [0, 3, 23, 22])
        self.assertLessEqual(0, search_array(a, 23))

    def test_sort_array(self):
        a = arr.array('i', [35, 3, 23, 22])
        x = len(a)
        a = sort_array(a)
        self.assertLessEqual(a[0], a[x - 1])


if __name__ == '__main__':
    unittest.main()
