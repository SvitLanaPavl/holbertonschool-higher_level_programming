#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Subclass of the TestCase testing the max_integer function"""
    def test_empty_list(self):
        """Tests if it returns None when the list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Tests that the function returns the element of the
        list when there is one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_multiple_elements_list(self):
        """Tests that the function returns the largest element
        of the list when there are multiple elements"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_numbers(self):
        """Tests that the function returns the largest element
        of the list when there are negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_non_numeric_elem(self):
        """Tests that the function raises a TypeError when
        the list contains non numeric elements"""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == "__main__":
    unittest.main()
