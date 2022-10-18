#!/usr/bin/python3
"""
Module 0-add_integer
@1 method - > returns an int sum
Accepts two values(either int or float,&  before adding casts to int
"""


def add_integer(a, b=98):
    """
    Returns int(a + b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
