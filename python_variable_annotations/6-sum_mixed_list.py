#!/usr/bin/env python3
"""
This is the function of 'sum_mixed_list' that takes in a list of integers
and floats and then returns their sum as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This is the function of 'sum_mixed_list' that takes in a
    list of integers and floats and then returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers
        and/or floats.

    Returns:
        float: The sum of all elements in the input list as a float.
    """
    return sum(mxd_lst)
