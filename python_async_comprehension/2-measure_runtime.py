#!/usr/bin/env python3


"""
Module that contains a coroutine that measures the runtime
of async_comprehension four times in parallel.    
"""


import asyncio
import time
from typing import Coroutine
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
