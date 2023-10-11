#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nm = [list(map(lambda x: x ** 2, sublist))
    for sublist in matrix]
    return nm

