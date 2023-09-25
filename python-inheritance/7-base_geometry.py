#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """public instance method that raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value

        Args:
            name: name
            value: value

        Raises:
            TypeError: name must ne an integer
            ValueError: name must be greater that 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
