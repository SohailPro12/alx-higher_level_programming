#!/usr/bin/python3
"""Module contain one functin handl matrix"""


def matrix_divided(matrix, div):
    """a fucntion devide all element of matrix on div
    
    Args:
        matrix: the matrix
        div: the division
        div_mat: matrix dup
        sub_mat: matrix element
    Return:
        matrix divided
     Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
            
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    div_mat = []  
    for submat in matrix:
        submat_div = [] 
        for e in submat:
            result = round(e / div, 2)
            submat_div.append(result)
            div_mat.append(submat_div)  
    return div_mat

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
