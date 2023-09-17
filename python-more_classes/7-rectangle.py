#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectanle class representation"""
    # Public class attribute
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of properties

        Args:
        width - width, must be an integer
        height - height, must be an integer
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method area"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += Rectangle.print_symbol
            rectangle_str += "\n"
        return rectangle_str[:-1]

    def __print__(self):
        """Prints rectangle to the console"""
        print(self)

    def __repr__(self):
        """Returns a string representation
        that can be used to recreate a new instance using eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints the message when the instance is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
