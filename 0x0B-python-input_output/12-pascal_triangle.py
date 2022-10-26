#!/usr/bin/python3
"""
Module 12-pascal_triangle

@funct -> returns int lists of pascal pascal_tri of any given size
"""


def pascal_triangle(n):
    """
    Return:
        empty list [] if n <= 0
        if n is 5, we should expect:
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal_tri = [[1]]
    for rows in range(n-1):
        pascal_tri.append([x+y for x, y in zip([0] + pascal_tri[-1],
                            pascal_tri[-1] + [0])])
    return pascal_tri
