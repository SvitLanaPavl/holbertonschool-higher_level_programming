#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setting the width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setting the height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Getting x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setting x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Getting y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setting y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Public area method"""
        return self.__height * self.__width

    def display(self):
        """Public display method"""
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """Str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigning an argument to each attribute
        Args:
            *args - the list of arguments
            **kwargs - a dictionary of key-value arguments
        """
        num_args = len(args)
        if num_args and num_args != 0:
            if num_args >= 1:
                self.id = args[0]
            elif num_args >= 2:
                self.__width = args[1]
            elif num_args >= 3:
                self.__height = args[2]
            elif num_args >= 4:
                self.__x = args[3]
            elif num_args == 5:
                self.__y = args[4]
        elif kwargs and kwargs != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
