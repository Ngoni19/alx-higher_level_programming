#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i_dx = 0
    while i_dx < x:
        try:
            print("{}".format(my_list[i_dx]), end="")
        except IndexError:
            break
        i_dx += 1
    print("")
    return i_dx
