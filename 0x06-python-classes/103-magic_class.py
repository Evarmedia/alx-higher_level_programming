#!/usr/bin/python3
"""Contains the `MagicClass` definition"""
from math import pi


class MagicClass:
    """Computes data for a circle based on a given radius_of"""

    def __init__(self, radius_of=0):
        """Checks for exceptions, Instantiates the radius_of

        Args:
            radius_of: An int or float value representing the radius_of of the circle
        """

        if type(radius_of) is not int and type(radius_of) is not float:
            raise TypeError("radius_of must be a number")
        self.__radius = radius_of

    def area(self):
        """Returns the area of the circle of given radius_of"""
        return pi * pow(self.__radius, 2)

    def circumference(self):
        """Returns the circumference of a circle of given radius_of"""
        return 2 * pi * self.__radius
