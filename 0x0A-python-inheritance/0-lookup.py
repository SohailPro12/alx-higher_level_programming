#!/usr/bin/python3
"""
Module for lookup method.
"""


def lookup(obj):
    """Lookup for object attributes and methods.
    Args:
        obj (object): list.

    Returns:
        list: the list of attributes.
    """
    return dir(obj)
