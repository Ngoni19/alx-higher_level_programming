#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m_row in matrix:
        for k in m_row:
            if k is not m_row[len(m_row) - 1]:
                print("{:d}".format(k), end=" ")
            else:
                print("{:d}".format(k), end="")
        print()
