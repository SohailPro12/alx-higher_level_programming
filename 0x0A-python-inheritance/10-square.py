#!/usr/bin/python3
"""
Module for Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass from the rectangle"""
    def __init__(self, size):
        """ i call the constructor of
        rectangle cuz it needs two args
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method for area of square."""
        return self.__size ** 2
