#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for k in range(list_length):
        _div = 0
        try:
            _div = my_list_1[k] / my_list_2[k]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            new_list.append(_div)
    return new_list
