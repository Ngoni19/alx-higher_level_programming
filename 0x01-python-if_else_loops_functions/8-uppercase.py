#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        if (ord(alpha) >= ord('a')) and (ord(alpha) <= ord('z')):
            alpha = chr(ord(alpha)-ord('a')+ord('A'))
        print("{}".format(alpha), end='')
    print()
