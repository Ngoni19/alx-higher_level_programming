#!/usr/bin/python3
"""
Module 7-base_geometry

@BaseGeometry -> class
with public instance method area & integer_validation
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """has exceptions; area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the inputs
        Args:
            name (str): assumed to be always a string
            value (int): greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
