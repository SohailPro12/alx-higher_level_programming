#!/usr/bin/python3

"""
Script that adds all arguments to a Python list.
"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = list(sys.argv[1:])

try:
    old_list = load_from_json_file('add_item.json')
except Exception:
    old_list = []

old_list.extend(my_list)
save_to_json_file(old_list, 'add_item.json')
