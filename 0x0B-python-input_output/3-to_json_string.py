#!/usr/bin/python3
"""
Module 3-to_json_string

@funct -> returns JSON repr of obj (string)
"""


def to_json_string(my_obj):
    """Returns JSON repr of obj (string)
    Args:
        my_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)
