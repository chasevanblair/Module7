import unittest
from unittest.mock import patch

from fun_with_collections import basic_list


class TestList(unittest.TestCase):
    #@patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self):
        self.assertEqual(basic_list.make_list(), [2, 2, 2])
