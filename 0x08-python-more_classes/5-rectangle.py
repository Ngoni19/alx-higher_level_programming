#!/usr/bin/python3
"""
Module 5-rectangle
Contains class Rectangle ->  private attribute width & height,
public area & perimeter methods,prints #'s, & deletes
"""


class Rectangle:
    """
    Defines class rectangle-> private attri width & height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    def __init__(self, width=0, height=0):
        """ Init rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width; if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter set height; if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return (width * height) """
        return self.__width * self.__height

    def perimeter(self):
        """ Return (2*width + 2*height || return 0;if width || height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ Print rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_print = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rect_print

    def __repr__(self):
        """ String representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Delete instance of class specified """
        print("Bye rectangle...")
