#!/usr/bin/python3
"""
Module 10-student

@class Student -> init public instance attri first_name,last_name,& age,
&has public method to_json (returns dictionary representation
of requested attributes or all if none were requested)
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionary repr
    """
    def __init__(self, first_name, last_name, age):
        """
        Init student with full name & age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return-> dictionary description with simple data structure
        (list, dictionary, str)
        for JSON serialization of an object

        Return:
            Only return dict of attrs given to us
            Return entire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for attrr in attrs:
                if attrr in self.__dict__.keys():
                    dict[attrr] = self.__dict__[attrr]
            return dict
