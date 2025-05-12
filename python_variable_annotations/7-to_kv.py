#!/usr/bin/env python3

"""
This function returns a tuple with a string and squared number.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function returns a tuple with a string and squared number.

    Returns:
        _type_: tuple containing the string k and the square v.
    """
    return (k, float(v ** 2))
