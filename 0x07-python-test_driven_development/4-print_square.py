#!/usr/bin/python3
"""
Module 4-print_square
@method-> prints square with #'s
arg: an int size
"""


def print_square(size):
    """
    Given int size- Print the square with #'s 
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
