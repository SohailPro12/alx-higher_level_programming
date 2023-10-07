#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copylist = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(0, len(my_list)):
        copylist.append(my_list[i])
        copylist = replace_in_list(copylist, idx, element)
        return copylist
def replace_in_list(my_list, idx, element):
    my_list[idx] = element
    return my_list
