#!/usr/bin/env python3

"""
Floor function that takes a float and returns the floor value as an int.
"""


import math

def floor(n: float) -> int:

    """
        Returns the floor of a floating-point number.

        Args:
            n (float): The input floating-point number.

        Returns:
            int: The largest integer less than or equal to n.
    """

    return math.floor(n)
