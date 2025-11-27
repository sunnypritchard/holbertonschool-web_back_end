#!/usr/bin/env python3
"""Module that contains an asynchronous generator function"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """Asynchronous generator that yields 10 random numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
