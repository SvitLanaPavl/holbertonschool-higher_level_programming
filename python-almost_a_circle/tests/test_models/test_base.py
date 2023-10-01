#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Unittest classes"""


class TestBase(unittest.TestCase):
    '''The subclass of the TestCase to test Base'''

    def test_init_id(self):
        '''Testing the __init__ method id'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base(-1)
        self.assertEqual(b6.id, -1)
        b7 = Base("Holberton")
        self.assertEqual(b7.id, "Holberton")
