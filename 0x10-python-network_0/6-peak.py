#!/usr/bin/python3
"""
Function -> finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    find number > than both left & right
    """
    if len(list_of_integers) == 0:
        return None

    I_int = list_of_integers
    sT = 0
    end = len(I_int)-1

    if I_int[sT] > I_int[sT+1]:
        return I_int[sT]
    if I_int[end] > I_int[end-1]:
        return I_int[end]

    half = (sT+end)//2
    if I_int[half-1] < I_int[half] and I_int[half+1] < I_int[half]:
        return I_int[half]
    if I_int[half] < I_int[half-1]:
        return find_peak(I_int[sT:half+1])
    elif I_int[half] < I_int[half+1]:
        return find_peak(I_int[half:end+1])
    else:
        return I_int[sT]
