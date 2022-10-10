#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        _div = a / b
    except (ZeroDivisionError, TypeError):
        _div = None
    finally:
        print("Inside result: {}".format(_div))
    return _div
