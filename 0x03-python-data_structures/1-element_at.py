#!/usr/bin/python3
def element_at(my_list, idx):
    if idx * -1 > 0 :
        return None
    elif idx > len(my_list):
        return None
    else:
        return("{:d}".format(my_list[idx]))
