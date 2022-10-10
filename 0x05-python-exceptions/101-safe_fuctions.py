#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, ZeroDivisionError, TypeError, ValueError) as eRR:
        stderr.write("Exception: {}\n".format(eRR))
        return None
