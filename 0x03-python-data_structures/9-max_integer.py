#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        for k in my_list:
            if k > max_int:
                max_int = k
        return max_int
    else:
        return None
