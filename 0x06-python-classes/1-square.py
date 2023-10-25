#!/usr/bin/python3
"""
    Square module: based on 0-square 
"""


class Square:
    """
    Defines a square class:
    one attribute
    """
    def __init__(self, size):
        """
        Constructor.

        Args:
            size: length of a side of the square.
        """
        self.__size = size
