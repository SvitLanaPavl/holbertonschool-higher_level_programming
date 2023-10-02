import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO
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
        self.assertEqual(r1.id, 14)

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

class TestRectangle_area(unittest.TestCase):
    '''Test rectangle area'''
    def test_area_regular(self):
        '''Test area'''
        rc = Rectangle(3, 2)
        self.assertEqual(rc.area(), 6)
        rc = Rectangle(2, 10)
        self.assertEqual(rc.area(), 20)
        rc = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rc.area(), 56)

    def test_area_change(self):
        '''test area when an argument changes'''
        rec = Rectangle(3, 2)
        self.assertEqual(rec.area(), 6)
        rec.width = 2
        self.assertEqual(rec.area(), 4)
        rec.height = 4
        self.assertEqual(rec.area(), 8)

    def test_area_1arg(self):
        '''test area for 1 arg'''
        rec1 = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            rec1.area(3)

class TestRectangle_display(unittest.TestCase):
    '''Test rectangle display'''
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
        rct = Rectangle(4, 4)
        exp_output = "####\n####\n####\n####\n"
        rct.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)

    def test_display_regular_full(self):
        '''test display'''
        rct = Rectangle(4, 4, 2, 2, 9)
        exp_output = "\n\n  ####\n  ####\n  ####\n  ####\n"
        rct.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)
    
    def test_display_x(self):
        '''test display with x'''
        rect = Rectangle(4, 4)
        rect.x = 4
        exp_output = "    ####\n    ####\n    ####\n    ####\n"
        rect.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)

    def test_display_y(self):
        '''test display with y'''
        rect = Rectangle(4, 4)
        rect.x = 4
        rect.y = 2
        exp_output = "\n\n    ####\n    ####\n    ####\n    ####\n"
        rect.display()
        self.assertEqual(self.captured_output.getvalue(), exp_output)

    def test_display_wr_args(self):
        '''wrong num of args'''
        rectn = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaises(TypeError):
            rectn.display(1)

class TestRectangle_string(unittest.TestCase):
    '''test string representation'''
    def test_str_full(self):
        '''test str representation'''
        rect1 = Rectangle(4, 6, 2, 1, 12)
        exp_output = "[Rectangle] ({}) 2/1 - 4/6".format(rect1.id)
        self.assertEqual(rect1.__str__(), exp_output)

    def test_str_2arg(self):
        '''test string 2 args given'''
        rect2 = Rectangle(2, 2)
        exp_output = "[Rectangle] ({}) 0/0 - 2/2".format(rect2.id)
        self.assertEqual(rect2.__str__(), exp_output)

    def test_str_3arg(self):
        '''test string 3 args'''
        rect3 = Rectangle(2, 2, 1)
        exp_output = "[Rectangle] ({}) 1/0 - 2/2".format(rect3.id)
        self.assertEqual(rect3.__str__(), exp_output)

    def test_str_4arg(self):
        '''test string 4 args'''
        rect3 = Rectangle(2, 2, 1, 1)
        exp_output = "[Rectangle] ({}) 1/1 - 2/2".format(rect3.id)
        self.assertEqual(rect3.__str__(), exp_output)

    def test_changed_values(self):
        '''update values'''
        rectn = Rectangle(4, 6, 2, 1, 12)
        rectn.width = 5
        rectn.height = 7
        rectn.x = 3
        rectn.y = 2
        exp_output = "[Rectangle] ({}) 3/2 - 5/7".format(rectn.id)
        self.assertEqual(rectn.__str__(), exp_output)

    def test_wrong_num_args(self):
        '''wrong arg num'''
        rectn = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaises(TypeError):
            rectn.__str__(1)

class TestRectangle_update(unittest.TestCase):
    '''test update function'''

    def update_call(self):
        '''calling update no args'''
        rc = Rectangle(10, 10, 10, 10, 10)
        exp_output = "[Rectangle] (10) 10/10 - 10/10"
        rc.update()
        self.assertEqual(rc.__str__(), exp_output)

    def update_1arg(self):
        '''update one arg'''
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89)
        exp_output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(rec.__str__(), exp_output)

    def update_2args(self):
        '''update two args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, 2)
        exp_output = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(recn.__str__(), exp_output)

    def update_3args(self):
        '''update three args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, 2, 3)
        exp_output = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(recn.__str__(), exp_output)

    def update_4args(self):
        '''update four args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, 2, 3, 4)
        exp_output = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(recn.__str__(), exp_output)

    def update_5args(self):
        '''update five args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, 2, 3, 4, 5)
        exp_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(recn.__str__(), exp_output)

    def update_6args(self):
        '''update six args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, 2, 3, 4, 5, 6)
        exp_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(recn.__str__(), exp_output)

    def update_6args(self):
        '''update six args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(None)
        exp_output = "[Rectangle] ({}) 4/5 - 2/3".format(recn.id)
        self.assertEqual(recn.__str__(), exp_output)

    def update_args_twice(self):
        '''update six args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, 2, 3, 4, 5)
        recn.update(89, 3, 3, 3, 3)
        exp_output = "[Rectangle] (89) 3/3 - 3/3"
        self.assertEqual(recn.__str__(), exp_output)

    def update_args_invalid_w(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            recn.update(89, '2')

    def update_args_negative_w(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            recn.update(89, -2)

    def update_args_zero_w(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            recn.update(89, 0)

    def update_args_invalid_h(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            recn.update(89, 2, '3')

    def update_args_negative_h(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            recn.update(89, 2, -3)

    def update_args_zero_h(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            recn.update(89, 2, 0)

    def update_args_invalid_x(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            recn.update(89, 2, 3, '4')

    def update_args_negative_x(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            recn.update(89, 2, 3, -4)

    def update_args_invalid_y(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            recn.update(89, 2, 3, 4, '5')

    def update_args_negative_x(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            recn.update(89, 2, 3, 4, -5)

    def update_args_invalid_several(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            recn.update(89, '2', 3, 4, '5')

    def update_args_negative_x(self):
        '''update with an invalid arg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            recn.update(89, -2, 3, 4, -5)

class TestRectangle_update_kwargs(unittest.TestCase):
    '''test update kwargs function'''
    def update_kwargs_height(self):
        '''calling update height'''
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(height=1)
        exp_output = "[Rectangle] (10) 10/10 - 10/1"
        self.assertEqual(rc.__str__(), exp_output)

    def update_kwargs_width_x(self):
        '''calling update width and x'''
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(width=1, x=2)
        exp_output = "[Rectangle] (10) 2/10 - 1/10"
        self.assertEqual(rc.__str__(), exp_output)

    def update_kwargs_width_y_x_id(self):
        '''calling update y width x id'''
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(y=1, width=2, x=3, id=89)
        exp_output = "[Rectangle] (89) 3/11 - 2/10"
        self.assertEqual(rc.__str__(), exp_output)

    def update_kwargs_width_y_x_height(self):
        '''calling update y width x height'''
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(x=1, height=2, y=3, width=4)
        exp_output = "[Rectangle] ({}) 1/3 - 4/2".format(rc.id)
        self.assertEqual(rc.__str__(), exp_output)

    def update_kwargs_invalid_w(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            recn.update(width='2')

    def update_kwargs_negative_w(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            recn.update(width=-2)

    def update_kwargs_zero_w(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            recn.update(width=0)

    def update_kwargs_invalid_h(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            recn.update(height='2')

    def update_kwargs_negative_h(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            recn.update(height=-2)

    def update_kwargs_zero_h(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            recn.update(height=0)

    def update_kwargs_invalid_x(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            recn.update(x='2')

    def update_kwargs_negative_x(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            recn.update(x=-2)

    def update_kwargs_invalid_y(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            recn.update(y='2')

    def update_kwargs_negative_y(self):
        '''update with an invalid kwarg'''
        recn = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            recn.update(y=-2)

    def update_kwargs_and_args(self):
        '''update with kwargs and args'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, 2, 3, x=4, y=5)
        exp_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(recn.__str__(), exp_output)

    def update_kwargs_and_args_wrkeys(self):
        '''update with wrong keys'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, a=2, b=3, c=4, d=5)
        exp_output = "[Rectangle] (10) 10/10 - 10/10"
        self.assertEqual(recn.__str__(), exp_output)

    def update_kwargs_and_args_smwrkeys(self):
        '''update with some wrong keys'''
        recn = Rectangle(10, 10, 10, 10, 10)
        recn.update(89, a=2, b=3, x=4, y=5)
        exp_output = "[Rectangle] (10) 4/5 - 10/10"
        self.assertEqual(recn.__str__(), exp_output)

if __name__ == "__main__":
    unittest.main()