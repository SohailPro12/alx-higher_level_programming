#!/usr/bin/python3

"""
Module with save_to_json_file method.
"""
import json


def save_to_json_file(my_obj, filename):
    """save to the file"""
    with open(filename, 'w') as file:
        jj = json.dumps(my_obj)
        file.write(jj)
