#!/usr/bin/env python3
"""Module that contains an asynchronous generator function"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous generator that yields 10 random numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
