#!/usr/bin/python3

"""
Module with append_file function.
"""


def append_write(filename="", text=""):
    """add in the file"""
    with open(filename, 'w',  encoding='UTF8') as file:
        return file.write(text)
