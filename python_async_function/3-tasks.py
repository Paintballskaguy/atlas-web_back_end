#!/usr/bin/env python3


"""
creates asyncio.Task from wait_random coroutine
"""


import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs wait_random with the given max_delay.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: Task object for the wait_random coroutine.
    """ 
    return asyncio.create_task(wait_random(max_delay))
