#!/usr/bin/python3
"""
Module 0-read_file

Contains function that reads & prints contents from a file
"""


def read_file(filename=""):
    """Read & print text from file"""
    with open(filename, mode="r", encoding="utf-8") as F:
        print(F.read(), end="")
