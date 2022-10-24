#!/usr/bin/python3
"""
Module 10-square

@parent class BaseGeometry
with public instance method area & integer_validation

@contains subclass Rectangle
with instantiation of priv attri width and height, validated by parent,
extends parent's area method & prints with __str__

Contains subcls Square
with instantiation of priv attri size, validated by superclass,
and prints with __str__
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """init size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
