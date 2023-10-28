#!/usr/bin/python3
"""Module for one mehtod matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Multiplies one matrix by another.

    Args:
        m_a: the first matrix
        m_b: the second matrix

    Returns:
        matrix: matrix1 par matrix2

    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    a_its_empty = 0
    b_its_empty = 0
    a_its_notrect = 0
    b_its_notrect = 0
    a_its_notnum = 0
    b_its_notnum = 0

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            a_its_notrect = 1
        for num in row:
            if not isinstance(num, (int, float)):
                a_itsnotnum = 1

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            b_its_notrect = 1
        for num in row:
            if not isinstance(num, (int, float)):
                b_its_notnum = 1

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if a_its_notnum:
        raise TypeError("m_a should contain only integers or floats")

    if b_its_notnum:
        raise TypeError("m_b should contain only integers or floats")

    if a_its_notrect:
        raise TypeError("each row of m_a must should be of the same size")

    if b_its_notrect:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    results = []
    for y in range(len(m_a)):
        results.append([])

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            results[i].append(c)

    return results

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
