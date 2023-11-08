#!/usr/bin/python3

"""
Module of append_after method.
"""


def append_after(filename="", search_string="", new_string=""):
    """ append into a file """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
