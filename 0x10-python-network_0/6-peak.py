#!/usr/bin/python3
"""Finds a peak in an unsorted list of integers"""


def find_peak(list_of_integers):
    """There might be more than one peak"""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = list_of_integers[mid]

        if (mid == 0 or mid_value >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or \
           mid_value >= list_of_integers[mid + 1]):
            return mid_value
        elif mid > 0 and mid_value < list_of_integers[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1

    return None
