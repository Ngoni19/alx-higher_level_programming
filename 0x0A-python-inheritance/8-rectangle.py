 #!/usr/bin/python3
"""
Module 8-rectangle

@parent class BaseGeometry
with public instance method area & integer_validator

@subclass Rectangle
with instantiation of __attributes width & height, validated by parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """validate; initialize width & height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
