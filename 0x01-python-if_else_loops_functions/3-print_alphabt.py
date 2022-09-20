#!/usr/bin/python3
for alpha in range(ord('a'), ord('z')+1):
    if alpha is not (ord('q')) and alpha is not (ord('e')):
        print('{}'.format(chr(alpha)), end='')
