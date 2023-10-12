#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda L: list(map(lambda ele: ele ** 2, L)), matrix))
