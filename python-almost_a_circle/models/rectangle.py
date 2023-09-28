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
        self.__width = width

    @property
    def height(self):
        """Get the height"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """Setting the height"""
        self.__height = height

    @property
    def x(self):
        """Getting x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setting x"""
        self.__x = x

    @property
    def y(self):
        """Getting y"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
