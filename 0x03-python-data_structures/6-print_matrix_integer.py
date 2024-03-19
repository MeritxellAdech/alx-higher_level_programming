#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 1
        rowl = len(row)
        for col in row:
            print("{:d}".format(col), end="{}".format(" " if i < rowl else ""))
            i += 1
        print()
