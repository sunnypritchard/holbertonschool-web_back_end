#!/usr/bin/env python3
"""Module that contains an asynchronous generator function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronous generator that yields 10 random numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
