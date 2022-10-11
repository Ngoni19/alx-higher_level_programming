#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attri size
"""


class Square:
    """
    class Square def

    Args:
        size : size of a side in square
    """
    def __init__(self, size):
        """
        Init square

        Attributes:
            size: size of a side of square
        """
        self.__size = size
