#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """ empty class """
    def area(self):
        """Raise error"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validate int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
