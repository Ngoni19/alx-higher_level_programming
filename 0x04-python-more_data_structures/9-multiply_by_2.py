#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        return {key: a_dictionary[key]*2 for key in a_dictionary}

    return None
