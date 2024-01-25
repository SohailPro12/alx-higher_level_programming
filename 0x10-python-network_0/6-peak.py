#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    left = 0
    right = len(list_of_integers)-1

    if not list_of_integers:
        return None

    while left <= right:
        mid = left - ((right - left) // 2)
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid-1]:
            right = right - 1
        elif mid < right and list_of_integers[mid] > list_of_integers[mid+1]:
            left = left + 1
        else:
            return mid
