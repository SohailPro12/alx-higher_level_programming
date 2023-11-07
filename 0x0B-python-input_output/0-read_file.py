#!/usr/bin/python3

"""
Module with read_file function.
"""


def read_file(filename=""):
    """read the file"""
    with open(filename, 'r', encoding='UTF8') as file:
        print(file.read())
