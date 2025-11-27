#!/usr/bin/env python3
"""Module that contains an asynchronous comprehension function"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """Collect 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]
