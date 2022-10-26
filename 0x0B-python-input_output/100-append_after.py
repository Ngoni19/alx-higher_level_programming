#!/usr/bin/python3
"""
Module 100-append_after

@funct -> appends str after lines that include keyword
"""


def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword (search_string)"""

    with open(filename, mode="r+", encoding="utf-8") as F:
        new_txt = ""
        for line in F:
            new_txt += line
            if search_string in line:
                new_txt += new_string
        F.seek(0)
        F.write(new_txt)
