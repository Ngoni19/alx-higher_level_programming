#!/usr/bin/python3
"""
Module 10-square

@parent class BaseGeometry
with public instance method area & integer_validation

Contains subcls Rectangle
with instantiation of private attri width & height, validated by parent,
extends parent's area method & prints with __str__

Contains subcls Square
with instantiation of private attri size, validated by superclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
