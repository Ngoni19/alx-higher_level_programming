#!/usr/bin/python3
"""
Module 6-load_from_json_file

@funct-> creates a Python obj from JSON file
"""


def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: file created
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as F:
        return json.load(F)

