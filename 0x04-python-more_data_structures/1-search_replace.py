#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return([y if y != search else replace for y in my_list])
    return None
