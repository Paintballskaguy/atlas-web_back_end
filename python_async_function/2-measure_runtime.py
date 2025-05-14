#!/usr/bin/env python3


"""
measuring that time. measure the time for execution time per task.
"""


import asyncio
import time
from typing import Callable


wait_n = __import__('1-concurrent_coroutines'). wait_n

def measure_time(n: int, max_delay: int) ->  float:
    """measure the time for execution time per task.

    Args:
        n (int):  Number of times to spawn wait_random
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        float: Average execution time per task.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
