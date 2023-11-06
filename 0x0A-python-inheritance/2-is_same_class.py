#!/usr/bin/python3
"""
Module of one class
"""


def is_same_class(obj, a_class):
    """
    check if the same type of a class

    Args:
        obj:the object
        a_class: the class

    Returns:
        true or false
    """
    return type(obj) ==  a_class
