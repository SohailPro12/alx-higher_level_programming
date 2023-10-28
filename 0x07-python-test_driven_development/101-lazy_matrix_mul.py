#!/usr/bin/python3
"""Module of one method lazy_matrix_mul."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that is given

    Args:
        m_a: first matrix
        m_b: second matrix
    
    Returns:
        return matrix1 par matrix2
    """

    return numpy.matmul(m_a, m_b)
