#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieving size"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigning attributes"""
        num_args = len(args)
        if num_args and num_args != 0:
            if num_args >= 1:
                self.id = args[0]
            elif num_args >= 2:
                self.size = args[1]
            elif num_args >= 3:
                self.x = args[2]
            elif num_args >= 4:
                self.y = args[3]
        elif kwargs and kwargs != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Str method"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
