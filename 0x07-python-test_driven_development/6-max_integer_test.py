#!/usr/bin/python3
"""Module finds max integer in a list
"""


def max_integer(list=[]):
    """Function to find & return: max integer in a list of integers
        if list [empty];return None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
