#!/usr/bin/python3
"""
Module 3-is_kind_of_class

@method is_kind_of_class
returns True; if obj is an instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use isinstance() to get class and any parent classes
    Return:
        True; if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
