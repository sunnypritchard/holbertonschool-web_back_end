#!/usr/bin/env python3
"""Module that defines a function to create an asyncio Task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        asyncio.Task: An asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
