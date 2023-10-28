#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module contain one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """ function that add two varables

    Args:
        a: first arg int
        b: second arg int
    
    Raises:
        TypeError: if a and b are not int or float

    Return:
        the sum of a and b
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
