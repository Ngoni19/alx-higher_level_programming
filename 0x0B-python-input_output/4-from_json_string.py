#!/usr/bin/python3
"""
Module 4-from_json_string

@funct -> returns python data structure from JSON string
"""


def from_json_string(my_str):
    """Return ->python data structure from JSON string
    Args:
        my_str: json string repr
    Return:
        python object
    """
    import json

    return json.loads(my_str)
