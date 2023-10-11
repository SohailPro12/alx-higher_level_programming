#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda new_mat: list(map(lambda x: x**2, new_mat)), matrix))
