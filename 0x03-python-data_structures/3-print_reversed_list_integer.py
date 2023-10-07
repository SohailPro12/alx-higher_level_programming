#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = []
    for i in range(1, len(my_list) + 1):
        rev.append(my_list[-i])
    for x in rev:
        print("{:d}".format(x))
