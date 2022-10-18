#!/usr/bin/python3
"""
Module 2-matrix_divided
@method -> divides all elements of a matrix & returns new matrix
Requires same size lists[ints, floats] , & max of two decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    Msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(Msg)

    NewMatrix = []
    SamLen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(Msg)
        if len(lists) != SamLen:
            raise TypeError("Each row of the matrix must have the same size")
        NewList = []
        for k in lists:
            if not isinstance(k, (int, float)):
                raise TypeError(Msg)
            NewList.append(round(k/div, 2))
        NewMatrix.append(NewList)
    return NewMatrix
