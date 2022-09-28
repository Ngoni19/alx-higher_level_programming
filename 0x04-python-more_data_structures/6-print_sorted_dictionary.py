#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dict_key, dict_value in sorted(a_dictionary.items()):
        print("{}: {}".format(dict_key, dict_value))
