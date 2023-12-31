#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)

        self.__size = size

        # call rectangle constructor
        super().__init__(size, size)

    def area(self):
        """Implementation of the area"""
        return self.__size * self.__size

    def __str__(self):
        """String repesentation"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
