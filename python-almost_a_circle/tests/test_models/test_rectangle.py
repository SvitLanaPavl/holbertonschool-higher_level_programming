import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Unittest classes"""


class TestRectangle(unittest.TestCase):
    '''The subclass of the TestCase to test Rectangle'''
    def test_init_param(self):
        '''Testing the __init__ method'''
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_value_type(self):
        '''data type value errors'''
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)

    def test_arg(self):
        '''few args'''
        with self.assertRaises(TypeError):
            r = Rectangle(1)
