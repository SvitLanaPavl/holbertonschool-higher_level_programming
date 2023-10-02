import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO
"""Unittest classes"""


class TestSquare_init(unittest.TestCase):
    '''The subclass of the TestCase to test Square'''
    def test_base_inheritance(self):
        '''if square is base'''
        self.assertIsInstance(Square(2), Base)

    def test_rectangle_inheritance(self):
        '''if square is base'''
        self.assertIsInstance(Square(2), Rectangle)

    def test_no_args(self):
        '''no args test'''
        with self.assertRaises(TypeError):
            Square()

    def test_many_args(self):
        '''test many args'''
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_one_arg(self):
        '''test one arg'''
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_two_args(self):
        '''test two args'''
        s = Square(5, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        
    def test_three_args(self):
        '''test three args'''
        s = Square(5, 5, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

    def test_four_args(self):
        '''test three args'''
        s = Square(5, 5, 5, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)
        self.assertEqual(s.id, 89)

    def private_access_width(self):
        '''Acess private attributes'''
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.__width

    def private_access_height(self):
        '''Acess private attributes'''
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.__height

    def private_access_x(self):
        '''Acess private attributes'''
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.__x

    def private_access_y(self):
        '''Acess private attributes'''
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.__y

class TestSquare_values_width(unittest.TestCase):
    '''Test the values of the square'''
    def test_for_None(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_for_string(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5", 5, 5, 5)

    def test_for_float(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5, 5, 5, 5)

    def test_for_zero(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 5, 5, 5)

    def test_for_negative(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5, 5, 5, 5)

    def test_for_dict(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({'5': 5}, 5, 5, 5)

    def test_for_bool(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 5, 5, 5)

    def test_for_list_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([], 5, 5, 5)

    def test_for_list_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([5], 5, 5, 5)

    def test_for_set_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({}, 5, 5, 5)

    def test_for_set_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({5}, 5, 5, 5)

    def test_for_tuple_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((), 5, 5, 5)

    def test_for_tuple_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((5,), 5, 5, 5)

class TestSquare_values_x(unittest.TestCase):
    '''Test the values of the square'''
    def test_for_None(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, None)

    def test_for_string(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "5", 5, 5)

    def test_for_float(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, 5.5, 5, 5)

    def test_for_negative(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -5, 5, 5)

    def test_for_dict(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {'5': 5}, 5, 5)

    def test_for_bool(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, True, 5, 5)

    def test_for_list_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [], 5, 5)

    def test_for_list_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [5], 5, 5)

    def test_for_set_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {}, 5, 5)

    def test_for_set_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {5}, 5, 5)

    def test_for_tuple_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, (), 5, 5)

    def test_for_tuple_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, (5,), 5, 5)

class TestSquare_values_y(unittest.TestCase):
    '''Test the values of the square'''
    def test_for_None(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, None)

    def test_for_string(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, "5", 5)

    def test_for_float(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, 5.5, 5)

    def test_for_negative(self):
        '''data type value errors'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 5, -5, 5)

    def test_for_dict(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, {'5': 5}, 5)

    def test_for_bool(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, True, 5)

    def test_for_list_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, [], 5)

    def test_for_list_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, [5], 5)

    def test_for_set_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, {}, 5)

    def test_for_set_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, {5}, 5)

    def test_for_tuple_em(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, (), 5)

    def test_for_tuple_fl(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, (5,), 5)
    
    def test_for_string_several(self):
        '''data type value errors'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5", 5, 5, "5")

class TestSquare_area(unittest.TestCase):
    '''Test rectangle area'''
    def test_area_regular(self):
        '''Test area'''
        s = Square(5)
        self.assertEqual(s.area(), 25)
        s = Square(2, 10, 10, 10)
        self.assertEqual(s.area(), 4)
        s = Square(111111111111111, 7, 0, 12)
        self.assertEqual(s.area(), 12345679012345654320987654321)

    def test_area_change(self):
        '''test area when an argument changes'''
        sq = Square(5, 7, 8, 9)
        self.assertEqual(sq.area(), 25)
        sq.size = 6
        self.assertEqual(sq.area(), 36)

    def test_one_arg_area(self):
        '''test one arg in area'''
        sq = Square(5, 7, 8, 9)
        with self.assertRaises(TypeError):
            sq.area(5)

class TestSquare_display(unittest.TestCase):
    '''Test square display'''
    def setUp(self):
        self.saved_stdout = sys.stdout
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        '''Restore the original sys.stdout'''
        sys.stdout = self.saved_stdout
        self.captured_output.close()

    def test_display_regular(self):
        '''test display'''
        sqr = Square(3)
        exp_output = "###\n###\n###\n"
        sqr.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)

    def test_display_regular_full(self):
        '''test display'''
        sqr = Square(3, 2, 3, 9)
        exp_output = "\n\n\n  ###\n  ###\n  ###\n"
        sqr.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)
    
    def test_display_x(self):
        '''test display with x'''
        sqr = Square(2, 3, 4, 7)
        sqr.x = 4
        exp_output = "\n\n\n\n    ##\n    ##\n"
        sqr.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)

    def test_display_y(self):
        '''test display with y'''
        sqr = Square(2, 3, 4, 10)
        sqr.x = 4
        sqr.y = 2
        exp_output = "\n\n    ##\n    ##\n"
        sqr.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)

    def test_display_wr_args(self):
        '''wrong num of args'''
        sqr = Square(4, 6, 2, 12)
        with self.assertRaises(TypeError):
            sqr.display(1)
