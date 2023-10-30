#!/usr/bin/python3
"""
Module with one class Rectngle
"""


class Rectangle:
    """ Rectangle class defines the width and 
    the height.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initilizes the height and the width"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances +=1

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
        """Calculate the perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """str print"""
        if self.width == 0 or self.height == 0:
            return ""
        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """repr() for developers"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """message after del"""
        Rectangle.number_of_instances -=1
        print("Bye rectangle...")
