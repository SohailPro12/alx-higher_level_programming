#!/usr/bin/python3

"""
Module with write_file function.
"""


def write_file(filename="", text=""):
    """write in the file"""
    with open(filename, 'w',  encoding='UTF8') as file:
        return file.write(text)
