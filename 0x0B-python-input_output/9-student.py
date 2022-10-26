#!/usr/bin/python3
"""
Module 9-student

@ class Student
that __int__ public instance attributes first_name, last_name, and age,
and has public method to_json that retrieves its dict repr
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

    def to_json(self):
        """
        Returns -> dictionary description with simple data structure
        (list, dictionary, str)
        for JSON serialization of an object
        """
        return self.__dict__
