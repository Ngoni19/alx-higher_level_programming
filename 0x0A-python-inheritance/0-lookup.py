#!/usr/bin/python3
"""
Module 0-lookup

@method -> lookup returns list of object's attribute & methods
"""


def lookup(obj):
    """returns list of object's attribute & methods"""
    return dir(obj)
