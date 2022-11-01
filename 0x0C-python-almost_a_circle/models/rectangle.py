#!/usr/bin/python3
"""
Module contains class Rectangle

Inherits from Base;
Initalize superclass' id
Contains private width, height, x, y
"""


class Rectangle(Base):
    """
    @class Rectangle; inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width          __height
        __x              __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize super(id from base)"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
