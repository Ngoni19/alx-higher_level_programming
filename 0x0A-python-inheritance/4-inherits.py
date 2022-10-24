#!/usr/bin/python3
"""
Module 4-inherits_from.py

@method inherits_from
returns True; if obj is instance of class
"""


def inherits_from(obj, a_class):
    """
    Note:
        type()-> get specific class
        isinstance() -> get class & any parent classes
        issubclass() -> get what object is a subclass of

    Return:
        True; if obj is instance of class
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
