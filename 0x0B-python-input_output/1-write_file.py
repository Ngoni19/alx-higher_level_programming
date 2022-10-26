#!/usr/bin/python3
"""
Module 1-write_file

@function -> writes to text file & returns num chars
"""


def write_file(filename="", text=""):
    """w to text file; returns num chars written"""
    with open(filename, mode="w", encoding="utf-8") as F:
        return(F.write(text))
