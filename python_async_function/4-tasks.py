#!/usr/bin/env python3
"""
Module that defines an asynchronous coroutine to
wait for n random delays using tasks.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    wait_list = []
    for _ in range(n):
        wait = await task_wait_random(max_delay)
        wait_list.append(wait)
    return sorted(wait_list)
