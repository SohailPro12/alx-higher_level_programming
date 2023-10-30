#!/usr/bin/python3
"""
Module with one class Rectngle
"""


class Rectangle:
    """ Rectangle class defines the width and 
    the height.
    """

    def __init__(self, width=0, height=0):
        """initilizes the height and the width"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
