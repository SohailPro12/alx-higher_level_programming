#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds the peak"""
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers)-1

    while left < right:
        mid = (right + left) // 2

        if list_of_integers[mid] > list_of_integers[mid+1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
