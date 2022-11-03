#!/usr/bin/python3
"""
Module contains -> class Rectangle

Inherits from Base;
Inits superclass' id
@private width, height, x & y
@public method area
Displays rectangle using "#"'s
Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>
Updates attr : arg1=id, arg2=width, arg3=height, arg4=x, arg5=y
Returns: dict representation of attributes
"""


from models.base import Base


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
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
        __str__          to_dictionary(self)
        update(self, *args, **kwargs)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize super class & others"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter width"""
        return self.__width

    @property
    def height(self):
        """Getter : height"""
        return self.__height

    @property
    def x(self):
        """Getter : x"""
        return self.__x

    @property
    def y(self):
        """Getter : y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter : width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter : height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter : x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter : y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return -> area"""
        return self.__width * self.__height

    def display(self):
        """stdout -> rectangle using #'s"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for j in range(self.__height)))

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        If args: set attri in order -> id, width, height, x, y
        If no args: set attributes according to kwargs
        """
        if args:
            for q, w in enumerate(args):
                if q == 0:
                    self.id = w
                elif q == 1:
                    self.width = w
                elif q == 2:
                    self.height = w
                elif q == 3:
                    self.x = w
                else:
                    self.y = w
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return -> dictionary representation"""
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
