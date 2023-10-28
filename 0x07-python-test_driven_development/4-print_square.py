#!/usr/bin/python3
"""Module with one method of print_square."""


def print_square(size):
    """module print squares

    Args:
        size: int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
  
    if size > 0:
        for i in range (0,size):
            for j in range(0,size):
                print('#', end='')
            print('')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
