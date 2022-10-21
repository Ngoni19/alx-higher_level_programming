#!/usr/bin/python3
"""
Module 5-text_indentation
@method -> prints text with 2 new lines after each ".", "?", and ":"
arg: a string
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    ListLines = [lines.strip(' ') for lines in text.split('\n')]
    corrected = "\n".join(ListLines)
    print(corrected, end="")
