#!/usr/bin/env python3
"""Module that contains a function to measure runtime of async_comprehension"""
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension"""
    start_time = time.time()
    await async_comprehension()
    end_time = time.time()
    return end_time - start_time
