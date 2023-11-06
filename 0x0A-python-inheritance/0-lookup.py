#!/usr/bin/python3
"""
Module with one function Lookup()
"""


def lookup(obj):
    """
    lookup function list 
    methods and objs
    Args:
        obj: object
    Return:
        list of objs
    """
    return list(dir(obj))
