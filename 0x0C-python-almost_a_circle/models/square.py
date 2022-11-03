#!/usr/bin/python3
"""
Module contains class Square

Inherits from Rectangle;
Init superclass-> id, width, height, x, y
@public attribute size
Prints -> [Square] (<id>) <x>/<y> - <size>
Update attributes: arg1=id, arg2=size, arg3=x, arg4=y
Returns;dictionary representation of attributes
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    @class Square; inherits from class Rectangle
    Inherited Attributes:
        id
        __height    __weight
        __x         __y
    Class Attributes:
        size
    Inherted Methods:
         Rectangle.init(self, width, height, x=0, y=0, id=None)
         Base.init(self, id=None)
         width(self)      width(self, value)
         height(self)     height(self, value)
         x(self)          x(self, value)
         y(self)          y(self, value)
         area(self)       display(self)
         update(self, *args, **kwargs)
    Methods:
        __str__
        __init__(self, size, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        size(self)                    size(self, value)
        to_dictionary(self)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize super class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter: size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size - sets width & height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Print -> [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """
        If args: set attributes -> id, width, height, x, y(in order)
        If no args: set attributes according to kwargs
        """
        if args:
            for j, s in enumerate(args):
                if j == 0:
                    self.id = s
                elif j == 1:
                    self.size = s
                elif j == 2:
                    self.x = s
                else:
                    self.y = s
        else:
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]

    def to_dictionary(self):
        """Return -> dict representation"""
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
