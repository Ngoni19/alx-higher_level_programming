#!/usr/bin/python3
"""
Module 1-my_list

@class -> MyList
inherit from list; public instance method to print sorted list
"""


class MyList(list):
    """inherits from list

    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints sorted list of ints in ascending order"""
        print(sorted(self))
