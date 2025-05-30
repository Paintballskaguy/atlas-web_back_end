#!/usr/bin/env python3


"""
This coroutine uses an asynchronous list comprehension to collect 10 random
numbers generated by the async_generator coroutine.
"""


import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    This coroutine uses an asynchronous list comprehension to collect 10 random
    numbers generated by the async_generator coroutine.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
