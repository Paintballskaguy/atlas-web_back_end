#!/usr/bin/env python3


"""
Asynchronously generates random numbers between 0 and 10.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random numbers between 0 and 10.

    This coroutine loops 10 times each time waiting asynchronously for 1 second
    before yielding a random float between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
