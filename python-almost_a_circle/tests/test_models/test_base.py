#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
"""Unittest classes"""


class TestBase(unittest.TestCase):
    '''The subclass of the TestCase to test Base'''
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_unique(self):
        '''Testing the __init__ method id'''
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_mult_obj(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_mix_obj(self):
        '''test number of obj'''
        base1 = Base()
        base3 = Base(29)
        base4 = Base()
        self.assertEqual(base1.id, base4.id - 1)

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

    def test_complex(self):
        '''test id'''
        b = Base(complex(10))
        self.assertEqual(b.id, complex(10))

    def froze_set(self):
        '''test id'''
        b = Base(frozenset({1, 2, 3}))
        self.assertEqual(b.id, frozenset({1, 2, 3}))

    def float_inf(self):
        '''test id'''
        b = Base(float('inf'))
        self.assertEqual(b.id, float('inf'))

    def test_nan(self):
        b = Base(float('nan'))
        self.assertNotEqual(b.id, float('nan'))

    def test_wr_arg(self):
        '''many args'''
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_private_access(self):
        '''test accessing private attributes'''
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects
        with self.assertRaises(AttributeError):
            b.nb_objects

    def change_id(self):
        '''change id'''
        base = Base(20)
        base.id = 15
        self.assertEqual(base.id, 15)

class TestBase_to_json_string(unittest.TestCase):
    '''Test to json string'''
    def test_more_args(self):
        '''test more args'''
        with self.assertRaises(TypeError):
            Base.to_json_string([], 0)

    def test_no_args(self):
        '''test more args'''
        with self.assertRaises(TypeError):
            Base.to_json_string()

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
        input = [
            {"id": 10, "width": 10, "height": 10, "x": 10, "y": 10},
            {"id": 5, "width": 5, "height": 5, "x": 5, "y": 5}
        ]
        result_str = Base.to_json_string(input)
        self.assertTrue(type(result_str) is str)
        result_loads = json.loads(result_str)
        self.assertEqual(result_loads, input)

class TestBase_from_json_string(unittest.TestCase):
    '''Test from json string'''
    def test_none(self):
        '''to json testing'''
        self.assertEqual([], Base.from_json_string(None))

    def test_empty(self):
        '''to json testing'''
        self.assertEqual([], Base.from_json_string("[]"))

    def no_arg_error(self):
        '''test for no arg'''
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def more_arg_error(self):
        '''test for no arg'''
        with self.assertRaises(TypeError):
            Base.from_json_string([], 0)

    def regular_case_type_rect(self):
        '''test from str'''
        input = [{'id': 10, 'width': 10, 'height': 10, 'x': 10, 'y': 10}]
        json_input = Rectangle.to_json_string(input)
        json_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(json_output))

    def regular_case_rect(self):
        '''test from str'''
        input = [{'id': 10, 'width': 10, 'height': 10, 'x': 10, 'y': 10}]
        json_input = Rectangle.to_json_string(input)
        json_output = Rectangle.from_json_string(json_input)
        self.assertEqual(input, json_output)

    def regular_two_dict_rect(self):
        '''two dict'''
        input = [
            {'id': 10, 'width': 10, 'height': 10, 'x': 10, 'y': 10},
            {'id': 5, 'width': 5, 'height': 5, 'x': 5, 'y': 5}
            ]
        json_input = Rectangle.to_json_string(input)
        json_output = Rectangle.from_json_string(json_input)
        self.assertEqual(input, json_output)

    def regular_case_type_sq(self):
        '''test from str'''
        input = [{'id': 10, 'size': 10, 'x': 10, 'y': 10}]
        json_input = Square.to_json_string(input)
        json_output = Square.from_json_string(json_input)
        self.assertEqual(list, type(json_output))

    def regular_case_sq(self):
        '''test from str'''
        input = [{'id': 10, 'square': 10, 'x': 10, 'y': 10}]
        json_input = Square.to_json_string(input)
        json_output = Square.from_json_string(json_input)
        self.assertEqual(input, json_output)

    def regular_two_dict_sq(self):
        '''two dict'''
        input = [
            {'id': 10, 'size': 10, 'x': 10, 'y': 10},
            {'id': 5, 'size': 5, 'x': 5, 'y': 5}
            ]
        json_input = Square.to_json_string(input)
        json_output = Square.from_json_string(json_input)
        self.assertEqual(input, json_output)

class TestBase_save_to_file(unittest.TestCase):
    '''save to file method test'''
    @classmethod
    def remove_files(self):
        '''remove created files'''
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_empty_Rect(self):
        '''empty list'''
        obj_lst = []
        Rectangle.save_to_file(obj_lst)
        with open("Rectangle.json", "r") as f:
            json_cont = f.read()
        self.assertEqual(json_cont, "[]")

    def test_save_empty_Sq(self):
        '''empty file'''
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_noargs(self):
        '''save to file no args'''
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_mult_args(self):
        '''save to file no args'''
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 10)    

    def save_rect(self):
        '''save one rectangle'''
        rec = Rectangle(10, 10, 10, 10, 10)
        Rectangle.save_to_file([rec])
        expected_length = len(json.dumps(rec.to_dictionary()))
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read) == expected_length)

    def save_rect(self):
        '''save one square'''
        sq = Square(5, 5, 5, 5)
        Square.save_to_file([sq])
        expected_length = len(json.dumps(sq.to_dictionary()))
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read) == expected_length)

    def two_rect(self):
        '''two rectangles'''
        rect1 = Rectangle(2, 3, 2, 2, 2)
        rect2 = Rectangle(3, 4, 3, 3, 3)
        Rectangle.save_to_file([rect1, rect2])
        expected_length = len(json.dumps(rect1.to_dictionary())) +\
            len(json.dumps(rect2.to_dictionary()))
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read) == expected_length)

    def two_sqr(self):
        '''two rectangles'''
        sq1 = Square(2, 2, 2, 2)
        sq2 = Square(3, 3, 3, 3)
        Square.save_to_file([sq1, sq2])
        expected_length = len(json.dumps(sq1.to_dictionary())) +\
            len(json.dumps(sq2.to_dictionary()))
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read) == expected_length)

class TestBase_create(unittest.TestCase):
    '''testing create method'''
    def create_rect(self):
        '''create rectangle'''
        rec1 = Rectangle(1, 2, 3, 4, 5)
        rec1_dict = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dict)
        self.assertEqual(str(rec1), str(rec2))
        self.assertFalse(rec1 is rec2)
        self.assertIsNot(rec1, rec2)

    def create_sqr(self):
        '''create rectangle'''
        sq1 = Square(2, 2, 3, 4)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (4) 2/3 - 2", str(sq1))
        self.assertEqual("[Square] (4) 2/3 - 2", str(sq2))
        self.assertFalse(sq1 is sq2)
        self.assertIsNot(sq1, sq2)

if __name__ == "__main__":
    unittest.main()
