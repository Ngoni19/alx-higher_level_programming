#!/usr/bin/python3
"""
Module 9-rectangle
Contains class Rectangle -> private attri width & height,
public area & peri methods, prints using any given symbol,
deletes, has public attri to keep track of number of instances,
has static method - returns bigger rectangle out of the two,
& has class method-returns a new class instance via square
"""


class Rectangle():
    """
    Defines class rectangle -> private attribute width and height

    Args:
        width (int): width
        height (int): height

    Attributes:
        number_of_instances (int): number of instances created & not deleted
        print_symbol (any type): used to print str representation

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
        bigger_or_equal(rect_1, rect_2)
        square(cls, size)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init rectangles """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ Deletes instance of class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
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
        """ Setter sets height; if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return (width * height) """
        return self.__width * self.__height

    def perimeter(self):
        """ Return (2*width + 2*height (|| return 0; if width || height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ Print rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_print = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return rect_print

    def __repr__(self):
        """ Str representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns -> bigger area rectangle"""
        if not isinstance(rect_1, Rectangle) or \
                not isinstance(rect_2, Rectangle):
            raise TypeError("{} must be an instance of Rectangle".
                            format("rect_1" if not
                                   isinstance(rect_1, Rectangle)
                                   else "rect_2"))
        if rect_2.area() < rect_1.area():
            
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Returns new rectangle instance with width == height == size """
        return cls(size, size)
