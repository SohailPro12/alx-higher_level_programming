#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    p = []
    if not list_of_integers:
        return None;
    for i in range(0, len(list_of_integers)-1):
        if list_of_integers[i] >= list_of_integers[i+1] and list_of_integers[i] >= list_of_integers[i-1]:
            p.append(list_of_integers[i])

    return p[0]
