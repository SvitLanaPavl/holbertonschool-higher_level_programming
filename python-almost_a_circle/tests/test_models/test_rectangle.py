import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Unittest classes"""


class TestRectangle(unittest.TestCase):
    '''The subclass of the TestCase to test Rectangle'''
    def test_init_id(self):
        '''Testing the __init__ method'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

