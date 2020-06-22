import unittest
import array as arr
from fun_with_collections.sort_and_search_array import search_array


class TestArrays(unittest.TestCase):

    def test_search_fail(self):
        a = arr.array('i', [0, 3, 23, 22])
        self.assertEqual(-1, search_array(a, 44))

    def test_search_found(self):
        a = arr.array('i', [0, 3, 23, 22])
        self.assertGreaterEqual(0, search_array(a, 23))


if __name__ == '__main__':
    unittest.main()
