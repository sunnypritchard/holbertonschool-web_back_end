#!/usr/bin/env python3
"""
Module that defines an asynchronous coroutine to
wait for n random delays.
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    wait_list = []
    for _ in range(n):
        wait = await wait_random(max_delay)
        wait_list.append(wait)
    return sorted(wait_list)
