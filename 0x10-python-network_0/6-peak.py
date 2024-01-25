#!/usr/bin/python3
"""This module contains a function to find peak in list of unsorted integers"""
def find_peak(list_of_integers):
    """
    Returns peak value in the list of integers specified by `list_of_integers`
    """
    if not list_of_integers:
        return None  # No peak in an empty list
    
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]

""" Complexity: O(log(n)) """

