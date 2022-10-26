#!/usr/bin/python3
"""
Module 5-save_to_json_file

@funct -> writes Python obj to file using JSON repr
"""


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON repr
    Args:
        my_obj: python object
        filename: file created
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as F:
        json.dump(my_obj, F)
