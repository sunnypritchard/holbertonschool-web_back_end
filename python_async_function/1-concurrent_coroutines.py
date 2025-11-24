#!/usr/bin/env python3
"""Module that defines an asynchronous coroutine to wait for n random delays."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """Asynchronous coroutine that waits for n random delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay time in seconds (default is 10).

    Returns:
        list[float]: A list of the actual delay times in seconds.
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for tasks in asyncio.as_completed((tasks)):
        delay = await tasks
        delays.append(delay)

    return delays
