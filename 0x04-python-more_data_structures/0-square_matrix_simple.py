#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            square = col * col
            new_row.append(square)
        sqr_matrix.append(new_row)
    return sqr_matrix
