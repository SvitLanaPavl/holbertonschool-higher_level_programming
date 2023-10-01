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
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_num_obj(self):
        '''test number of obj'''
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base(12)
        self.assertEqual(b5.id, 12)

    def test_None(self):
        '''Test none'''
        b = Base(None)
        self.assertEqual(b.id, 1)

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
            Base(1, 1)

    def test_private_access(self):
        '''test accessing private attributes'''
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects
