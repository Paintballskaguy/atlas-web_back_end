#!/usr/bin/env python3

"""
Multiplier of a float and returns a multiple float.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplier of a float and returns a multiple float.

    Args:
        multiplier (float): the float value to multiply by.

    Returns:
        Callable[[float], float]: returns the product of the math
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
