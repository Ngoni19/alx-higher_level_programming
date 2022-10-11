#!/usr/bin/python3
"""
Module -> 5-square
Def class Square with private size & public area
thus access & update size
print to stdout the square -> #'s
"""


class Square:
    """
    class Square def

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        print(self)
    """

    def __init__(self, size=0):
        """
        Init square

        Attributes:
            size (int): defaults to 0 if none;
        """
        self.size = size

    @property
    def size(self):
        """"
        Getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: set size to value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calc area of square

        Returns:
            area
        """
        return (self.__size)**2

    def my_print(self):
        """
        Print square with #'s
        """
        print("".join(["#" * self.__size for rows in range(self.__size)]))
