#!/usr/bin/python3
"""
A function that adds attributes to objects.
"""


def add_attribute(obj, name, value):
    """Add a new attribute
    Args:
        obj (any): The object
        name (str): The att
        value (any): The value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
