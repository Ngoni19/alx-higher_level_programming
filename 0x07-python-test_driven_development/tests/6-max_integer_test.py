#!/usr/bin/python3
"""Unittest too find max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """run-> python3 -m unittest -v tests.6-max_integer_test"""

    def test_module_docstr(self):
        ModuleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(ModuleDoc) > 1)

    def test_funct_docstr(self):
        funcDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(funcDoc) > 1)

    def test_signed_ints_and_floats(self):
        self.assertEqual(max_integer([{2, 4}, {2}, {3}]), {2, 4})
        self.assertEqual(max_integer([-1.7, -3.3]), -1.7)
        self.assertEqual(max_integer([1, 2, 7, -3]), 7)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, -9, 9]), 9)
        self.assertEqual(max_integer([0]), 0)    
    
    def test_list_of_str(self):
        self.assertEqual(max_integer(['e', 'f', 'g', 'x', 'y', 'z']), 'z')
        self.assertEqual(max_integer(["efg", 'x']), 'x')
        self.assertEqual(max_integer("efgxyz"), 'z')
        self.assertEqual(max_integer("1234"), '4')

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 4]]), [1, 4])

    def test_other_seq(self):
        with self.assertRaises(TypeError):
            max_integer({2, 3}, {4, 5, 6})
        with self.assertRaises(TypeError):
            max_integer({3, 4, 5, 6, 7})
        with self.assertRaises(TypeError):
            max_integer([-11, 4.5, "str", {3, 2}])
        with self.assertRaises(TypeError):
            max_integer([None, True])

    def test_None(self):
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        

if __name__ == "__main__":
    unittest.main()
