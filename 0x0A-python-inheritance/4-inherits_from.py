#!/usr/bin/python3
"""
Module for inherits_from method
"""


def inherits_from(obj, a_class):
    """Are you a subclass or not?"""
    return isinstance(obj, a_class) and type(obj) != a_class
