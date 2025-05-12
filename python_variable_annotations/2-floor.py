#!/usr/bin/env python3
import math


"""
uses math to find the floor of a float.    
"""


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The input floating-point number.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
