#!/usr/bin/python3
for k in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(k) if k % 2 == 0 else chr(k-32), end='')
