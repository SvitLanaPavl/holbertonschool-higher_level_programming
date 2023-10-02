#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
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
    
    def test_float_id(self):
        '''float id'''
        b1 = Base(1.1)
        self.assertEqual(b1.id, 1.1)

    def test_bool_id(self):
        '''bool id'''
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_list_F_id(self):
        '''bool id'''
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_list_id(self):
        '''bool id'''
        b1 = Base([1,])
        self.assertEqual(b1.id, [1,])

    def test_tuple_id(self):
        '''tuple id'''
        b1 = Base((1))
        self.assertEqual(b1.id, (1))

    def test_tuple_m_id(self):
        '''tuple id'''
        b1 = Base((1, 2, 3))
        self.assertEqual(b1.id, (1, 2, 3))

    def test_dict_id(self):
        '''dict id'''
        b1 = Base({'1': 2})
        self.assertEqual(b1.id, {'1': 2})

    def test_set_id(self):
        '''set id'''
        b1 = Base({2})
        self.assertEqual(b1.id, {2})

    def test_arg(self):
        '''many args'''
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_private_access(self):
        '''test accessing private attributes'''
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects

class TestBase_to_json_string(unittest.TestCase):
    '''Test to json string'''
    def test_empty_list(self):
        '''to json testing'''
        result = Base.to_json_string([])
        self.assertTrue(type(result) is str)
        self.assertEqual(result, "[]")

    def test_none_list(self):
        '''to json testing'''
        result = Base.to_json_string(None)
        self.assertTrue(type(result) is str)
        self.assertEqual(result, "[]")

    def test_regular_list(self):
        '''to json testing'''
        Base.__Base__nb_objects = 0
        rec1 = {"id": 10, "width": 10, "height": 10, "x": 10, "y": 10}
        rec2 = {"id": 5, "width": 5, "height": 5, "x": 5, "y": 5}
        result_str = Base.to_json_string([rec1, rec2])
        self.assertTrue(type(result_str) is str)
        result_loads = json.loads(result_str)
        self.assertEqual(result_loads, [rec1, rec2])
