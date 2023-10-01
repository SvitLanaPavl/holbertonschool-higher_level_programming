#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Unittest classes"""


class TestBase(unittest.TestCase):
    '''The subclass of the TestCase to test Base'''

    def test_id(self):
        '''Testing the __init__ method id'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
    
    def test_several_id(self):
        '''Testing several id's''' 
        b1 = Base(None)
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 4)

    def test_negative_id(self):
        '''negative id'''
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

    def test_string_id(self):
        '''string id''' 
        b1 = Base("Holberton")
        self.assertEqual(b1.id, "Holberton")
        b2 = Base("1")
        self.assertEqual(b2.id, "1")

    def test_arg(self):
        '''many args'''
        with self.assertRaises(TypeError):
            b1 = Base(1, 1)
