#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from Base.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.

        :param width: width of the rectangle
        :param height: height of the rectangle
        :param x: x coordinate of the rectangle
        :param y: y coordinate of the rectangle
        :param id: id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: new width of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        :param value: new height of the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
        Get the x coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x coordinate of the rectangle.

        :param value: new x coordinate of the rectangle
        """
        self.__x = value

    @property
    def y(self):
        """
        Get the y coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y coordinate of the rectangle.

        :param value: new y coordinate of the rectangle
        """
        self.__y = value
