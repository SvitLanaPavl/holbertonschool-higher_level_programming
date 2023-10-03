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

    def test_private_access_width(self):
        '''Acess private attributes'''
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.__width

    def test_private_access_height(self):
        '''Acess private attributes'''
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.__height

    def test_private_access_x(self):
        '''Acess private attributes'''
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.__x

    def test_private_access_y(self):
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


class TestSquare_string(unittest.TestCase):
    '''test string representation'''
    def test_str_full(self):
        '''test str representation'''
        sq = Square(4, 6, 2, 12)
        exp_output = "[Square] (12) 6/2 - 4"
        self.assertEqual(sq.__str__(), exp_output)

    def test_str_2arg(self):
        '''test string 2 args given'''
        sq = Square(2, 2)
        exp_output = "[Square] ({}) 2/0 - 2".format(sq.id)
        self.assertEqual(sq.__str__(), exp_output)

    def test_str_3arg(self):
        '''test string 3 args'''
        sq = Square(2, 2, 1)
        exp_output = "[Square] ({}) 2/1 - 2".format(sq.id)
        self.assertEqual(sq.__str__(), exp_output)

    def test_changed_values(self):
        '''update values'''
        sq = Square(4, 6, 2, 12)
        sq.size = 5
        sq.x = 3
        sq.y = 2
        exp_output = "[Square] (12) 3/2 - 5"
        self.assertEqual(sq.__str__(), exp_output)

    def test_wrong_num_args(self):
        '''wrong arg num'''
        sq = Square(4, 6, 2, 12)
        with self.assertRaises(TypeError):
            sq.__str__(1)


class TestSquare_update(unittest.TestCase):
    '''test update function'''

    def test_update_call(self):
        '''calling update no args'''
        sq = Square(10, 10, 10, 10)
        exp_output = "[Square] (10) 10/10 - 10"
        sq.update()
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_1arg(self):
        '''update one arg'''
        sq = Square(10, 10, 10, 10)
        sq.update(89)
        exp_output = "[Square] (89) 10/10 - 10"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_2args(self):
        '''update two args'''
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        exp_output = "[Square] (89) 10/10 - 2"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_3args(self):
        '''update three args'''
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3)
        exp_output = "[Square] (89) 3/10 - 2"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_4args(self):
        '''update four args'''
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        exp_output = "[Square] (89) 3/4 - 2"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_5args(self):
        '''update six args'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaises(IndexError):
            sq.update(89, 2, 3, 4, 5)
        # exp_output = "[Rectangle] (89) 3/4 - 2"
        # self.assertEqual(sq.__str__(), exp_output)

    def test_update_args_twice(self):
        '''update six args'''
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        sq.update(89, 3, 3, 3)
        exp_output = "[Square] (89) 3/3 - 3"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_args_invalid_size(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, '2')

    def test_update_args_negative_size(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(89, -2)

    def test_update_args_zero_size(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(89, 0)

    def test_update_args_invalid_x(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(89, 2, '3')

    def test_update_args_negative_x(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(89, 2, -3)

    def test_update_args_invalid_y(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(89, 2, 3, '4')

    def test_update_args_negative_y(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(89, 2, 3, -4)

    def test_update_args_invalid_several(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(89, '2', 3, '5')

    def test_update_args_negative(self):
        '''update with an invalid arg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(89, -2, 4, -5)


class TestSquare_update_kwargs(unittest.TestCase):
    '''test update kwargs function'''
    def test_update_kwargs_size(self):
        '''calling update size'''
        sq = Square(10, 10, 10, 10)
        sq.update(size=2)
        exp_output = "[Square] (10) 10/10 - 2"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_kwargs_size_x(self):
        '''calling update size and x'''
        sq = Square(10, 10, 10, 10)
        sq.update(size=2, x=2)
        exp_output = "[Square] (10) 2/10 - 2"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_kwargs_width_y_x_id(self):
        '''calling update y width x id'''
        sq = Square(10, 10, 10, 10)
        sq.update(y=1, size=2, x=3, id=89)
        exp_output = "[Square] (89) 3/1 - 2"
        self.assertEqual(sq.__str__(), exp_output)

    def test_update_kwargs_invalid_size(self):
        '''update with an invalid kwarg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size='2')

    def test_update_kwargs_negative_size(self):
        '''update with an invalid kwarg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-2)

    def test_update_kwargs_zero_size(self):
        '''update with an invalid kwarg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=0)

    def test_update_kwargs_invalid_x(self):
        '''update with an invalid kwarg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x='2')

    def test_update_kwargs_negative_x(self):
        '''update with an invalid kwarg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-2)

    def test_update_kwargs_invalid_y(self):
        '''update with an invalid kwarg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y='2')

    def test_update_kwargs_negative_y(self):
        '''update with an invalid kwarg'''
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-2)

    '''def test_update_kwargs_and_args(self):
        update with kwargs and args'''
    '''sq = Square(10, 10, 10, 10)
        sq.update(89, 2, x=4, y=5)
        exp_output = "[Square] (89) 4/5 - 2"
        self.assertEqual(sq.__str__(), exp_output)'''

    def test_update_kwargs_and_args_wrkeys(self):
        '''update with wrong keys'''
        sq = Square(10, 10, 10, 10)
        sq.update(89, a=2, b=3, c=4, d=5)
        exp_output = "[Square] (89) 10/10 - 10"
        self.assertEqual(sq.__str__(), exp_output)

    '''def test_update_kwargs_and_args_smwrkeys(self):
        update with some wrong keys'''
    '''sq = Square(10, 10, 10, 10)
        sq.update(89, b=3, x=4, y=5)
        exp_output = "[Square] (89) 4/5 - 10"
        self.assertEqual(sq.__str__(), exp_output)
    '''


if __name__ == "__main__":
    unittest.main()
