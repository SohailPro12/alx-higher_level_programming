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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area"""
        return self.height * self.width

    def perimeter(self):
        """Calculate the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        rectangle_str = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle_str += "#"
            rectangle_str += "\n"
        return rectangle_str
