#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) < 1:
        return None
    listdivs = []
    for i in my_list:
        if (i % 2) == 0:
            listdivs.append(True)
        else:
            listdivs.append(False)
    return listdivs
