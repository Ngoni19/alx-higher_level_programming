#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        tmp_dic = {key: value}
        a_dictionary.update(tmp_dic)
        return (a_dictionary)
    else:
        return None
