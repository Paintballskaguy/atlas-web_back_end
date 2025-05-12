#!/usr/bin/env python3

"""
This module provides a function that returns element lengths in an iterable.
The module contains a single function 'element_length' that takes an iterable
of sequences and returns a list of tuples containing
each element and its length.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a
    list of tuples with each element and its length.

    Args:
        lst: An iterable containing sequence-like
        elements (strings, lists, etc.)

    Returns:
        A list of tuples where each tuple contains (element, element_length)
    """
    return [(i, len(i)) for i in lst]
