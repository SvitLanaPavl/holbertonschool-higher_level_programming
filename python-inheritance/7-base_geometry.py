#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """public instance method that raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance methid that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
