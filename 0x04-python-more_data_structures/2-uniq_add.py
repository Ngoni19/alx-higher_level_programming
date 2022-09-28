#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_total = 0
    for i in set(my_list):
        unique_total += i
    return (unique_total)
