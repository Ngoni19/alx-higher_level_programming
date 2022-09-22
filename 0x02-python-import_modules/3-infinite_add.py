#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add_result = 0
    if (len(sys.argv) > 1):
        for k in range(1, len(sys.argv)):
            add_result += (int(sys.argv[k]))
    print("{:d}".format(add_result))
