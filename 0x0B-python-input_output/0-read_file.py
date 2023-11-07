#!/usr/bin/python3
"""
Module with read_file function.
"""


def read_file(filename=""):
    """read the file"""
    with open(filename,'r') as file:
        for line in file:
            print(line.strip())
