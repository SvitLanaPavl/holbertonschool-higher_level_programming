import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Unittest classes"""


class TestRectangle_init(unittest.TestCase):
    '''The subclass of the TestCase to test Rectangle'''
    def test_inheritance(self):
        '''if rectangle is base'''
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_one_arg(self):
        '''few args'''
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_no_arg(self):
        '''no args'''
        with self.assertRaises(TypeError):
            Rectangle()

    def test_many_args(self):
        '''many args'''
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 12, 13)

    def test_two_args(self):
        '''Testing a rectangle of two args'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 5)

    def test_five_args(self):
        '''Testing a rectangle of five args'''
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 12)

    def private_access_width(self):
        '''Acess private attributes'''
        r = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def private_access_height(self):
        '''Acess private attributes'''
        r = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            r.__height

    def private_access_x(self):
        '''Acess private attributes'''
        r = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            r.__x

    def private_access_y(self):
        '''Acess private attributes'''
        r = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            r.__y

    def test_area(self):
        '''Test area'''
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        '''Test display'''
        r1 = Rectangle(4, 6)
        self

class TestRectangle_values_width(unittest.TestCase):
    '''Test the values of the rectangle'''
    def test_for_None(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_for_string(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_for_float(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.1, 2)

    def test_for_negative(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_for_zero(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_for_boolean(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_for_list(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([], 2)

    def test_for_list_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 2)

    def test_for_list_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_for_set(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({}, 2)

    def test_for_set_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1}, 2)

    def test_for_set_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_for_tuple(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((), 2)

    def test_for_tuple_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1,), 2)

    def test_for_tuple_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)
    
    def test_for_dict(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 10}, 2)

class TestRectangle_values_height(unittest.TestCase):
    '''Test the values of the rectangle'''
    def test_for_None(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_for_string(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_for_float(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.1)

    def test_for_negative(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_for_zero(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_for_boolean(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)

    def test_for_list(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [])

    def test_for_list_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [2])

    def test_for_list_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [1, 2, 3])

    def test_for_set(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {})

    def test_for_set_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {2})

    def test_for_set_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {1, 2, 3})

    def test_for_tuple(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, ())

    def test_for_tuple_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (2,))

    def test_for_tuple_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (1, 2, 3))
    
    def test_for_dict(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {"a": 2})

class TestRectangle_values_x(unittest.TestCase):
    '''Test the values of the rectangle'''
    def test_for_None(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None, 1, 12)

    def test_for_string(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "1", 1, 12)

    def test_for_float(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 1.1, 1, 12)

    def test_for_negative(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 1, 12)

    def test_for_boolean(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, True, 1, 12)

    def test_for_list(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [], 1, 12)

    def test_for_list_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1], 1, 12)

    def test_for_list_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1, 2, 3], 1, 12)

    def test_for_set(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {}, 1, 12)

    def test_for_set_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {1}, 1, 12)

    def test_for_set_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {1, 2, 3}, 1, 12)

    def test_for_tuple(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (), 1, 12)

    def test_for_tuple_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (1,), 1, 12)

    def test_for_tuple_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, (1, 2, 3), 1, 12)
    
    def test_for_dict(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {"a": 1}, 1, 12)

class TestRectangle_values_y(unittest.TestCase):
    '''Test the values of the rectangle'''
    def test_for_None(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, None, 12)

    def test_for_string(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, "1", 12)

    def test_for_float(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, 1.1, 12)

    def test_for_negative(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 1, -1, 12)

    def test_for_boolean(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, True, 12)

    def test_for_list(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, [], 12)

    def test_for_list_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, [1], 12)

    def test_for_list_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, [1, 2, 3], 12)

    def test_for_set(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, {}, 12)

    def test_for_set_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, {1}, 12)

    def test_for_set_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, {1, 2, 3}, 12)

    def test_for_tuple(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, (), 12)

    def test_for_tuple_1(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, (1,), 12)

    def test_for_tuple_full(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, (1, 2, 3), 12)
    
    def test_for_dict(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, {"a": 1}, 12)
