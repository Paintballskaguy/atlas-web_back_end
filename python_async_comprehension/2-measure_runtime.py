#!/usr/bin/env python3


"""
Module that contains a coroutine that measures the runtime
of async_comprehension four times in parallel.    
"""


import asyncio
import time
from typing import Coroutine


async def measure_runtime() -> float:
    
    """
    Executes 4 async_comprehensions in parallel and measures runtime.

    Returns:
        _type_: Total runtime in seconds.
    """
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    return end_time - start_time
