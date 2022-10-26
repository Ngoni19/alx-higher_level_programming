#!/usr/bin/python3
"""
Module 2-append_write

@funct-> appends to text file & returns num chars added
"""


def append_write(filename="", text=""):
    """append to text file; returns num chars added"""
    with open(filename, mode="a", encoding="utf-8") as F:
        return(F.write(text))
