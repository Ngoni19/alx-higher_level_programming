#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    n = 0
    rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for k, j in zip(roman_string, roman_string[1:]):
        if k not in rom_dict.keys():
            return 0
        elif rom_dict[k] >= rom_dict[j]:
            n += rom_dict[k]
        else:
            n -= rom_dict[k]
    n += rom_dict[roman_string[-1]]
    return n
